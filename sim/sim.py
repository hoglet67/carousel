'''
Construct a netlist, read in a series of primary input events and then
for each step in the event list simulate the circuit until stable.
'''
import net
import gate
import getopt
import time
import testbench
import trace
import imp
import sys
import pin
import os
import primitive
import logic_extraction

goptions = {'verbose':False, 'nostrobe':False, \
                'stoponfail':False, 'stats':False, \
                'osclimit':40, "romfile":'' , \
                'gateopt':False, 'debug': '' }


def report_circuit_stats(tb):

    stats= []
    stats.append( '*   Number of signal nets: %d' % len ( [ n for n in (tb.get_nets(hier=True)) if not n.issupply ]))
    stats.append( '*   Number of gates: %d' % len(tb.get_gates(hier=True)))
    stats.append( '*   Number of modules: %d' % len([ i for i in tb.get_gates(hier=True) if not i.is_a_primitive]))
    stats.append( "*   Primitive instances:")
    stats.append( "* ")
    primitive_list = [ i for i in tb.get_gates(hier=True) if i.is_a_primitive]
    prim_count = dict()
    for i in primitive_list:
        name = i.__class__.__name__
        if name in prim_count:
            prim_count[name] += 1
        else:
            prim_count[name] = 1
    for i in sorted(prim_count.keys()):
        stats.append( "*    %-10s %4d" % ( i, prim_count[i]))
    stats.append( "*    %s %s" % ('-'*10, '-'*4))
    stats.append( '*    %-10s %4d' % ( 'Total', len(primitive_list)))
    stats.append( "*    %s %s" % ('-'*10, '-'*4))
    return '\n'.join(stats)


def static_optimization(tb):
    '''
    Perform simple static optimizations on the testbench/DUT
    '''
    # Find all nets which have a single input driver, no pullups/downs and no 
    # charge_storage attribute and reconfigure them to use the simple (non tri
    # state) net resolution function.

    messages_on = goptions['verbose'] 

    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    print "* Static Optimization"
    print "*"
    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    print '* Circuit Statistics before optimisation:\n*'
    print report_circuit_stats(tb)
    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'    


    # Standard static optimizations
    logic_extraction.eliminate_weak_transistors(tb, hier=True, verbose=True)
    logic_extraction.eliminate_diodes(tb, hier=True, verbose=True)
    logic_extraction.eliminate_common_sd_transistors(tb, hier=True, verbose=True)

#    for n in [ n for n in tb.get_nets(regexp='', hier=True)]:     
#        if not n.issupply:
#            n.charge_storage = True if (n.pullup_str ==0 and n.pulldown_str== 0) else False

    if goptions['gateopt']:
        print "* Extracting transistors to logic primitives. "
        logic_extraction.logic_extraction( tb, hier=True, verbose=messages_on, top_module=True, debug=goptions['debug']) 
        print "* Checking for orphaned nets ...",
        deleted_nets = tb.purge_nets(hier=True, verbose=messages_on)
        print " DONE\n* - Purged %d unconnected nets " % deleted_nets

    print "* Checking for unidirectional transistors ...",
    directional_count = logic_extraction.set_transistor_direction(tb, True, logic_opt=goptions['gateopt'])
    print " DONE\n* - Set %d transistor%s to be unidirectional" % \
        (directional_count,'s' if directional_count != 1 else '')

    print "* Checking for single driver nets... ", 
    count = 0
    for n in [ n for n in tb.get_nets(regexp='', hier=True)]:     
        if not n.issupply:
            n.value = '0'
            n.strength = 0
            if len(n.drivers) == 1 and n.pullup_str == 0 and n.pulldown_str == 0 :
                # print "Identified single driver on net ", n.fullname
                if n.charge_storage:
                    n.resolve = n.resolve_single_driver_with_storage
                else:
                    n.resolve = n.resolve_single_driver
                count += 1
            elif (n.pullup_str > 0 or n.pulldown_str > 0 ) :
                n.charge_storage = False
    print "DONE\n* - Found %d single driver nets" % count

    # Need to setup source/drain driver lists for all N(P)MOS gates after processing and annotate nets
    # connected to them
    print "* Finding bidirectional switches and annotating nets... ", 
    count = 0
    for g in [ g for g in tb.get_gates(regexp='', hier=True) if isinstance(g, (primitive.NMOS, primitive.PMOS))]:    
        count += 1
        drain = g.inputlist[0]
        source = g.inputlist[1]

        drain.has_bidir_elements = True
        source.has_bidir_elements = True

        if g.simulate not in drain.bidir_efanout:
            drain.bidir_efanout.append(g.simulate)            
        if g.simulate not in source.bidir_efanout:
            source.bidir_efanout.append(g.simulate)

        # build the lists of drivers to be considered when evaluating any NMOS gates
        g.source_drivers = [p for p in source.drivers if p != g.sourcepin ]
        g.drain_drivers = [p for p in drain.drivers if p != g.drainpin ] 
        # eliminate transistors in parallel (same source/drain + same or different gate) to avoid cyclic 
        # loops when evaluating nets. Any transistors which have supply as a terminal will already be directional
        source_parents = [p.parent for p in g.source_drivers]
        drain_parents = [p.parent for p in g.drain_drivers]
        delete_set = set()        
        for s in source_parents:
            if isinstance(s, primitive.NMOS) and s in drain_parents:
                delete_set.add(s)
        g.source_drivers = [ p for p in g.source_drivers if p.parent not in delete_set]
        g.drain_drivers = [ p for p in g.drain_drivers if p.parent not in delete_set]
        


    print "DONE\n* - Found %d bidirectional switches" % count

    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    print '* Circuit Statistics after optimisation:\n*'
    print report_circuit_stats(tb)
    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'    


