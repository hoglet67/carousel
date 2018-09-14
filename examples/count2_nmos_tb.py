import gate
import net
from testbench import testbench
from count2_nmos import count2_nmos


class count2_nmos_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self,options)

        self.netlist.update( gate.wire([ 'clk', 'q0', 'q1', 'rstb']))

        nn = self.netlist
        
        self.gatelist = [\
            count2_nmos( "count2_0_u", dict([('Q0', nn['q0']),('Q1', nn['q1']),('RSTB', nn['rstb']),('PHI',nn['clk'])]), self)
            ]

        vector_string = '''

PI clk
PI rstb
PO q1
PO q0

  00 LL
  00 LL
  01 LL
  01 LL
  11 LH
  01 LH
  11 HL
  01 HL
  11 HH
  01 HH
  11 LL
  01 LL
  11 LH
  01 LH
  11 HL
  01 HL
  11 HH
  01 HH
  11 LL
  01 LL
  11 LH
  01 LH
  11 HL
  01 HL


'''

        self.events  = self.read_flex_string( vector_string)
