'''
Define all basic primitive logic elements. Build a standard cell library, with gate 
or path delays etc on top of this.

In the simulate methods gates can choose either to return

(self.outputnet, (result, self.strength), self.driverpin)

and the simulation main loop will update the net driver table before the next pass
through the event loop, or the simulate method can update the net driver table
directly (so that all subsequent net evaluation in the same iteration will pick
up the new value), in which case it should return None in the self.driverpin field. This 
ensures that the net's fanout will still get scheduled for evaluation but saves
both the simulate() and main loop updating the driver table twice.
'''
import net
import gate
import pin
from net import sevaluate_net_drivers, DEPL_STR, SUPPLY_STR
#from cnet import sevaluate_net_drivers

P_NOT = dict( [('0','1'), ('1','0'), ('X', 'X'), ('Z', 'X')])
P_BUF = dict( [('1','1'), ('0','0'), ('X', 'X'), ('Z', 'X')])

def P_DLAT(vals):
    (d, rstb, phi, q_prev) = vals
    if rstb == '0':
        result = '0'
    elif rstb == 'X':
        result = 'X'
    elif phi == '1':
        result = P_BUF[d]
    else:
        result = q_prev
    return result

class primitive(gate.gate):

    '''
    Class of basic single output, multiple input logic elements where the order of inputs
    is unimportant.

    ie AND, OR, NAND, NOR, INV, BUF, XOR, XNOR
    '''
    def __init__(self, name, nlist, parent=None, strength=1,  pulldown_str=net.SUPPLY_STR, pullup_str=net.DEPL_STR) :
        # take unordered list of inputs and single output for generic multi-input gates        
        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", nlist[0])])
        idx = 0        

        self.outputnet = nlist[0]
        self.outputport = "O" 
        self.inputlist = nlist[1:]
        self.strength = strength

        for i in nlist[1:] :
            portname = "I%d" % idx
            portlist[portname] = gate.IN
            mapping[portname] =  i
            idx +=1                        
        gate.gate.__init__( self, name, portlist, mapping, parent, strength, pullup_str, pulldown_str, is_a_primitive=True)
        
        # Primitives have a single output so store this for speed in returning simulation results
        self.driverpin = self.outputpins[self.outputport] 
        

class AND(primitive):  
    '''
    AND O I0 I1 ...
    '''
    def simulate(self) :
        result = ('1', self.pullup_str)
        for v in [n.value for n in self.inputlist] :
            if v == '0':
                result = ('0', self.pulldown_str)
                break
            elif v == 'Z' or v =='X':
                result == ('X', self.pullup_str)
        return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else []

class NAND(primitive):        
    '''
    NAND O I0 I1 ...
    '''
    def simulate(self) :
        result = ('0', self.pulldown_str)
        for v in [ n.value for n in self.inputlist]:
            if v == '0':
                result = ('1', self.pullup_str)
                break
            elif v == 'Z' or v =='X':
                result == ('X', self.pullup_str)
        return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else []

class OR(primitive):        
    '''
    OR O I0 I1 ...
    '''
    def simulate(self) :
        result = ('0', self.pulldown_str)
        for v in [ n.value for n in self.inputlist]:
            if v == '1':
                result = ('1', self.pullup_str)
                break
            elif v == 'Z' or v =='X':
                result == ('X', self.pullup_str)
        return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else []

class NOR(primitive):        
    '''
    NOR O I0 I1 ...
    '''
    def simulate(self) :
        result = ('1', self.pullup_str)
        for v in [ n.value for n in self.inputlist]:
            if v == '1':
                result = ('0', self.pulldown_str)
                break
            elif v == 'Z' or v =='X':                
                result == ('X', self.pullup_str)
        return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else []


class XOR(primitive):        
    '''
    XOR O I0 I1 ...
    '''
    def simulate(self) :
        result = '0'
        for v in [ n.value for n in self.inputlist ]:
            if v == 'X' or v == 'Z':
                result = 'X'
                break
            elif result == '1':
                result = P_NOT[v]
            else:
                result = P_BUF[v]
        return [(self.outputnet, (result, self.strength), self.driverpin)] if result != self.driverpin.state[0] else ()

class INV(primitive):
    '''
    INV O I0 
    '''
    def simulate(self) :
        input = self.inputlist[0].value  
        if input == '0':
            result = ('1', self.pullup_str)
        elif input == '1':
            result = ('0', self.pulldown_str)
        else:
            result = ('X', self.pullup_str)
        return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else ()

