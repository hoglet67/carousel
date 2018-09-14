import gate
import net
from testbench import testbench
from primitive import UNMOS, PULLUP

class nmos_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self,options)

        self.netlist.update( gate.wire([ 'in0', 'in1', 'out', 'n0']))
        self.netlist['out'].pullup_str=1

        dut0 = UNMOS( "unmos_0_u", [ self.netlist['n0'], self.netlist['vss'], self.netlist['in0']], self)       
        dut1 = UNMOS( "unmos_1_u", [ self.netlist['out'], self.netlist['n0'], self.netlist['in1']], self)       

        self.gatelist = [dut0, dut1]

        vector_string = '''

PI in0
PI in1
PO out

#  ii o
#  nn u
#  01 t
# ------
   00 H
   01 H
   10 H
   11 L
   01 H
   10 H
   00 H
   10 H
   11 L
'''

        self.events  = self.read_flex_string( vector_string)
