'''
Simple utilities for extracting primitive logic element from
transistors in a standard module.
'''
import gate
import primitive
import net
import re

gbydiff =dict()
gbygate = dict()

ginvert_buffer_lut = { 
    primitive.BUF:primitive.INV,
    primitive.INV:primitive.BUF
}

ginvert_fn_lut = {
    primitive.BUF:primitive.INV,
    primitive.INV:primitive.BUF,
    primitive.AND:primitive.NAND,
    primitive.OR:primitive.NOR,
    primitive.NAND:primitive.AND, 
    primitive.NOR:primitive.OR,
    primitive.DLATB:primitive.DLAT,
    primitive.DLAT:primitive.DLATB,
    primitive.AOI:primitive.AO,
    primitive.AO:primitive.AOI, 
    primitive.MUX21:primitive.NMUX21
    };

gnext_gate_idx = 10000


def eliminate_weak_transistors(mod, hier=True, verbose=False):
    # Remove weak transistors
    print "* Eliminating weak transistors ... ", 
    delete_set = set()
    for g in [ g for g in mod.get_gates(regexp='', hier=hier) if isinstance(g, (primitive.NMOS, primitive.PMOS))]:    
        if g.isweak and g.parent != None:
            delete_set.add(g)

    print "DONE\n* - Found %d weak transistors" % len(delete_set)
    for g in delete_set:
        g.parent.delete_gate(g, False)


def eliminate_diodes(mod, hier=True, verbose=False):
    # Eliminate all transistors with source or drain and gate connected to GND
    if verbose:
        print "* Checking for transistors wired as diodes ...",

    transistor_list = mod.get_gates_by_type(type=primitive.NMOS, hier=hier)
    transistor_list.extend(mod.get_gates_by_type(type=primitive.UNMOS, hier=hier))
    delete_set = set()
    for tr in transistor_list:
        source = tr.port['SOURCE'].netconn
        drain = tr.port['DRAIN'].netconn
        gate = tr.port['GATE'].netconn
        if (source==gate) or (drain==gate):
            if gate.issupply and isinstance(gate, net.supply0):
                # print tr.fullname(), tr.parent.fullname()
                delete_set.add(tr)

    if verbose:
        print "DONE\n* - Found %d." % len(delete_set)

    for g in delete_set: 
        # print "deleting diode ", g, g.tostring()
        g.parent.delete_gate(g, False)
   

def eliminate_common_sd_transistors(mod, hier=True, verbose=False):
    # Eliminate all transistors with source and drain connected together (capacitors?)
    if verbose:
        print "* Checking for transistors with common source and drain...",
    transistor_list = mod.get_gates_by_type(type=primitive.NMOS, hier=hier)
    transistor_list.extend(mod.get_gates_by_type(type=primitive.UNMOS, hier=hier))
    delete_set = set()
    for tr in transistor_list:
        if tr.port['SOURCE'].netconn == tr.port['DRAIN'].netconn:
            delete_set.add(tr)

    if verbose:
        print "DONE\n* - Found %d." % len(delete_set)

    for g in delete_set: 
        g.parent.delete_gate(g, False)
    


def set_transistor_direction(mod, hier=True, logic_opt=False):
    # swap all bidir transistors with either source or drain 
    # connected to a supply for unidir type
    directional_count = 0
    delete_set = set()
    newtr_list = []
    
    for tr in mod.get_gates_by_type(type=primitive.NMOS, hier=hier): 
        source = tr.port['SOURCE'].netconn
        drain = tr.port['DRAIN'].netconn
        ggate = tr.port['GATE'].netconn
        if source.issupply or drain.issupply:
            if drain.issupply and not source.issupply:
                newtr_list.append((tr.parent, (tr.name, [source, drain, ggate], tr.parent, tr.isweak)))
            else:
                newtr_list.append((tr.parent, (tr.name, [drain, source, ggate], tr.parent, tr.isweak)))
            directional_count += 1
            delete_set.add(tr)

    # ensure that all supply connections are dealt with first before identifying more pass gates
    for g in delete_set: 
        g.parent.delete_gate(g, False)    
    for (m,g) in newtr_list:
        m.gatelist.append(primitive.UNMOS(g[0], g[1], g[2], g[3]))

    update_dict = dict()
    duplicate_list = []

    if logic_opt: 
        for g in  [ m for m in mod.get_gates(regexp=".*", hier=hier) if m.is_a_primitive ]:
            # for all logic gates set direction on any pass gates attached to the output
            if not(isinstance(g, (primitive.INV_APU, primitive.NOR_APU, primitive.NAND_APU)) or \
                        isinstance(g, (primitive.NMOS, primitive.UNMOS)) or g.pullup_str< net.DEPL_STR):
                for p in g.outputpins.values():
                    n = p.netconn
                    for f in n.prim_fanout:
                        if isinstance(f, primitive.NMOS):
                            source = f.port['SOURCE'].netconn
                            drain = f.port['DRAIN'].netconn
                            ggate = f.port['GATE'].netconn
                            
                            if (drain==n or source==n) and not ggate==n:
                                if drain==n:
                                    drain = source
                                    source = n

                                end_pt_pullup_str = max([ss.strength for ss in drain.all_gate_fanin])
                                # on the first pass gate after a proper gate with pullup surely this is 
                                # unidirectional gate ? 6800 has gates connected together like this though
                                # so not clear which is the 'winner' and able to set the direction.
                                if (drain.pullup_str==0 and end_pt_pullup_str==0):
                                    if f in update_dict:
                                        duplicate_list.append(f)
                                    else:
                                        update_dict[f] = (f.parent,  (f.name, [drain,source,ggate], f.parent, f.isweak))

    
    for key in update_dict:
        (m, g) =  update_dict[key]
        if key not in duplicate_list:
            # don't replace any transistors which might have conflicting directions
            directional_count +=1        
            key.parent.delete_gate(key, False)
            m.gatelist.append(primitive.UNMOS(g[0], g[1], g[2], g[3]))


    # Process bidirs which only have connections to logic or transistor input pins, ie
    # don't expect that charge stored on those inputs is ever used to drive back through
    # the pass gate, so we can assume that these are unidirectional. Run several passes
    # to pick up chains of pass gates, one level at a time.
    found_more = True
    pass_count = 0
    while found_more and pass_count < 5:
        found_more = False
        update_dict = dict()
        pass_count += 1
        unmos_count = 0
        for f in mod.get_gates_by_type(type=primitive.NMOS, hier=hier) :
            source = f.port['SOURCE'].netconn
            drain = f.port['DRAIN'].netconn
            ggate = f.port['GATE'].netconn
            # connects to one or more logic/unmos inputs but this is the only driver
            if (len(source.prim_fanout) >=1 and len(source.drivers)==1 and source.pullup_str==0):
                unmos_count += 1
                update_dict[f] = (f.parent,  (f.name, [source,drain,ggate], f.parent, False))
                found_more = True
            elif (len(drain.prim_fanout) >=1 and len (drain.drivers)==1 and drain.pullup_str==0) :
                unmos_count += 1
                update_dict[f] = (f.parent,  (f.name, [drain,source,ggate], f.parent, False))                           
                found_more = True
            # Next two have inputs only on one side of the device (apart from this NMOS being considered), drivers on the other (incl. the NMOS)
            elif (len(drain.prim_fanout)==1 and len(drain.drivers) >0) and source.pullup_str==0 :
                unmos_count += 1
                update_dict[f] = (f.parent,  (f.name, [source,drain,ggate], f.parent, False))
                found_more = True
            elif (len(source.prim_fanout)==1 and len(source.drivers)>0) and drain.pullup_str==0:
                unmos_count += 1
                update_dict[f] = (f.parent,  (f.name, [drain,source,ggate], f.parent, False))                           
                found_more = True

                
            
        for key in update_dict:
            (m, g) =  update_dict[key]
            directional_count +=1        
            key.parent.delete_gate(key, False)
            m.gatelist.append(primitive.UNMOS(g[0], g[1], g[2], g[3]))

    return directional_count


