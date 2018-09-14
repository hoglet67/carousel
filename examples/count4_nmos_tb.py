import gate
import net
from testbench import testbench
from count4_nmos import count4_nmos


class count4_nmos_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self,options)

        self.netlist.update( gate.wire([ 'clk', 'q0', 'q1', 'q2', 'q3', 'cout', 'cin', 'rstb']))

        nn = self.netlist
        
        self.gatelist = [\
            count4_nmos( "count4_0_u", dict([('Q0', nn['q0']),('Q1', nn['q1']),('Q2', nn['q2']),('Q3', nn['q3']), \
                                                 ('COUT',nn['cout']), ('CIN', nn['cin']), ('RSTB', nn['rstb']), \
                                                 ('PHI',nn['clk'])]), self)
            ]

        vector_string = '''

PI clk
PI rstb
PI cin
PO q3
PO q2
PO q1
PO q0

  001 LLLL
  011 LLLL
  011 LLLL
  111 LLLH
  011 LLLH
  111 LLHL
  011 LLHL
  111 LLHH
  011 LLHH
  111 LHLL
  011 LHLL
  111 LHLH
  011 LHLH
  111 LHHL
  011 LHHL
  111 LHHH
  011 LHHH
  111 HLLL
  011 HLLL
  111 HLLH
  011 HLLH
  111 HLHL
  011 HLHL


'''

        self.events  = self.read_flex_string( vector_string)
