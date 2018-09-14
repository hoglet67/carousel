from collections import deque
import gate 
from net import net
import net
import pin


class testbench(gate.module) :

    def __init__(self, options) :
        gate.module.__init__( self, name='', portlist=[], mapping=dict())
        self.events = []
        self.pins = dict() # create a new list for storing pins on PIs and IOs
        self.options = options # dictionary of any settings required for subcomponents

    def read_flex_string(self,  string):
        events = []
    
        signal_list = []
        prev_drive_data = dict()
    
        valid_chars = '01HLZX'
        expect_table = { 'H':'1','L':'0','Z':'X', 'X':'X','1':'1','0':'0' }
        pin_decl = True
        for line in string.split('\n'):
            l = line.strip()
            f = l.split()
            if l.startswith('#') or not l:
                # skip blanks
                pass
            elif pin_decl:
                if l.startswith('PI'):
                    signal_list.append( (f[1], gate.IN, self.netlist[f[1]]))
                    if f[1] not in self.pins:
                        p = pin.pin(name=f[1], parent=self, netconn=self.netlist[f[1]], strength = net.SUPPLY_STR)
                        self.pins[f[1]] = p                        
                        if self.pins[f[1]] not in self.netlist[f[1]].drivers:
                            self.netlist[f[1]].drivers.append(p)
                    prev_drive_data[f[1]] = 'X'
                if l.startswith('PO'):
                    signal_list.append( (f[1], gate.OUT,  self.netlist[f[1]]))
                    prev_drive_data[f[1]] = 'X'
                if l.startswith('IO_HL'):
                    signal_list.append( (f[1], gate.INOUT,  self.netlist[f[1]]))
                    if f[1] not in self.pins:
                        self.pins[f[1]] = pin.pin(name=f[1], parent=self, netconn=self.netlist[f[1]],\
                                                      strength=net.SUPPLY_STR)
                        if self.pins[f[1]] not in self.netlist[f[1]].drivers:
                            self.netlist[f[1]].drivers.append(p)

                    prev_drive_data[f[1]] = 'X'
                if l[0] in valid_chars:
                    pin_decl = False
            if not pin_decl:
                vector_data = []
                pi_events = []
                po_events = []

        
                for c in l:
                    if c == '#' :
                        continue
                    elif c in valid_chars:
                        vector_data.append(c)
    
                # Always force the inputs and let the event driven simulation cope  - important
                # when bidirs contend for example and need to reassert the input
                for (c, port) in zip( vector_data, signal_list):
                    if port[1] == gate.IN:
                        if prev_drive_data[port[0]] != c:
                            pi_events.append((port[2], (c, net.SUPPLY_STR), self.pins[port[0]]))
                            prev_drive_data[port[0]] = c
                    elif port[1] == gate.OUT:
                        if c != 'X':
                            po_events.append((port[2], expect_table[c], 'pi'))
                    elif port[1] == gate.INOUT:
                        if c == 'H' or c == 'L' or c =='X':
                            if prev_drive_data[port[0]] != 'Z':
                                pi_events.append((port[2], ('Z', 0),  self.pins[port[0]]))
                                prev_drive_data[port[0]] = 'Z'
                            if c != 'X':
                                po_events.append((port[2], expect_table[c], 'pi' ))
                        elif c == '1' or c == '0' or c == 'Z':
                            if prev_drive_data[port[0]] != c:
                                pi_events.append((port[2], (c, 0), self.pins[port[0]]))
                                prev_drive_data[port[0]] = c
    
                events.append( (pi_events, po_events))

        return events

if __name__ == '__main__':
    v = '''
# comment
PI A
PI B
PO C
IO_HL D

11HL
11LH # comment
11LL
10HZ
'''

    tb = testbench.testbench('dummy');
    tb.netlist = dict()
    tb.netlist.update(gate.wire( ['A','B', 'C', 'D']))
    tb.read_flex_string(v)
