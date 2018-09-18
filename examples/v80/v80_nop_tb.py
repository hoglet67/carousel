import gate
import net
from testbench import testbench
from v80 import v80


class v80_nop_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)

        self.netlist.update( gate.wire(['data%d_w' %i for i in range(0,8)]))
        self.netlist.update( gate.wire(['addr%02d_w' %i for i in range(0,16)]))
        self.netlist.update( gate.wire(['clk_w', '_reset_w', '_wait_w', '_int_w', '_nmi_w', '_busrq_w', '_m1_w', '_rd_w', '_wr_w', '_mreq_w', '_iorq_w', '_rfsh_w', '_halt_w', '_busak_w']))

        self.netlist['vcc'] = net.supply1('vcc')
        self.netlist['vss'] = net.supply0('vss')
        self.netlist['vdd'] = net.supply1('vdd')
        
        self.gatelist = [ v80( "v80_0_u", dict([\
                        ('clk',     self.netlist['clk_w']),
                        ('a0',      self.netlist['addr00_w']),
                        ('a1',      self.netlist['addr01_w']),
                        ('a2',      self.netlist['addr02_w']),
                        ('a3',      self.netlist['addr03_w']),
                        ('a4',      self.netlist['addr04_w']),
                        ('a5',      self.netlist['addr05_w']),
                        ('a6',      self.netlist['addr06_w']),
                        ('a7',      self.netlist['addr07_w']),
                        ('a8',      self.netlist['addr08_w']),
                        ('a9',      self.netlist['addr09_w']),
                        ('a10',     self.netlist['addr10_w']),
                        ('a11',     self.netlist['addr11_w']),
                        ('a12',     self.netlist['addr12_w']),
                        ('a13',     self.netlist['addr13_w']),
                        ('a14',     self.netlist['addr14_w']),
                        ('a15',     self.netlist['addr15_w']),
                        ('_reset',  self.netlist['_reset_w']),
                        ('_wait',   self.netlist['_wait_w']),
                        ('_int',    self.netlist['_int_w']),
                        ('_nmi',    self.netlist['_nmi_w']),
                        ('_busrq',  self.netlist['_busrq_w']),
                        ('_m1',     self.netlist['_m1_w']),
                        ('_rd',     self.netlist['_rd_w']),
                        ('_wr',     self.netlist['_wr_w']),
                        ('_mreq',   self.netlist['_mreq_w']),
                        ('_iorq',   self.netlist['_iorq_w']),
                        ('_rfsh',   self.netlist['_rfsh_w']),
                        ('d0',      self.netlist['data0_w']),
                        ('d1',      self.netlist['data1_w']),
                        ('d2',      self.netlist['data2_w']),
                        ('d3',      self.netlist['data3_w']),
                        ('d4',      self.netlist['data4_w']),
                        ('d5',      self.netlist['data5_w']),
                        ('d6',      self.netlist['data6_w']),
                        ('d7',      self.netlist['data7_w']),
                        ('_halt',   self.netlist['_halt_w']), 
                        ('_busak',  self.netlist['_busak_w']),
                        ('vss',     self.netlist['vss']),
                        ('vcc',     self.netlist['vcc']),
                        ])) ]
                          


        vector_string = '''
PI _reset_w

PI clk_w

PI data7_w
PI data6_w
PI data5_w
PI data4_w
PI data3_w
PI data2_w
PI data1_w
PI data0_w

PI _wait_w
PI _int_w
PI _nmi_w
PI _busrq_w

'''
        vectors = []
        opcode = '00000000'
        reset = '0'
        for i in range (0, 4096):
            for clockseq in ['0','1']:
                vectors.append( " %s %s %s 1111" % (reset, clockseq, opcode))
            if i > 10:
                reset = '1'
        vector_string += '\n'.join(vectors)


        self.events  = self.read_flex_string( vector_string)

