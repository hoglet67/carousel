#!/usr/bin/env python
# usage: python v6502netlister.py <transdef.js> <segdefs.js>
#
# Consolidate datastructures into a python executable

import sys


def read_segments(filename) :
    pycmd = []
    pycmd.append("segments=[ ")
    for l in open(filename, 'r') :
        if l.startswith('['):
            pycmd.append(l)
    pycmd.append(']')
    return(''.join(pycmd))    

def read_nodenames(filename) :
    pycmd = []
    pycmd.append("nodenames=dict([ ")
    for l in open(filename, 'r') :
        fields=l.split()        
        if len(fields) > 1 and fields[0].endswith(':'):
            name = fields[0][:-1]
            # Dont read the whacky names with equations etc in them
            if not name.startswith('"'):
                net = fields[1][:-1]
                pycmd.append( '(\'%s\', \'%s\'), ' %(net, name) )
    pycmd.append('])')
    return(''.join(pycmd))    



def read_netlist(filename) :
    pycmd = []
    start = False
    for ll in open(filename, 'r') :
        l = ((ll.strip()).replace('false', '"False"')).replace('true', '"True"')

        
        if not start :
            if l.startswith("var"):
                start = True
                pycmd.append("transdefs=[ ")
        else :
            pycmd.append(l)
            if l.startswith("]"):
                break      

    return(''.join(pycmd))
    

def write_for_carousel( trans, segs, nodenames, padlist, module_name ) :
    '''
    based on expand netlist
    '''
    f = open( "%s.py" % module_name, "w")

    f.write(\
'''
import gate
import net
from primitive import NMOS

''' + 
"class %s( gate.module ):" % module_name + 
'''
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict([
''')
    for (p,dir) in padlist:
        f.write ("            (\'%s\', gate.%s),\n" % ( p, dir))

    f.write(\
'''
        ])
        gate.module.__init__( self, name, portlist, mapping, parent)

        ## Net Declarations
''' )


    nets = dict()
    components = list()
    new_trans = dict()

    if True:
        ## --------------------------------------------------
        # SORT THE TRANSISTORS AND ELIMINATE THE DUPLICATES !
        ##
        net_trans = []
        for t in trans:
            n = t[0]
            g = t[1]
            s = t[2]
            d = t[3]
            if len(t) > 6:
                isweak = t[6]
            else:
                isweak = False
            if s > d:
                tmp  = d
                d = s
                s = tmp
            net_trans.append( (g,s,d,n, t, isweak) )
    
               
        current = ( 0,0,0,None)
        removals = []
        for n in sorted(net_trans):
            match = False
            if n[0] != current[0] or n[1] != current[1] or n[2] != current[2]:
                # keep a count of the transistor replication
                current = n
                new_trans[n[3]]= n[4]
    
            else:
                # increment the count
                new_trans[current[3]] = current[4]
        ## --------------------
    else:
        for t in trans:
            new_trans[t[0]]= ( t, 10)

    # First parse the transistors
    for name in new_trans:    
        t = new_trans[name]
        name = t[0]
        gate = str(t[1])
        source = str(t[2])
        drain = str(t[3])
        if len(t) > 6 :
            isweak = t[6]
        else:
            isweak = False

        if gate in nodenames:
            gate = nodenames[gate]
        else:
            gate = 'n%s'% gate
        if source in nodenames:
            source = nodenames[source]
        else:
            source = "n%s"% source
        if drain in nodenames:
            drain = nodenames[drain]
        else:
            drain = "n%s"% drain                


        # set charge_storage attribute on all nets 
        nets[gate] = (0, True)
        for n in (source, drain):
            if not n in nets:
                nets[n] = (0, True)
            
        # add the component
        components.append ( (name, gate, source, drain, isweak))

    idx = 0
    
    # now look at the nets for depletion pullups
    for s in segs:
        netname = str(s[0])
        if netname in nodenames:
            netname = nodenames[netname]
        else:
            netname = "n%s"%netname

        # if its a depletion net then remove charge_storage attribute
        if s[1] == '+' :
            nets[netname] = (1, False)
        
    
    padnames = dict()
    for (n,dir) in padlist:
        padnames[n] = dir

    for n in sorted(list(nets)):
        name = n
        # Dont write the supplies as nets
        if name not in ('vss', 'vcc', 'vdd', 'gnd'):
            if name not in padnames:
                f.write('        self.netlist[\'%s\'] = net.net(\'%s\', %s %s parent=self)\n' \
                            % (name, name, \
                                   'pullup_str=100, 'if nets[n][0] else '', \
                                   'charge_storage=True, ' if nets[n][1] else ''))
            else:
                if nets[n][0]:
                    f.write('        self.port[\'%s\'].netconn.pullup_str=100\n'%name)
                if nets[n][1]:
                    f.write('        self.port[\'%s\'].netconn.charge_storage=True\n'%name)

        elif name in ('vcc'):
            f.write('        self.netlist[\'%s\'] = net.supply1(\'%s\')\n' %(name,name))            
        elif name in ('gnd'):
            f.write('        self.netlist[\'%s\'] = net.supply0(\'%s\')\n' %(name,name))            


    f.write( '        ## Component declarations\n')
    f.write( '        self.gatelist.extend([\n')
    for g in components:        
        (name, gate, source, drain, isweak) = g
        connections = []
        for c in ( drain, source, gate ) :
            if c not in padnames:
                connections.append('self.netlist[\'%s\']'%c )
            else:
                connections.append('self.port[\'%s\'].netconn'%c )

        type = "NMOS"
        f.write('            %s(\"%s\", [%s], isweak=%s, parent=self),\n' % \
                    (type, name,','.join(connections), isweak ))
    f.write( '        ])\n')
    f.close()
    return



def main(argv) :
    exec(read_nodenames(argv[3]))
    exec(read_segments(argv[2]))
    exec(read_netlist(argv[1]))
    execfile(argv[4])
    module_name = argv[5]

    write_for_carousel( transdefs, segments, nodenames, padlist, module_name)


if __name__ == '__main__' :
    main(sys.argv)
