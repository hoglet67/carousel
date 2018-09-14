import gate
import net
from testbench import testbench
from primitive import UNMOS, UPMOS, INV

class domino_tb(testbench):

    '''
    Simple dynamic logic gate with unidirectional transistors

                            vdd-*-
                                |
    prech ---|>o------*------o|[    n0
                      |         *---*---------|>o---- out
                      | in2 --|[n1  |
                      | in1 --|[n2 === 
                      | in0 --|[n3  |
                      `-------|[    |
                              -*----*--
                               vss
    '''

    def __init__(self, options):
        testbench.__init__(self, options)

        # Declare nets
        for name in [ 'prechb', 'prech', 'in0', 'in1', 'in2', 'n0', 'n1', 'n2', 'n3', 'out' ]:
            self.netlist[name]=net.net(name)

        self.netlist['n0'].charge_storage=True               

        dut0 = UPMOS( "upmos_0_u", [ self.netlist['n0'], self.netlist['vdd'], self.netlist['prechb']], self)       
        dut1 = UNMOS( "unmos_1_u", [ self.netlist['n0'], self.netlist['n1'], self.netlist['in2']], self)       
        dut2 = UNMOS( "unmos_2_u", [ self.netlist['n1'], self.netlist['n2'], self.netlist['in1']], self)       
        dut3 = UNMOS( "unmos_3_u", [ self.netlist['n2'], self.netlist['n3'], self.netlist['in0']], self)       
        dut4 = UNMOS( "unmos_4_u", [ self.netlist['n3'], self.netlist['vss'], self.netlist['prechb']], self)       
        dut5 = INV( "inv_0_u", [ self.netlist['prechb'], self.netlist['prech']], self)       
        dut6 = INV( "inv_1_u", [ self.netlist['out'], self.netlist['n0']], self)       

        self.gatelist = [dut0, dut1, dut2, dut3, dut4, dut5 ]

        vector_string = '''

PI prech
PI in0
PI in1
PI in2
PO out

#  p
#  r
#  eiii o
#  cnnn u
#  h012 t
# ------
   1000 L
   0010 L
   0100 L
   0111 H 
   1111 L
   0100 L
   0010 L
   0001 L
   0111 H
   0000 H
'''

        self.events  = self.read_flex_string( vector_string)