def logic_extraction(mod, hier=True , verbose = False, top_module = True, debug = "") :

    global gbydiff
    global gbygate

    if verbose:
        print "* Identifying logic gate structures...",

    # now find all transistor primitives and the complete list of nets in the design
    nmos_list = mod.get_gates_by_type(type=primitive.NMOS, hier=hier)
    nmos_list.extend(mod.get_gates_by_type(type=primitive.UNMOS, hier=hier))
    nets_list = mod.get_nets(hier=hier)
    # build the dict sorted by diffusion
    for n in nmos_list:
        source = n.port['SOURCE'].netconn
        drain = n.port['DRAIN'].netconn
        gate = n.port['GATE'].netconn
        
        t = (n.name, n, gate, source, drain)

        for s in (source, drain):
            if s not in gbydiff:
                gbydiff[s] = [t]
            else:
                gbydiff[s].append(t)

        if not gate in gbygate:
            gbygate[gate] = [t]
        else: 
            gbygate[gate].append(t)
    

    pulldown = dict()
    pullup = dict()
    # process all nodes which have depletion devices and find the pulldown trees
    depletion_nets = set()
    for k in nets_list:
        if k.pullup_str > 0:
            depletion_nets.add(k)

    # try adding nets with single active pullup to the list
    for n in nets_list:
        if not n in depletion_nets and not n.issupply:
            for g in n.prim_fanout:
                if (isinstance(g, primitive.NMOS) and \
                        (isinstance(g.port['DRAIN'].netconn, net.supply1) or \
                             isinstance(g.port['SOURCE'].netconn, net.supply1))):
                    if n==g.port['DRAIN'].netconn or n==g.port['SOURCE'].netconn:
                        depletion_nets.add(n)


    for n in depletion_nets:
        if not n.issupply :
            pulldowneqn= []
            pullupeqn= []
            passgateeqn = []            
            generate_graphs_dfs(n, [], [], pulldowneqn, pullupeqn, passgateeqn) 
            if pulldowneqn :
                pulldown[n] = reduce_and_or_terms(pulldowneqn)
            if pullupeqn :
                pullup[n] = reduce_and_or_terms(pullupeqn)

            # Need to strip out any pulldowns trees which share devices in the passgate eqn
            all_pass_gates = set()
            for plist1 in passgateeqn:
                for p in plist1:
                    all_pass_gates.add(p)

            revised_pulldown = []  
            if n in pulldown:
                for pd in pulldown[n]:                                        
                    result = True
                    for tr in pd:
                        if tr in all_pass_gates:
                            result = False
                    if result:
                        revised_pulldown.append(pd)
                if revised_pulldown:
                    pulldown[n] = revised_pulldown
                else:
                    pulldown.remove(n)

    delete_set = set()
    newgate_list = []
    newgate_idx = 0

    for n in pulldown:
        #turn pulldown list into simple list of gate nodes
        gatepin_list = []
        for pd in pulldown[n]:
            subtree = set()
            for g in pd:
                subtree.add(g[2])
            gatepin_list.append(list(subtree))



        parent =  None
        successful_ident=False
        for pd in pulldown[n]:
            for g in pd:
                my_parent=g[1].parent

        if len(gatepin_list)==1 and len(gatepin_list[0])== 1:
            if n in pullup and len(pullup[n])==1 and len(pullup[n][0])==1 :
                (name, id, gt, src, dr) = pullup[n][0][0]
                delete_set.add(id)
                newgate_list.append((my_parent, primitive.INV_APU("reopt_%s" % (name), \
                                                                        n,[gt, gatepin_list[0][0]], \
                                                                        strength=net.SUPPLY_STR, \
                                                                        parent=my_parent)))
                newgate_idx += 1
                successful_ident=True
            elif n.pullup_str >0:
                newgate_list.append((my_parent, primitive.INV("reopt_gate_%d" % newgate_idx, \
                                                                    [n, gatepin_list[0][0]], \
                                                                    pulldown_str=net.SUPPLY_STR, pullup_str=net.DEPL_STR, \
                                                                    parent=my_parent)))
                n.pullup_str =0
                newgate_idx += 1
                successful_ident=True

        elif len(gatepin_list)==1  and len(gatepin_list[0])> 1 :
            nets = [n]
            nets.extend(gatepin_list[0])            
            if n in pullup and len(pullup[n])==1 and len(pullup[n][0])==1 :
                (name, id, gt, src, dr) = pullup[n][0][0]
                delete_set.add(id)
                nets = [gt]
                nets.extend([p[0] for p in gatepin_list])                
                newgate_list.append((my_parent, primitive.NAND_APU("reopt_gate_%d" % newgate_idx, \
                                                                        [n]+ nets, \
                                                                        strength=net.SUPPLY_STR, \
                                                                        parent=my_parent)))                
                newgate_idx += 1
                successful_ident=True
            elif n.pullup_str >0:
                newgate_list.append((my_parent, primitive.NAND("reopt_gate_%d" % newgate_idx, nets, \
                                                                     pulldown_str=net.SUPPLY_STR, pullup_str=n.pullup_str,\
                                                                     parent=my_parent)))
                n.pullup_str = 0
                newgate_idx += 1
                successful_ident=True
            else:
                newgate_list.append((my_parent, primitive.NAND_OD("reopt_gate_%d" % newgate_idx, n, gatepin_list, \
                                                                     pulldown_str=net.SUPPLY_STR, pullup_str=n.pullup_str,\
                                                                     parent=my_parent)))
                newgate_idx += 1
                successful_ident=True


        elif len(gatepin_list) > 1 and max([ len(subtree) for subtree in gatepin_list ])==1:
            nets = [n]
            nets.extend([p[0] for p in gatepin_list])
            if n in pullup and len(pullup[n])==1 and len(pullup[n][0])==1 :
                (name, id, gt, src, dr) = pullup[n][0][0]
                delete_set.add(id)
                nets = [gt]
                nets.extend([p[0] for p in gatepin_list])                
                newgate_list.append((my_parent, primitive.NOR_APU("reopt_gate_%d" % newgate_idx, \
                                                                        [n]+ nets, \
                                                                        strength=net.SUPPLY_STR, \
                                                                        parent=my_parent)))
                
                newgate_idx += 1
                successful_ident=True
            elif n.pullup_str>0:
                # net has full depletion pullup so instantiate complete logic gate
                newgate_list.append((my_parent, primitive.NOR("reopt_gate_%d" % newgate_idx, nets , my_parent)))
                n.pullup_str = 0
                newgate_idx += 1
                successful_ident=True
            else:
                # net has active pullup so need open drain pulldown only
                newgate_list.append((my_parent, primitive.NOR_OD("reopt_gate_%d" % newgate_idx, n, [p[0] for p in gatepin_list] , my_parent)))
                newgate_idx += 1
                successful_ident=True
        elif len(gatepin_list) > 1 and max([ len(subtree) for subtree in gatepin_list ]) > 1 :
            if n.pullup_str>0:
                newgate_list.append((my_parent, primitive.AOI("reopt_gate_%d" % newgate_idx, n, gatepin_list, my_parent)))
                n.pullup_str = 0
                newgate_idx += 1
                successful_ident=True
            else:
                newgate_list.append((my_parent, primitive.AOI_OD("reopt_gate_%d" % newgate_idx, n, gatepin_list, my_parent)))
                newgate_idx += 1
                successful_ident=True

        if successful_ident:
            for pd in pulldown[n]:
                for g in pd:
                    my_parent=g[1].parent
                    delete_set.add(g[1])


    if verbose:
        print "DONE"
        print "* - Found %d logic elements, eliminated %d transistors" % \
            (len(newgate_list),len(delete_set))

    for g in delete_set: 
        g.parent.delete_gate(g, False)

    if newgate_list:
        for (m,g) in newgate_list:
            m.gatelist.append(g)

    logic_extraction_pass2(mod, hier=hier , verbose=verbose, top_module=top_module, debug=debug) 



