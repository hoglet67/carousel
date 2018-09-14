import gate
import net
from testbench import testbench
from primitive import BUFIF1, BUF

class tristate_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)

        for name in ['in0', 'in1', 'in2', 'en0', 'en1', 'en2', 'n0', 'n1']:
            self.netlist[name]=net.net(name)

        dut0 = BUFIF1( "bufif1_0_u", [ self.netlist['n0'], self.netlist['in0'], self.netlist['en0']], strength=net.SUPPLY_STR)       
        dut1 = BUFIF1( "bufif1_1_u", [ self.netlist['n0'], self.netlist['in1'], self.netlist['en1']], strength=net.SUPPLY_STR)
        dut2 = BUFIF1( "bufif1_2_u", [ self.netlist['n0'], self.netlist['in2'], self.netlist['en2']], strength=net.SUPPLY_STR)

        dut3 = BUF("buf_0_u", [ self.netlist['n1'], self.netlist['n0']])

        self.gatelist = [dut0, dut1, dut2, dut3 ]

        vector_string = '''
PI in0
PI in1
PI in2
PI en0
PI en1
PI en2
PO n0
PO n1

 000   000 XX
 000   001 00
 000   010 00
 000   011 00
 000   100 00
 000   101 00
 000   110 00
 000   111 00
 100   000 XX
 100   001 00
 100   010 00
 100   011 00
 100   100 11
 100   101 XX
 100   110 XX
 100   111 00
'''

        self.events  = self.read_flex_string( vector_string)


