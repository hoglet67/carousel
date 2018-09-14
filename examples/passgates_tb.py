import gate
import net
from testbench import testbench
from primitive import NMOS, UNMOS

class passgates_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)

        self.netlist.update(gate.wire( ['in0', 'in1', 'in2', 'in3', 'in4', 'in5', 'n0', 'n1', 'n2', 'n3', 'out' ]))
        self.netlist['out'].pullup_str = net.DEPL_STR
        self.netlist['n0'].pullup_str = net.DEPL_STR
        self.netlist['n1'].pullup_str = net.DEPL_STR
        self.netlist['n2'].charge_storage = True
        self.netlist['n3'].charge_storage = True
        
        self.gatelist = [
            NMOS( "nmos_0_u", [ self.netlist['n0'], self.netlist['vss'], self.netlist['in0']], self),
            NMOS( "nmos_1_u", [ self.netlist['n1'], self.netlist['vss'], self.netlist['in1']], self),
            NMOS( "nmos_2_u", [ self.netlist['n2'], self.netlist['vss'], self.netlist['in2']], self),
            NMOS( "nmos_3_u", [ self.netlist['n0'], self.netlist['n2'], self.netlist['in3']], self),
            NMOS( "nmos_4_u", [ self.netlist['n1'], self.netlist['n2'], self.netlist['in4']], self),
            UNMOS( "unmos_5_u", [ self.netlist['n3'], self.netlist['n2'], self.netlist['in5']], self),
            NMOS( "nmos_6_u", [ self.netlist['out'], self.netlist['vss'], self.netlist['n3']], self),

            ]
        



        vector_string = '''

PI in0
PI in1
PI in2
PI in3
PI in4
PI in5
PO n2
PO out

#  iiiiii   o
#  nnnnnn n u
#  012345 2 t
# -------------
   111111 L H
   000000 L H
   000100 H H
   000001 H L
   000000 H L
   101010 L L
   010101 H L
   000110 H L
   000101 H L
   101000 L L
   000001 L H
'''

        self.events  = self.read_flex_string( vector_string)