def logic_extraction_pass2(mod, hier=True , verbose = False, top_module = True, debug=""): 
    print "* Merging logic functions ... "

    changes = 1
    passes = 0
    while changes:
        passes += 1
        print '* Pass %2d: Merging inverters and buffers' % passes
        changes = rollup_inv_buf_gates(mod, hier, verbose, ginvert_buffer_lut, restricted_fanout=True)
        changes += rollup_apu_gates(mod, hier, verbose, debug=debug)
        print '* Pass %2d: Processing feedback transistors and latches' % passes
        changes += process_latches_pass2(mod, hier, verbose)
        print '* Pass %2d: Merging inverters and buffers with other logic' % passes    
        changes += rollup_inv_buf_gates(mod, hier, verbose, ginvert_fn_lut, restricted_fanout=True)
        print '* Pass %2d: Setting transistor directions' % passes    
        changes += set_transistor_direction(mod, hier=True, logic_opt=True)

        print "* Pass %2d: Processing latches" % passes
        changes += process_latches_v3(mod, hier=True, verbose=False, debug=debug)

    #mod.write_netlist(filename="debug-preopt.py")
# Was failing MEM_TEST and JSR_TEST but passing with this disabled.
#    print '* Pass %2d: Merging inverters and buffers with unrestricted fanout' % passes
#    rollup_inv_buf_gates(mod, hier, verbose, ginvert_buffer_lut, restricted_fanout=False, debug=debug)
    #mod.write_netlist(filename="debug-postopt.py")
    print '* Pass %2d: Processing feedback transistors and latches' % passes
    process_latches_pass2(mod, hier, verbose)
    print '* Pass %2d: Processing mux21 structures' % passes    
    process_mux21_gates(mod, hier, verbose)
    print '* Pass %2d: Merging inverters and buffers with other logic' % passes    
    changes += rollup_inv_buf_gates(mod, hier, verbose, ginvert_fn_lut, restricted_fanout=True)

    spot_cross_coupled_gates(mod, hier, verbose, primitive.NAND)
    spot_cross_coupled_gates(mod, hier, verbose, primitive.NOR)
    spot_clocked_cross_coupled_gates(mod, hier, verbose, primitive.NOR)
    spot_clocked_cross_coupled_gates(mod, hier, verbose, primitive.NAND)
    
    return