def simulate( tb, max_pi_events=-1, trace_list = [], trace_mode="none"):
    '''
    Breadth first simulation
    
    '''

    if trace_mode == "event":
        traceevent = True
        traceon = True
    elif trace_mode == "end"  or trace_mode == "none":
        traceevent = False
        traceon = False
    else : # trace_mode == "tick"
        traceevent = False
        traceon = True

    verbose = goptions['verbose']
    statson = goptions['stats']
    osclimit = goptions['osclimit']
    nostrobe = goptions['nostrobe']

    # ensure that all gates in the top level netlist have their verbose
    # attribute set, if it exists
    if verbose:
        for g in tb.gatelist:
            if hasattr(g, "verbose"):
                g.verbose = True

    sticky_result = True

    netlist = tb.netlist
    if not len(tb.events) :
        print "Error - no events to simulate"
        return( None, 0, None, None, 0)
    elif max_pi_events <0:
        max_pi_events = len(tb.events)+1

    tr = trace.trace( trace_list, tb)
    if verbose:
        print tr.log_header()

    # supply nets start simulation with their correct values, but need to 
    # add their fanout to the eval list for the first pass through the 
    # simulation. Also resolve all nets based on 'X' starting values in
    # drivers
    eval_list = []
    for n in [ n for n in tb.get_nets(regexp='', hier=True)]:
        n.resolve()

#    # add all (simulatable) gates to the evaluation list for the first pass through - this seems to work better
#    # for gate level netlists though not for predominantly transistor level ones!        
    eval_list = [ [g.simulate for g in tb.get_gates(regexp='', hier=True) if hasattr(g,'simulate')] ]

    total_passes = 0
    total_fails = 0    
    stats = {"Rotations":[],
             "Wheel lengths": [],
             "Net Evals": [],
             "Gate Evals": [],
             }

    pi_count = -1

    s = time.time()

    for (events, po_events) in tb.events[:max_pi_events]:

        pi_count += 1
        loop_counter = 0

        if statson:
            stats["Wheel lengths"] = []
            stats["Gate Evals"] = []
            stats["Net Evals"] = []
        else:
            stats=None

        event_wheel = [ events ] 

        while event_wheel :
            loop_counter += 1    
            net_evals = 0
            # and add fanout of nets to the evaluation list
            if traceevent:                
                result = tr.log_changes(pi_count)[0]
                if verbose and result:
                    print result

            # first update all nets drivers based on the event_wheel contents, resolve the net
            # and add the fanout events to the evaluation list. 
            while event_wheel:
                for (n, state, driverpin ) in event_wheel.pop():
                    # some nets may enter the event_wheel more than once so only resolve those
                    # where a change could take place
                    if driverpin.state != state:
                        driverpin.state = state
                        net_evals +=1
                        eval_list.append(n.resolve())
                    
            if statson:
                stats["Wheel lengths"].append(len(event_wheel))
                stats["Gate Evals"].append(len(eval_list))    
                stats["Net Evals"].append(net_evals)
                stats["Rotations"] = [loop_counter+1]

            event_wheel = [ e() for ee in eval_list for e in ee ]
            eval_list = []
            
            if loop_counter > osclimit :
                print "* Oscillations detected, bailing out of simulation tick", pi_count
                break                                

        if not nostrobe or traceon:
            (result, passes, fails) = tr.log_changes(pi_count, po_events, nostrobe, \
                                                         stats=stats, traceon=traceon)        
            total_passes += passes
            total_fails += fails
            
            if result and verbose:
                print result

            if goptions['stoponfail'] and fails > 0:
                break

    e = time.time()
    if trace_mode == "end":
        result = tr.log_changes(pi_count, None, nostrobe, stats=None, traceon=True, force=True)[0]
        if verbose:
            print result

    if verbose:
        print tr.log_footer()
        
    return (tr, pi_count+1, total_passes, total_fails, (e-s))


            
