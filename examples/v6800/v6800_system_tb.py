import gate
import net
from testbench import testbench
from primitive import INV, NAND, OR
from v6800 import v6800
from rom32k import rom32k
from ram32k import ram32k

class v6800_system_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)


        self.netlist.update( gate.wire(['data%d_w' %i for i in range(0,8)]))
        self.netlist.update( gate.wire(['addr%02d_w' %i for i in range(0,16)]))
        self.netlist.update( gate.wire([ 'rstb_w', 'rnw_w', 'tsc_w', 'haltb_w', 'vma_w', 'phi1_w', 'phi2_w',  'phi2b_w', 'ba_w', 'nmib_w', 'irqb_w', 'not_addr15_w']))
        self.netlist.update( gate.wire([ "web_w"]))

        self.netlist['vcc'] = net.supply1('vcc')
        self.netlist['vss'] = net.supply0('vss')
        self.netlist['vdd'] = net.supply1('vdd')

        self.gatelist = [ v6800( "v6800_0_u", dict([\
                        ('reset', self.netlist['rstb_w']),
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
                        ('phi1',self.netlist['phi1_w']),
                        ('phi2',self.netlist['phi2_w']),
                        ('irq', self.netlist['irqb_w']),
                        ('nmi', self.netlist['nmib_w']),
                        ('halt',  self.netlist['haltb_w']),
                        ('tsc',self.netlist['tsc_w']), 
                        ('ba', self.netlist['ba_w']),
                        ('vma', self.netlist['vma_w']),
                        ('dbe', self.netlist['phi2_w']),
                        ('gnd', self.netlist['vss']),
                        ('vcc', self.netlist['vcc']),
                        ])) ]
                          
        self.gatelist.append( rom32k( "rom32k_0_u", dict([\
                        ('oeb', self.netlist['phi2b_w']),
                        ('csb', self.netlist['not_addr15_w']),
                        ('adr00', self.netlist['addr00_w']),
                        ('adr01', self.netlist['addr01_w']),
                        ('adr02', self.netlist['addr02_w']),
                        ('adr03', self.netlist['addr03_w']),
                        ('adr04', self.netlist['addr04_w']),
                        ('adr05', self.netlist['addr05_w']),
                        ('adr06', self.netlist['addr06_w']),
                        ('adr07', self.netlist['addr07_w']),
                        ('adr08', self.netlist['addr08_w']),
                        ('adr09', self.netlist['addr09_w']),
                        ('adr10', self.netlist['addr10_w']),
                        ('adr11', self.netlist['addr11_w']),
                        ('adr12', self.netlist['addr12_w']),
                        ('adr13', self.netlist['addr13_w']),
                        ('adr14', self.netlist['addr14_w']),
                        ('data0', self.netlist['data0_w']),
                        ('data1', self.netlist['data1_w']),
                        ('data2', self.netlist['data2_w']),
                        ('data3', self.netlist['data3_w']),
                        ('data4', self.netlist['data4_w']),
                        ('data5', self.netlist['data5_w']),
                        ('data6', self.netlist['data6_w']),
                        ('data7', self.netlist['data7_w']),]), \
                                          adr_lo=0x8000,\
                                          filename=self.options["rom_filename"]\
                                          ))

        self.gatelist.append( ram32k( "ram32k_0_u", dict([\
                        ('oeb', self.netlist['phi2b_w']),
                        ('csb', self.netlist['addr15_w']),
                        ('web', self.netlist['web_w']),
                        ('adr00', self.netlist['addr00_w']),
                        ('adr01', self.netlist['addr01_w']),
                        ('adr02', self.netlist['addr02_w']),
                        ('adr03', self.netlist['addr03_w']),
                        ('adr04', self.netlist['addr04_w']),
                        ('adr05', self.netlist['addr05_w']),
                        ('adr06', self.netlist['addr06_w']),
                        ('adr07', self.netlist['addr07_w']),
                        ('adr08', self.netlist['addr08_w']),
                        ('adr09', self.netlist['addr09_w']),
                        ('adr10', self.netlist['addr10_w']),
                        ('adr11', self.netlist['addr11_w']),
                        ('adr12', self.netlist['addr12_w']),
                        ('adr13', self.netlist['addr13_w']),
                        ('adr14', self.netlist['addr14_w']),
                        ('data0', self.netlist['data0_w']),
                        ('data1', self.netlist['data1_w']),
                        ('data2', self.netlist['data2_w']),
                        ('data3', self.netlist['data3_w']),
                        ('data4', self.netlist['data4_w']),
                        ('data5', self.netlist['data5_w']),
                        ('data6', self.netlist['data6_w']),
                        ('data7', self.netlist['data7_w'])]),\
                                          adr_lo=0x0000,))

        self.gatelist.append( INV( "inv_0_u", [self.netlist['not_addr15_w'], self.netlist['addr15_w']]))
        # NB - for 6800 phi2b != phi1 ! Clocks have to be non-overlapping
        self.gatelist.append( INV( "inv_1_u", [self.netlist['phi2b_w'], self.netlist['phi2_w']]))
        self.gatelist.append( OR( "or_0_u", [self.netlist['web_w'], self.netlist['rnw_w'], self.netlist['phi2b_w']]))
        

        vector_string = '''
PI rstb_w

PI phi1_w
PI phi2_w

PI tsc_w
PI nmib_w
PI irqb_w
PI haltb_w

'''
        vectors = []
        reset = '0'
        for i in range (0, 8192):
            for clockseq in [ '00', '10', '00', '01']:
                vectors.append( " %s %s 0111" % (reset, clockseq))
            if i > 3:
                reset = '1'
        vector_string += '\n'.join(vectors)


        self.events  = self.read_flex_string( vector_string)