def spot_cross_coupled_gates(mod, hier=True, verbose=False, gate_type=primitive.NOR):
    ccgate_count = 0
    for g in mod.get_gates_by_type(gate_type, hier=hier):
        for fo in g.outputnet.prim_fanout:
            if isinstance(fo, gate_type) and (fo.outputnet in g.inputlist):
                ccgate_count += 1
                print "* Cross coupled gate #", ccgate_count
                for k in [g, fo]:
                    print "* - ", k.tostring()

def spot_clocked_cross_coupled_gates(mod, hier=True, verbose=False, gate_type=primitive.NOR):
    
    ccgate_count = 0

    for g in mod.get_gates_by_type(gate_type, hier=hier):
        g_outnet = g.outputnet
        for fo in g_outnet.prim_fanout:
            if isinstance(fo, (primitive.UNMOS, primitive.NMOS)):
                if fo.port['SOURCE'].netconn == g_outnet:
                    fo_outnet = fo.port['DRAIN'].netconn
                else:
                    fo_outnet = fo.port['SOURCE'].netconn                

                for fo1 in fo_outnet.prim_fanout:                    
                    if isinstance(fo1, (primitive.NOR, primitive.AOI, primitive.NAND )):
                        fo1_outnet = fo1.outputnet
                        for fo2 in fo1_outnet.prim_fanout:
                            if isinstance(fo2, (primitive.UNMOS, primitive.NMOS) ):
                                if fo2.port['SOURCE'].netconn == fo1_outnet:
                                    fo2_outnet = fo2.port['DRAIN'].netconn
                                else:
                                    fo2_outnet = fo2.port['SOURCE'].netconn                

                                if g in fo2_outnet.prim_fanout:

                                    # restrict spotting to pairs where the first one is a 2 input gate for now
                                    if len(g.inputlist) == 2:
                                        ccgate_count += 1
                                        print "* Clocked cross coupled gates #", ccgate_count
                                        for k in [g, fo, fo1, fo2]:
                                            print "* - ", k.tostring()

                                        if ( isinstance(g, primitive.NOR) and isinstance(fo1, primitive.NOR)):

                                            # For 2 input NORs the 'other' input is the one not involved in the loop
                                            ran = g.inputlist[0] if g.inputlist[0] != fo2_outnet else g.inputlist[1]
                                            rbn = list( fo1.inputlist ) 
                                            rbn.remove( fo_outnet )                                            
                                        
                                            print( '* mslat( Q(%s), QB(%s), RAN(%s), PHIA(%s), RBN(%s), PHIB(%s)) ' % \
                                                       ( g_outnet.fullname, fo1_outnet.fullname, ran.fullname, \
                                                             fo.port['GATE'].netconn.fullname,\
                                                             [n.fullname for n in rbn], \
                                                             fo2.port['GATE'].netconn.fullname))
                                            


def process_mux21_gates(mod, hier=True, verbose=False ) :
    global gnext_gate_idx
    nmos_list = mod.get_gates_by_type(type=primitive.NMOS, hier=hier)
    nmos_list.extend(mod.get_gates_by_type(type=primitive.UNMOS, hier=hier))

    mux_count = 0
    delete_set = set()
    driver_set = set()
    newgate_list = []

    for tr1 in nmos_list:
        for tr2 in nmos_list:
            if tr1 != tr2 and tr1 not in delete_set and tr2 not in delete_set:
                if tr1.port['DRAIN'].netconn == tr2.port['DRAIN'].netconn or \
                   tr1.port['SOURCE'].netconn == tr2.port['DRAIN'].netconn or \
                   tr1.port['DRAIN'].netconn == tr2.port['SOURCE'].netconn or \
                   tr1.port['SOURCE'].netconn == tr2.port['SOURCE'].netconn :
                    gate1 = tr1.port['GATE'].netconn
                    gate2 = tr2.port['GATE'].netconn
                    if len(gate1.all_gate_fanin) == 1 and len(gate2.all_gate_fanin) == 1:
                        driving_cell2 = list(gate2.all_gate_fanin)[0]
                        driving_cell1 = list(gate1.all_gate_fanin)[0]
                        if isinstance(driving_cell2, primitive.INV) and isinstance(driving_cell1, primitive.BUF):
                            if driving_cell1.port['I0'].netconn == driving_cell2.port['I0'].netconn: 
                                mux_count +=1
                                driver_set.add(driving_cell1)
                                driver_set.add(driving_cell2)
                                delete_set.add(tr1)
                                delete_set.add(tr2)

                                if tr1.port['DRAIN'].netconn in [tr2.port['DRAIN'].netconn, tr2.port['SOURCE'].netconn]:
                                    outputnet = tr1.port['DRAIN'].netconn
                                    input1 = tr1.port['SOURCE'].netconn
                                else:
                                    outputnet = tr1.port['SOURCE'].netconn
                                    input1 = tr1.port['DRAIN'].netconn

                                if tr2.port['DRAIN'].netconn == outputnet:
                                    input0 = tr2.port['SOURCE'].netconn
                                else:
                                    input0 = tr2.port['DRAIN'].netconn

                                select = driving_cell1.port['I0'].netconn
                                ng = primitive.MUX21(name="reopt_mux21_%d" % gnext_gate_idx, \
                                                 nlist = [ outputnet, input0, input1, select], \
                                                 pulldown_str = net.SUPPLY_STR, \
                                                 pullup_str = net.DEPL_STR, \
                                                 parent = tr1.parent )
                                newgate_list.append( (tr1.parent, ng) )
                                                 
                                                 
                    elif len(gate2.all_gate_fanin) == 1:
                        driving_cell = list(gate2.all_gate_fanin)[0]
                        if isinstance(driving_cell, primitive.INV) :
                            if driving_cell.port['I0'].netconn == gate1:
                                mux_count +=1
                                driver_set.add(driving_cell)
                                delete_set.add(tr1)
                                delete_set.add(tr2)

                                if tr1.port['DRAIN'].netconn in [tr2.port['DRAIN'].netconn, tr2.port['SOURCE'].netconn]:
                                    outputnet = tr1.port['DRAIN'].netconn
                                    input1 = tr1.port['SOURCE'].netconn
                                else:
                                    outputnet = tr1.port['SOURCE'].netconn
                                    input1 = tr1.port['DRAIN'].netconn

                                if tr2.port['DRAIN'].netconn == outputnet:
                                    input0 = tr2.port['SOURCE'].netconn
                                else:
                                    input0 = tr2.port['DRAIN'].netconn

                                select = driving_cell.port['I0'].netconn
                                ng = primitive.MUX21(name="reopt_mux21_%d" % gnext_gate_idx, \
                                                 nlist = [ outputnet, input0, input1, select], \
                                                 pulldown_str = net.SUPPLY_STR, \
                                                 pullup_str = net.DEPL_STR, \
                                                 parent = tr1.parent )
                                newgate_list.append( (tr1.parent, ng) )

    print "* - identified %d mux21 gates" % mux_count

    for g in delete_set:
        g.parent.delete_gate(g, False)
        
    for (p,g) in newgate_list:
        p.gatelist.append(g)
            
    for g in driver_set:
        if len(g.outputnet.prim_fanout)==0 :
            g.parent.delete_gate(g, False)
    
    return mux_count
                




