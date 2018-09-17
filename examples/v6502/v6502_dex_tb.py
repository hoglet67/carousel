import gate
import net
from testbench import testbench
from source import v6502


class v6502_dex_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)


        self.netlist.update( gate.wire(['data%d_w' %i for i in range(0,8)]))
        self.netlist.update( gate.wire(['addr%02d_w' %i for i in range(0,16)]))
        self.netlist.update( gate.wire([ 'rstb_w', 'rnw_w', 'sync_w', 'sob_w', 'phi0_w', 'phi1_w', 'phi2_w', 'rdy_w', 'nmib_w', 'irqb_w']))

        self.netlist['vcc'] = net.supply1('vcc')
        self.netlist['vss'] = net.supply0('vss')
        self.netlist['vdd'] = net.supply1('vdd')

        self.gatelist = [ v6502( "v6502_0_u", dict([\
                        ('res', self.netlist['rstb_w']),
                        ('rw',  self.netlist['rnw_w']),
                        ('db0', self.netlist['data0_w']),
                        ('db1', self.netlist['data1_w']),
                        ('db2', self.netlist['data2_w']),
                        ('db3', self.netlist['data3_w']),
                        ('db4', self.netlist['data4_w']),
                        ('db5', self.netlist['data5_w']),
                        ('db6', self.netlist['data6_w']),
                        ('db7', self.netlist['data7_w']),
                        ('ab0', self.netlist['addr00_w']),
                        ('ab1', self.netlist['addr01_w']),
                        ('ab2', self.netlist['addr02_w']),
                        ('ab3', self.netlist['addr03_w']),
                        ('ab4', self.netlist['addr04_w']),
                        ('ab5', self.netlist['addr05_w']),
                        ('ab6', self.netlist['addr06_w']),
                        ('ab7', self.netlist['addr07_w']),
                        ('ab8', self.netlist['addr08_w']),
                        ('ab9', self.netlist['addr09_w']),
                        ('ab10',self.netlist['addr10_w']),
                        ('ab11',self.netlist['addr11_w']),
                        ('ab12',self.netlist['addr12_w']),
                        ('ab13',self.netlist['addr13_w']),
                        ('ab14',self.netlist['addr14_w']),
                        ('ab15',self.netlist['addr15_w']),
                        ('sync',self.netlist['sync_w']), 
                        ('so',  self.netlist['sob_w']),
                        ('clk0',self.netlist['phi0_w']),
                        ('clk1out',self.netlist['phi1_w']),
                        ('clk2out',self.netlist['phi2_w']),
                        ('rdy', self.netlist['rdy_w']),
                        ('nmi', self.netlist['nmib_w']),
                        ('irq', self.netlist['irqb_w']),
                        ('vss', self.netlist['vss']),
                        ('vcc', self.netlist['vcc']),
                        ])) ]
                          


        vector_string = '''
PI rstb_w

PI phi0_w

PI data7_w
PI data6_w
PI data5_w
PI data4_w
PI data3_w
PI data2_w
PI data1_w
PI data0_w

PI sob_w
PI nmib_w
PI irqb_w
PI rdy_w

'''
        vectors = []
        opcode = '11001010'
        reset = '0'
        for i in range (0, 4096):
            for clockseq in ['0','1']:
                vectors.append( " %s %s %s 10111" % (reset, clockseq, opcode))
            if i > 3:
                reset = '1'
        vector_string += '\n'.join(vectors)


        self.events  = self.read_flex_string( vector_string)

