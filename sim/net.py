import gate
SUPPLY_STR = 1000
DEPL_STR = 100

class net :

    def __init__ ( self, name, value='X', strength=0, parent=None, issupply=False, pullup_str=0, pulldown_str=0, charge_storage=False, cap=1):
        if parent:
            self.fullname = '.'.join([parent.fullname(), name]) 
        else:
            self.fullname = name        
        self.issupply=issupply
        self.pullup_str = pullup_str
        self.pulldown_str = pulldown_str
        self.charge_storage = charge_storage 
        self.parent = parent
        self.name = name         
        self.value = value         # logic value
        self.poc_prev_value = 'U'  # immediately previous value - used for print on change tracing
        self.strength = strength   # resolved strength of mulitple drivers
        self.all_fanin = set([])   # all pin objects
        self.all_gate_fanin = set() # all gate objects
        self.drivers = list()      # drivers only
        self.all_fanout = set()    # all gate objects
        self.prim_fanout = set()   # leaf cells only
        self.bidir_efanout = list() # leaf cell evaluators of gates with bidirectional pins on fanout
        self.efanout = []          # leaf cell evaluators
        self.toggle_ctr = 0
        self.resolution_ctr = 0
        self.has_bidir_elements=False 

    def all_connected(self, primitive_only=True):
        '''
        Return a list of all gate elements connected to a net
        '''
        cset = set()
        if primitive_only:
            cset = set( [ c for c in self.all_gate_fanin if c.is_a_primitive] )
            cset.update( [ c for c in self.all_fanout if c.is_a_primitive])
        else:
            cset = set(set.all_fanin)
            cset.update(all_fanout)
        return list(cset)

    def to_str( self ) :
        result = "%s:%s" % (self.name, self.value[0])
        return result

    def resolve_single_driver(self):
        self.resolution_ctr += 1
        result = self.drivers[0].state
        if result != (self.value, self.strength):
            # new result returns evaluators of all fanout
            (self.value, self.strength) = result
            self.toggle_ctr +=1
            return self.efanout
        else:
            # always return bidir elements for evaluation due to 'memory' effect
             # return self.bidir_efanout
            return []

    def resolve_single_driver_with_storage(self):
        self.resolution_ctr += 1
        result = self.drivers[0].state
        current_value = self.value
        # resolve the case where the net has storage
        if result[0] == 'Z' or result[1] == 0:
            result = (current_value, 1 if current_value =='1' else 0)

        if result != (current_value, self.strength):
            # new result returns evaluators of all fanout
            (self.value, self.strength) = result
            self.toggle_ctr +=1
            return self.efanout
        else:
            # always return bidir elements for evaluation due to 'memory' effect
            # return self.bidir_efanout
            return []

    def resolve(self):
        '''
        Net resolution function needs to account for charge storage
        '''
        self.resolution_ctr += 1
        result = sevaluate_net_drivers(self, self.drivers)

        if result != (self.value, self.strength):
            # new result returns evaluators of all fanout
            (self.value, self.strength) = result
            self.toggle_ctr +=1
            return self.efanout
        else:
            # always return bidir elements for evaluation due to 'memory' effect
            return self.bidir_efanout

def sevaluate_net_drivers(netobj, driverpin_list):
    '''
    Evaluate the result on a net due to all drivers or explicit driver list.

    Routine is faster to call as a static definition than as an instance
    method and is used from other modules as well as this net.py module.
    '''
    ones = netobj.pullup_str
    zeros = netobj.pulldown_str            

    for (val,str) in [ n.state for n in driverpin_list]:
        if val == '1' and ones < str:
            ones = str
        elif val == '0' and zeros < str:
            zeros = str

    if zeros == SUPPLY_STR:
        # zero always wins if at supply strength
        return ('0', SUPPLY_STR )               
    elif zeros > ones : 
        return ('0', zeros)
    elif ones > zeros or ones != 0:
        # Ones win if stronger than zero, or if equal then
        # weak/floating high wins
        return ('1', ones)
    elif netobj.charge_storage : 
        return (netobj.value,  1 if netobj.value =='1' else 0)
    else:
        return ('Z', 0)                


class supply0 (net):
    def __init__ ( self, name, parent=None):
        net.__init__( self, name, value='0', strength=SUPPLY_STR, parent=parent, issupply=True)

    def resolve(self):
        # supply net never changes so always return emtpy set
        return []

class supply1 (net):
    def __init__ ( self, name, parent=None):
        net.__init__( self, name, value='1', strength=SUPPLY_STR, parent=parent, issupply=True)

    def resolve(self):
        # supply net never changes so always return empty set
        return []


if __name__ == '__main__':

    n1 = net("dummy")
    n1.drivers['a'] = ('0', 0)
    n1.drivers['b'] = ('1', 0)
    n1.drivers['c'] = ('0', 0)
    print n1.resolve()
    print n1.to_str()
