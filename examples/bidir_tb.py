import gate
import net
from testbench import testbench
from primitive import UNMOS, PULLUP
from bidir_nmos_lib import NMOS_NMAJ, NMOS_NOR2

class bidir_tb(testbench):

    def __init__(self,options):
        testbench.__init__(self, options)

        self.netlist.update( gate.wire([ 'a', 'b', 'c', 's', 'r', 'q', 'qb', 'o']))

        dut0 = NMOS_NMAJ( "nmos_maj_0_u", dict([('OUT', self.netlist['o']), ('I0', self.netlist['a']),
                                               ('I1', self.netlist['b']), ('I2', self.netlist['c'])]), self)
        self.gatelist = [dut0]

        self.pi_events = []

        vector_string = '''
PI a
PI b
PI c
PO o
#   abc o
# ---------
    000 H
    001 H
    010 H
    011 L
    100 H
    101 L
    110 L
    111 L
'''

        self.events  = self.read_flex_string( vector_string)