def load_testbench( testbench_top='' , filename='', options=dict()):
    if filename.endswith('pyc'):
        tb_class =  imp.load_compiled(testbench_top, filename)
    elif filename.endswith('py'):
        tb_class =  imp.load_source(testbench_top, filename)
    else:
        print "testbench must be a python .py or .pyc file"
        sys.exit(2)
    
    # instance the top class in the testbench
    tb = getattr(__import__(testbench_top), testbench_top)(options)
    return tb

def usage():
    usage_string = '''

  USAGE:

    sim --top <top_module_name> --filename <filename> 

  MANDATORY SWITCHES

    -t | --top                Name of top (testbench) module 
    -f | --filename           Name of filename containing top module

  OPTIONAL SWITCHES
    -a | --tracemode <option> Select trace mode (to be used injunction with tracelist). Options
                              are:
                                tick   - update on each simulation tick
                                event  - update on each pass through event wheel
                                end    - update at end of simulation only
                                none   - no traces emitted

                              Default is 'none' unless the --tracelist option is used, in
                              which case 'tick' is set automatically. 
           
    -l | --tracelist <list>   Space separated list of signals to trace. Use '-' character
                              to add spaces into trace. Use python regexps for busses etc.
                              Use this option as many times as necessary to build up a full
                              tracelist (see examples below).
    -m | --max <int>          Maximum number of simulation ticks to run
    -r | --romfile <filename> Specify a ROM file to be used with a single rom32k primitive
    -x | --ramdump <options>  Options are a colon separated string of variable assigments. The
                              following are available:
                                filename=<filename>
                                lo=<low address>
                                numbytes=<numbytes>
                                hi=<high address>
               
                              At least one option, or a dummy string must be preset for this
                              switch.
    -d | --stats              Display stats with trace
    -g | --gateopt            Optimize transistors to logic primitives where possible
    -h | --help               Show this help message
    -n | --nostrobe           Ignore expected data in any testbench vector file
    -o | --osclimit           Set max number of passes through event wheel for a simulation 
                              tick. If this number is exceeded a warning is issued and simulation
                              moves onto the next tick. Default is 40.
    -s | --stoponfail         Stop simulation if simulation data doesn't match expected data
                              in testbench vector file
    -v | --verbose            Print traces as each cycle is executed (default it wait 'til the
                              end of simulation). Provide additional run time info
   
   EXAMPLES

     python sim.py --top domino_tb --filename examples/domino_tb.py \\
                   --tracelist 'in0 in1 in2 - prech - n0 n1 n2 n3 - out ' --max 16 


     # Remember to setup python path if any netlist modules need to reference
     # other submodules in different directories.
     setenv PYTHONPATH .:examples
     # 6502 examples
     pypy sim.py --top v6502_nop_tb --filename examples/v6502_nop_tb.py \\
         --tracelist 'rstb_w - phi0_w - phi1_w phi2_w - addr.* - data.* - sob_w rnw_w sync_w - v6502_0_u.pcl. '\\
         --tracelist '- v6502_0_u.ir. ' \\
         --tracelist '- v6502_0_u.clock. - v6502_0_u.adh. v6502_0_u.adl. - v6502_0_u.notidl. - v6502_0_u.idl.' \\
         --verbose --max 128

'''
    print usage_string
    sys.exit(2)