def rollup_inv_buf_gates(mod, hier=True, verbose=False, lookup_table=dict(), restricted_fanout=True, debug=""):
    '''
    Need to be able to restrict the swapping to inv/buf only to help with 
    rolling up latches and APU gates. Call again without the restriction
    after this is complete.

    restrict fanout allows swapping only where driver has no other fanout - avoid nets forking
    '''
    noopt_nets = [ "v6502_0_u.n358", # Fail INC test and rolror test
                   "v6502_0_u.ir0", 
                   "v6502_0_u.ir1", # fail rolror test
                   "v6502_0_u.ir2", 
                   "v6502_0_u.ir3",  # Fail INC test
                   "v6502_0_u.ir4",
                   "v6502_0_u.ir5", 
                   "v6502_0_u.ir6",
                   "v6502_0_u.ir7", # Fail INC test and rolror test
                   "v6502_0_u.n1715" # Fail INC test and rolror test
                   ]


    changes = 0
    delete_set = set([1]) 
    global gnext_gate_idx
    while delete_set:
        delete_set = set()
        driver_set = set()
        newgate_list = []

        candidate_list = mod.get_gates_by_type(type=primitive.INV, hier=hier)
        candidate_list.extend(mod.get_gates_by_type(type=primitive.BUF, hier=hier))
        for c in candidate_list:
            if (c not in driver_set) and (c not in delete_set):
                # need to go around the loop again if a buffer/inv has already been identified as
                # a driver gate in case it should get optimized away rather than transformed
                innet = c.inputlist[0]
                if len(innet.drivers)==1 and len(innet.all_gate_fanin)==1:
                    if (len(innet.prim_fanout)==1 and restricted_fanout) or \
                            (not restricted_fanout and innet.fullname not in noopt_nets ):
                        driver_gate = list(innet.all_gate_fanin)[0]                        
                        # even if we don't invert the gate must be in the LUT to be sure that the input
                        # parameters are consistent
                        if c.parent==driver_gate.parent:
                            driver_gate_type = driver_gate.__class__
                            if driver_gate_type in lookup_table:
                                # print c.fullname(),c.__class__.__name__, innet.drivers, innet.all_gate_fanin                            
                                if isinstance(c, primitive.BUF):
                                    newgate = driver_gate_type
                                else:
                                    newgate = lookup_table[driver_gate_type]
                                    
#                                if not restricted_fanout:
#                                    print "CANDIDATE BEFORE", c.tostring(), [g.tostring() for g in innet.prim_fanout]

                                
                                delete_set.add(c)
                                driver_set.add(driver_gate)
                                # create gate with mix of input gate and output gate parameters
                                if isinstance(driver_gate, (primitive.AOI, primitive.AO)):
                                    ng = newgate(name="reopt_gate_pass2_%d" % gnext_gate_idx, \
                                                     outputnet = c.outputnet, \
                                                     nlist= driver_gate.inputlist, \
                                                     pulldown_str=c.pulldown_str,\
                                                     pullup_str=c.pullup_str,\
                                                     parent=c.parent)
                                else:
                                    ng = newgate(name="reopt_gate_pass2_%d" % gnext_gate_idx, \
                                                     nlist=[ c.outputnet] + driver_gate.inputlist,\
                                                     pulldown_str=c.pulldown_str,\
                                                     pullup_str=c.pullup_str,\
                                                     parent=c.parent)

                                newgate_list.append((c.parent,ng ))
#                                if (not restricted_fanout and isinstance(c, primitive.INV)):
#                                    print "CANDIDATE AFTER", ng.tostring(),[g.tostring() for g in innet.prim_fanout]


                                changes += 1
                                gnext_gate_idx += 1
        
        for g in delete_set:
            g.parent.delete_gate(g, False)

        for (p,g) in newgate_list:
            p.gatelist.append(g)
            
        for g in driver_set:
            if len(g.outputnet.prim_fanout)==0 :
                g.parent.delete_gate(g, False)

    return changes

