import gate
import net
from testbench import testbench
from primitive import NMOS, UNMOS

class latch_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)

        self.netlist.update(gate.wire( ['cclk', 'n821', 'n826', 'n318', 'n1062', 'n1315', 'n705', 'out', 'abh0' ]))
        self.netlist['n1315'].pullup_str = net.DEPL_STR
        self.netlist['abh0'].pullup_str = net.DEPL_STR
        self.netlist['n1062'].charge_storage = True
        
        self.gatelist = [
            NMOS( "nmos_0_u", [ self.netlist['out'], self.netlist['vdd'], self.netlist['n826']], self),
            NMOS( "nmos_1_u", [ self.netlist['out'], self.netlist['vss'], self.netlist['n318']], self),

            NMOS( "nmos_2_u", [ self.netlist['n318'], self.netlist['vdd'], self.netlist['n1315']], self),
            NMOS( "nmos_3_u", [ self.netlist['n318'], self.netlist['vss'], self.netlist['abh0']], self),

            NMOS( "nmos_4_u", [ self.netlist['n826'], self.netlist['vdd'], self.netlist['abh0']], self),
            NMOS( "nmos_5_u", [ self.netlist['n826'], self.netlist['vss'], self.netlist['n318']], self),

            NMOS( "nmos_6_u", [ self.netlist['n1315'], self.netlist['vss'], self.netlist['abh0']], self),
            NMOS( "nmos_7_u", [ self.netlist['abh0'], self.netlist['vss'], self.netlist['n1062']], self),
            NMOS( "nmos_8_u", [ self.netlist['n318'], self.netlist['n1062'], self.netlist['cclk']], self),
            NMOS( "nmos_9_u", [ self.netlist['n705'], self.netlist['n1062'], self.netlist['n821']], self),
            ]
        



        vector_string = '''

PI n705
PI n821
PI cclk
PO out

   001 X
   010 H
   001 H
   101 H
   110 L
   101 L
   001 L
   010 H


'''  

        self.events  = self.read_flex_string( vector_string)