def main( argv ) :

    filename = ''
    top_module = ''
    global goptions

    tb_options = dict()
    trace_list = []
    trace_mode = "none"
    max = -1
    try:
        opts, args = getopt.getopt(argv[1:], "f:t:a:l:m:o:r:x:b:vnsdgh", \
                                       ["filename=","top=","tracemode=", "tracelist=",\
                                            "max=","osclimit=",\
                                            "romfile=", "ramdump=", "debug=", "verbose",\
                                            "nostrobe", "stoponfail","stats", "gateopt", \
                                            "help"])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    for opt,arg in opts:
        if opt in ("-f", "--filename"):
            filename=arg
        elif opt in ("-t", "--top"):
            top_module=arg
        elif opt in ("-b", "--debug"):
            goptions['debug'] = arg
        elif opt in ("-l", "--tracemode"):            
            if arg in [ "event", "end", "tick", "none"]:
                trace_mode = arg
        elif opt in ("-l", "--tracelist"):            
            trace_list.extend( arg.split())
            if trace_mode == "none":
                trace_mode = "tick"
        elif opt in ("-m", "--max"):            
            max = int(arg)
        elif opt in ("-d", "--stats"): 
            goptions['stats'] = True
        elif opt in ("-g", "--gateopt"):
            goptions['gateopt'] = True
        elif opt in ("-h", "--help"):
            usage()
        elif opt in ("-n", "--nostrobe"):            
            goptions['nostrobe'] = True
        elif opt in ("-o", "--osclimit"):            
            goptions['osclimit'] = int(arg)        
        elif opt in ("-s", "--stoponfail"):            
            goptions['stoponfail'] = True
        elif opt in ("-v", "--verbose"):            
            goptions['verbose'] = True
        elif opt in ("-r", "--romfile"):
            tb_options["rom_filename"] = arg
            if not os.path.exists("%s" %arg) :
                print "Error - specified ROM file %s does not exist" % arg
                sys.exit(2)
        elif opt in ("-x", "--ramdump"):
            if ':' in arg:
                myargs = arg.split(':')
                tb_options["ramdump"] = dict()
                for subopt in myargs:
                    f = subopt.split('=')
                    tb_options["ramdump"][f[0]] = f[1]
            else:
                tb_options["ramdump"] = [True]


    if filename=='' or top_module=='':
        usage()
    print '''

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
* C A R O U S E L  - mixed mode switch & logic simulation
*
* (c) Richard Evans 2011
*
* $Revision$
*
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
'''
    print '*', 
    for i in argv:
        print i,
    print

    tb = load_testbench( top_module, filename, tb_options)    
    static_optimization( tb ) 

    (trace, ticks, passes, fails, run_time)  = simulate(tb, max_pi_events = max, \
                                                            trace_list=trace_list, trace_mode=trace_mode)

    if not goptions['verbose']:
        print trace.to_string()
    print 

    for g in tb.gatelist:
        g.finish_simulation(tb_options)

    if not goptions['nostrobe']:
        if fails == 0 and passes > 0:
            print 'PASS: all %d comparisons between simulation and expected data match' % (passes + fails)
        elif fails >0 :
            print 'FAIL: mismatch on %d of %d comparisons (%3.2f%%) between simulation and expected data'% ( fails, passes+fails, float(fails)*100.0/float(passes+fails))
    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    print '* Statistics:'
    print '*   Number of signal nets: %d' % len ( [ n for n in (tb.get_nets(hier=True)) if not n.issupply ])
    print '*   Number of gates: %d' % len(tb.get_gates(hier=True))
    print '*   Number of primitives: %d' % len([ i for i in tb.get_gates(hier=True) if i.is_a_primitive])
    print '*   Number of modules: %d' % len([ i for i in tb.get_gates(hier=True) if not i.is_a_primitive])
    print '*   Number of simulation ticks: %d' % ticks
    print "*\n*   Run time = %1.3f s" % run_time
    print "*   Simulation Ticks/s = %4.2f Hz" % ( ticks/(run_time+0.0000001))
    print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'

    # top 20 nets by number of calls to net resolution

#    print sorted( [(n.resolution_ctr, n.fullname) for n in (tb.get_nets(hier=True)) ])[-100:]
#    print sorted( [(n.toggle_ctr, n.fullname) for n in (tb.get_nets(hier=True)) ])[-100:]
    

#    for n in (tb.get_nets(hier=True)) :
#        if  n.issupply:
#            print n.fullname, n.value, n.strength
#
#    for n in (tb.get_nets(hier=True)) :
#        if  not n.issupply:
#            print n.fullname, n.value, n.strength

    tb.write_netlist(filename="%s-reopt.py" % top_module)

    # report all nets in the design
#    for n in tb.get_nets(regexp=".*", hier=True):
#        print n.fullname
#        print n.efanout, n.all_fanout, n.prim_fanout, n.drivers
#        if n.drivers:
#            for p in n.drivers:
#                print p.fullname
    # for n in sorted(tb.netlist):
    # print the value
    # print tb.netlist[n].to_str(),
    # print the ports/pins which drive the net
    # print netlist[n].drivers.keys(), 
    #  print the full list of ports (ie incl hierarchy)
    #    print "FANIN: ",
    #    for d in  netlist[n].all_fanin:
    #        print d.fullname, 
    #    print "FANOUT: ",
    #    for d in  netlist[n].fanout:
    #        print d.fullname, 
    #print
        





if __name__ == '__main__':
    main( sys.argv )