def rollup_apu_gates(mod, hier=True, verbose=False, debug=""):
    changes = 0

    global gnext_gate_idx


    # Eliminate parallel copies of INV_APU (increased drive)    
    gate_dict = dict()
    for c in mod.get_gates_by_type(type=primitive.INV_APU, hier=hier):
        if c.outputnet in gate_dict:
            gate_dict[c.outputnet].append(c)
        else:
            gate_dict[c.outputnet] = [c]

    for node in gate_dict:
        if len(gate_dict[node]) > 1 :
            ref = gate_dict[node][0]
            for other in gate_dict[node][1:]:
                if ref.inputlist==other.inputlist:
                    other.parent.delete_gate(other)
                    print "* Removing parallel INV_APU gate ", other.fullname()
                    changes += 1
                
    delete_set = set([1]) 
    while delete_set:
        delete_set = set()
        driver_set = set()
        newgate_list = []

        candidate_list = mod.get_gates_by_type(type=primitive.INV_APU, hier=hier)
        for c in candidate_list:
            if (c not in driver_set) and (c not in delete_set):
                # need to go around the loop again if a buffer/inv has already been identified as
                # a driver gate in case it should get optimized away rather than transformed
                pullup_ctl = c.inputlist[0]
                pulldown_ctl = c.inputlist[1]
                
                # check gate connected to pullup and pulldown
                if len(pullup_ctl.drivers)==1 and len(pullup_ctl.all_gate_fanin)==1 and \
                        len(pulldown_ctl.drivers)==1 and len(pulldown_ctl.all_gate_fanin)==1:
                    pullup_ctl_driver = list(pullup_ctl.all_gate_fanin)[0]                    
                    pullup_ctl_driver_type = pullup_ctl_driver.__class__
                    pulldown_ctl_driver = list(pulldown_ctl.all_gate_fanin)[0]                    
                    pulldown_ctl_driver_type = pulldown_ctl_driver.__class__
                    if (pulldown_ctl_driver in delete_set) or (pullup_ctl_driver in delete_set):
                        newgate = None
                    elif pulldown_ctl==pullup_ctl_driver.inputlist[0] and \
                            isinstance(pullup_ctl_driver, primitive.INV):
                        newgate = primitive.INV
                        innet = pulldown_ctl
                        driver_gate_list = [pullup_ctl_driver]
                    elif pullup_ctl==pulldown_ctl_driver.inputlist[0] and \
                            isinstance(pulldown_ctl_driver, primitive.INV):
                        newgate = primitive.BUF
                        driver_gate_list = [pulldown_ctl_driver]
                        innet = pullup_ctl
                    elif pullup_ctl_driver.inputlist[0]==pulldown_ctl_driver.inputlist[0] and \
                            isinstance(pullup_ctl_driver, primitive.BUF) and \
                            isinstance(pulldown_ctl_driver, primitive.INV): \
                        # ensemble wires as buffer
                        newgate = primitive.BUF
                        driver_gate_list = [pulldown_ctl_driver, pullup_ctl_driver]
                        innet =  pullup_ctl_driver.inputlist[0]
                    elif pullup_ctl_driver.inputlist[0]==pulldown_ctl_driver.inputlist[0] and \
                           isinstance(pullup_ctl_driver, primitive.INV) and \
                           isinstance(pulldown_ctl_driver, primitive.BUF):
                        newgate = primitive.INV
                        ## FIXME: Should be able to put pulldown_ctl_driver in list here too!
                        ## print pulldown_ctl_driver.fullname(), pulldown_ctl_driver.tostring()
                        driver_gate_list = [pullup_ctl_driver]
                        innet =  pullup_ctl_driver.inputlist[0]
                    else:
                        newgate = None
    
                    if newgate :
                        #print "CANDIDATE ", c.fullname(), c.tostring()
                        delete_set.add(c)
                        driver_set.update(driver_gate_list)
                        # create gate with mix of input gate and output gate parameters
                        newgate_list.append((c.parent, newgate(name="reopt_gate_pass2_%d" % gnext_gate_idx, \
                                                                   nlist=[ c.outputnet, innet],\
                                                                   pulldown_str=c.pulldown_str,\
                                                                   pullup_str=c.pullup_str,\
                                                                   parent=c.parent)))
                        changes += 1
                        gnext_gate_idx += 1
        
        for g in delete_set:
            g.parent.delete_gate(g, False)

        for (p,g) in newgate_list:
            p.gatelist.append(g)
    
        for g in driver_set:
            if len(g.outputnet.prim_fanout)==0 :
                # have removed all its fanout now so delete this too
                g.parent.delete_gate(g, False)
    
    return changes



def process_latches_v3( mod, hier=True, verbose=False, debug=""):
    ''' 
    Try to replace all unidirectional pass gates which feed a logic input with a latch.
    Restrict it to fanout of 1 FFs only initially.
    '''
    delete_set = set()
    newgate_list = []
    feedback_trs = 0
    latches = 0
    newgate_idx = 0
    changes = 0
    for f in mod.get_gates_by_type(type=primitive.UNMOS, hier=hier) :
        outnet = f.port['DRAIN'].netconn
        innet = f.port['SOURCE'].netconn        
        clk = f.port['GATE'].netconn        
        if len(outnet.all_gate_fanin) == 1 and f.parent != None and len(outnet.all_fanout)==1:
            if debug == "" or debug == f.fullname():
                print "* latch candidate = ", f.fullname()
                delete_set.add(f)
                newgate_list.append((f.parent, primitive.DLAT("%s_lat_%d" % (f.name,newgate_idx), \
                                                                  nlist=[outnet, innet, clk ],\
                                                                  pulldown_str=f.pulldown_str,\
                                                                  pullup_str=f.pullup_str,\
                                                                  parent=f.parent)))
                newgate_idx += 1            

    for g in delete_set:
        g.parent.delete_gate(g, False)

    for (p,g) in newgate_list:
        p.gatelist.append(g)

    changes= newgate_idx

    return changes

        



