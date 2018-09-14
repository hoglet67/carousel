import gate
import net
from testbench import testbench
from primitive import BUF, INV, NMOS, UNMOS

class muxtest_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)

        self.netlist.update(gate.wire( ['in0', 'in1', 'in2', 'n0', 'n1', 'n2', 'n2b', 'mx0', 'mx1', 'out', 'out1' ]))
        self.netlist['mx0'].charge_storage = True
        
        self.gatelist = [

            INV ("inv_0_u", [self.netlist['n0'], self.netlist['in0']], self),
            INV ("inv_1_u", [self.netlist['n1'], self.netlist['in1']], self),
            INV ("inv_2_u", [self.netlist['n2b'], self.netlist['in2']], self),            
            BUF ("buf_0_u", [self.netlist['n2'], self.netlist['in2']], self),            
            UNMOS( "nmos_0_u", [ self.netlist['mx0'], self.netlist['n0'], self.netlist['n2b']], self),
            UNMOS( "nmos_1_u", [ self.netlist['mx0'], self.netlist['n1'], self.netlist['in2']], self),
            UNMOS( "nmos_2_u", [ self.netlist['mx1'], self.netlist['n0'], self.netlist['n2b']], self),
            UNMOS( "nmos_3_u", [ self.netlist['mx1'], self.netlist['n1'], self.netlist['n2']], self),
            INV ("inv_3_u", [self.netlist['out'], self.netlist['mx0']], self),
            INV ("inv_4_u", [self.netlist['out1'], self.netlist['mx1']], self),
            ]

        vector_string = '''

PI in0
PI in1
PI in2
PO out
#       o
#  iii ou
#  nnn ut
#  012 t1
# -------------
   000 LL
   001 LL
   010 LL
   011 HH
   100 HH
   101 LL
   110 HH
   111 HH
   000 LL
   001 LL
   010 LL
   011 HH
'''

        self.events  = self.read_flex_string( vector_string)