class BUF(primitive):
    '''
    BUF O I0 
    '''
    def simulate(self) :
        input = self.inputlist[0].value  
        if input == '0':
            result = ('0', self.pulldown_str)
        elif input == '1':
            result = ('1', self.pullup_str)
        else:
            result = ('X', self.pullup_str)
        return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else ()


class MUX21( primitive ) :
    '''
    MUX21 O I0 I1 SEL
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None ) :
        self.strength = strength
        self.outputnet = nlist[0]
        portlist = dict( [("O", gate.OUT),("I0", gate.IN),("I1", gate.IN),("SEL", gate.IN)] )
        mapping = dict([ ("O", nlist[0]),("I0", nlist[1]),("I1", nlist[2]),("SEL", nlist[3])] )
        gate.gate.__init__( self, name, portlist, mapping, parent,  pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.driverpin = self.outputpins['O'] 
        self.inputlist = nlist[1:]
 

    def simulate( self ) :
        linputlist = self.inputlist
        sel = linputlist[2].value  
        if sel == '0':
            result = P_BUF[linputlist[0].value]
        elif sel == '1':
            result = P_BUF[linputlist[1].value]
        elif sel == 'Z' or sel == 'X':
            a = linputlist[0].value
            b = linputlist[1].value              
            result = a if a == b else 'X'
        else:
            result = 'X'

        str = self.pulldown_str if result == '0' else self.pullup_str

        return [( self.outputnet, (result, str), self.driverpin) ] if result != self.driverpin.state[0] else ()

class NMUX21( MUX21 ) :
    '''
    NMUX21 O I0 I1 SEL
    '''
    def simulate( self ) :
        linputlist = self.inputlist
        sel = linputlist[2].value  
        if sel == '0':
            result = P_NOT[linputlist[0].value]
        elif sel == '1':
            result = P_NOT[linputlist[1].value]
        elif sel == 'Z' or sel == 'X':
            a = linputlist[0].value
            b = linputlist[1].value      
            result = a if a == b else 'X'
        else:
            result = 'X'

        str = self.pulldown_str if result == '0' else self.pullup_str

        return [( self.outputnet, (result, str), self.driverpin) ] if result != self.driverpin.state[0] else ()


class DLAT2( primitive ) :
    '''
    DLAT2 Q QB D PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("Q", gate.OUT), ("QB", gate.OUT), ("D", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("Q", nlist[0]),("QB", nlist[1]),("D", nlist[2]),("PHI", nlist[3])] )
        self.inputlist = nlist[2:]
        self.outputlist = nlist[:2]
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.driverpin_q = self.outputpins['Q'] 
        self.driverpin_qb = self.outputpins['QB'] 

    def simulate(self) :
        d = self.inputlist[0].value[0]
        if  self.inputlist[1].value == '1':
            # transparent when phi == 1
            if d == '0':
                result = ('0', self.pulldown_str)
                resultb = ('1', self.pullup_str)
            elif d == '1':
                result = ('1', self.pullup_str)
                resultb = ('0', self.pulldown_str)
            else:
                # trial - is returning a pair of Xs too pessimistic for mixed level simulation
                result = ('X', self.pullup_str)
                resultb = ('X', self.pulldown_str)

            if result[0] != self.driverpin_q.state[0] or result[1] != self.driverpin_qb.state[0]:
                return [ (self.outputlist[0], result, self.driverpin_q),
                         (self.outputlist[1], resultb, self.driverpin_qb) ]
            else:
                return ()
        else:
            # no change 
            return ()