def process_latches_pass2(mod, hier=True, verbose=False):
    # 1. Remove feedback transistors on buffers 
    delete_set = set()
    newgate_list = []
    feedback_trs = 0
    latches = 0
    newgate_idx = 0
    changes = 0
    for f in mod.get_gates_by_type(type=primitive.BUF, hier=hier) :
        outnet = f.port['O'].netconn
        innet = f.port['I0'].netconn
        for g in outnet.prim_fanout:
            if isinstance(g, (primitive.UNMOS, primitive.NMOS)):
                source = g.port['SOURCE'].netconn
                drain = g.port['DRAIN'].netconn
                gate = g.port['GATE'].netconn

                if isinstance(g, primitive.UNMOS) :                    
                    if source==outnet and drain==innet:
                        # print g.fullname(), g.tostring()
                        feedback_trs += 1
                        delete_set.add(g)
                elif isinstance(g, primitive.NMOS) :
                    if (source==outnet and drain==innet) \
                            or (source==innet and drain==outnet):
                        # print g.fullname(), g.tostring()
                        feedback_trs += 1
                        delete_set.add(g)

        

    for g in delete_set:
        g.parent.delete_gate(g, False)


    changes += feedback_trs
    print "* - deleted %d feedback transistors" % feedback_trs


    # 2. Check if this now makes a latch - one pass gate driver - after the feedback devices are removed
    candidates = mod.get_gates_by_type(type=primitive.BUF, hier=hier) 
    candidates.extend(mod.get_gates_by_type(type=primitive.INV, hier=hier) )

    for f in candidates:
        isinverting = isinstance(f, primitive.INV)
        outnet = f.port['O'].netconn
        innet = f.port['I0'].netconn
        # a. plain pass gate + BUF/INV = DLAT/B
        if len(innet.drivers)==1 and innet.pullup_str==0 and len(innet.all_gate_fanin)==1:
            pg = list(innet.all_gate_fanin)[0]
            # input transistor needs to be directional
            if isinstance(pg, primitive.UNMOS):
                pass_innet = pg.port['SOURCE'].netconn
                pass_gate = pg.port['GATE'].netconn
                pass_outnet = pg.port['DRAIN'].netconn

                # FIXME - ensure that the pass gate feed only this device and that the other end is strongly
                # driven and doesn't come via a pass chain where charge sharing could occur.
                if len(pass_outnet.all_fanout)==1 : # and (pass_innet.pullup_str>0 or pass_innet.issupply):
                    delete_set.add(pg)
                    delete_set.add(f)
                    latches += 1
                    
                    newgate = primitive.DLATB if isinverting else primitive.DLAT
                    netparam = [outnet, pass_innet, pass_gate]
                    newgate_list.append((pg.parent, newgate("reopt_gate_pass2b_%d" % newgate_idx, \
                                                                netparam,\
                                                                pulldown_str=f.pulldown_str,\
                                                                pullup_str=f.pullup_str,\
                                                                parent=pg.parent)))
                    newgate_idx += 1
        # b. pass gate with additional pullup/down tr + BUF/INV = DLATR/S/B
        elif 1<len(innet.drivers)<3 and innet.pullup_str==0 and 1<len(innet.all_gate_fanin)<3:
            reset_tr = None
            set_tr = None
            latch_type = None
            clock_tr = None
            clock_net = None
            reset_net = None
            set_net = None
            d_net = None

            valid = True
            for t in list(innet.all_gate_fanin):
                if not isinstance(t, primitive.UNMOS):
                    valid = False
                else:    
                    gg = t.port['GATE'].netconn
                    dd = t.port['DRAIN'].netconn
                    ss = t.port['SOURCE'].netconn
                    # Fanout/in needs to be by source or drain not gate
                    if dd==innet or ss==innet:
                        if isinstance(dd, net.supply0) or isinstance(ss, net.supply0):
                            if latch_type != None:
                                if isinverting:
                                    latch_type = primitive.DLATRSB                  
                                else:
                                    latch_type = primitive.DLATRS 
                            else:
                                if isinverting:
                                    latch_type = primitive.DLATRB                    
                                else:
                                    latch_type = primitive.DLATR
                                    
                            reset_tr = t
                            reset_net = gg
                        elif isinstance(dd, net.supply1) or isinstance(ss, net.supply1):
                            if latch_type != None:
                                if isinverting:
                                    latch_type = primitive.DLATRSB                    
                                else:
                                    latch_type = primitive.DLATRS
                            else:
                                if isinverting:
                                    latch_type = primitive.DLATSB      
                                else:
                                    latch_type = primitive.DLATS
                            set_tr = t
                            set_net = gg
                        elif not isinstance(gg, net.supply0):
                            clock_tr = t
                            clock_net = gg
                            d_net = ss if ss != innet else dd

            if valid:
                if latch_type == None:
                    if isinverting:
                        latch_type = primitive.DLATB
                    else:
                        latch_type = primitive.DLAT
                        
                if set_tr and clock_tr and not reset_tr :
                    delete_set.add(f)
                    delete_set.add(set_tr)
                    delete_set.add(clock_tr)
                    newgate_list.append((f.parent, latch_type("%s_rpl"% f.name,\
                                                                  [outnet, d_net, set_net, clock_net], \
                                                                  pulldown_str=net.SUPPLY_STR, \
                                                                  pullup_str=f.pullup_str,\
                                                                  parent=f.parent)))
                elif reset_tr and clock_tr and not set_tr :
                    delete_set.add(f)
                    delete_set.add(reset_tr)
                    delete_set.add(clock_tr)
                    newgate_list.append((f.parent, latch_type("%s_rpl"% f.name,\
                                                                  [outnet, d_net, reset_net, clock_net], \
                                                                  pulldown_str=net.SUPPLY_STR, \
                                                                  pullup_str=f.pullup_str,\
                                                                  parent=f.parent)))
                elif reset_tr and clock_tr and set_tr:
                    delete_set.add(f)
                    delete_set.add(reset_tr)
                    delete_set.add(set_tr)
                    delete_set.add(clock_tr)
                    delete_set = set([f, reset_tr, clock_tr])
                    newgate_list.append((f.parent, latch_type("%s_rpl"% f.name,\
                                                                  [outnet, d_net, reset_net, set_net, clock_net], \
                                                                  pulldown_str=net.SUPPLY_STR, \
                                                                  pullup_str=f.pullup_str,\
                                                                  parent=f.parent)))
                elif clock_tr and len(innet.all_connected())==2:
                    delete_set.add(f)
                    delete_set.add(clock_tr)
                    newgate_list.append((f.parent, latch_type("%s_rpl"% f.name,\
                                                                  [outnet, d_net, clock_net], \
                                                                  pulldown_str=net.SUPPLY_STR, \
                                                                  pullup_str=f.pullup_str,\
                                                                  parent=f.parent)))

    for g in delete_set:
        g.parent.delete_gate(g, False)

    for (p,g) in newgate_list:
        p.gatelist.append(g)


    # 3. Look for more complex latches with dual outputs and or dual pass gate inputs
    newgate_list = []
    delete_set = set()                    
    for f in mod.get_gates_by_type(type=primitive.BUF, hier=hier) :
        outnet = f.port['O'].netconn
        innet = f.port['I0'].netconn
        if len(innet.drivers)==1 and innet.pullup_str==0 and len(innet.all_gate_fanin)==1:
            pg = list(innet.all_gate_fanin)[0]
            # input transistor needs to be directional
            if isinstance(pg, primitive.UNMOS):
                pass_innet = pg.port['SOURCE'].netconn
                pass_gate = pg.port['GATE'].netconn
                pass_outnet = pg.port['DRAIN'].netconn

                if len(pass_outnet.prim_fanout)==2 and len(pass_outnet.drivers)==1 \
                        and pass_outnet.pullup_str==0 and pass_outnet.charge_storage \
                        and (pass_innet.pullup_str>0 or pass_innet.issupply):
                    (g0,g1) = list(pass_outnet.prim_fanout)[0:2]

                    if (isinstance(g0, primitive.INV) and isinstance(g1, primitive.BUF)):
                        netparam = [g0.outputnet, g1.outputnet, pass_innet, pass_gate]
                        newgate = primitive.DLAT2
                    elif  (isinstance(g0, primitive.BUF) and isinstance(g1, primitive.INV)):
                        netparam = [g0.outputnet, g1.outputnet, pass_innet, pass_gate]
                        newgate = primitive.DLAT2                        
                    else:
                        newgate = None

                    if newgate:
                        delete_set.add(g0)
                        delete_set.add(g1)
                        delete_set.add(pg)
                        newgate_list.append((pg.parent, newgate(name="reopt_gate_pass2b_%d" % newgate_idx, \
                                                                   nlist=netparam,\
                                                                   pulldown_str=g1.pulldown_str,\
                                                                   pullup_str=g1.pullup_str,\
                                                                   parent=pg.parent)))
                        newgate_idx += 1
                        latches += 1

                elif len(pass_outnet.prim_fanout)==2 and len(pass_outnet.drivers)==1 \
                        and pass_outnet.pullup_str==0 and pass_outnet.charge_storage \
                        and pass_innet.pullup_str==0 and len(pass_innet.drivers)==1 \
                        and len(pass_innet.all_gate_fanin) == 1:
                    # could be a two pass transistor chain
                    g2 = list(pass_innet.all_gate_fanin)[0]
                    if isinstance(g2, primitive.UNMOS):
                        g2_innet = g2.port['SOURCE'].netconn
                        g2_gate = g2.port['GATE'].netconn
                        g2.outnet = g2.port['DRAIN'].netconn

                        if (g2_innet.pullup_str > 0 or g2_innet.issupply) or True:
                            (g0,g1) = list(pass_outnet.prim_fanout)[0:2]

                            if (isinstance(g0, primitive.INV) and isinstance(g1, primitive.BUF)):
                                netparam = [g1.outputnet, g0.outputnet, pass_innet, pass_gate, g2_gate]
                                newgate = primitive.DLAT2EN
                            elif  (isinstance(g0, primitive.BUF) and isinstance(g1, primitive.INV)):
                                netparam = [g0.outputnet, g1.outputnet, pass_innet, pass_gate, g2_gate]
                                newgate = primitive.DLAT2EN                        
                            else:
                                newgate = None
                                
                            if newgate:
                                delete_set.add(g0)
                                delete_set.add(g1)
                                delete_set.add(pg)
                                newgate_list.append((pg.parent, newgate(name="reopt_gate_pass2b_%d" % newgate_idx, \
                                                                            nlist=netparam,\
                                                                            pulldown_str=g1.pulldown_str,\
                                                                            pullup_str=g1.pullup_str,\
                                                                            parent=pg.parent)))
                                newgate_idx += 1
                                latches += 1
                            

    for g in delete_set:
        g.parent.delete_gate(g, False)

    for (p,g) in newgate_list:
        p.gatelist.append(g)


    changes += latches
    print "* - identified %d latches" % latches

    return changes


