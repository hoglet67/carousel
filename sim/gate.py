'''Basic logic gate class and constant definitions'''

# gate/module port types
IN     = 0
INOUT  = 1
OUT    = 2
TRIOUT = 3
NULL   = 4

DIR_TO_STRING = [ "IN", "INOUT", "OUT", "TRIOUT", "NULL" ]

import net
import pin
import re


class gate:
    def __init__ ( self,  name, portlist, mapping,  parent=None, strength=1, pullup_str=None, pulldown_str=None,is_a_primitive=False): 
        self.name = name
        self.port = dict()
        self.parent = parent
        self.outputpins = dict()
        
        if not pulldown_str:
            self.pulldown_str = strength
        else:
            self.pulldown_str = pulldown_str
        if not pullup_str:
            self.pullup_str = strength
        else:
            self.pullup_str = pullup_str
        self.strength = min( [self.pulldown_str, self.pullup_str] )
            
        self.is_a_primitive = is_a_primitive
        # Map each port to a simulation net and update the simulation
        # net's fanin and fanout lists appropriately
        for portname in mapping:
            n = mapping[portname]
            if portname in portlist :
                direction = portlist[portname]
                p = pin.pin(name=portname, parent=self, netconn=n, direction=direction ) 
                self.port[portname] = p
                if  direction == IN or direction == INOUT :                    
                    #n.all_fanout.add( p )
                    n.all_fanout.add( self ) # point at the gate rather than a pin
                    if is_a_primitive:
                        # n.prim_fanout.add( p )
                        n.prim_fanout.add( self ) # point at the gate rather than a pin
                        if self.simulate not in n.efanout:
                            n.efanout.append(self.simulate)
                if  direction == OUT or direction == INOUT :
                    self.outputpins[portname] = p
                    n.all_fanin.add(p)    
                    n.all_gate_fanin.add(self)
                    # all drivers default to drive 'X' on startup
                    if is_a_primitive:
                        n.drivers.append(p)

        for portname in portlist:
            if not portname in self.port:
                self.port[portname] = pin.pin(name=portname, parent=self, netconn=net.net('unconnected'))

    def finish_simulation ( self, options ) :
        # Subclasses will override this method to dump status data at the end of a simulation run        
        pass

    def tostring(self) :

        inputs = []
        outputs = []
        result = [ self.fullname(), self.__class__.__name__ ]
        for i in sorted(self.port):
            result.append( "%s:%s" % (i, self.port[i].netconn.fullname ))
        return ' '.join(result)

    def fullname(self) :
        if not self.parent:
            return self.name
        else:
            return '.'.join( [self.parent.fullname(), self.name])


