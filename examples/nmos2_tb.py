import gate
import net
from testbench import testbench
from nmos_lib import NMOS_NMAJ, NMOS_XOR2, NMOS_DFF


class nmos2_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self,options)

        self.netlist.update( gate.wire([ 'clk', 'in0', 'in1', 'in2', 'net0', 'net1', 'out1', 'out2', 'rstb']))
        dut0 = NMOS_NMAJ( "maj_0_u", dict([('OUT',self.netlist['net0']), ('I0',self.netlist['in1']), ('I1',self.netlist['in2']), ('I2',self.netlist['in0'])]), self)       
        dut1 = NMOS_XOR2( "xor_1_u", dict([('OUT',self.netlist['net1']),('I0',self.netlist['out1']), ('I1',self.netlist['in1'])]), self)       
        dut2 = NMOS_XOR2( "xor_2_u", dict([('OUT',self.netlist['out1']),('I0',self.netlist['in2']), ('I1',self.netlist['in1'])]), self)       
        dut3 = NMOS_DFF( "dff_0_u", dict([('Q',self.netlist['out2']),('RSTB',self.netlist['rstb']), ('PHI',self.netlist['clk']),('D',self.netlist['net1'])]), self)       
        self.gatelist = [dut0, dut1, dut2, dut3]

        vector_string = '''

PI clk 
PI rstb
PI in0
PI in1
PI in2
PO out1
PO out2

  00 000 00
  01 000 00
  01 000 00
  11 010 10
  01 100 00
  01 110 10
  11 010 10
  01 100 00
  11 000 00
  01 100 00
  11 110 10
  01 000 00
  11 011 00
  01 101 10
  11 111 01
  01 011 01
  11 101 11
  01 001 11
'''

        self.events  = self.read_flex_string( vector_string)