class DLAT2EN( primitive ) :
    '''
    DLAT2EN Q QB D PHI EN
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("Q", gate.OUT), ("QB", gate.OUT), ("D", gate.IN),("PHI", gate.IN), ("EN", gate.IN)] )
        mapping = dict([ ("Q", nlist[0]),("QB", nlist[1]),("D", nlist[2]),("PHI", nlist[3]), ("EN", nlist[4])] )
        self.inputlist = nlist[2:]
        self.outputlist = nlist[:2]
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.driverpin_q = self.outputpins['Q'] 
        self.driverpin_qb = self.outputpins['QB'] 

    def simulate(self) :
        d = self.inputlist[0].value[0]
        phi = self.inputlist[1].value[0]
        en = self.inputlist[2].value[0]

        if  phi == '1' and en == '1':
            # transparent when phi == 1 and en == '1'
            if d == '0':
                result = ('0', self.pulldown_str)
                resultb = ('1', self.pullup_str)
            elif d == '1':
                result = ('1', self.pullup_str)
                resultb = ('0', self.pulldown_str)
            else:
                # trial - is returning a pair of Xs too pessimistic for mixed level simulation
                result = ('X', self.pullup_str)
                resultb = ('X', self.pulldown_str)

            if result[0] != self.driverpin_q.state[0] or result[1] != self.driverpin_qb.state[0]:
                return [ (self.outputlist[0], result, self.driverpin_q),
                         (self.outputlist[1], resultb, self.driverpin_qb) ]
            else:
                return ()
        else:
            # no change 
            return ()

class DLATR( primitive ) :
    '''
    DLATR Q D RST PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("Q", gate.OUT),("D", gate.IN),("RST", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("Q", nlist[0]),("D", nlist[1]),("RST", nlist[2]),("PHI", nlist[3])] )
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.oldphi = 'X'
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.driverpin = self.outputpins['Q'] 

    def simulate(self) :
        d = self.inputlist[0].value
        if  self.inputlist[1].value == '1':
            # rst applied, reset storage node
            result = ('0', self.pulldown_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        elif  self.inputlist[2].value == '1':
            # transparent when phi == 1
            if d == '0':
                result = ('0', self.pulldown_str)
            elif d == '1':
                result = ('1', self.pullup_str)
            else:
                result = ('X', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        else:
            # no change 
            return []  


class DLAT( DLATR ) :
    '''
    DLAT Q D PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("Q", gate.OUT),("D", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("Q", nlist[0]),("D", nlist[1]),("PHI", nlist[2])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.driverpin = self.outputpins['Q'] 

    def simulate(self) :
        d = self.inputlist[0].value
        if  self.inputlist[1].value == '1':
            # transparent when phi == 1
            if d == '0':
                result = ('0', self.pulldown_str)
            elif d == '1':
                result = ('1', self.pullup_str)
            else:
                result = ('X', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        else:
            # no change 
            return []


class DLATB( DLAT ) :
    '''
    DLATB QB D PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("QB", gate.OUT),("D", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("QB", nlist[0]),("D", nlist[1]),("PHI", nlist[2])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.driverpin = self.outputpins['QB'] 

    def simulate(self) :
        d = self.inputlist[0].value
        if  self.inputlist[1].value == '1':
            # transparent when phi == 1
            if d == '0':
                result = ('1', self.pullup_str)
            elif d == '1':
                result = ('0', self.pulldown_str)
            else:
                result = ('X', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        else:
            # no change 
            return []

class DLATRB( DLAT ) :
    '''
    DLAT QB D RST PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("QB", gate.OUT),("D", gate.IN),("RST", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("QB", nlist[0]),("D", nlist[1]),("RST", nlist[2]),("PHI", nlist[3])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.driverpin = self.outputpins['QB'] 

    def simulate(self) :
        d = self.inputlist[0].value
        if  self.inputlist[1].value == '1':
            # rst applied, reset storage node, and invert to QB
            result = ('1', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        elif  self.inputlist[2].value == '1':
            # transparent when phi == 1
            if d == '0':
                result = ('1', self.pullup_str)
            elif d == '1':
                result = ('0', self.pulldown_str)
            else:
                result = ('X', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        else:
            # no change 
            return []


class DLATSB( DLAT ) :
    '''
    DLAT QB D SET PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("QB", gate.OUT),("D", gate.IN),("SET", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("QB", nlist[0]),("D", nlist[1]),("SET", nlist[2]),("PHI", nlist[3])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.driverpin = self.outputpins['QB'] 

    def simulate(self) :
        d = self.inputlist[0].value
        if self.inputlist[1].value == '1':
            # set applied, set storage node, and invert to QB
            result = ('0', self.pulldown_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        elif  self.inputlist[2].value == '1':
            # transparent when phi == 1
            if d == '0':
                result = ('1', self.pullup_str)
            elif d == '1':
                result = ('0', self.pulldown_str)
            else:
                result = ('X', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        else:
            # no change 
            return []

class DLATRSB( DLAT ) :
    '''
    DLAT QB D RST SET PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.strength = strength  
        portlist = dict( [("QB", gate.OUT),("D", gate.IN),("RST", gate.IN),("SET", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("QB", nlist[0]),("D", nlist[1]),("RST", nlist[2]),("SET", nlist[3]),("PHI", nlist[4])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=pullup_str, pulldown_str=pulldown_str, is_a_primitive=True)
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.driverpin = self.outputpins['QB'] 

    def simulate(self) :
        d = self.inputlist[0].value
        reset = self.inputlist[1].value
        set = self.inputlist[2].value
        if reset == '1':
            # set storage node, and invert to QB
            result = ('1', self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        elif set == '1':
            # set storage node, and invert to QB
            result = ('0', self.pulldown_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        elif  self.inputlist[2].value == '1':
            # transparent when phi == 1
            result = (P_NOT[d], self.pulldown_str if d == '1' else self.pullup_str)
            return [(self.outputnet, result, self.driverpin)] if result[0] != self.driverpin.state[0] else [] 
        else:
            # no change 
            return []
    
class DFF( primitive ) :
    '''
    DFF Q D RSTB PHI
    '''
    def __init__(self, name, nlist, parent=None, strength=1) :
        self.strength = strength  
        portlist = dict( [("Q", gate.OUT),("D", gate.IN),("RSTB", gate.IN),("PHI", gate.IN)] )
        mapping = dict([ ("Q", nlist[0]),("D", nlist[1]),("RSTB", nlist[2]),("PHI", nlist[3])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, strength=strength, is_a_primitive=True)
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.gatelist = []
        self.oldphi = 'X'
        self.driverpin = self.outputpins['Q'] 

    def simulate(self):
        linputlist = self.inputlist
        rstb = linputlist[1].value[0]
        phi = linputlist[2].value[0]
        phi_prev = self.oldphi
        if rstb == '0':
            result = '0'
        elif rstb == 'X':
            result = 'X'
        elif phi == phi_prev or phi == '0':
            q_prev = self.outputnet.value[0]      
            result = q_prev
        elif phi == '1' and phi_prev == '0' :
            d = linputlist[0].value[0]
            result = P_BUF[d]
        else:
            result = 'X'
        self.oldphi = phi
        return [(self.outputnet, (result, self.strength), self.driverpin)] if result != self.driverpin.state[0] else []
        
class BUFIF1 (primitive):
    '''
    BUFIF1 O IN EN
    '''
    def __init__(self, name, nlist, parent=None, strength=1) :
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        portlist = dict( [("O", gate.INOUT),("IN", gate.IN),("EN", gate.IN)])
        mapping = dict([ ("O", nlist[0]),("IN", nlist[1]),("EN", nlist[2])])
        gate.gate.__init__( self, name, portlist, mapping, parent, strength=strength, is_a_primitive=True)
        self.driverpin = self.outputpins['O'] 

    def simulate( self ) :
        en = self.inputlist[1].value
        if (en == '0'):
            result = ('Z', 0)
        elif ( en == '1'):
            a = self.inputlist[0].value
            result = (P_BUF[a], self.strength)
        else:
            result = ('X', self.strength)
        
        return [( self.outputnet, result, self.driverpin) ] if self.driverpin.state[0] != result[0] else []


class BUFIF0 (BUFIF1):
    '''
    BUFIF0 O IN EN
    '''
    def simulate( self ) :
        en = self.inputlist[1].value
        if (en == '1'):
            result = ('Z', 0)
        elif ( en == '0'):
            a = self.inputlist[0].value        
            result = (P_BUF[a], self.strength)
        else:
            result = ('X', self.strength)

        return [( self.outputnet, result, self.driverpin) ] if self.driverpin.state[0] != result[0] else []


class AOI(primitive):
    '''
    AOI OUTPUT [ [inputs] [ inputs] [...]]

    inputs in list of lists where inner lists are AND (series) trees and the 
    output list is the OR (parallel) tree
    '''
    def __init__(self, name, outputnet,  nlist, parent=None, strength=net.SUPPLY_STR, pulldown_str=net.SUPPLY_STR, pullup_str=net.DEPL_STR) :
        self.inputlist = nlist
        self.outputnet = outputnet

        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", outputnet)])
        group = 0
        for sublist in nlist:
            idx = 0
            for element in sublist:
                portname = "I%d_%d" % ( group, idx) 
                portlist[portname] = gate.IN
                mapping[portname] = element
                idx += 1
            group +=1
        gate.gate.__init__( self, name, portlist, mapping, parent, pulldown_str=pulldown_str, \
                                pullup_str=pullup_str, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 


    def simulate(self):
        # Workout whether pulldown tree is conducting first
        result = '0'
        for andterms in self.inputlist:
            sub = '1'
            for i in andterms:
                if i.value == '0':
                    sub = '0'
                    break
                elif i.value != '1':
                    sub = 'X'
            if sub == '1':
                result = '1'
                break
            elif result == '0' and sub == 'X':
                result == 'X'
        # Then turn it into the final output
        if result == '0':
            result = ('1',self.pullup_str) 
        elif result == '1':
            result = ('0', self.pulldown_str)
        else:
            result = ('X', self.pullup_str)
        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []


class AO(primitive):
    '''
    AO OUTPUT [ [inputs] [ inputs] [...]]

    inputs in list of lists where inner lists are AND (series) trees and the 
    output list is the OR (parallel) tree
    '''
    def __init__(self, name, outputnet,  nlist, parent=None, strength=net.SUPPLY_STR, pulldown_str=net.SUPPLY_STR, pullup_str=net.DEPL_STR) :
        self.inputlist = nlist
        self.outputnet = outputnet

        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", outputnet)])
        group = 0
        for sublist in nlist:
            idx = 0
            for element in sublist:
                portname = "I%d_%d" % ( group, idx) 
                portlist[portname] = gate.IN
                mapping[portname] = element
                idx += 1
            group +=1
        gate.gate.__init__( self, name, portlist, mapping, parent, pulldown_str=pulldown_str, \
                                pullup_str=pullup_str, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 


    def simulate(self):
        # Workout whether pulldown tree is conducting first
        result = '0'
        for andterms in self.inputlist:
            sub = '1'
            for i in andterms:
                if i.value == '0':
                    sub = '0'
                    break
                elif i.value != '1':
                    sub = 'X'
            if sub == '1':
                result = '1'
                break
            elif result == '0' and sub == 'X':
                result == 'X'
        # Then turn it into the final output
        if result == '0':
            result = ('0',self.pulldown_str) 
        elif result == '1':
            result = ('1', self.pullup_str)
        else:
            result = ('X', self.pullup_str)
        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []


    
class AOI_OD(primitive):
    '''
    Complex, but unidirectional pulldown tree (open drain)

    AOI_OD OUTPUT [ [inputs] [ inputs] [...]]

    inputs in list of lists where inner lists are AND (series) trees and the 
    output list is the OR (parallel) tree

    '''
    def __init__(self, name, outputnet,  nlist, parent=None, strength=net.SUPPLY_STR) :
        self.inputlist = nlist
        self.outputnet = outputnet

        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", outputnet)])
        group = 0
        for sublist in nlist:
            idx = 0
            for element in sublist:
                portname = "I%d_%d" % ( group, idx) 
                portlist[portname] = gate.IN
                mapping[portname] = element
                idx += 1
            group +=1
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=0, pulldown_str=strength, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 


    def simulate(self):
        result = '0'
        for andterms in self.inputlist:
            if all( [ i.value=='1' for i in andterms]):
                result = '1'
                break
            else:
                sub = '0' if any ( [i.value=='0' for i in andterms]) else 'X'
            if result == '0' and sub == 'X':
                result == 'X'

        # now turn the result into an open collector result
        if result == '0':
            result = ('Z',0)    # no pulldown
        elif result == '1':
            result = ('0', self.strength)
        else:
            # Dont turn X or Z into changes on the output to avoid glitches
            return []

        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []





class INV_APU(primitive):
    '''
    Inverter with active pullup

    INV_APU OUTPUT [pullup control, pulldown control]

    '''
    def __init__(self, name, outputnet,  nlist, parent=None, strength=net.SUPPLY_STR) :
        self.inputlist = nlist
        self.outputnet = outputnet

        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", outputnet)])

        idx = 0        
        for i in nlist :
            portname = "I%d" % idx
            portlist[portname] = gate.IN
            mapping[portname] =  i
            idx +=1            

        gate.gate.__init__( self, name, portlist, mapping, parent, strength, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 

    def simulate(self):
        pullup = self.inputlist[0].value
        pulldown = self.inputlist[1].value

        if pulldown == '1':
            result = ('0', self.strength)
        elif pullup == '1':
            result = ('1', self.strength)
        elif pulldown == '0' and pullup == '0':
            result = ('Z', 0)
        else:
            # too pessimistic to return 'X's if one of the inputs goes to 'Z' or ;X; in swithc
            # level simulation
            return []

        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []


class NAND_APU(primitive):
    '''
    NAND gate with active pullup

    NAND_APU [ OUTPUT , pullup control, pulldown control ...]

    '''
    def __init__(self, name, nlist, parent=None, strength=net.SUPPLY_STR) :
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]

        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", self.outputnet)])

        idx = 0        
        for i in nlist :
            portname = "I%d" % idx
            portlist[portname] = gate.IN
            mapping[portname] =  i
            idx +=1            

        gate.gate.__init__( self, name, portlist, mapping, parent, strength, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 

    def simulate(self):
        pd_values = [(i.value=='1',i.value=='0') for i in self.inputlist[1:]]
        pu_value  = self.inputlist[0].value

        if all([v[0] for v in pd_values ]):
            # pull down active if all transistors are on
            result = ('0', self.strength) 
        elif pu_value == '1':
            result = ('1', self.strength)
        elif any ([v[1] for v in pd_values ]) and pu_value =='0' :
            # all transistors open
            result = ('Z', 0)
        else:
            # Don't return result for X case to avoid glitches
            return []
        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []



class NOR_APU(NAND_APU):
    '''
    NOR gate with active pullup

    NOR_APU OUTPUT [pullup control, pulldown control ...]

    '''
    def simulate(self):
        # determine state of pullup first
        linputlist = self.inputlist
        if linputlist[0].value == '1':
            result = ('1', self.strength)
        else:
            result = ('Z', self.strength)
            
        # now work through pulldown list
        for n in linputlist[1:]:
            if n.value == '1':
                # pull down active if any transistors are on
                result = ('0', self.strength) 
                break
            elif n.value != '0':
                # don't return a value for Xs in a mixed level simulation - too pessimistic
                return []

        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []



class INV_OD(primitive):
    '''
    Single transistor pulldown tree with open drain (effectively same
    as NMOS transistor

    INV_OD OUTPUT INPUT 

    '''
    def __init__(self, name, outputnet,  inputnet, parent=None, strength=net.SUPPLY_STR) :
        self.inputlist = [inputnet]
        self.outputnet = outputnet

        portlist = dict([("O", gate.OUT), ("I0", gate.IN)])
        mapping = dict([("O", outputnet), ("I0", inputnet)])
        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=0, pulldown_str=strength, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 
        self.inputnet = inputnet
        
        
    def simulate(self):
        v = self.inputnet.value
        result = None
        if v == '1':
            result = ('0', self.strength)
        elif v == '0':
            result = ('Z', 0)          
        else:
            return []

        if self.driverpin.state[0] != result[0]:
            return [( self.outputnet, result , self.driverpin) ] 

class NAND_OD(primitive):
    '''
    Series transistor pulldown tree with open drain

    NAND_OD OUTPUT [inputs]

    '''
    def __init__(self, name, outputnet,  nlist, parent=None, strength=net.SUPPLY_STR, pullup_str=None, pulldown_str=None) :
        self.inputlist = nlist
        self.outputnet = outputnet

        portlist = dict([("O", gate.OUT)])
        mapping = dict([("O", outputnet)])

        idx = 0        
        for i in nlist :
            portname = "I%d" % idx
            portlist[portname] = gate.IN
            mapping[portname] =  i
            idx +=1            

        gate.gate.__init__( self, name, portlist, mapping, parent, pullup_str=0, pulldown_str=strength, is_a_primitive=True)
        self.driverpin = self.outputpins["O"] 


    def simulate(self):
        result = ('0', self.strength)
        for n in self.inputlist:
            if n.value == '0':
                result = ('Z', 0)
                break
            elif n.value != '1':
                # don't return an X value to avoid glitches
                return []
        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []


class NOR_OD(NAND_OD):
    '''
    Parallel transistor pulldown tree with open drain

    NOR_OD OUTPUT [inputs]

    '''
    def simulate(self):
        # simplified pulldown tree - dont return X's only 0 or Z
        result = ('Z', 0)
        for n in self.inputlist:
            if n.value == '1':
                result = ('0', self.pulldown_str)
                break
            elif n.value != '0':
                return []
        return [( self.outputnet, result , self.driverpin)] if self.driverpin.state[0] != result[0] else []


class UNMOS(primitive):
    '''
    Unidirectional NMOS transistor.

    UNMOS DRAIN SOURCE GATE

    Data moves from source to drain controlled by gate
    '''
    def __init__(self, name, nlist, parent=None, isweak=False) :
        self.inputlist = nlist[1:]
        self.outputnet = nlist[0]
        self.isweak = isweak
        portlist = dict( [("DRAIN", gate.OUT),("SOURCE", gate.IN),("GATE", gate.IN)])
        mapping = dict([ ("DRAIN", nlist[0]),("SOURCE", nlist[1]),("GATE", nlist[2])])
        gate.gate.__init__( self, name, portlist, mapping, parent, strength=0, is_a_primitive=True)
        self.driverpin = self.outputpins["DRAIN"] 

    def simulate( self) :
        gate = self.inputlist[1].value
        if gate == '0':
            result = ('Z',0)
        elif gate == '1':
            drain = self.inputlist[0]
            if self.isweak:
                result = ( drain.value, min(DEPL_STR-1, drain.strength) )
            else:
                result = ( drain.value, drain.strength)
        else:
            # same as for bidir case - return nothing if gate goes to x else
            # too pessimistic, eg momentary X on gate disturbing dynamic latches            
            return[]

        return [] if self.driverpin.state == result else [( self.outputnet, result, self.driverpin)] 


class UPMOS (UNMOS):
    '''
    Unidirectional PMOS transistor.

    UPMOS DRAIN SOURCE GATE

    Data moves from source to drain controlled by gate
    '''
    def simulate( self) :
        gate = self.inputlist[1].value
        if gate == '1' :
            result = ('Z',0)
        elif gate == '0':
            result = (self.inputlist[0].value, self.inputlist[0].strength)
        else:
            # same as for bidir case - return nothing if gate goes to x else
            # too pessimistic, eg momentary X on gate disturbing dynamic latches
            return[]

        return [] if self.driverpin.state == result else [( self.outputnet, result, self.driverpin)] 


class NMOS (primitive):
    '''
    Bidirectional NMOS transistor.

    NMOS DRAIN SOURCE GATE

    '''
    def __init__(self, name, nlist, parent=None, isweak=False) :
        self.inputlist = nlist
        self.drainnet = nlist[0]
        self.sourcenet = nlist[1]
        self.isweak = isweak
        portlist = dict( [("DRAIN", gate.INOUT),("SOURCE", gate.INOUT),("GATE", gate.IN)])
        mapping = dict([ ("DRAIN", nlist[0]),("SOURCE", nlist[1]),("GATE", nlist[2])])
        gate.gate.__init__( self, name, portlist, mapping, parent, strength=0, is_a_primitive=True)
        self.sourcepin = self.outputpins['SOURCE']
        self.drainpin = self.outputpins['DRAIN']
        self.source_drivers = None
        self.drain_drivers = None
        self.all_drivers = None

    def simulate( self ) :
        # gate is input only so just read the value directly 
        linputlist = self.inputlist
        gate = linputlist[2].value
        if gate == '0':
            source_result = drain_result = ('Z', 0)
        elif gate == '1':
            # Evaluate drivers on source (drain) side excluding this device's own pins
            # and propagate the result to the drain (source side).
            (dval, dstr) = sevaluate_net_drivers(linputlist[1], self.source_drivers) 
            (sval, sstr) = sevaluate_net_drivers(linputlist[0], self.drain_drivers) 
            if self.isweak:
                dstr = min(DEPL_STR-1, dstr)
                sstr = min(DEPL_STR-1, sstr)
            source_result = (sval, sstr)
            drain_result = (dval, dstr)

        else: 
            # Return no change if the gate goes to 'x' - too pessimistic to do anything
            # else as nodes can go 0X1 or 1X0 as transitions it this iterative system
            return []

        result = []
        if self.sourcepin.state != source_result:
            result = [( self.sourcenet, source_result, self.sourcepin)]
        if self.drainpin.state != drain_result:
            result.append( ( self.drainnet, drain_result, self.drainpin) )
        return result


class PMOS (NMOS):
    '''
    Bidirectional PMOS transistor.

    PMOS DRAIN SOURCE GATE

    '''

    def simulate( self ) :
        # gate is input only so just read the value directly 
        gate = self.inputlist[2].value
        drain = self.inputlist[0]
        source = self.inputlist[1]
        if self.source_drivers == None:
            self.source_drivers = [p for p in source.drivers if p != self.sourcepin ]
        if self.drain_drivers == None:
            self.drain_drivers = [p for p in drain.drivers if p != self.drainpin ] 
        
        if (gate == '1'):
            source_result = ('Z', 0)
            drain_result = ('Z', 0)
        elif (gate == '0'):
            # Find value and strength of source and drain excluding input from the pins themselves
            # NB. Static optimization always eliminates NMOS gates which have supply 
            # connected to diffusion, so no need to handle these as a special case
            drain_result = sevaluate_net_drivers(source, self.source_drivers) 
            source_result = sevaluate_net_drivers(drain, self.drain_drivers)                
        else: 
            # Return no change if the gate goes to 'x' - too pessimistic to do anything
            # else as nodes can go 0X1 or 1X0 as transitions it this iterative system
            return []

        result = []
        if self.sourcepin.state != source_result:
            result.append( ( self.sourcenet, source_result, self.sourcepin) )
        if self.drainpin.state != drain_result:
            result.append( ( self.drainnet, drain_result, self.drainpin) )
        return result

class PULLUP(primitive):
    '''
    PULLUP OUT
    '''
    def __init__(self, name, nlist, parent=None, strength=1) :
        self.inputlist = nlist
        self.outputnet = nlist[0]
        portlist = dict( [("OUT", gate.OUT)])
        mapping = dict([ ("OUT", nlist[0])])
        # not sure we even need to add this as a component
        gate.gate.__init__( self, name, portlist, mapping, parent, strength=strength, is_a_primitive=True)
        self.driverpin = self.outputpins["OUT"] 
        # Pullups have a constant value so only ever need to include this in a net's driver table        
        self.driverpin.state = ('1',self.strength)

    def simulate( self ) :
        # Should never need to return a simulation result from a pull-up
        # return [( self.outputnet, ('1', 1), self.driverpin) ] 
        return []


class MSLAT( primitive ) :
    '''
    MSLAT Q QB RAN PHIA RBN PHIB
    '''
    def __init__(self, name, nlist, parent=None, strength=1) :
        self.strength = strength  
        portlist = dict( [("Q", gate.OUT),("QB", gate.OUT), ("RAN", gate.IN),("PHIA", gate.IN),("RBN", gate.IN),("PHIB", gate.IN)] )
        mapping = dict([ ("Q", nlist[0]),("QB", nlist[1]),("RAN", nlist[2]),("PHIA", nlist[3]),("RBN", nlist[4]),("PHIB", nlist[5])] )
        gate.gate.__init__( self, name, portlist, mapping, parent, strength=strength, is_a_primitive=True)
        self.inputlist = nlist[2:]
        self.outputnets = nlist[0:2]
        self.gatelist = []
        self.qa = 'X'
        self.qan = 'X'
        self.qb = 'X'
        self.qbn = 'X'
        self.driverpins = [self.outputpins['Q'], self.outputpins['QB']]

    def simulate(self):
        ran = self.inputlist[0].value[0]
        phia = self.inputlist[1].value[0]
        rbn = self.inputlist[2].value[0]
        phib = self.inputlist[3].value[0]

        for iteration in xrange(0,1):
            # iterate twice in case both clocks are open !
            if phia == '1':
                self.qa = self.qbn
        
            if ran == '1' or self.qa == '1':
                self.qan = '0'
            elif ran == '0' and self.qa == '0':
                self.qan = '0'
            else:
                self.qan = 'X'
                
            if phib == '1':
                self.qb = self.qan
                
            if rbn == '1' or self.qb == '1':
                self.qbn = '0'
            elif rbn == '0' and self.qb == '0':
                self.qbn = '0'
            else:
                self.qbn = 'X'

        results = []
        if self.qan != self.outputpins['Q'].state[0] :
            results.append( (nlist[0], (self.qan, self.strength), self.outputpins['Q'] ))
        if self.qbn != self.outputpins['Q'].state[0] :
            results.append( (nlist[1], (self.qbn, self.strength), self.outputpins['QB']))

        return results


if __name__ == "__main__":

    n = [ net.net( "n%d" %i ) for i in xrange (0, 10)]


    i0 = INV( name="DUT", nlist=[n[0], n[1]] , parent=None, strength=0)
    i1 = DFF( name="DUT_FF", nlist=n[0:4] , parent=None, strength=0)
    i2 = BUFIF1( name = "TRI", nlist=n[0:3] , parent=None, strength=10)
    print i2.tostring()