def generate_graphs_dfs(node , nodes_visited=[], graph=[], pulldowneqn=[], pullupeqn=[], passgateeqn=[], stopnets = []) :
    '''
    Construct list of lists for pullup/pulldown trees from the given node
    '''
    nodes_visited.append(node)
    if node in gbydiff:
        for tr in gbydiff[ node ] :
            (name, id, gate, source, drain)  = tr
            n = source if drain==node else drain
            if n not in nodes_visited :
                if n in stopnets:
                    # user defined list of dead ends which has highest priority
                    pass
                if n.issupply and isinstance(n, net.supply0):
                    pulldowneqn.append(graph + [tr])
                elif n.issupply and isinstance(n, net.supply1):
                    pullupeqn.append(graph + [tr])
                elif n.pullup_str > 0 :
                    # prevent trees passing through other notes
                    pass
                elif (n in gbygate):
                    # if diffusion fans out to gates then can't include this in a pulldown tree
                    passgateeqn.append(graph + [tr])                
                else :
                    generate_graphs_dfs(n, nodes_visited,  graph+[tr], pulldowneqn, pullupeqn, passgateeqn, stopnets)
    else:
        pass
        # print "* FAILED TO FIND node %s in diff connections" %  node.fullname
    nodes_visited.pop()


def reduce_and_or_terms(orterms, debug=False):
    '''
    reduce and-or terms in form of a list of lists to remove
    logically redundant lists, and redundant elements in each
    list. Individual AND lists are no longer in the same order.
    '''
    if debug:
        print "* Entering reduce_or_terms with list ",  orterms
    reduced = []
    for l in orterms:
        is_unique = True    
        lset = set(l)
        for j in [ set(ll) for ll in orterms if ll != l ] :
            if lset.issuperset(j):
                is_unique = False        
        if is_unique:
            reduced.append(list(lset))

    if debug:
        print "* Removed %d redundant entries" % (len(orterms) - len(reduced))
        print "* Exiting reduce_or_terms with list ",  reduced
    return reduced