class module(gate) :

    def __init__(self, name, portlist, mapping,  parent=None, strength=1, is_a_primitive=False): 
        gate.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent, strength=strength, is_a_primitive=is_a_primitive)
        self.gatelist = []
        self.netlist = dict()

        # Always define the globals vdd and vss as supply nets
        if not "vdd" in self.netlist:                
            n = self.get_parent_net( "vdd" )
            if n :
                self.netlist["vdd"] = n
            else:
                self.netlist["vdd"] =net.supply1("vdd")
        if not "vss" in self.netlist:                
            n = self.get_parent_net( "vss" )
            if n :
                self.netlist["vss"] = n
            else:
                self.netlist["vss"] =net.supply0("vss")

    def tostring(self) :
        result = []
        inputs = []
        outputs = []
        for i in sorted(self.port):
            result.append( "%s.%s:%s=%s" % (self.fullname(), i, self.port[i].netconn.fullname, self.port[i].netconn.value ))
        for i in self.netlist:
            result.append( "%s.%s:%s=%s" % (self.fullname(), i, self.netlist[i].fullname, self.netlist[i].value ))
        return ' '.join(result)
       
    def get_nets(self, regexp='', hier=True):
        '''
        Return all net objects referenced by the testbench optionally
        descending through the hierarchy
        '''
        all_nets = [self.netlist[n] for n in self.netlist ]
        
        if hier:
            for g in self.gatelist:
                if isinstance(g, module):
                    all_nets.extend(g.get_nets(hier=True))
                
        filtered_nets = []
        if regexp != '':
            r = re.compile(regexp)
            for n in all_nets:
                if r.search(n.fullname):
                    filtered_nets.append(n)
        else:
            filtered_nets = all_nets

        return filtered_nets

    def get_gates_by_type(self, type=None, hier=True):
        '''
        Return all gate objects matching a given type
        '''
        all_gates = [g for g in self.gatelist]
        if hier:
            for g in self.gatelist:
                if isinstance(g, module):
                    all_gates.extend(g.get_gates(hier=True))
                    
        if type:                    
            result = [ g for g in all_gates if isinstance(g, type) ]
        else:
            result = all_gates

        return result

    def get_gates(self, regexp='', hier=True):
        '''
        Return all gate objects matching an instance name regexp
        '''
        all_gates = [g for g in self.gatelist]
        if hier:
            for g in self.gatelist:
                if isinstance(g, module):
                    all_gates.extend(g.get_gates(hier=True))
                                
        filtered_gates = []
        if regexp != '':
            r = re.compile(regexp)
            for n in all_gates:
                if r.search(n.fullname()):
                    filtered_gates.append(n)
        else:
            filtered_gates = all_gates

        return filtered_gates

    def get_parent_net(self, netname) :
        '''Return a reference to a net in current or parent module or None if not found'''
        if self.parent:
            return self.parent.get_parent_net(netname)
        elif netname in self.netlist :
            return self.netlist[netname]
        else:
            return None

    def purge_nets(self, hier=True, verbose=False):
        '''
        Purge all nets from a gate and optionally lower level gates which have
        neither fanin nor fanout
        '''
        all_gates = [g for g in self.gatelist]
        all_gates.append(self)
        if hier:
            for g in self.gatelist:
                if isinstance(g, module):
                    all_gates.extend(g.get_gates(hier=True))
        
        removed_nets = []
        for g in all_gates:
            #print "Checking in gate ", g.fullname()
            if not g.is_a_primitive:
                for netname in g.netlist:
                    n = g.netlist[netname]
                    #print "checking ", netname
                    #print n.issupply, n.efanout, n.all_fanin, n.drivers, n.all_fanout
                    #for p in n.all_fanin:
                    #    print p.fullname
                    if not n.issupply and len(n.efanout) == 0 and \
                            len( n.all_fanin) == 0 and \
                            len( n.drivers ) == 0 and \
                            len( n.all_fanout ) == 0:
                        removed_nets.append(n)

        for n in removed_nets:
            if n.parent:
                #print "purging %s" % n.fullname
                del n.parent.netlist[n.name]
            else:
                #print "purging %s" % n.fullname
                del self.netlist[n.name]
                n = None

        return len(removed_nets)

    def delete_gate(self, id, verbose=False):
        '''
        remove a gate from its parent netlist and any net connection fanin/fanout tables
        '''
        success = False
        if id in self.gatelist:
            success = True
            self.gatelist.remove(id)

        for pinname in id.port:
            pinobj = id.port[pinname]
            n = pinobj.netconn

            if id in n.all_fanin:
                n.all_fanin.remove(id)

            if id in n.all_gate_fanin:
                n.all_gate_fanin.remove(id)

            if id in n.all_fanout:
                n.all_fanout.remove(id)

            if id in n.prim_fanout:
                n.prim_fanout.remove(id)

            if id.simulate in n.bidir_efanout:
                n.bidir_efanout.remove(id)

            if id.simulate in n.efanout:
                n.efanout.remove(id.simulate)

            if pinobj in n.all_fanin:
                n.all_fanin.remove(pinobj)

            if pinobj in n.drivers:
                n.drivers.remove(pinobj)
                    
        if verbose:
            print "* Removed %s and connections from netlist " % id.name

        # remove the gate object completely to help in garbage collection
        id = None
        return success

    def write_netlist(self, filename=""):
        if filename == "":
            filename="%s.py.debug" % (self.name())
        f = open(filename,'w')
        results = [ i for i in self.get_gates(hier=True) if i.is_a_primitive]
        for r in results:
            f.write( r.tostring() + '\n')
        for n in [ i for i in self.get_nets(hier=True) if i.pullup_str >0 ]:
            f.write( 'PULLUP %s\n' % n.fullname)
        f.close()
        
        
        
def wire(net_names, pullup_str=0, parent=None, charge_storage=False) :
    '''
    convenience function for declaring nets in a gate object
    '''
    newnets = dict()    
    for name in net_names:
        newnets[name] = net.net(name, pullup_str=pullup_str, parent=parent, charge_storage=False)
    return newnets

