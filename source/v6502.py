
import gate
import net
from primitive import NMOS

class v6502( gate.module ):
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict([
            ('res', gate.IN),
            ('rw', gate.OUT),
            ('db0', gate.INOUT),
            ('db1', gate.INOUT),
            ('db3', gate.INOUT),
            ('db2', gate.INOUT),
            ('db4', gate.INOUT),
            ('db5', gate.INOUT),
            ('db6', gate.INOUT),
            ('db7', gate.INOUT),
            ('ab0', gate.OUT),
            ('ab1', gate.OUT),
            ('ab2', gate.OUT),
            ('ab3', gate.OUT),
            ('ab4', gate.OUT),
            ('ab5', gate.OUT),
            ('ab6', gate.OUT),
            ('ab7', gate.OUT),
            ('ab8', gate.OUT),
            ('ab9', gate.OUT),
            ('ab12', gate.OUT),
            ('ab13', gate.OUT),
            ('ab10', gate.OUT),
            ('ab11', gate.OUT),
            ('ab14', gate.OUT),
            ('ab15', gate.OUT),
            ('sync', gate.OUT),
            ('so', gate.IN),
            ('clk0', gate.IN),
            ('clk1out', gate.OUT),
            ('clk2out', gate.OUT),
            ('rdy', gate.IN),
            ('nmi', gate.IN),
            ('irq', gate.IN),
            ('vcc', gate.IN),
            ('vss', gate.IN),

        ])
        gate.module.__init__( self, name, portlist, mapping, parent)

        ## Net Declarations
        self.netlist['AxB1'] = net.net('AxB1', pullup_str=100,   parent=self)
        self.netlist['AxB3'] = net.net('AxB3', pullup_str=100,   parent=self)
        self.netlist['AxB5'] = net.net('AxB5', pullup_str=100,   parent=self)
        self.netlist['AxB7'] = net.net('AxB7', pullup_str=100,   parent=self)
        self.netlist['BRtaken'] = net.net('BRtaken', pullup_str=100,   parent=self)
        self.netlist['C01'] = net.net('C01', pullup_str=100,   parent=self)
        self.netlist['C12'] = net.net('C12', pullup_str=100,   parent=self)
        self.netlist['C23'] = net.net('C23', pullup_str=100,   parent=self)
        self.netlist['C34'] = net.net('C34', pullup_str=100,   parent=self)
        self.netlist['C45'] = net.net('C45', pullup_str=100,   parent=self)
        self.netlist['C56'] = net.net('C56', pullup_str=100,   parent=self)
        self.netlist['C67'] = net.net('C67', pullup_str=100,   parent=self)
        self.netlist['D1x1'] = net.net('D1x1', pullup_str=100,   parent=self)
        self.netlist['DBNeg'] = net.net('DBNeg', pullup_str=100,   parent=self)
        self.netlist['DBZ'] = net.net('DBZ', pullup_str=100,   parent=self)
        self.netlist['DC34'] = net.net('DC34', pullup_str=100,   parent=self)
        self.netlist['DC78'] = net.net('DC78', pullup_str=100,   parent=self)
        self.netlist['H1x1'] = net.net('H1x1', pullup_str=100,   parent=self)
        self.netlist['INTG'] = net.net('INTG', pullup_str=100,   parent=self)
        self.netlist['IRQP'] = net.net('IRQP',  charge_storage=True,  parent=self)
        self.netlist['NMIL'] = net.net('NMIL', pullup_str=100,   parent=self)
        self.netlist['NMIP'] = net.net('NMIP', pullup_str=100,   parent=self)
        self.netlist['Pout0'] = net.net('Pout0', pullup_str=100,   parent=self)
        self.netlist['Pout1'] = net.net('Pout1', pullup_str=100,   parent=self)
        self.netlist['Pout2'] = net.net('Pout2', pullup_str=100,   parent=self)
        self.netlist['Pout3'] = net.net('Pout3', pullup_str=100,   parent=self)
        self.netlist['Pout4'] = net.net('Pout4', pullup_str=100,   parent=self)
        self.netlist['Pout6'] = net.net('Pout6', pullup_str=100,   parent=self)
        self.netlist['Pout7'] = net.net('Pout7', pullup_str=100,   parent=self)
        self.netlist['RESG'] = net.net('RESG', pullup_str=100,   parent=self)
        self.netlist['RESP'] = net.net('RESP', pullup_str=100,   parent=self)
        self.netlist['RnWstretched'] = net.net('RnWstretched',  charge_storage=True,  parent=self)
        self.netlist['VEC0'] = net.net('VEC0', pullup_str=100,   parent=self)
        self.netlist['VEC1'] = net.net('VEC1', pullup_str=100,   parent=self)
        self.netlist['a0'] = net.net('a0',  charge_storage=True,  parent=self)
        self.netlist['a1'] = net.net('a1',  charge_storage=True,  parent=self)
        self.netlist['a2'] = net.net('a2',  charge_storage=True,  parent=self)
        self.netlist['a3'] = net.net('a3',  charge_storage=True,  parent=self)
        self.netlist['a4'] = net.net('a4',  charge_storage=True,  parent=self)
        self.netlist['a5'] = net.net('a5',  charge_storage=True,  parent=self)
        self.netlist['a6'] = net.net('a6',  charge_storage=True,  parent=self)
        self.netlist['a7'] = net.net('a7',  charge_storage=True,  parent=self)
        self.port['ab0'].netconn.charge_storage=True
        self.port['ab1'].netconn.charge_storage=True
        self.port['ab10'].netconn.charge_storage=True
        self.port['ab11'].netconn.charge_storage=True
        self.port['ab12'].netconn.charge_storage=True
        self.port['ab13'].netconn.charge_storage=True
        self.port['ab14'].netconn.charge_storage=True
        self.port['ab15'].netconn.charge_storage=True
        self.port['ab2'].netconn.charge_storage=True
        self.port['ab3'].netconn.charge_storage=True
        self.port['ab4'].netconn.charge_storage=True
        self.port['ab5'].netconn.charge_storage=True
        self.port['ab6'].netconn.charge_storage=True
        self.port['ab7'].netconn.charge_storage=True
        self.port['ab8'].netconn.charge_storage=True
        self.port['ab9'].netconn.charge_storage=True
        self.netlist['abh0'] = net.net('abh0', pullup_str=100,   parent=self)
        self.netlist['abh1'] = net.net('abh1', pullup_str=100,   parent=self)
        self.netlist['abh2'] = net.net('abh2', pullup_str=100,   parent=self)
        self.netlist['abh3'] = net.net('abh3', pullup_str=100,   parent=self)
        self.netlist['abh4'] = net.net('abh4', pullup_str=100,   parent=self)
        self.netlist['abh5'] = net.net('abh5', pullup_str=100,   parent=self)
        self.netlist['abh6'] = net.net('abh6', pullup_str=100,   parent=self)
        self.netlist['abh7'] = net.net('abh7', pullup_str=100,   parent=self)
        self.netlist['abl0'] = net.net('abl0', pullup_str=100,   parent=self)
        self.netlist['abl1'] = net.net('abl1', pullup_str=100,   parent=self)
        self.netlist['abl2'] = net.net('abl2', pullup_str=100,   parent=self)
        self.netlist['abl3'] = net.net('abl3', pullup_str=100,   parent=self)
        self.netlist['abl4'] = net.net('abl4', pullup_str=100,   parent=self)
        self.netlist['abl5'] = net.net('abl5', pullup_str=100,   parent=self)
        self.netlist['abl6'] = net.net('abl6', pullup_str=100,   parent=self)
        self.netlist['abl7'] = net.net('abl7', pullup_str=100,   parent=self)
        self.netlist['adh0'] = net.net('adh0',  charge_storage=True,  parent=self)
        self.netlist['adh1'] = net.net('adh1',  charge_storage=True,  parent=self)
        self.netlist['adh2'] = net.net('adh2',  charge_storage=True,  parent=self)
        self.netlist['adh3'] = net.net('adh3',  charge_storage=True,  parent=self)
        self.netlist['adh4'] = net.net('adh4',  charge_storage=True,  parent=self)
        self.netlist['adh5'] = net.net('adh5',  charge_storage=True,  parent=self)
        self.netlist['adh6'] = net.net('adh6',  charge_storage=True,  parent=self)
        self.netlist['adh7'] = net.net('adh7',  charge_storage=True,  parent=self)
        self.netlist['adl0'] = net.net('adl0',  charge_storage=True,  parent=self)
        self.netlist['adl1'] = net.net('adl1',  charge_storage=True,  parent=self)
        self.netlist['adl2'] = net.net('adl2',  charge_storage=True,  parent=self)
        self.netlist['adl3'] = net.net('adl3',  charge_storage=True,  parent=self)
        self.netlist['adl4'] = net.net('adl4',  charge_storage=True,  parent=self)
        self.netlist['adl5'] = net.net('adl5',  charge_storage=True,  parent=self)
        self.netlist['adl6'] = net.net('adl6',  charge_storage=True,  parent=self)
        self.netlist['adl7'] = net.net('adl7',  charge_storage=True,  parent=self)
        self.netlist['alu0'] = net.net('alu0', pullup_str=100,   parent=self)
        self.netlist['alu1'] = net.net('alu1', pullup_str=100,   parent=self)
        self.netlist['alu2'] = net.net('alu2', pullup_str=100,   parent=self)
        self.netlist['alu3'] = net.net('alu3', pullup_str=100,   parent=self)
        self.netlist['alu4'] = net.net('alu4', pullup_str=100,   parent=self)
        self.netlist['alu5'] = net.net('alu5', pullup_str=100,   parent=self)
        self.netlist['alu6'] = net.net('alu6', pullup_str=100,   parent=self)
        self.netlist['alu7'] = net.net('alu7', pullup_str=100,   parent=self)
        self.netlist['alua0'] = net.net('alua0',  charge_storage=True,  parent=self)
        self.netlist['alua1'] = net.net('alua1',  charge_storage=True,  parent=self)
        self.netlist['alua2'] = net.net('alua2',  charge_storage=True,  parent=self)
        self.netlist['alua3'] = net.net('alua3',  charge_storage=True,  parent=self)
        self.netlist['alua4'] = net.net('alua4',  charge_storage=True,  parent=self)
        self.netlist['alua5'] = net.net('alua5',  charge_storage=True,  parent=self)
        self.netlist['alua6'] = net.net('alua6',  charge_storage=True,  parent=self)
        self.netlist['alua7'] = net.net('alua7',  charge_storage=True,  parent=self)
        self.netlist['alub0'] = net.net('alub0',  charge_storage=True,  parent=self)
        self.netlist['alub1'] = net.net('alub1',  charge_storage=True,  parent=self)
        self.netlist['alub2'] = net.net('alub2',  charge_storage=True,  parent=self)
        self.netlist['alub3'] = net.net('alub3',  charge_storage=True,  parent=self)
        self.netlist['alub4'] = net.net('alub4',  charge_storage=True,  parent=self)
        self.netlist['alub5'] = net.net('alub5',  charge_storage=True,  parent=self)
        self.netlist['alub6'] = net.net('alub6',  charge_storage=True,  parent=self)
        self.netlist['alub7'] = net.net('alub7',  charge_storage=True,  parent=self)
        self.netlist['alucin'] = net.net('alucin', pullup_str=100,   parent=self)
        self.netlist['alucout'] = net.net('alucout', pullup_str=100,   parent=self)
        self.netlist['alurawcout'] = net.net('alurawcout', pullup_str=100,   parent=self)
        self.netlist['aluvout'] = net.net('aluvout', pullup_str=100,   parent=self)
        self.netlist['cclk'] = net.net('cclk',  charge_storage=True,  parent=self)
        self.netlist['clearIR'] = net.net('clearIR', pullup_str=100,   parent=self)
        self.port['clk0'].netconn.charge_storage=True
        self.port['clk1out'].netconn.charge_storage=True
        self.port['clk2out'].netconn.charge_storage=True
        self.netlist['clock1'] = net.net('clock1',  charge_storage=True,  parent=self)
        self.netlist['clock2'] = net.net('clock2', pullup_str=100,   parent=self)
        self.netlist['cp1'] = net.net('cp1',  charge_storage=True,  parent=self)
        self.netlist['dasb0'] = net.net('dasb0',  charge_storage=True,  parent=self)
        self.netlist['dasb1'] = net.net('dasb1', pullup_str=100,   parent=self)
        self.netlist['dasb2'] = net.net('dasb2', pullup_str=100,   parent=self)
        self.netlist['dasb3'] = net.net('dasb3', pullup_str=100,   parent=self)
        self.netlist['dasb4'] = net.net('dasb4',  charge_storage=True,  parent=self)
        self.netlist['dasb5'] = net.net('dasb5', pullup_str=100,   parent=self)
        self.netlist['dasb6'] = net.net('dasb6', pullup_str=100,   parent=self)
        self.netlist['dasb7'] = net.net('dasb7', pullup_str=100,   parent=self)
        self.port['db0'].netconn.charge_storage=True
        self.port['db1'].netconn.charge_storage=True
        self.port['db2'].netconn.charge_storage=True
        self.port['db3'].netconn.charge_storage=True
        self.port['db4'].netconn.charge_storage=True
        self.port['db5'].netconn.charge_storage=True
        self.port['db6'].netconn.charge_storage=True
        self.port['db7'].netconn.charge_storage=True
        self.netlist['dor0'] = net.net('dor0', pullup_str=100,   parent=self)
        self.netlist['dor1'] = net.net('dor1', pullup_str=100,   parent=self)
        self.netlist['dor2'] = net.net('dor2', pullup_str=100,   parent=self)
        self.netlist['dor3'] = net.net('dor3', pullup_str=100,   parent=self)
        self.netlist['dor4'] = net.net('dor4', pullup_str=100,   parent=self)
        self.netlist['dor5'] = net.net('dor5', pullup_str=100,   parent=self)
        self.netlist['dor6'] = net.net('dor6', pullup_str=100,   parent=self)
        self.netlist['dor7'] = net.net('dor7', pullup_str=100,   parent=self)
        self.netlist['dpc0_YSB'] = net.net('dpc0_YSB',  charge_storage=True,  parent=self)
        self.netlist['dpc10_ADLADD'] = net.net('dpc10_ADLADD',  charge_storage=True,  parent=self)
        self.netlist['dpc11_SBADD'] = net.net('dpc11_SBADD',  charge_storage=True,  parent=self)
        self.netlist['dpc12_0ADD'] = net.net('dpc12_0ADD',  charge_storage=True,  parent=self)
        self.netlist['dpc13_ORS'] = net.net('dpc13_ORS',  charge_storage=True,  parent=self)
        self.netlist['dpc14_SRS'] = net.net('dpc14_SRS',  charge_storage=True,  parent=self)
        self.netlist['dpc15_ANDS'] = net.net('dpc15_ANDS',  charge_storage=True,  parent=self)
        self.netlist['dpc16_EORS'] = net.net('dpc16_EORS',  charge_storage=True,  parent=self)
        self.netlist['dpc17_SUMS'] = net.net('dpc17_SUMS',  charge_storage=True,  parent=self)
        self.netlist['dpc19_ADDSB7'] = net.net('dpc19_ADDSB7',  charge_storage=True,  parent=self)
        self.netlist['dpc1_SBY'] = net.net('dpc1_SBY',  charge_storage=True,  parent=self)
        self.netlist['dpc20_ADDSB06'] = net.net('dpc20_ADDSB06',  charge_storage=True,  parent=self)
        self.netlist['dpc21_ADDADL'] = net.net('dpc21_ADDADL',  charge_storage=True,  parent=self)
        self.netlist['dpc23_SBAC'] = net.net('dpc23_SBAC',  charge_storage=True,  parent=self)
        self.netlist['dpc24_ACSB'] = net.net('dpc24_ACSB',  charge_storage=True,  parent=self)
        self.netlist['dpc25_SBDB'] = net.net('dpc25_SBDB',  charge_storage=True,  parent=self)
        self.netlist['dpc26_ACDB'] = net.net('dpc26_ACDB',  charge_storage=True,  parent=self)
        self.netlist['dpc27_SBADH'] = net.net('dpc27_SBADH',  charge_storage=True,  parent=self)
        self.netlist['dpc28_0ADH0'] = net.net('dpc28_0ADH0', pullup_str=100,   parent=self)
        self.netlist['dpc29_0ADH17'] = net.net('dpc29_0ADH17',  charge_storage=True,  parent=self)
        self.netlist['dpc2_XSB'] = net.net('dpc2_XSB',  charge_storage=True,  parent=self)
        self.netlist['dpc30_ADHPCH'] = net.net('dpc30_ADHPCH',  charge_storage=True,  parent=self)
        self.netlist['dpc31_PCHPCH'] = net.net('dpc31_PCHPCH',  charge_storage=True,  parent=self)
        self.netlist['dpc32_PCHADH'] = net.net('dpc32_PCHADH',  charge_storage=True,  parent=self)
        self.netlist['dpc33_PCHDB'] = net.net('dpc33_PCHDB',  charge_storage=True,  parent=self)
        self.netlist['dpc34_PCLC'] = net.net('dpc34_PCLC', pullup_str=100,   parent=self)
        self.netlist['dpc35_PCHC'] = net.net('dpc35_PCHC', pullup_str=100,   parent=self)
        self.netlist['dpc37_PCLDB'] = net.net('dpc37_PCLDB',  charge_storage=True,  parent=self)
        self.netlist['dpc38_PCLADL'] = net.net('dpc38_PCLADL',  charge_storage=True,  parent=self)
        self.netlist['dpc39_PCLPCL'] = net.net('dpc39_PCLPCL',  charge_storage=True,  parent=self)
        self.netlist['dpc3_SBX'] = net.net('dpc3_SBX',  charge_storage=True,  parent=self)
        self.netlist['dpc40_ADLPCL'] = net.net('dpc40_ADLPCL',  charge_storage=True,  parent=self)
        self.netlist['dpc4_SSB'] = net.net('dpc4_SSB',  charge_storage=True,  parent=self)
        self.netlist['dpc5_SADL'] = net.net('dpc5_SADL',  charge_storage=True,  parent=self)
        self.netlist['dpc6_SBS'] = net.net('dpc6_SBS',  charge_storage=True,  parent=self)
        self.netlist['dpc7_SS'] = net.net('dpc7_SS',  charge_storage=True,  parent=self)
        self.netlist['dpc8_nDBADD'] = net.net('dpc8_nDBADD',  charge_storage=True,  parent=self)
        self.netlist['dpc9_DBADD'] = net.net('dpc9_DBADD',  charge_storage=True,  parent=self)
        self.netlist['fetch'] = net.net('fetch', pullup_str=100,   parent=self)
        self.netlist['idb0'] = net.net('idb0',  charge_storage=True,  parent=self)
        self.netlist['idb1'] = net.net('idb1',  charge_storage=True,  parent=self)
        self.netlist['idb2'] = net.net('idb2',  charge_storage=True,  parent=self)
        self.netlist['idb3'] = net.net('idb3',  charge_storage=True,  parent=self)
        self.netlist['idb4'] = net.net('idb4',  charge_storage=True,  parent=self)
        self.netlist['idb5'] = net.net('idb5',  charge_storage=True,  parent=self)
        self.netlist['idb6'] = net.net('idb6',  charge_storage=True,  parent=self)
        self.netlist['idb7'] = net.net('idb7',  charge_storage=True,  parent=self)
        self.netlist['idl0'] = net.net('idl0', pullup_str=100,   parent=self)
        self.netlist['idl1'] = net.net('idl1', pullup_str=100,   parent=self)
        self.netlist['idl2'] = net.net('idl2', pullup_str=100,   parent=self)
        self.netlist['idl3'] = net.net('idl3', pullup_str=100,   parent=self)
        self.netlist['idl4'] = net.net('idl4', pullup_str=100,   parent=self)
        self.netlist['idl5'] = net.net('idl5', pullup_str=100,   parent=self)
        self.netlist['idl6'] = net.net('idl6', pullup_str=100,   parent=self)
        self.netlist['idl7'] = net.net('idl7', pullup_str=100,   parent=self)
        self.netlist['ir0'] = net.net('ir0', pullup_str=100,   parent=self)
        self.netlist['ir1'] = net.net('ir1', pullup_str=100,   parent=self)
        self.netlist['ir2'] = net.net('ir2', pullup_str=100,   parent=self)
        self.netlist['ir3'] = net.net('ir3', pullup_str=100,   parent=self)
        self.netlist['ir4'] = net.net('ir4', pullup_str=100,   parent=self)
        self.netlist['ir5'] = net.net('ir5', pullup_str=100,   parent=self)
        self.netlist['ir6'] = net.net('ir6', pullup_str=100,   parent=self)
        self.netlist['ir7'] = net.net('ir7', pullup_str=100,   parent=self)
        self.netlist['irline3'] = net.net('irline3', pullup_str=100,   parent=self)
        self.port['irq'].netconn.charge_storage=True
        self.netlist['n0'] = net.net('n0', pullup_str=100,   parent=self)
        self.netlist['n10'] = net.net('n10', pullup_str=100,   parent=self)
        self.netlist['n100'] = net.net('n100',  charge_storage=True,  parent=self)
        self.netlist['n1000'] = net.net('n1000',  charge_storage=True,  parent=self)
        self.netlist['n1002'] = net.net('n1002', pullup_str=100,   parent=self)
        self.netlist['n1003'] = net.net('n1003', pullup_str=100,   parent=self)
        self.netlist['n1004'] = net.net('n1004',  charge_storage=True,  parent=self)
        self.netlist['n1006'] = net.net('n1006', pullup_str=100,   parent=self)
        self.netlist['n1007'] = net.net('n1007', pullup_str=100,   parent=self)
        self.netlist['n101'] = net.net('n101',  charge_storage=True,  parent=self)
        self.netlist['n1010'] = net.net('n1010', pullup_str=100,   parent=self)
        self.netlist['n1012'] = net.net('n1012',  charge_storage=True,  parent=self)
        self.netlist['n1013'] = net.net('n1013',  charge_storage=True,  parent=self)
        self.netlist['n1014'] = net.net('n1014',  charge_storage=True,  parent=self)
        self.netlist['n1016'] = net.net('n1016', pullup_str=100,   parent=self)
        self.netlist['n1018'] = net.net('n1018', pullup_str=100,   parent=self)
        self.netlist['n1019'] = net.net('n1019', pullup_str=100,   parent=self)
        self.netlist['n102'] = net.net('n102',  charge_storage=True,  parent=self)
        self.netlist['n1020'] = net.net('n1020',  charge_storage=True,  parent=self)
        self.netlist['n1021'] = net.net('n1021', pullup_str=100,   parent=self)
        self.netlist['n1024'] = net.net('n1024', pullup_str=100,   parent=self)
        self.netlist['n1026'] = net.net('n1026', pullup_str=100,   parent=self)
        self.netlist['n1027'] = net.net('n1027',  charge_storage=True,  parent=self)
        self.netlist['n1028'] = net.net('n1028', pullup_str=100,   parent=self)
        self.netlist['n1030'] = net.net('n1030',  charge_storage=True,  parent=self)
        self.netlist['n1031'] = net.net('n1031', pullup_str=100,   parent=self)
        self.netlist['n1033'] = net.net('n1033', pullup_str=100,   parent=self)
        self.netlist['n1034'] = net.net('n1034', pullup_str=100,   parent=self)
        self.netlist['n1035'] = net.net('n1035', pullup_str=100,   parent=self)
        self.netlist['n1037'] = net.net('n1037', pullup_str=100,   parent=self)
        self.netlist['n1038'] = net.net('n1038', pullup_str=100,   parent=self)
        self.netlist['n1039'] = net.net('n1039', pullup_str=100,   parent=self)
        self.netlist['n104'] = net.net('n104', pullup_str=100,   parent=self)
        self.netlist['n1040'] = net.net('n1040',  charge_storage=True,  parent=self)
        self.netlist['n1041'] = net.net('n1041',  charge_storage=True,  parent=self)
        self.netlist['n1043'] = net.net('n1043', pullup_str=100,   parent=self)
        self.netlist['n1044'] = net.net('n1044', pullup_str=100,   parent=self)
        self.netlist['n1045'] = net.net('n1045', pullup_str=100,   parent=self)
        self.netlist['n1046'] = net.net('n1046', pullup_str=100,   parent=self)
        self.netlist['n1047'] = net.net('n1047', pullup_str=100,   parent=self)
        self.netlist['n1048'] = net.net('n1048', pullup_str=100,   parent=self)
        self.netlist['n1049'] = net.net('n1049',  charge_storage=True,  parent=self)
        self.netlist['n105'] = net.net('n105', pullup_str=100,   parent=self)
        self.netlist['n1050'] = net.net('n1050', pullup_str=100,   parent=self)
        self.netlist['n1052'] = net.net('n1052', pullup_str=100,   parent=self)
        self.netlist['n1053'] = net.net('n1053',  charge_storage=True,  parent=self)
        self.netlist['n1054'] = net.net('n1054', pullup_str=100,   parent=self)
        self.netlist['n1055'] = net.net('n1055', pullup_str=100,   parent=self)
        self.netlist['n1056'] = net.net('n1056', pullup_str=100,   parent=self)
        self.netlist['n1057'] = net.net('n1057', pullup_str=100,   parent=self)
        self.netlist['n1058'] = net.net('n1058',  charge_storage=True,  parent=self)
        self.netlist['n1059'] = net.net('n1059',  charge_storage=True,  parent=self)
        self.netlist['n106'] = net.net('n106',  charge_storage=True,  parent=self)
        self.netlist['n1061'] = net.net('n1061',  charge_storage=True,  parent=self)
        self.netlist['n1062'] = net.net('n1062',  charge_storage=True,  parent=self)
        self.netlist['n1063'] = net.net('n1063', pullup_str=100,   parent=self)
        self.netlist['n1065'] = net.net('n1065', pullup_str=100,   parent=self)
        self.netlist['n1067'] = net.net('n1067', pullup_str=100,   parent=self)
        self.netlist['n1069'] = net.net('n1069', pullup_str=100,   parent=self)
        self.netlist['n107'] = net.net('n107',  charge_storage=True,  parent=self)
        self.netlist['n1070'] = net.net('n1070', pullup_str=100,   parent=self)
        self.netlist['n1071'] = net.net('n1071',  charge_storage=True,  parent=self)
        self.netlist['n1072'] = net.net('n1072',  charge_storage=True,  parent=self)
        self.netlist['n1073'] = net.net('n1073', pullup_str=100,   parent=self)
        self.netlist['n1074'] = net.net('n1074', pullup_str=100,   parent=self)
        self.netlist['n1075'] = net.net('n1075', pullup_str=100,   parent=self)
        self.netlist['n1076'] = net.net('n1076',  charge_storage=True,  parent=self)
        self.netlist['n1079'] = net.net('n1079', pullup_str=100,   parent=self)
        self.netlist['n108'] = net.net('n108', pullup_str=100,   parent=self)
        self.netlist['n1080'] = net.net('n1080',  charge_storage=True,  parent=self)
        self.netlist['n1081'] = net.net('n1081', pullup_str=100,   parent=self)
        self.netlist['n1082'] = net.net('n1082', pullup_str=100,   parent=self)
        self.netlist['n1083'] = net.net('n1083', pullup_str=100,   parent=self)
        self.netlist['n1084'] = net.net('n1084', pullup_str=100,   parent=self)
        self.netlist['n1085'] = net.net('n1085', pullup_str=100,   parent=self)
        self.netlist['n1086'] = net.net('n1086', pullup_str=100,   parent=self)
        self.netlist['n1087'] = net.net('n1087', pullup_str=100,   parent=self)
        self.netlist['n1089'] = net.net('n1089', pullup_str=100,   parent=self)
        self.netlist['n109'] = net.net('n109', pullup_str=100,   parent=self)
        self.netlist['n1090'] = net.net('n1090', pullup_str=100,   parent=self)
        self.netlist['n1091'] = net.net('n1091', pullup_str=100,   parent=self)
        self.netlist['n1092'] = net.net('n1092',  charge_storage=True,  parent=self)
        self.netlist['n1093'] = net.net('n1093', pullup_str=100,   parent=self)
        self.netlist['n1094'] = net.net('n1094', pullup_str=100,   parent=self)
        self.netlist['n1095'] = net.net('n1095',  charge_storage=True,  parent=self)
        self.netlist['n1097'] = net.net('n1097', pullup_str=100,   parent=self)
        self.netlist['n1099'] = net.net('n1099', pullup_str=100,   parent=self)
        self.netlist['n11'] = net.net('n11', pullup_str=100,   parent=self)
        self.netlist['n110'] = net.net('n110', pullup_str=100,   parent=self)
        self.netlist['n1100'] = net.net('n1100',  charge_storage=True,  parent=self)
        self.netlist['n1101'] = net.net('n1101', pullup_str=100,   parent=self)
        self.netlist['n1102'] = net.net('n1102',  charge_storage=True,  parent=self)
        self.netlist['n1103'] = net.net('n1103',  charge_storage=True,  parent=self)
        self.netlist['n1105'] = net.net('n1105',  charge_storage=True,  parent=self)
        self.netlist['n1106'] = net.net('n1106', pullup_str=100,   parent=self)
        self.netlist['n1107'] = net.net('n1107', pullup_str=100,   parent=self)
        self.netlist['n1109'] = net.net('n1109', pullup_str=100,   parent=self)
        self.netlist['n111'] = net.net('n111', pullup_str=100,   parent=self)
        self.netlist['n1110'] = net.net('n1110', pullup_str=100,   parent=self)
        self.netlist['n1111'] = net.net('n1111', pullup_str=100,   parent=self)
        self.netlist['n1113'] = net.net('n1113',  charge_storage=True,  parent=self)
        self.netlist['n1114'] = net.net('n1114', pullup_str=100,   parent=self)
        self.netlist['n1115'] = net.net('n1115', pullup_str=100,   parent=self)
        self.netlist['n1117'] = net.net('n1117', pullup_str=100,   parent=self)
        self.netlist['n1118'] = net.net('n1118',  charge_storage=True,  parent=self)
        self.netlist['n112'] = net.net('n112',  charge_storage=True,  parent=self)
        self.netlist['n1120'] = net.net('n1120', pullup_str=100,   parent=self)
        self.netlist['n1121'] = net.net('n1121',  charge_storage=True,  parent=self)
        self.netlist['n1122'] = net.net('n1122', pullup_str=100,   parent=self)
        self.netlist['n1124'] = net.net('n1124',  charge_storage=True,  parent=self)
        self.netlist['n1126'] = net.net('n1126',  charge_storage=True,  parent=self)
        self.netlist['n1128'] = net.net('n1128',  charge_storage=True,  parent=self)
        self.netlist['n1129'] = net.net('n1129', pullup_str=100,   parent=self)
        self.netlist['n113'] = net.net('n113', pullup_str=100,   parent=self)
        self.netlist['n1130'] = net.net('n1130', pullup_str=100,   parent=self)
        self.netlist['n1131'] = net.net('n1131',  charge_storage=True,  parent=self)
        self.netlist['n1132'] = net.net('n1132',  charge_storage=True,  parent=self)
        self.netlist['n1133'] = net.net('n1133', pullup_str=100,   parent=self)
        self.netlist['n1134'] = net.net('n1134', pullup_str=100,   parent=self)
        self.netlist['n1135'] = net.net('n1135', pullup_str=100,   parent=self)
        self.netlist['n1137'] = net.net('n1137', pullup_str=100,   parent=self)
        self.netlist['n114'] = net.net('n114',  charge_storage=True,  parent=self)
        self.netlist['n1140'] = net.net('n1140',  charge_storage=True,  parent=self)
        self.netlist['n1141'] = net.net('n1141', pullup_str=100,   parent=self)
        self.netlist['n1144'] = net.net('n1144', pullup_str=100,   parent=self)
        self.netlist['n1145'] = net.net('n1145', pullup_str=100,   parent=self)
        self.netlist['n1147'] = net.net('n1147',  charge_storage=True,  parent=self)
        self.netlist['n1149'] = net.net('n1149',  charge_storage=True,  parent=self)
        self.netlist['n1151'] = net.net('n1151',  charge_storage=True,  parent=self)
        self.netlist['n1152'] = net.net('n1152',  charge_storage=True,  parent=self)
        self.netlist['n1153'] = net.net('n1153', pullup_str=100,   parent=self)
        self.netlist['n1154'] = net.net('n1154', pullup_str=100,   parent=self)
        self.netlist['n1155'] = net.net('n1155', pullup_str=100,   parent=self)
        self.netlist['n1157'] = net.net('n1157', pullup_str=100,   parent=self)
        self.netlist['n1158'] = net.net('n1158',  charge_storage=True,  parent=self)
        self.netlist['n1159'] = net.net('n1159', pullup_str=100,   parent=self)
        self.netlist['n1161'] = net.net('n1161',  charge_storage=True,  parent=self)
        self.netlist['n1162'] = net.net('n1162',  charge_storage=True,  parent=self)
        self.netlist['n1164'] = net.net('n1164', pullup_str=100,   parent=self)
        self.netlist['n1166'] = net.net('n1166', pullup_str=100,   parent=self)
        self.netlist['n1168'] = net.net('n1168', pullup_str=100,   parent=self)
        self.netlist['n1169'] = net.net('n1169', pullup_str=100,   parent=self)
        self.netlist['n117'] = net.net('n117', pullup_str=100,   parent=self)
        self.netlist['n1170'] = net.net('n1170', pullup_str=100,   parent=self)
        self.netlist['n1172'] = net.net('n1172',  charge_storage=True,  parent=self)
        self.netlist['n1173'] = net.net('n1173', pullup_str=100,   parent=self)
        self.netlist['n1174'] = net.net('n1174', pullup_str=100,   parent=self)
        self.netlist['n1175'] = net.net('n1175', pullup_str=100,   parent=self)
        self.netlist['n1177'] = net.net('n1177',  charge_storage=True,  parent=self)
        self.netlist['n1178'] = net.net('n1178', pullup_str=100,   parent=self)
        self.netlist['n1179'] = net.net('n1179', pullup_str=100,   parent=self)
        self.netlist['n118'] = net.net('n118', pullup_str=100,   parent=self)
        self.netlist['n1180'] = net.net('n1180', pullup_str=100,   parent=self)
        self.netlist['n1181'] = net.net('n1181', pullup_str=100,   parent=self)
        self.netlist['n1183'] = net.net('n1183',  charge_storage=True,  parent=self)
        self.netlist['n1184'] = net.net('n1184', pullup_str=100,   parent=self)
        self.netlist['n1185'] = net.net('n1185', pullup_str=100,   parent=self)
        self.netlist['n1187'] = net.net('n1187', pullup_str=100,   parent=self)
        self.netlist['n1189'] = net.net('n1189',  charge_storage=True,  parent=self)
        self.netlist['n119'] = net.net('n119',  charge_storage=True,  parent=self)
        self.netlist['n1190'] = net.net('n1190', pullup_str=100,   parent=self)
        self.netlist['n1191'] = net.net('n1191',  charge_storage=True,  parent=self)
        self.netlist['n1192'] = net.net('n1192', pullup_str=100,   parent=self)
        self.netlist['n1193'] = net.net('n1193', pullup_str=100,   parent=self)
        self.netlist['n1194'] = net.net('n1194', pullup_str=100,   parent=self)
        self.netlist['n1195'] = net.net('n1195', pullup_str=100,   parent=self)
        self.netlist['n1196'] = net.net('n1196', pullup_str=100,   parent=self)
        self.netlist['n1197'] = net.net('n1197', pullup_str=100,   parent=self)
        self.netlist['n1198'] = net.net('n1198',  charge_storage=True,  parent=self)
        self.netlist['n1199'] = net.net('n1199', pullup_str=100,   parent=self)
        self.netlist['n12'] = net.net('n12',  charge_storage=True,  parent=self)
        self.netlist['n120'] = net.net('n120', pullup_str=100,   parent=self)
        self.netlist['n1201'] = net.net('n1201',  charge_storage=True,  parent=self)
        self.netlist['n1202'] = net.net('n1202', pullup_str=100,   parent=self)
        self.netlist['n1203'] = net.net('n1203',  charge_storage=True,  parent=self)
        self.netlist['n1204'] = net.net('n1204', pullup_str=100,   parent=self)
        self.netlist['n1205'] = net.net('n1205', pullup_str=100,   parent=self)
        self.netlist['n1209'] = net.net('n1209', pullup_str=100,   parent=self)
        self.netlist['n1210'] = net.net('n1210', pullup_str=100,   parent=self)
        self.netlist['n1211'] = net.net('n1211', pullup_str=100,   parent=self)
        self.netlist['n1213'] = net.net('n1213', pullup_str=100,   parent=self)
        self.netlist['n1214'] = net.net('n1214', pullup_str=100,   parent=self)
        self.netlist['n1215'] = net.net('n1215', pullup_str=100,   parent=self)
        self.netlist['n1217'] = net.net('n1217', pullup_str=100,   parent=self)
        self.netlist['n1218'] = net.net('n1218', pullup_str=100,   parent=self)
        self.netlist['n1219'] = net.net('n1219', pullup_str=100,   parent=self)
        self.netlist['n122'] = net.net('n122', pullup_str=100,   parent=self)
        self.netlist['n1221'] = net.net('n1221',  charge_storage=True,  parent=self)
        self.netlist['n1222'] = net.net('n1222', pullup_str=100,   parent=self)
        self.netlist['n1223'] = net.net('n1223', pullup_str=100,   parent=self)
        self.netlist['n1224'] = net.net('n1224', pullup_str=100,   parent=self)
        self.netlist['n1225'] = net.net('n1225', pullup_str=100,   parent=self)
        self.netlist['n1226'] = net.net('n1226', pullup_str=100,   parent=self)
        self.netlist['n1227'] = net.net('n1227', pullup_str=100,   parent=self)
        self.netlist['n1228'] = net.net('n1228', pullup_str=100,   parent=self)
        self.netlist['n1229'] = net.net('n1229', pullup_str=100,   parent=self)
        self.netlist['n123'] = net.net('n123', pullup_str=100,   parent=self)
        self.netlist['n1230'] = net.net('n1230', pullup_str=100,   parent=self)
        self.netlist['n1231'] = net.net('n1231', pullup_str=100,   parent=self)
        self.netlist['n1233'] = net.net('n1233', pullup_str=100,   parent=self)
        self.netlist['n1236'] = net.net('n1236', pullup_str=100,   parent=self)
        self.netlist['n1238'] = net.net('n1238', pullup_str=100,   parent=self)
        self.netlist['n1239'] = net.net('n1239', pullup_str=100,   parent=self)
        self.netlist['n124'] = net.net('n124', pullup_str=100,   parent=self)
        self.netlist['n1240'] = net.net('n1240', pullup_str=100,   parent=self)
        self.netlist['n1243'] = net.net('n1243', pullup_str=100,   parent=self)
        self.netlist['n1244'] = net.net('n1244', pullup_str=100,   parent=self)
        self.netlist['n1245'] = net.net('n1245', pullup_str=100,   parent=self)
        self.netlist['n1246'] = net.net('n1246', pullup_str=100,   parent=self)
        self.netlist['n1247'] = net.net('n1247',  charge_storage=True,  parent=self)
        self.netlist['n1249'] = net.net('n1249',  charge_storage=True,  parent=self)
        self.netlist['n125'] = net.net('n125', pullup_str=100,   parent=self)
        self.netlist['n1251'] = net.net('n1251', pullup_str=100,   parent=self)
        self.netlist['n1252'] = net.net('n1252',  charge_storage=True,  parent=self)
        self.netlist['n1253'] = net.net('n1253', pullup_str=100,   parent=self)
        self.netlist['n1254'] = net.net('n1254',  charge_storage=True,  parent=self)
        self.netlist['n1255'] = net.net('n1255', pullup_str=100,   parent=self)
        self.netlist['n1256'] = net.net('n1256', pullup_str=100,   parent=self)
        self.netlist['n1257'] = net.net('n1257', pullup_str=100,   parent=self)
        self.netlist['n1258'] = net.net('n1258', pullup_str=100,   parent=self)
        self.netlist['n1259'] = net.net('n1259', pullup_str=100,   parent=self)
        self.netlist['n126'] = net.net('n126',  charge_storage=True,  parent=self)
        self.netlist['n1260'] = net.net('n1260', pullup_str=100,   parent=self)
        self.netlist['n1262'] = net.net('n1262', pullup_str=100,   parent=self)
        self.netlist['n1264'] = net.net('n1264',  charge_storage=True,  parent=self)
        self.netlist['n1265'] = net.net('n1265', pullup_str=100,   parent=self)
        self.netlist['n1267'] = net.net('n1267', pullup_str=100,   parent=self)
        self.netlist['n1268'] = net.net('n1268', pullup_str=100,   parent=self)
        self.netlist['n1269'] = net.net('n1269',  charge_storage=True,  parent=self)
        self.netlist['n127'] = net.net('n127', pullup_str=100,   parent=self)
        self.netlist['n1270'] = net.net('n1270', pullup_str=100,   parent=self)
        self.netlist['n1271'] = net.net('n1271', pullup_str=100,   parent=self)
        self.netlist['n1272'] = net.net('n1272',  charge_storage=True,  parent=self)
        self.netlist['n1273'] = net.net('n1273', pullup_str=100,   parent=self)
        self.netlist['n1274'] = net.net('n1274',  charge_storage=True,  parent=self)
        self.netlist['n1275'] = net.net('n1275', pullup_str=100,   parent=self)
        self.netlist['n1276'] = net.net('n1276',  charge_storage=True,  parent=self)
        self.netlist['n1277'] = net.net('n1277', pullup_str=100,   parent=self)
        self.netlist['n1278'] = net.net('n1278',  charge_storage=True,  parent=self)
        self.netlist['n1279'] = net.net('n1279',  charge_storage=True,  parent=self)
        self.netlist['n128'] = net.net('n128', pullup_str=100,   parent=self)
        self.netlist['n1280'] = net.net('n1280',  charge_storage=True,  parent=self)
        self.netlist['n1281'] = net.net('n1281', pullup_str=100,   parent=self)
        self.netlist['n1286'] = net.net('n1286', pullup_str=100,   parent=self)
        self.netlist['n1289'] = net.net('n1289', pullup_str=100,   parent=self)
        self.netlist['n1290'] = net.net('n1290', pullup_str=100,   parent=self)
        self.netlist['n1291'] = net.net('n1291',  charge_storage=True,  parent=self)
        self.netlist['n1292'] = net.net('n1292', pullup_str=100,   parent=self)
        self.netlist['n1293'] = net.net('n1293', pullup_str=100,   parent=self)
        self.netlist['n1294'] = net.net('n1294', pullup_str=100,   parent=self)
        self.netlist['n1295'] = net.net('n1295', pullup_str=100,   parent=self)
        self.netlist['n1296'] = net.net('n1296',  charge_storage=True,  parent=self)
        self.netlist['n1298'] = net.net('n1298',  charge_storage=True,  parent=self)
        self.netlist['n130'] = net.net('n130', pullup_str=100,   parent=self)
        self.netlist['n1300'] = net.net('n1300',  charge_storage=True,  parent=self)
        self.netlist['n1303'] = net.net('n1303', pullup_str=100,   parent=self)
        self.netlist['n1304'] = net.net('n1304', pullup_str=100,   parent=self)
        self.netlist['n1305'] = net.net('n1305', pullup_str=100,   parent=self)
        self.netlist['n1307'] = net.net('n1307',  charge_storage=True,  parent=self)
        self.netlist['n1309'] = net.net('n1309', pullup_str=100,   parent=self)
        self.netlist['n131'] = net.net('n131', pullup_str=100,   parent=self)
        self.netlist['n1310'] = net.net('n1310',  charge_storage=True,  parent=self)
        self.netlist['n1311'] = net.net('n1311', pullup_str=100,   parent=self)
        self.netlist['n1312'] = net.net('n1312', pullup_str=100,   parent=self)
        self.netlist['n1313'] = net.net('n1313', pullup_str=100,   parent=self)
        self.netlist['n1315'] = net.net('n1315', pullup_str=100,   parent=self)
        self.netlist['n1316'] = net.net('n1316', pullup_str=100,   parent=self)
        self.netlist['n1318'] = net.net('n1318', pullup_str=100,   parent=self)
        self.netlist['n1319'] = net.net('n1319', pullup_str=100,   parent=self)
        self.netlist['n132'] = net.net('n132', pullup_str=100,   parent=self)
        self.netlist['n1322'] = net.net('n1322',  charge_storage=True,  parent=self)
        self.netlist['n1323'] = net.net('n1323', pullup_str=100,   parent=self)
        self.netlist['n1324'] = net.net('n1324', pullup_str=100,   parent=self)
        self.netlist['n1325'] = net.net('n1325',  charge_storage=True,  parent=self)
        self.netlist['n1326'] = net.net('n1326',  charge_storage=True,  parent=self)
        self.netlist['n1327'] = net.net('n1327', pullup_str=100,   parent=self)
        self.netlist['n133'] = net.net('n133', pullup_str=100,   parent=self)
        self.netlist['n1330'] = net.net('n1330',  charge_storage=True,  parent=self)
        self.netlist['n1333'] = net.net('n1333',  charge_storage=True,  parent=self)
        self.netlist['n1335'] = net.net('n1335', pullup_str=100,   parent=self)
        self.netlist['n1337'] = net.net('n1337', pullup_str=100,   parent=self)
        self.netlist['n1338'] = net.net('n1338',  charge_storage=True,  parent=self)
        self.netlist['n1339'] = net.net('n1339', pullup_str=100,   parent=self)
        self.netlist['n134'] = net.net('n134', pullup_str=100,   parent=self)
        self.netlist['n1341'] = net.net('n1341',  charge_storage=True,  parent=self)
        self.netlist['n1342'] = net.net('n1342', pullup_str=100,   parent=self)
        self.netlist['n1343'] = net.net('n1343', pullup_str=100,   parent=self)
        self.netlist['n1344'] = net.net('n1344', pullup_str=100,   parent=self)
        self.netlist['n1345'] = net.net('n1345', pullup_str=100,   parent=self)
        self.netlist['n1346'] = net.net('n1346', pullup_str=100,   parent=self)
        self.netlist['n1347'] = net.net('n1347', pullup_str=100,   parent=self)
        self.netlist['n1348'] = net.net('n1348',  charge_storage=True,  parent=self)
        self.netlist['n135'] = net.net('n135',  charge_storage=True,  parent=self)
        self.netlist['n1351'] = net.net('n1351',  charge_storage=True,  parent=self)
        self.netlist['n1352'] = net.net('n1352', pullup_str=100,   parent=self)
        self.netlist['n1353'] = net.net('n1353',  charge_storage=True,  parent=self)
        self.netlist['n1354'] = net.net('n1354',  charge_storage=True,  parent=self)
        self.netlist['n1355'] = net.net('n1355', pullup_str=100,   parent=self)
        self.netlist['n1356'] = net.net('n1356', pullup_str=100,   parent=self)
        self.netlist['n1357'] = net.net('n1357', pullup_str=100,   parent=self)
        self.netlist['n1358'] = net.net('n1358', pullup_str=100,   parent=self)
        self.netlist['n136'] = net.net('n136',  charge_storage=True,  parent=self)
        self.netlist['n1360'] = net.net('n1360',  charge_storage=True,  parent=self)
        self.netlist['n1362'] = net.net('n1362',  charge_storage=True,  parent=self)
        self.netlist['n1364'] = net.net('n1364', pullup_str=100,   parent=self)
        self.netlist['n1365'] = net.net('n1365',  charge_storage=True,  parent=self)
        self.netlist['n1366'] = net.net('n1366',  charge_storage=True,  parent=self)
        self.netlist['n1367'] = net.net('n1367',  charge_storage=True,  parent=self)
        self.netlist['n1368'] = net.net('n1368', pullup_str=100,   parent=self)
        self.netlist['n1369'] = net.net('n1369', pullup_str=100,   parent=self)
        self.netlist['n137'] = net.net('n137',  charge_storage=True,  parent=self)
        self.netlist['n1371'] = net.net('n1371', pullup_str=100,   parent=self)
        self.netlist['n1375'] = net.net('n1375', pullup_str=100,   parent=self)
        self.netlist['n1376'] = net.net('n1376', pullup_str=100,   parent=self)
        self.netlist['n1377'] = net.net('n1377', pullup_str=100,   parent=self)
        self.netlist['n1378'] = net.net('n1378',  charge_storage=True,  parent=self)
        self.netlist['n1379'] = net.net('n1379', pullup_str=100,   parent=self)
        self.netlist['n138'] = net.net('n138',  charge_storage=True,  parent=self)
        self.netlist['n1380'] = net.net('n1380', pullup_str=100,   parent=self)
        self.netlist['n1381'] = net.net('n1381', pullup_str=100,   parent=self)
        self.netlist['n1382'] = net.net('n1382', pullup_str=100,   parent=self)
        self.netlist['n1383'] = net.net('n1383', pullup_str=100,   parent=self)
        self.netlist['n1385'] = net.net('n1385', pullup_str=100,   parent=self)
        self.netlist['n1386'] = net.net('n1386', pullup_str=100,   parent=self)
        self.netlist['n1387'] = net.net('n1387',  charge_storage=True,  parent=self)
        self.netlist['n1388'] = net.net('n1388',  charge_storage=True,  parent=self)
        self.netlist['n1389'] = net.net('n1389', pullup_str=100,   parent=self)
        self.netlist['n139'] = net.net('n139', pullup_str=100,   parent=self)
        self.netlist['n1390'] = net.net('n1390',  charge_storage=True,  parent=self)
        self.netlist['n1391'] = net.net('n1391', pullup_str=100,   parent=self)
        self.netlist['n1392'] = net.net('n1392', pullup_str=100,   parent=self)
        self.netlist['n1395'] = net.net('n1395',  charge_storage=True,  parent=self)
        self.netlist['n1396'] = net.net('n1396', pullup_str=100,   parent=self)
        self.netlist['n1397'] = net.net('n1397',  charge_storage=True,  parent=self)
        self.netlist['n1398'] = net.net('n1398', pullup_str=100,   parent=self)
        self.netlist['n1399'] = net.net('n1399', pullup_str=100,   parent=self)
        self.netlist['n14'] = net.net('n14', pullup_str=100,   parent=self)
        self.netlist['n1400'] = net.net('n1400', pullup_str=100,   parent=self)
        self.netlist['n1401'] = net.net('n1401', pullup_str=100,   parent=self)
        self.netlist['n1402'] = net.net('n1402', pullup_str=100,   parent=self)
        self.netlist['n1404'] = net.net('n1404',  charge_storage=True,  parent=self)
        self.netlist['n1406'] = net.net('n1406',  charge_storage=True,  parent=self)
        self.netlist['n1407'] = net.net('n1407',  charge_storage=True,  parent=self)
        self.netlist['n1408'] = net.net('n1408', pullup_str=100,   parent=self)
        self.netlist['n1409'] = net.net('n1409',  charge_storage=True,  parent=self)
        self.netlist['n1410'] = net.net('n1410', pullup_str=100,   parent=self)
        self.netlist['n1411'] = net.net('n1411',  charge_storage=True,  parent=self)
        self.netlist['n1412'] = net.net('n1412', pullup_str=100,   parent=self)
        self.netlist['n1413'] = net.net('n1413', pullup_str=100,   parent=self)
        self.netlist['n1416'] = net.net('n1416', pullup_str=100,   parent=self)
        self.netlist['n1417'] = net.net('n1417',  charge_storage=True,  parent=self)
        self.netlist['n1419'] = net.net('n1419', pullup_str=100,   parent=self)
        self.netlist['n1420'] = net.net('n1420', pullup_str=100,   parent=self)
        self.netlist['n1422'] = net.net('n1422',  charge_storage=True,  parent=self)
        self.netlist['n1423'] = net.net('n1423', pullup_str=100,   parent=self)
        self.netlist['n1424'] = net.net('n1424',  charge_storage=True,  parent=self)
        self.netlist['n1425'] = net.net('n1425', pullup_str=100,   parent=self)
        self.netlist['n1426'] = net.net('n1426',  charge_storage=True,  parent=self)
        self.netlist['n1427'] = net.net('n1427', pullup_str=100,   parent=self)
        self.netlist['n1428'] = net.net('n1428', pullup_str=100,   parent=self)
        self.netlist['n143'] = net.net('n143', pullup_str=100,   parent=self)
        self.netlist['n1430'] = net.net('n1430', pullup_str=100,   parent=self)
        self.netlist['n1431'] = net.net('n1431',  charge_storage=True,  parent=self)
        self.netlist['n1433'] = net.net('n1433', pullup_str=100,   parent=self)
        self.netlist['n1440'] = net.net('n1440', pullup_str=100,   parent=self)
        self.netlist['n1441'] = net.net('n1441', pullup_str=100,   parent=self)
        self.netlist['n1445'] = net.net('n1445',  charge_storage=True,  parent=self)
        self.netlist['n1446'] = net.net('n1446', pullup_str=100,   parent=self)
        self.netlist['n1447'] = net.net('n1447',  charge_storage=True,  parent=self)
        self.netlist['n1448'] = net.net('n1448', pullup_str=100,   parent=self)
        self.netlist['n1449'] = net.net('n1449', pullup_str=100,   parent=self)
        self.netlist['n145'] = net.net('n145', pullup_str=100,   parent=self)
        self.netlist['n1450'] = net.net('n1450',  charge_storage=True,  parent=self)
        self.netlist['n1451'] = net.net('n1451',  charge_storage=True,  parent=self)
        self.netlist['n1452'] = net.net('n1452',  charge_storage=True,  parent=self)
        self.netlist['n1454'] = net.net('n1454',  charge_storage=True,  parent=self)
        self.netlist['n1455'] = net.net('n1455', pullup_str=100,   parent=self)
        self.netlist['n1456'] = net.net('n1456',  charge_storage=True,  parent=self)
        self.netlist['n1457'] = net.net('n1457', pullup_str=100,   parent=self)
        self.netlist['n1459'] = net.net('n1459', pullup_str=100,   parent=self)
        self.netlist['n146'] = net.net('n146', pullup_str=100,   parent=self)
        self.netlist['n1460'] = net.net('n1460', pullup_str=100,   parent=self)
        self.netlist['n1462'] = net.net('n1462', pullup_str=100,   parent=self)
        self.netlist['n1463'] = net.net('n1463', pullup_str=100,   parent=self)
        self.netlist['n1464'] = net.net('n1464', pullup_str=100,   parent=self)
        self.netlist['n1466'] = net.net('n1466', pullup_str=100,   parent=self)
        self.netlist['n1467'] = net.net('n1467',  charge_storage=True,  parent=self)
        self.netlist['n1469'] = net.net('n1469', pullup_str=100,   parent=self)
        self.netlist['n147'] = net.net('n147',  charge_storage=True,  parent=self)
        self.netlist['n1470'] = net.net('n1470',  charge_storage=True,  parent=self)
        self.netlist['n1471'] = net.net('n1471', pullup_str=100,   parent=self)
        self.netlist['n1472'] = net.net('n1472',  charge_storage=True,  parent=self)
        self.netlist['n1474'] = net.net('n1474', pullup_str=100,   parent=self)
        self.netlist['n1476'] = net.net('n1476', pullup_str=100,   parent=self)
        self.netlist['n1477'] = net.net('n1477',  charge_storage=True,  parent=self)
        self.netlist['n1478'] = net.net('n1478', pullup_str=100,   parent=self)
        self.netlist['n1479'] = net.net('n1479',  charge_storage=True,  parent=self)
        self.netlist['n1480'] = net.net('n1480',  charge_storage=True,  parent=self)
        self.netlist['n1482'] = net.net('n1482', pullup_str=100,   parent=self)
        self.netlist['n1483'] = net.net('n1483',  charge_storage=True,  parent=self)
        self.netlist['n1486'] = net.net('n1486', pullup_str=100,   parent=self)
        self.netlist['n1487'] = net.net('n1487', pullup_str=100,   parent=self)
        self.netlist['n1488'] = net.net('n1488', pullup_str=100,   parent=self)
        self.netlist['n1489'] = net.net('n1489',  charge_storage=True,  parent=self)
        self.netlist['n149'] = net.net('n149', pullup_str=100,   parent=self)
        self.netlist['n1491'] = net.net('n1491', pullup_str=100,   parent=self)
        self.netlist['n1492'] = net.net('n1492', pullup_str=100,   parent=self)
        self.netlist['n1495'] = net.net('n1495', pullup_str=100,   parent=self)
        self.netlist['n1497'] = net.net('n1497', pullup_str=100,   parent=self)
        self.netlist['n1498'] = net.net('n1498',  charge_storage=True,  parent=self)
        self.netlist['n1499'] = net.net('n1499', pullup_str=100,   parent=self)
        self.netlist['n15'] = net.net('n15',  charge_storage=True,  parent=self)
        self.netlist['n150'] = net.net('n150',  charge_storage=True,  parent=self)
        self.netlist['n1500'] = net.net('n1500', pullup_str=100,   parent=self)
        self.netlist['n1501'] = net.net('n1501',  charge_storage=True,  parent=self)
        self.netlist['n1504'] = net.net('n1504', pullup_str=100,   parent=self)
        self.netlist['n1505'] = net.net('n1505',  charge_storage=True,  parent=self)
        self.netlist['n1506'] = net.net('n1506', pullup_str=100,   parent=self)
        self.netlist['n1507'] = net.net('n1507', pullup_str=100,   parent=self)
        self.netlist['n1508'] = net.net('n1508',  charge_storage=True,  parent=self)
        self.netlist['n1509'] = net.net('n1509',  charge_storage=True,  parent=self)
        self.netlist['n1510'] = net.net('n1510',  charge_storage=True,  parent=self)
        self.netlist['n1511'] = net.net('n1511', pullup_str=100,   parent=self)
        self.netlist['n1512'] = net.net('n1512', pullup_str=100,   parent=self)
        self.netlist['n1513'] = net.net('n1513',  charge_storage=True,  parent=self)
        self.netlist['n1514'] = net.net('n1514',  charge_storage=True,  parent=self)
        self.netlist['n1515'] = net.net('n1515',  charge_storage=True,  parent=self)
        self.netlist['n1517'] = net.net('n1517', pullup_str=100,   parent=self)
        self.netlist['n1518'] = net.net('n1518', pullup_str=100,   parent=self)
        self.netlist['n1519'] = net.net('n1519', pullup_str=100,   parent=self)
        self.netlist['n152'] = net.net('n152', pullup_str=100,   parent=self)
        self.netlist['n1520'] = net.net('n1520', pullup_str=100,   parent=self)
        self.netlist['n1523'] = net.net('n1523', pullup_str=100,   parent=self)
        self.netlist['n1524'] = net.net('n1524', pullup_str=100,   parent=self)
        self.netlist['n1525'] = net.net('n1525', pullup_str=100,   parent=self)
        self.netlist['n1526'] = net.net('n1526', pullup_str=100,   parent=self)
        self.netlist['n1527'] = net.net('n1527',  charge_storage=True,  parent=self)
        self.netlist['n1528'] = net.net('n1528',  charge_storage=True,  parent=self)
        self.netlist['n1529'] = net.net('n1529',  charge_storage=True,  parent=self)
        self.netlist['n153'] = net.net('n153',  charge_storage=True,  parent=self)
        self.netlist['n1531'] = net.net('n1531', pullup_str=100,   parent=self)
        self.netlist['n1533'] = net.net('n1533',  charge_storage=True,  parent=self)
        self.netlist['n1534'] = net.net('n1534', pullup_str=100,   parent=self)
        self.netlist['n1538'] = net.net('n1538',  charge_storage=True,  parent=self)
        self.netlist['n154'] = net.net('n154', pullup_str=100,   parent=self)
        self.netlist['n1540'] = net.net('n1540', pullup_str=100,   parent=self)
        self.netlist['n1541'] = net.net('n1541', pullup_str=100,   parent=self)
        self.netlist['n1542'] = net.net('n1542', pullup_str=100,   parent=self)
        self.netlist['n1543'] = net.net('n1543', pullup_str=100,   parent=self)
        self.netlist['n1545'] = net.net('n1545',  charge_storage=True,  parent=self)
        self.netlist['n1546'] = net.net('n1546',  charge_storage=True,  parent=self)
        self.netlist['n1547'] = net.net('n1547',  charge_storage=True,  parent=self)
        self.netlist['n1548'] = net.net('n1548', pullup_str=100,   parent=self)
        self.netlist['n1549'] = net.net('n1549', pullup_str=100,   parent=self)
        self.netlist['n155'] = net.net('n155', pullup_str=100,   parent=self)
        self.netlist['n1550'] = net.net('n1550',  charge_storage=True,  parent=self)
        self.netlist['n1552'] = net.net('n1552', pullup_str=100,   parent=self)
        self.netlist['n1554'] = net.net('n1554',  charge_storage=True,  parent=self)
        self.netlist['n1555'] = net.net('n1555',  charge_storage=True,  parent=self)
        self.netlist['n1556'] = net.net('n1556',  charge_storage=True,  parent=self)
        self.netlist['n1557'] = net.net('n1557', pullup_str=100,   parent=self)
        self.netlist['n1558'] = net.net('n1558',  charge_storage=True,  parent=self)
        self.netlist['n1559'] = net.net('n1559',  charge_storage=True,  parent=self)
        self.netlist['n1560'] = net.net('n1560', pullup_str=100,   parent=self)
        self.netlist['n1562'] = net.net('n1562', pullup_str=100,   parent=self)
        self.netlist['n1563'] = net.net('n1563',  charge_storage=True,  parent=self)
        self.netlist['n1564'] = net.net('n1564',  charge_storage=True,  parent=self)
        self.netlist['n1565'] = net.net('n1565',  charge_storage=True,  parent=self)
        self.netlist['n1566'] = net.net('n1566', pullup_str=100,   parent=self)
        self.netlist['n1568'] = net.net('n1568',  charge_storage=True,  parent=self)
        self.netlist['n1569'] = net.net('n1569', pullup_str=100,   parent=self)
        self.netlist['n157'] = net.net('n157', pullup_str=100,   parent=self)
        self.netlist['n1570'] = net.net('n1570',  charge_storage=True,  parent=self)
        self.netlist['n1571'] = net.net('n1571', pullup_str=100,   parent=self)
        self.netlist['n1572'] = net.net('n1572',  charge_storage=True,  parent=self)
        self.netlist['n1573'] = net.net('n1573', pullup_str=100,   parent=self)
        self.netlist['n1574'] = net.net('n1574',  charge_storage=True,  parent=self)
        self.netlist['n1575'] = net.net('n1575', pullup_str=100,   parent=self)
        self.netlist['n1578'] = net.net('n1578', pullup_str=100,   parent=self)
        self.netlist['n1579'] = net.net('n1579',  charge_storage=True,  parent=self)
        self.netlist['n1580'] = net.net('n1580', pullup_str=100,   parent=self)
        self.netlist['n1581'] = net.net('n1581',  charge_storage=True,  parent=self)
        self.netlist['n1582'] = net.net('n1582', pullup_str=100,   parent=self)
        self.netlist['n1583'] = net.net('n1583',  charge_storage=True,  parent=self)
        self.netlist['n1584'] = net.net('n1584',  charge_storage=True,  parent=self)
        self.netlist['n1585'] = net.net('n1585', pullup_str=100,   parent=self)
        self.netlist['n1586'] = net.net('n1586', pullup_str=100,   parent=self)
        self.netlist['n1587'] = net.net('n1587', pullup_str=100,   parent=self)
        self.netlist['n1588'] = net.net('n1588', pullup_str=100,   parent=self)
        self.netlist['n1589'] = net.net('n1589', pullup_str=100,   parent=self)
        self.netlist['n1590'] = net.net('n1590',  charge_storage=True,  parent=self)
        self.netlist['n1592'] = net.net('n1592', pullup_str=100,   parent=self)
        self.netlist['n1593'] = net.net('n1593', pullup_str=100,   parent=self)
        self.netlist['n1594'] = net.net('n1594', pullup_str=100,   parent=self)
        self.netlist['n1595'] = net.net('n1595', pullup_str=100,   parent=self)
        self.netlist['n1596'] = net.net('n1596', pullup_str=100,   parent=self)
        self.netlist['n1598'] = net.net('n1598',  charge_storage=True,  parent=self)
        self.netlist['n1599'] = net.net('n1599', pullup_str=100,   parent=self)
        self.netlist['n16'] = net.net('n16', pullup_str=100,   parent=self)
        self.netlist['n160'] = net.net('n160', pullup_str=100,   parent=self)
        self.netlist['n1600'] = net.net('n1600', pullup_str=100,   parent=self)
        self.netlist['n1601'] = net.net('n1601', pullup_str=100,   parent=self)
        self.netlist['n1602'] = net.net('n1602',  charge_storage=True,  parent=self)
        self.netlist['n1604'] = net.net('n1604',  charge_storage=True,  parent=self)
        self.netlist['n1605'] = net.net('n1605', pullup_str=100,   parent=self)
        self.netlist['n1606'] = net.net('n1606',  charge_storage=True,  parent=self)
        self.netlist['n1608'] = net.net('n1608',  charge_storage=True,  parent=self)
        self.netlist['n1609'] = net.net('n1609',  charge_storage=True,  parent=self)
        self.netlist['n161'] = net.net('n161', pullup_str=100,   parent=self)
        self.netlist['n1610'] = net.net('n1610', pullup_str=100,   parent=self)
        self.netlist['n1612'] = net.net('n1612', pullup_str=100,   parent=self)
        self.netlist['n1613'] = net.net('n1613', pullup_str=100,   parent=self)
        self.netlist['n1614'] = net.net('n1614', pullup_str=100,   parent=self)
        self.netlist['n1615'] = net.net('n1615',  charge_storage=True,  parent=self)
        self.netlist['n1616'] = net.net('n1616',  charge_storage=True,  parent=self)
        self.netlist['n1617'] = net.net('n1617',  charge_storage=True,  parent=self)
        self.netlist['n1618'] = net.net('n1618', pullup_str=100,   parent=self)
        self.netlist['n1619'] = net.net('n1619', pullup_str=100,   parent=self)
        self.netlist['n1620'] = net.net('n1620',  charge_storage=True,  parent=self)
        self.netlist['n1621'] = net.net('n1621', pullup_str=100,   parent=self)
        self.netlist['n1622'] = net.net('n1622', pullup_str=100,   parent=self)
        self.netlist['n1623'] = net.net('n1623', pullup_str=100,   parent=self)
        self.netlist['n1624'] = net.net('n1624',  charge_storage=True,  parent=self)
        self.netlist['n1625'] = net.net('n1625',  charge_storage=True,  parent=self)
        self.netlist['n1628'] = net.net('n1628', pullup_str=100,   parent=self)
        self.netlist['n1629'] = net.net('n1629', pullup_str=100,   parent=self)
        self.netlist['n163'] = net.net('n163', pullup_str=100,   parent=self)
        self.netlist['n1631'] = net.net('n1631', pullup_str=100,   parent=self)
        self.netlist['n1632'] = net.net('n1632', pullup_str=100,   parent=self)
        self.netlist['n1633'] = net.net('n1633',  charge_storage=True,  parent=self)
        self.netlist['n1635'] = net.net('n1635', pullup_str=100,   parent=self)
        self.netlist['n1636'] = net.net('n1636',  charge_storage=True,  parent=self)
        self.netlist['n1638'] = net.net('n1638', pullup_str=100,   parent=self)
        self.netlist['n1639'] = net.net('n1639',  charge_storage=True,  parent=self)
        self.netlist['n164'] = net.net('n164',  charge_storage=True,  parent=self)
        self.netlist['n1641'] = net.net('n1641', pullup_str=100,   parent=self)
        self.netlist['n1642'] = net.net('n1642', pullup_str=100,   parent=self)
        self.netlist['n1643'] = net.net('n1643', pullup_str=100,   parent=self)
        self.netlist['n1644'] = net.net('n1644',  charge_storage=True,  parent=self)
        self.netlist['n1646'] = net.net('n1646', pullup_str=100,   parent=self)
        self.netlist['n1649'] = net.net('n1649', pullup_str=100,   parent=self)
        self.netlist['n165'] = net.net('n165',  charge_storage=True,  parent=self)
        self.netlist['n1650'] = net.net('n1650', pullup_str=100,   parent=self)
        self.netlist['n1654'] = net.net('n1654', pullup_str=100,   parent=self)
        self.netlist['n1655'] = net.net('n1655', pullup_str=100,   parent=self)
        self.netlist['n1656'] = net.net('n1656',  charge_storage=True,  parent=self)
        self.netlist['n1657'] = net.net('n1657', pullup_str=100,   parent=self)
        self.netlist['n1658'] = net.net('n1658', pullup_str=100,   parent=self)
        self.netlist['n1659'] = net.net('n1659',  charge_storage=True,  parent=self)
        self.netlist['n1660'] = net.net('n1660', pullup_str=100,   parent=self)
        self.netlist['n1661'] = net.net('n1661',  charge_storage=True,  parent=self)
        self.netlist['n1662'] = net.net('n1662', pullup_str=100,   parent=self)
        self.netlist['n1664'] = net.net('n1664', pullup_str=100,   parent=self)
        self.netlist['n1665'] = net.net('n1665', pullup_str=100,   parent=self)
        self.netlist['n1667'] = net.net('n1667',  charge_storage=True,  parent=self)
        self.netlist['n1668'] = net.net('n1668', pullup_str=100,   parent=self)
        self.netlist['n167'] = net.net('n167', pullup_str=100,   parent=self)
        self.netlist['n1671'] = net.net('n1671', pullup_str=100,   parent=self)
        self.netlist['n1673'] = net.net('n1673',  charge_storage=True,  parent=self)
        self.netlist['n1674'] = net.net('n1674',  charge_storage=True,  parent=self)
        self.netlist['n1675'] = net.net('n1675',  charge_storage=True,  parent=self)
        self.netlist['n1676'] = net.net('n1676', pullup_str=100,   parent=self)
        self.netlist['n1677'] = net.net('n1677', pullup_str=100,   parent=self)
        self.netlist['n1679'] = net.net('n1679',  charge_storage=True,  parent=self)
        self.netlist['n168'] = net.net('n168', pullup_str=100,   parent=self)
        self.netlist['n1681'] = net.net('n1681',  charge_storage=True,  parent=self)
        self.netlist['n1682'] = net.net('n1682', pullup_str=100,   parent=self)
        self.netlist['n1683'] = net.net('n1683',  charge_storage=True,  parent=self)
        self.netlist['n1684'] = net.net('n1684', pullup_str=100,   parent=self)
        self.netlist['n1685'] = net.net('n1685',  charge_storage=True,  parent=self)
        self.netlist['n1686'] = net.net('n1686',  charge_storage=True,  parent=self)
        self.netlist['n1687'] = net.net('n1687', pullup_str=100,   parent=self)
        self.netlist['n1688'] = net.net('n1688', pullup_str=100,   parent=self)
        self.netlist['n1689'] = net.net('n1689', pullup_str=100,   parent=self)
        self.netlist['n169'] = net.net('n169', pullup_str=100,   parent=self)
        self.netlist['n1691'] = net.net('n1691', pullup_str=100,   parent=self)
        self.netlist['n1692'] = net.net('n1692',  charge_storage=True,  parent=self)
        self.netlist['n1693'] = net.net('n1693',  charge_storage=True,  parent=self)
        self.netlist['n1694'] = net.net('n1694', pullup_str=100,   parent=self)
        self.netlist['n1695'] = net.net('n1695',  charge_storage=True,  parent=self)
        self.netlist['n1696'] = net.net('n1696',  charge_storage=True,  parent=self)
        self.netlist['n1697'] = net.net('n1697', pullup_str=100,   parent=self)
        self.netlist['n1699'] = net.net('n1699',  charge_storage=True,  parent=self)
        self.netlist['n17'] = net.net('n17', pullup_str=100,   parent=self)
        self.netlist['n1703'] = net.net('n1703',  charge_storage=True,  parent=self)
        self.netlist['n1705'] = net.net('n1705', pullup_str=100,   parent=self)
        self.netlist['n1706'] = net.net('n1706',  charge_storage=True,  parent=self)
        self.netlist['n1707'] = net.net('n1707',  charge_storage=True,  parent=self)
        self.netlist['n1708'] = net.net('n1708', pullup_str=100,   parent=self)
        self.netlist['n1709'] = net.net('n1709', pullup_str=100,   parent=self)
        self.netlist['n171'] = net.net('n171',  charge_storage=True,  parent=self)
        self.netlist['n1710'] = net.net('n1710', pullup_str=100,   parent=self)
        self.netlist['n1711'] = net.net('n1711', pullup_str=100,   parent=self)
        self.netlist['n1712'] = net.net('n1712', pullup_str=100,   parent=self)
        self.netlist['n1714'] = net.net('n1714', pullup_str=100,   parent=self)
        self.netlist['n1715'] = net.net('n1715', pullup_str=100,   parent=self)
        self.netlist['n1716'] = net.net('n1716', pullup_str=100,   parent=self)
        self.netlist['n1717'] = net.net('n1717', pullup_str=100,   parent=self)
        self.netlist['n1718'] = net.net('n1718', pullup_str=100,   parent=self)
        self.netlist['n1719'] = net.net('n1719', pullup_str=100,   parent=self)
        self.netlist['n172'] = net.net('n172', pullup_str=100,   parent=self)
        self.netlist['n1720'] = net.net('n1720', pullup_str=100,   parent=self)
        self.netlist['n1721'] = net.net('n1721', pullup_str=100,   parent=self)
        self.netlist['n1723'] = net.net('n1723',  charge_storage=True,  parent=self)
        self.netlist['n1724'] = net.net('n1724', pullup_str=100,   parent=self)
        self.netlist['n174'] = net.net('n174', pullup_str=100,   parent=self)
        self.netlist['n176'] = net.net('n176', pullup_str=100,   parent=self)
        self.netlist['n177'] = net.net('n177', pullup_str=100,   parent=self)
        self.netlist['n179'] = net.net('n179', pullup_str=100,   parent=self)
        self.netlist['n18'] = net.net('n18',  charge_storage=True,  parent=self)
        self.netlist['n180'] = net.net('n180', pullup_str=100,   parent=self)
        self.netlist['n182'] = net.net('n182', pullup_str=100,   parent=self)
        self.netlist['n185'] = net.net('n185',  charge_storage=True,  parent=self)
        self.netlist['n186'] = net.net('n186',  charge_storage=True,  parent=self)
        self.netlist['n188'] = net.net('n188', pullup_str=100,   parent=self)
        self.netlist['n189'] = net.net('n189',  charge_storage=True,  parent=self)
        self.netlist['n19'] = net.net('n19', pullup_str=100,   parent=self)
        self.netlist['n190'] = net.net('n190',  charge_storage=True,  parent=self)
        self.netlist['n191'] = net.net('n191', pullup_str=100,   parent=self)
        self.netlist['n192'] = net.net('n192', pullup_str=100,   parent=self)
        self.netlist['n193'] = net.net('n193', pullup_str=100,   parent=self)
        self.netlist['n196'] = net.net('n196', pullup_str=100,   parent=self)
        self.netlist['n198'] = net.net('n198', pullup_str=100,   parent=self)
        self.netlist['n2'] = net.net('n2',  charge_storage=True,  parent=self)
        self.netlist['n20'] = net.net('n20', pullup_str=100,   parent=self)
        self.netlist['n200'] = net.net('n200', pullup_str=100,   parent=self)
        self.netlist['n201'] = net.net('n201', pullup_str=100,   parent=self)
        self.netlist['n202'] = net.net('n202',  charge_storage=True,  parent=self)
        self.netlist['n204'] = net.net('n204', pullup_str=100,   parent=self)
        self.netlist['n206'] = net.net('n206', pullup_str=100,   parent=self)
        self.netlist['n207'] = net.net('n207', pullup_str=100,   parent=self)
        self.netlist['n21'] = net.net('n21', pullup_str=100,   parent=self)
        self.netlist['n210'] = net.net('n210',  charge_storage=True,  parent=self)
        self.netlist['n212'] = net.net('n212', pullup_str=100,   parent=self)
        self.netlist['n213'] = net.net('n213', pullup_str=100,   parent=self)
        self.netlist['n216'] = net.net('n216', pullup_str=100,   parent=self)
        self.netlist['n217'] = net.net('n217', pullup_str=100,   parent=self)
        self.netlist['n218'] = net.net('n218', pullup_str=100,   parent=self)
        self.netlist['n219'] = net.net('n219', pullup_str=100,   parent=self)
        self.netlist['n22'] = net.net('n22', pullup_str=100,   parent=self)
        self.netlist['n220'] = net.net('n220', pullup_str=100,   parent=self)
        self.netlist['n221'] = net.net('n221', pullup_str=100,   parent=self)
        self.netlist['n223'] = net.net('n223',  charge_storage=True,  parent=self)
        self.netlist['n224'] = net.net('n224', pullup_str=100,   parent=self)
        self.netlist['n225'] = net.net('n225', pullup_str=100,   parent=self)
        self.netlist['n226'] = net.net('n226',  charge_storage=True,  parent=self)
        self.netlist['n227'] = net.net('n227', pullup_str=100,   parent=self)
        self.netlist['n228'] = net.net('n228', pullup_str=100,   parent=self)
        self.netlist['n23'] = net.net('n23', pullup_str=100,   parent=self)
        self.netlist['n231'] = net.net('n231', pullup_str=100,   parent=self)
        self.netlist['n232'] = net.net('n232', pullup_str=100,   parent=self)
        self.netlist['n233'] = net.net('n233', pullup_str=100,   parent=self)
        self.netlist['n236'] = net.net('n236', pullup_str=100,   parent=self)
        self.netlist['n237'] = net.net('n237',  charge_storage=True,  parent=self)
        self.netlist['n238'] = net.net('n238', pullup_str=100,   parent=self)
        self.netlist['n239'] = net.net('n239',  charge_storage=True,  parent=self)
        self.netlist['n24'] = net.net('n24',  charge_storage=True,  parent=self)
        self.netlist['n241'] = net.net('n241', pullup_str=100,   parent=self)
        self.netlist['n242'] = net.net('n242', pullup_str=100,   parent=self)
        self.netlist['n243'] = net.net('n243', pullup_str=100,   parent=self)
        self.netlist['n244'] = net.net('n244', pullup_str=100,   parent=self)
        self.netlist['n245'] = net.net('n245', pullup_str=100,   parent=self)
        self.netlist['n246'] = net.net('n246',  charge_storage=True,  parent=self)
        self.netlist['n249'] = net.net('n249', pullup_str=100,   parent=self)
        self.netlist['n25'] = net.net('n25', pullup_str=100,   parent=self)
        self.netlist['n250'] = net.net('n250',  charge_storage=True,  parent=self)
        self.netlist['n251'] = net.net('n251', pullup_str=100,   parent=self)
        self.netlist['n252'] = net.net('n252', pullup_str=100,   parent=self)
        self.netlist['n253'] = net.net('n253', pullup_str=100,   parent=self)
        self.netlist['n254'] = net.net('n254', pullup_str=100,   parent=self)
        self.netlist['n255'] = net.net('n255', pullup_str=100,   parent=self)
        self.netlist['n256'] = net.net('n256', pullup_str=100,   parent=self)
        self.netlist['n257'] = net.net('n257', pullup_str=100,   parent=self)
        self.netlist['n258'] = net.net('n258', pullup_str=100,   parent=self)
        self.netlist['n259'] = net.net('n259', pullup_str=100,   parent=self)
        self.netlist['n260'] = net.net('n260', pullup_str=100,   parent=self)
        self.netlist['n261'] = net.net('n261', pullup_str=100,   parent=self)
        self.netlist['n262'] = net.net('n262', pullup_str=100,   parent=self)
        self.netlist['n264'] = net.net('n264', pullup_str=100,   parent=self)
        self.netlist['n265'] = net.net('n265',  charge_storage=True,  parent=self)
        self.netlist['n266'] = net.net('n266',  charge_storage=True,  parent=self)
        self.netlist['n267'] = net.net('n267', pullup_str=100,   parent=self)
        self.netlist['n269'] = net.net('n269', pullup_str=100,   parent=self)
        self.netlist['n270'] = net.net('n270', pullup_str=100,   parent=self)
        self.netlist['n271'] = net.net('n271', pullup_str=100,   parent=self)
        self.netlist['n272'] = net.net('n272', pullup_str=100,   parent=self)
        self.netlist['n273'] = net.net('n273', pullup_str=100,   parent=self)
        self.netlist['n274'] = net.net('n274', pullup_str=100,   parent=self)
        self.netlist['n275'] = net.net('n275', pullup_str=100,   parent=self)
        self.netlist['n277'] = net.net('n277',  charge_storage=True,  parent=self)
        self.netlist['n278'] = net.net('n278', pullup_str=100,   parent=self)
        self.netlist['n279'] = net.net('n279', pullup_str=100,   parent=self)
        self.netlist['n28'] = net.net('n28',  charge_storage=True,  parent=self)
        self.netlist['n280'] = net.net('n280', pullup_str=100,   parent=self)
        self.netlist['n281'] = net.net('n281', pullup_str=100,   parent=self)
        self.netlist['n282'] = net.net('n282', pullup_str=100,   parent=self)
        self.netlist['n284'] = net.net('n284', pullup_str=100,   parent=self)
        self.netlist['n285'] = net.net('n285', pullup_str=100,   parent=self)
        self.netlist['n286'] = net.net('n286', pullup_str=100,   parent=self)
        self.netlist['n288'] = net.net('n288', pullup_str=100,   parent=self)
        self.netlist['n289'] = net.net('n289',  charge_storage=True,  parent=self)
        self.netlist['n29'] = net.net('n29', pullup_str=100,   parent=self)
        self.netlist['n291'] = net.net('n291', pullup_str=100,   parent=self)
        self.netlist['n293'] = net.net('n293', pullup_str=100,   parent=self)
        self.netlist['n295'] = net.net('n295', pullup_str=100,   parent=self)
        self.netlist['n296'] = net.net('n296',  charge_storage=True,  parent=self)
        self.netlist['n297'] = net.net('n297', pullup_str=100,   parent=self)
        self.netlist['n298'] = net.net('n298',  charge_storage=True,  parent=self)
        self.netlist['n299'] = net.net('n299', pullup_str=100,   parent=self)
        self.netlist['n3'] = net.net('n3', pullup_str=100,   parent=self)
        self.netlist['n300'] = net.net('n300', pullup_str=100,   parent=self)
        self.netlist['n301'] = net.net('n301', pullup_str=100,   parent=self)
        self.netlist['n302'] = net.net('n302', pullup_str=100,   parent=self)
        self.netlist['n303'] = net.net('n303', pullup_str=100,   parent=self)
        self.netlist['n304'] = net.net('n304',  charge_storage=True,  parent=self)
        self.netlist['n306'] = net.net('n306', pullup_str=100,   parent=self)
        self.netlist['n307'] = net.net('n307', pullup_str=100,   parent=self)
        self.netlist['n308'] = net.net('n308', pullup_str=100,   parent=self)
        self.netlist['n309'] = net.net('n309', pullup_str=100,   parent=self)
        self.netlist['n31'] = net.net('n31', pullup_str=100,   parent=self)
        self.netlist['n310'] = net.net('n310',  charge_storage=True,  parent=self)
        self.netlist['n311'] = net.net('n311', pullup_str=100,   parent=self)
        self.netlist['n312'] = net.net('n312', pullup_str=100,   parent=self)
        self.netlist['n313'] = net.net('n313',  charge_storage=True,  parent=self)
        self.netlist['n316'] = net.net('n316',  charge_storage=True,  parent=self)
        self.netlist['n317'] = net.net('n317', pullup_str=100,   parent=self)
        self.netlist['n318'] = net.net('n318', pullup_str=100,   parent=self)
        self.netlist['n319'] = net.net('n319', pullup_str=100,   parent=self)
        self.netlist['n320'] = net.net('n320', pullup_str=100,   parent=self)
        self.netlist['n321'] = net.net('n321', pullup_str=100,   parent=self)
        self.netlist['n322'] = net.net('n322',  charge_storage=True,  parent=self)
        self.netlist['n323'] = net.net('n323',  charge_storage=True,  parent=self)
        self.netlist['n324'] = net.net('n324', pullup_str=100,   parent=self)
        self.netlist['n326'] = net.net('n326', pullup_str=100,   parent=self)
        self.netlist['n327'] = net.net('n327', pullup_str=100,   parent=self)
        self.netlist['n329'] = net.net('n329', pullup_str=100,   parent=self)
        self.netlist['n33'] = net.net('n33', pullup_str=100,   parent=self)
        self.netlist['n330'] = net.net('n330', pullup_str=100,   parent=self)
        self.netlist['n332'] = net.net('n332', pullup_str=100,   parent=self)
        self.netlist['n334'] = net.net('n334', pullup_str=100,   parent=self)
        self.netlist['n335'] = net.net('n335', pullup_str=100,   parent=self)
        self.netlist['n336'] = net.net('n336', pullup_str=100,   parent=self)
        self.netlist['n339'] = net.net('n339',  charge_storage=True,  parent=self)
        self.netlist['n34'] = net.net('n34', pullup_str=100,   parent=self)
        self.netlist['n340'] = net.net('n340', pullup_str=100,   parent=self)
        self.netlist['n341'] = net.net('n341', pullup_str=100,   parent=self)
        self.netlist['n342'] = net.net('n342', pullup_str=100,   parent=self)
        self.netlist['n343'] = net.net('n343',  charge_storage=True,  parent=self)
        self.netlist['n344'] = net.net('n344', pullup_str=100,   parent=self)
        self.netlist['n345'] = net.net('n345', pullup_str=100,   parent=self)
        self.netlist['n346'] = net.net('n346',  charge_storage=True,  parent=self)
        self.netlist['n347'] = net.net('n347', pullup_str=100,   parent=self)
        self.netlist['n35'] = net.net('n35', pullup_str=100,   parent=self)
        self.netlist['n350'] = net.net('n350', pullup_str=100,   parent=self)
        self.netlist['n351'] = net.net('n351', pullup_str=100,   parent=self)
        self.netlist['n352'] = net.net('n352', pullup_str=100,   parent=self)
        self.netlist['n354'] = net.net('n354', pullup_str=100,   parent=self)
        self.netlist['n355'] = net.net('n355', pullup_str=100,   parent=self)
        self.netlist['n356'] = net.net('n356',  charge_storage=True,  parent=self)
        self.netlist['n358'] = net.net('n358', pullup_str=100,   parent=self)
        self.netlist['n359'] = net.net('n359',  charge_storage=True,  parent=self)
        self.netlist['n36'] = net.net('n36', pullup_str=100,   parent=self)
        self.netlist['n360'] = net.net('n360',  charge_storage=True,  parent=self)
        self.netlist['n363'] = net.net('n363',  charge_storage=True,  parent=self)
        self.netlist['n364'] = net.net('n364',  charge_storage=True,  parent=self)
        self.netlist['n365'] = net.net('n365', pullup_str=100,   parent=self)
        self.netlist['n366'] = net.net('n366', pullup_str=100,   parent=self)
        self.netlist['n367'] = net.net('n367',  charge_storage=True,  parent=self)
        self.netlist['n368'] = net.net('n368', pullup_str=100,   parent=self)
        self.netlist['n37'] = net.net('n37',  charge_storage=True,  parent=self)
        self.netlist['n370'] = net.net('n370', pullup_str=100,   parent=self)
        self.netlist['n371'] = net.net('n371', pullup_str=100,   parent=self)
        self.netlist['n372'] = net.net('n372', pullup_str=100,   parent=self)
        self.netlist['n373'] = net.net('n373',  charge_storage=True,  parent=self)
        self.netlist['n374'] = net.net('n374', pullup_str=100,   parent=self)
        self.netlist['n375'] = net.net('n375',  charge_storage=True,  parent=self)
        self.netlist['n378'] = net.net('n378', pullup_str=100,   parent=self)
        self.netlist['n379'] = net.net('n379', pullup_str=100,   parent=self)
        self.netlist['n38'] = net.net('n38', pullup_str=100,   parent=self)
        self.netlist['n380'] = net.net('n380',  charge_storage=True,  parent=self)
        self.netlist['n381'] = net.net('n381',  charge_storage=True,  parent=self)
        self.netlist['n382'] = net.net('n382', pullup_str=100,   parent=self)
        self.netlist['n383'] = net.net('n383', pullup_str=100,   parent=self)
        self.netlist['n384'] = net.net('n384', pullup_str=100,   parent=self)
        self.netlist['n385'] = net.net('n385', pullup_str=100,   parent=self)
        self.netlist['n386'] = net.net('n386', pullup_str=100,   parent=self)
        self.netlist['n387'] = net.net('n387',  charge_storage=True,  parent=self)
        self.netlist['n388'] = net.net('n388', pullup_str=100,   parent=self)
        self.netlist['n389'] = net.net('n389', pullup_str=100,   parent=self)
        self.netlist['n39'] = net.net('n39', pullup_str=100,   parent=self)
        self.netlist['n390'] = net.net('n390', pullup_str=100,   parent=self)
        self.netlist['n392'] = net.net('n392', pullup_str=100,   parent=self)
        self.netlist['n393'] = net.net('n393',  charge_storage=True,  parent=self)
        self.netlist['n395'] = net.net('n395',  charge_storage=True,  parent=self)
        self.netlist['n396'] = net.net('n396', pullup_str=100,   parent=self)
        self.netlist['n397'] = net.net('n397', pullup_str=100,   parent=self)
        self.netlist['n398'] = net.net('n398',  charge_storage=True,  parent=self)
        self.netlist['n4'] = net.net('n4', pullup_str=100,   parent=self)
        self.netlist['n400'] = net.net('n400', pullup_str=100,   parent=self)
        self.netlist['n402'] = net.net('n402',  charge_storage=True,  parent=self)
        self.netlist['n403'] = net.net('n403', pullup_str=100,   parent=self)
        self.netlist['n404'] = net.net('n404', pullup_str=100,   parent=self)
        self.netlist['n405'] = net.net('n405',  charge_storage=True,  parent=self)
        self.netlist['n406'] = net.net('n406',  charge_storage=True,  parent=self)
        self.netlist['n408'] = net.net('n408',  charge_storage=True,  parent=self)
        self.netlist['n409'] = net.net('n409', pullup_str=100,   parent=self)
        self.netlist['n41'] = net.net('n41',  charge_storage=True,  parent=self)
        self.netlist['n410'] = net.net('n410', pullup_str=100,   parent=self)
        self.netlist['n415'] = net.net('n415',  charge_storage=True,  parent=self)
        self.netlist['n416'] = net.net('n416',  charge_storage=True,  parent=self)
        self.netlist['n417'] = net.net('n417',  charge_storage=True,  parent=self)
        self.netlist['n419'] = net.net('n419', pullup_str=100,   parent=self)
        self.netlist['n42'] = net.net('n42',  charge_storage=True,  parent=self)
        self.netlist['n420'] = net.net('n420', pullup_str=100,   parent=self)
        self.netlist['n423'] = net.net('n423', pullup_str=100,   parent=self)
        self.netlist['n424'] = net.net('n424', pullup_str=100,   parent=self)
        self.netlist['n426'] = net.net('n426',  charge_storage=True,  parent=self)
        self.netlist['n427'] = net.net('n427', pullup_str=100,   parent=self)
        self.netlist['n428'] = net.net('n428', pullup_str=100,   parent=self)
        self.netlist['n429'] = net.net('n429',  charge_storage=True,  parent=self)
        self.netlist['n43'] = net.net('n43',  charge_storage=True,  parent=self)
        self.netlist['n430'] = net.net('n430',  charge_storage=True,  parent=self)
        self.netlist['n431'] = net.net('n431',  charge_storage=True,  parent=self)
        self.netlist['n432'] = net.net('n432', pullup_str=100,   parent=self)
        self.netlist['n433'] = net.net('n433',  charge_storage=True,  parent=self)
        self.netlist['n434'] = net.net('n434', pullup_str=100,   parent=self)
        self.netlist['n436'] = net.net('n436', pullup_str=100,   parent=self)
        self.netlist['n440'] = net.net('n440', pullup_str=100,   parent=self)
        self.netlist['n441'] = net.net('n441', pullup_str=100,   parent=self)
        self.netlist['n442'] = net.net('n442', pullup_str=100,   parent=self)
        self.netlist['n445'] = net.net('n445', pullup_str=100,   parent=self)
        self.netlist['n446'] = net.net('n446', pullup_str=100,   parent=self)
        self.netlist['n447'] = net.net('n447', pullup_str=100,   parent=self)
        self.netlist['n452'] = net.net('n452',  charge_storage=True,  parent=self)
        self.netlist['n453'] = net.net('n453', pullup_str=100,   parent=self)
        self.netlist['n454'] = net.net('n454',  charge_storage=True,  parent=self)
        self.netlist['n455'] = net.net('n455',  charge_storage=True,  parent=self)
        self.netlist['n457'] = net.net('n457', pullup_str=100,   parent=self)
        self.netlist['n458'] = net.net('n458', pullup_str=100,   parent=self)
        self.netlist['n459'] = net.net('n459',  charge_storage=True,  parent=self)
        self.netlist['n46'] = net.net('n46', pullup_str=100,   parent=self)
        self.netlist['n460'] = net.net('n460',  charge_storage=True,  parent=self)
        self.netlist['n461'] = net.net('n461', pullup_str=100,   parent=self)
        self.netlist['n462'] = net.net('n462', pullup_str=100,   parent=self)
        self.netlist['n463'] = net.net('n463',  charge_storage=True,  parent=self)
        self.netlist['n465'] = net.net('n465', pullup_str=100,   parent=self)
        self.netlist['n466'] = net.net('n466', pullup_str=100,   parent=self)
        self.netlist['n467'] = net.net('n467', pullup_str=100,   parent=self)
        self.netlist['n468'] = net.net('n468', pullup_str=100,   parent=self)
        self.netlist['n469'] = net.net('n469',  charge_storage=True,  parent=self)
        self.netlist['n47'] = net.net('n47',  charge_storage=True,  parent=self)
        self.netlist['n470'] = net.net('n470', pullup_str=100,   parent=self)
        self.netlist['n471'] = net.net('n471',  charge_storage=True,  parent=self)
        self.netlist['n472'] = net.net('n472', pullup_str=100,   parent=self)
        self.netlist['n473'] = net.net('n473', pullup_str=100,   parent=self)
        self.netlist['n474'] = net.net('n474', pullup_str=100,   parent=self)
        self.netlist['n475'] = net.net('n475',  charge_storage=True,  parent=self)
        self.netlist['n476'] = net.net('n476', pullup_str=100,   parent=self)
        self.netlist['n477'] = net.net('n477', pullup_str=100,   parent=self)
        self.netlist['n478'] = net.net('n478', pullup_str=100,   parent=self)
        self.netlist['n479'] = net.net('n479', pullup_str=100,   parent=self)
        self.netlist['n480'] = net.net('n480', pullup_str=100,   parent=self)
        self.netlist['n482'] = net.net('n482',  charge_storage=True,  parent=self)
        self.netlist['n484'] = net.net('n484', pullup_str=100,   parent=self)
        self.netlist['n486'] = net.net('n486', pullup_str=100,   parent=self)
        self.netlist['n487'] = net.net('n487', pullup_str=100,   parent=self)
        self.netlist['n490'] = net.net('n490', pullup_str=100,   parent=self)
        self.netlist['n491'] = net.net('n491', pullup_str=100,   parent=self)
        self.netlist['n492'] = net.net('n492', pullup_str=100,   parent=self)
        self.netlist['n494'] = net.net('n494', pullup_str=100,   parent=self)
        self.netlist['n496'] = net.net('n496', pullup_str=100,   parent=self)
        self.netlist['n499'] = net.net('n499', pullup_str=100,   parent=self)
        self.netlist['n5'] = net.net('n5', pullup_str=100,   parent=self)
        self.netlist['n50'] = net.net('n50',  charge_storage=True,  parent=self)
        self.netlist['n501'] = net.net('n501', pullup_str=100,   parent=self)
        self.netlist['n503'] = net.net('n503', pullup_str=100,   parent=self)
        self.netlist['n504'] = net.net('n504', pullup_str=100,   parent=self)
        self.netlist['n506'] = net.net('n506', pullup_str=100,   parent=self)
        self.netlist['n507'] = net.net('n507', pullup_str=100,   parent=self)
        self.netlist['n508'] = net.net('n508',  charge_storage=True,  parent=self)
        self.netlist['n509'] = net.net('n509',  charge_storage=True,  parent=self)
        self.netlist['n51'] = net.net('n51',  charge_storage=True,  parent=self)
        self.netlist['n510'] = net.net('n510', pullup_str=100,   parent=self)
        self.netlist['n511'] = net.net('n511',  charge_storage=True,  parent=self)
        self.netlist['n512'] = net.net('n512',  charge_storage=True,  parent=self)
        self.netlist['n513'] = net.net('n513', pullup_str=100,   parent=self)
        self.netlist['n514'] = net.net('n514',  charge_storage=True,  parent=self)
        self.netlist['n515'] = net.net('n515', pullup_str=100,   parent=self)
        self.netlist['n516'] = net.net('n516', pullup_str=100,   parent=self)
        self.netlist['n517'] = net.net('n517', pullup_str=100,   parent=self)
        self.netlist['n518'] = net.net('n518', pullup_str=100,   parent=self)
        self.netlist['n519'] = net.net('n519', pullup_str=100,   parent=self)
        self.netlist['n520'] = net.net('n520',  charge_storage=True,  parent=self)
        self.netlist['n521'] = net.net('n521',  charge_storage=True,  parent=self)
        self.netlist['n522'] = net.net('n522', pullup_str=100,   parent=self)
        self.netlist['n523'] = net.net('n523', pullup_str=100,   parent=self)
        self.netlist['n524'] = net.net('n524',  charge_storage=True,  parent=self)
        self.netlist['n525'] = net.net('n525', pullup_str=100,   parent=self)
        self.netlist['n526'] = net.net('n526',  charge_storage=True,  parent=self)
        self.netlist['n528'] = net.net('n528', pullup_str=100,   parent=self)
        self.netlist['n53'] = net.net('n53', pullup_str=100,   parent=self)
        self.netlist['n531'] = net.net('n531', pullup_str=100,   parent=self)
        self.netlist['n532'] = net.net('n532', pullup_str=100,   parent=self)
        self.netlist['n533'] = net.net('n533', pullup_str=100,   parent=self)
        self.netlist['n535'] = net.net('n535', pullup_str=100,   parent=self)
        self.netlist['n536'] = net.net('n536',  charge_storage=True,  parent=self)
        self.netlist['n537'] = net.net('n537',  charge_storage=True,  parent=self)
        self.netlist['n538'] = net.net('n538', pullup_str=100,   parent=self)
        self.netlist['n540'] = net.net('n540', pullup_str=100,   parent=self)
        self.netlist['n541'] = net.net('n541',  charge_storage=True,  parent=self)
        self.netlist['n543'] = net.net('n543', pullup_str=100,   parent=self)
        self.netlist['n544'] = net.net('n544', pullup_str=100,   parent=self)
        self.netlist['n545'] = net.net('n545',  charge_storage=True,  parent=self)
        self.netlist['n546'] = net.net('n546', pullup_str=100,   parent=self)
        self.netlist['n547'] = net.net('n547',  charge_storage=True,  parent=self)
        self.netlist['n548'] = net.net('n548', pullup_str=100,   parent=self)
        self.netlist['n55'] = net.net('n55',  charge_storage=True,  parent=self)
        self.netlist['n550'] = net.net('n550', pullup_str=100,   parent=self)
        self.netlist['n551'] = net.net('n551', pullup_str=100,   parent=self)
        self.netlist['n552'] = net.net('n552', pullup_str=100,   parent=self)
        self.netlist['n553'] = net.net('n553', pullup_str=100,   parent=self)
        self.netlist['n554'] = net.net('n554',  charge_storage=True,  parent=self)
        self.netlist['n555'] = net.net('n555', pullup_str=100,   parent=self)
        self.netlist['n556'] = net.net('n556', pullup_str=100,   parent=self)
        self.netlist['n557'] = net.net('n557',  charge_storage=True,  parent=self)
        self.netlist['n559'] = net.net('n559',  charge_storage=True,  parent=self)
        self.netlist['n560'] = net.net('n560',  charge_storage=True,  parent=self)
        self.netlist['n562'] = net.net('n562',  charge_storage=True,  parent=self)
        self.netlist['n564'] = net.net('n564', pullup_str=100,   parent=self)
        self.netlist['n566'] = net.net('n566', pullup_str=100,   parent=self)
        self.netlist['n568'] = net.net('n568', pullup_str=100,   parent=self)
        self.netlist['n569'] = net.net('n569',  charge_storage=True,  parent=self)
        self.netlist['n57'] = net.net('n57',  charge_storage=True,  parent=self)
        self.netlist['n570'] = net.net('n570', pullup_str=100,   parent=self)
        self.netlist['n571'] = net.net('n571', pullup_str=100,   parent=self)
        self.netlist['n572'] = net.net('n572', pullup_str=100,   parent=self)
        self.netlist['n575'] = net.net('n575', pullup_str=100,   parent=self)
        self.netlist['n577'] = net.net('n577',  charge_storage=True,  parent=self)
        self.netlist['n578'] = net.net('n578', pullup_str=100,   parent=self)
        self.netlist['n579'] = net.net('n579', pullup_str=100,   parent=self)
        self.netlist['n58'] = net.net('n58', pullup_str=100,   parent=self)
        self.netlist['n580'] = net.net('n580',  charge_storage=True,  parent=self)
        self.netlist['n581'] = net.net('n581',  charge_storage=True,  parent=self)
        self.netlist['n582'] = net.net('n582', pullup_str=100,   parent=self)
        self.netlist['n583'] = net.net('n583', pullup_str=100,   parent=self)
        self.netlist['n585'] = net.net('n585',  charge_storage=True,  parent=self)
        self.netlist['n586'] = net.net('n586', pullup_str=100,   parent=self)
        self.netlist['n587'] = net.net('n587', pullup_str=100,   parent=self)
        self.netlist['n588'] = net.net('n588', pullup_str=100,   parent=self)
        self.netlist['n590'] = net.net('n590',  charge_storage=True,  parent=self)
        self.netlist['n591'] = net.net('n591',  charge_storage=True,  parent=self)
        self.netlist['n592'] = net.net('n592', pullup_str=100,   parent=self)
        self.netlist['n593'] = net.net('n593', pullup_str=100,   parent=self)
        self.netlist['n594'] = net.net('n594', pullup_str=100,   parent=self)
        self.netlist['n595'] = net.net('n595', pullup_str=100,   parent=self)
        self.netlist['n597'] = net.net('n597',  charge_storage=True,  parent=self)
        self.netlist['n598'] = net.net('n598',  charge_storage=True,  parent=self)
        self.netlist['n599'] = net.net('n599',  charge_storage=True,  parent=self)
        self.netlist['n6'] = net.net('n6', pullup_str=100,   parent=self)
        self.netlist['n60'] = net.net('n60', pullup_str=100,   parent=self)
        self.netlist['n600'] = net.net('n600', pullup_str=100,   parent=self)
        self.netlist['n602'] = net.net('n602', pullup_str=100,   parent=self)
        self.netlist['n603'] = net.net('n603', pullup_str=100,   parent=self)
        self.netlist['n604'] = net.net('n604', pullup_str=100,   parent=self)
        self.netlist['n605'] = net.net('n605',  charge_storage=True,  parent=self)
        self.netlist['n607'] = net.net('n607', pullup_str=100,   parent=self)
        self.netlist['n608'] = net.net('n608', pullup_str=100,   parent=self)
        self.netlist['n609'] = net.net('n609', pullup_str=100,   parent=self)
        self.netlist['n61'] = net.net('n61', pullup_str=100,   parent=self)
        self.netlist['n610'] = net.net('n610',  charge_storage=True,  parent=self)
        self.netlist['n611'] = net.net('n611', pullup_str=100,   parent=self)
        self.netlist['n612'] = net.net('n612',  charge_storage=True,  parent=self)
        self.netlist['n613'] = net.net('n613', pullup_str=100,   parent=self)
        self.netlist['n616'] = net.net('n616', pullup_str=100,   parent=self)
        self.netlist['n617'] = net.net('n617', pullup_str=100,   parent=self)
        self.netlist['n618'] = net.net('n618', pullup_str=100,   parent=self)
        self.netlist['n619'] = net.net('n619',  charge_storage=True,  parent=self)
        self.netlist['n62'] = net.net('n62', pullup_str=100,   parent=self)
        self.netlist['n620'] = net.net('n620', pullup_str=100,   parent=self)
        self.netlist['n621'] = net.net('n621',  charge_storage=True,  parent=self)
        self.netlist['n623'] = net.net('n623', pullup_str=100,   parent=self)
        self.netlist['n624'] = net.net('n624', pullup_str=100,   parent=self)
        self.netlist['n625'] = net.net('n625', pullup_str=100,   parent=self)
        self.netlist['n626'] = net.net('n626', pullup_str=100,   parent=self)
        self.netlist['n628'] = net.net('n628', pullup_str=100,   parent=self)
        self.netlist['n629'] = net.net('n629', pullup_str=100,   parent=self)
        self.netlist['n630'] = net.net('n630', pullup_str=100,   parent=self)
        self.netlist['n631'] = net.net('n631', pullup_str=100,   parent=self)
        self.netlist['n632'] = net.net('n632', pullup_str=100,   parent=self)
        self.netlist['n633'] = net.net('n633',  charge_storage=True,  parent=self)
        self.netlist['n634'] = net.net('n634',  charge_storage=True,  parent=self)
        self.netlist['n635'] = net.net('n635',  charge_storage=True,  parent=self)
        self.netlist['n636'] = net.net('n636', pullup_str=100,   parent=self)
        self.netlist['n637'] = net.net('n637', pullup_str=100,   parent=self)
        self.netlist['n638'] = net.net('n638', pullup_str=100,   parent=self)
        self.netlist['n639'] = net.net('n639',  charge_storage=True,  parent=self)
        self.netlist['n641'] = net.net('n641', pullup_str=100,   parent=self)
        self.netlist['n642'] = net.net('n642',  charge_storage=True,  parent=self)
        self.netlist['n643'] = net.net('n643',  charge_storage=True,  parent=self)
        self.netlist['n644'] = net.net('n644',  charge_storage=True,  parent=self)
        self.netlist['n645'] = net.net('n645', pullup_str=100,   parent=self)
        self.netlist['n646'] = net.net('n646', pullup_str=100,   parent=self)
        self.netlist['n647'] = net.net('n647', pullup_str=100,   parent=self)
        self.netlist['n648'] = net.net('n648',  charge_storage=True,  parent=self)
        self.netlist['n649'] = net.net('n649', pullup_str=100,   parent=self)
        self.netlist['n65'] = net.net('n65', pullup_str=100,   parent=self)
        self.netlist['n651'] = net.net('n651', pullup_str=100,   parent=self)
        self.netlist['n653'] = net.net('n653',  charge_storage=True,  parent=self)
        self.netlist['n656'] = net.net('n656',  charge_storage=True,  parent=self)
        self.netlist['n658'] = net.net('n658', pullup_str=100,   parent=self)
        self.netlist['n659'] = net.net('n659',  charge_storage=True,  parent=self)
        self.netlist['n66'] = net.net('n66',  charge_storage=True,  parent=self)
        self.netlist['n660'] = net.net('n660', pullup_str=100,   parent=self)
        self.netlist['n661'] = net.net('n661',  charge_storage=True,  parent=self)
        self.netlist['n662'] = net.net('n662', pullup_str=100,   parent=self)
        self.netlist['n663'] = net.net('n663',  charge_storage=True,  parent=self)
        self.netlist['n664'] = net.net('n664', pullup_str=100,   parent=self)
        self.netlist['n665'] = net.net('n665', pullup_str=100,   parent=self)
        self.netlist['n666'] = net.net('n666',  charge_storage=True,  parent=self)
        self.netlist['n667'] = net.net('n667', pullup_str=100,   parent=self)
        self.netlist['n668'] = net.net('n668',  charge_storage=True,  parent=self)
        self.netlist['n669'] = net.net('n669', pullup_str=100,   parent=self)
        self.netlist['n670'] = net.net('n670', pullup_str=100,   parent=self)
        self.netlist['n671'] = net.net('n671',  charge_storage=True,  parent=self)
        self.netlist['n673'] = net.net('n673', pullup_str=100,   parent=self)
        self.netlist['n674'] = net.net('n674', pullup_str=100,   parent=self)
        self.netlist['n676'] = net.net('n676',  charge_storage=True,  parent=self)
        self.netlist['n677'] = net.net('n677', pullup_str=100,   parent=self)
        self.netlist['n678'] = net.net('n678', pullup_str=100,   parent=self)
        self.netlist['n680'] = net.net('n680',  charge_storage=True,  parent=self)
        self.netlist['n681'] = net.net('n681', pullup_str=100,   parent=self)
        self.netlist['n682'] = net.net('n682', pullup_str=100,   parent=self)
        self.netlist['n686'] = net.net('n686', pullup_str=100,   parent=self)
        self.netlist['n688'] = net.net('n688',  charge_storage=True,  parent=self)
        self.netlist['n689'] = net.net('n689', pullup_str=100,   parent=self)
        self.netlist['n69'] = net.net('n69',  charge_storage=True,  parent=self)
        self.netlist['n691'] = net.net('n691', pullup_str=100,   parent=self)
        self.netlist['n692'] = net.net('n692', pullup_str=100,   parent=self)
        self.netlist['n693'] = net.net('n693', pullup_str=100,   parent=self)
        self.netlist['n694'] = net.net('n694', pullup_str=100,   parent=self)
        self.netlist['n695'] = net.net('n695', pullup_str=100,   parent=self)
        self.netlist['n696'] = net.net('n696', pullup_str=100,   parent=self)
        self.netlist['n698'] = net.net('n698',  charge_storage=True,  parent=self)
        self.netlist['n699'] = net.net('n699', pullup_str=100,   parent=self)
        self.netlist['n7'] = net.net('n7',  charge_storage=True,  parent=self)
        self.netlist['n70'] = net.net('n70', pullup_str=100,   parent=self)
        self.netlist['n700'] = net.net('n700', pullup_str=100,   parent=self)
        self.netlist['n701'] = net.net('n701', pullup_str=100,   parent=self)
        self.netlist['n703'] = net.net('n703',  charge_storage=True,  parent=self)
        self.netlist['n705'] = net.net('n705',  charge_storage=True,  parent=self)
        self.netlist['n707'] = net.net('n707',  charge_storage=True,  parent=self)
        self.netlist['n708'] = net.net('n708', pullup_str=100,   parent=self)
        self.netlist['n709'] = net.net('n709', pullup_str=100,   parent=self)
        self.netlist['n71'] = net.net('n71', pullup_str=100,   parent=self)
        self.netlist['n711'] = net.net('n711',  charge_storage=True,  parent=self)
        self.netlist['n712'] = net.net('n712', pullup_str=100,   parent=self)
        self.netlist['n714'] = net.net('n714', pullup_str=100,   parent=self)
        self.netlist['n715'] = net.net('n715', pullup_str=100,   parent=self)
        self.netlist['n716'] = net.net('n716',  charge_storage=True,  parent=self)
        self.netlist['n717'] = net.net('n717', pullup_str=100,   parent=self)
        self.netlist['n718'] = net.net('n718', pullup_str=100,   parent=self)
        self.netlist['n719'] = net.net('n719',  charge_storage=True,  parent=self)
        self.netlist['n720'] = net.net('n720', pullup_str=100,   parent=self)
        self.netlist['n721'] = net.net('n721', pullup_str=100,   parent=self)
        self.netlist['n722'] = net.net('n722',  charge_storage=True,  parent=self)
        self.netlist['n724'] = net.net('n724',  charge_storage=True,  parent=self)
        self.netlist['n725'] = net.net('n725', pullup_str=100,   parent=self)
        self.netlist['n726'] = net.net('n726', pullup_str=100,   parent=self)
        self.netlist['n728'] = net.net('n728', pullup_str=100,   parent=self)
        self.netlist['n731'] = net.net('n731', pullup_str=100,   parent=self)
        self.netlist['n732'] = net.net('n732', pullup_str=100,   parent=self)
        self.netlist['n733'] = net.net('n733', pullup_str=100,   parent=self)
        self.netlist['n734'] = net.net('n734',  charge_storage=True,  parent=self)
        self.netlist['n735'] = net.net('n735', pullup_str=100,   parent=self)
        self.netlist['n738'] = net.net('n738',  charge_storage=True,  parent=self)
        self.netlist['n739'] = net.net('n739', pullup_str=100,   parent=self)
        self.netlist['n74'] = net.net('n74',  charge_storage=True,  parent=self)
        self.netlist['n740'] = net.net('n740',  charge_storage=True,  parent=self)
        self.netlist['n742'] = net.net('n742',  charge_storage=True,  parent=self)
        self.netlist['n743'] = net.net('n743', pullup_str=100,   parent=self)
        self.netlist['n745'] = net.net('n745',  charge_storage=True,  parent=self)
        self.netlist['n747'] = net.net('n747', pullup_str=100,   parent=self)
        self.netlist['n748'] = net.net('n748', pullup_str=100,   parent=self)
        self.netlist['n75'] = net.net('n75', pullup_str=100,   parent=self)
        self.netlist['n750'] = net.net('n750', pullup_str=100,   parent=self)
        self.netlist['n751'] = net.net('n751',  charge_storage=True,  parent=self)
        self.netlist['n753'] = net.net('n753', pullup_str=100,   parent=self)
        self.netlist['n754'] = net.net('n754', pullup_str=100,   parent=self)
        self.netlist['n755'] = net.net('n755', pullup_str=100,   parent=self)
        self.netlist['n756'] = net.net('n756',  charge_storage=True,  parent=self)
        self.netlist['n757'] = net.net('n757', pullup_str=100,   parent=self)
        self.netlist['n759'] = net.net('n759',  charge_storage=True,  parent=self)
        self.netlist['n76'] = net.net('n76', pullup_str=100,   parent=self)
        self.netlist['n760'] = net.net('n760',  charge_storage=True,  parent=self)
        self.netlist['n761'] = net.net('n761', pullup_str=100,   parent=self)
        self.netlist['n762'] = net.net('n762', pullup_str=100,   parent=self)
        self.netlist['n763'] = net.net('n763', pullup_str=100,   parent=self)
        self.netlist['n764'] = net.net('n764', pullup_str=100,   parent=self)
        self.netlist['n766'] = net.net('n766',  charge_storage=True,  parent=self)
        self.netlist['n767'] = net.net('n767', pullup_str=100,   parent=self)
        self.netlist['n768'] = net.net('n768',  charge_storage=True,  parent=self)
        self.netlist['n769'] = net.net('n769', pullup_str=100,   parent=self)
        self.netlist['n770'] = net.net('n770', pullup_str=100,   parent=self)
        self.netlist['n771'] = net.net('n771', pullup_str=100,   parent=self)
        self.netlist['n772'] = net.net('n772', pullup_str=100,   parent=self)
        self.netlist['n773'] = net.net('n773', pullup_str=100,   parent=self)
        self.netlist['n774'] = net.net('n774', pullup_str=100,   parent=self)
        self.netlist['n776'] = net.net('n776', pullup_str=100,   parent=self)
        self.netlist['n778'] = net.net('n778', pullup_str=100,   parent=self)
        self.netlist['n779'] = net.net('n779', pullup_str=100,   parent=self)
        self.netlist['n780'] = net.net('n780',  charge_storage=True,  parent=self)
        self.netlist['n781'] = net.net('n781', pullup_str=100,   parent=self)
        self.netlist['n782'] = net.net('n782', pullup_str=100,   parent=self)
        self.netlist['n783'] = net.net('n783', pullup_str=100,   parent=self)
        self.netlist['n784'] = net.net('n784', pullup_str=100,   parent=self)
        self.netlist['n785'] = net.net('n785',  charge_storage=True,  parent=self)
        self.netlist['n786'] = net.net('n786', pullup_str=100,   parent=self)
        self.netlist['n787'] = net.net('n787', pullup_str=100,   parent=self)
        self.netlist['n788'] = net.net('n788', pullup_str=100,   parent=self)
        self.netlist['n789'] = net.net('n789', pullup_str=100,   parent=self)
        self.netlist['n79'] = net.net('n79', pullup_str=100,   parent=self)
        self.netlist['n790'] = net.net('n790', pullup_str=100,   parent=self)
        self.netlist['n791'] = net.net('n791', pullup_str=100,   parent=self)
        self.netlist['n792'] = net.net('n792',  charge_storage=True,  parent=self)
        self.netlist['n793'] = net.net('n793',  charge_storage=True,  parent=self)
        self.netlist['n794'] = net.net('n794',  charge_storage=True,  parent=self)
        self.netlist['n795'] = net.net('n795', pullup_str=100,   parent=self)
        self.netlist['n796'] = net.net('n796',  charge_storage=True,  parent=self)
        self.netlist['n797'] = net.net('n797', pullup_str=100,   parent=self)
        self.netlist['n798'] = net.net('n798',  charge_storage=True,  parent=self)
        self.netlist['n799'] = net.net('n799',  charge_storage=True,  parent=self)
        self.netlist['n8'] = net.net('n8', pullup_str=100,   parent=self)
        self.netlist['n80'] = net.net('n80', pullup_str=100,   parent=self)
        self.netlist['n800'] = net.net('n800', pullup_str=100,   parent=self)
        self.netlist['n802'] = net.net('n802',  charge_storage=True,  parent=self)
        self.netlist['n803'] = net.net('n803', pullup_str=100,   parent=self)
        self.netlist['n804'] = net.net('n804', pullup_str=100,   parent=self)
        self.netlist['n805'] = net.net('n805',  charge_storage=True,  parent=self)
        self.netlist['n806'] = net.net('n806',  charge_storage=True,  parent=self)
        self.netlist['n807'] = net.net('n807', pullup_str=100,   parent=self)
        self.netlist['n809'] = net.net('n809', pullup_str=100,   parent=self)
        self.netlist['n810'] = net.net('n810', pullup_str=100,   parent=self)
        self.netlist['n811'] = net.net('n811', pullup_str=100,   parent=self)
        self.netlist['n812'] = net.net('n812', pullup_str=100,   parent=self)
        self.netlist['n813'] = net.net('n813', pullup_str=100,   parent=self)
        self.netlist['n814'] = net.net('n814',  charge_storage=True,  parent=self)
        self.netlist['n815'] = net.net('n815', pullup_str=100,   parent=self)
        self.netlist['n816'] = net.net('n816',  charge_storage=True,  parent=self)
        self.netlist['n817'] = net.net('n817', pullup_str=100,   parent=self)
        self.netlist['n818'] = net.net('n818', pullup_str=100,   parent=self)
        self.netlist['n819'] = net.net('n819', pullup_str=100,   parent=self)
        self.netlist['n820'] = net.net('n820',  charge_storage=True,  parent=self)
        self.netlist['n821'] = net.net('n821',  charge_storage=True,  parent=self)
        self.netlist['n822'] = net.net('n822', pullup_str=100,   parent=self)
        self.netlist['n824'] = net.net('n824', pullup_str=100,   parent=self)
        self.netlist['n825'] = net.net('n825',  charge_storage=True,  parent=self)
        self.netlist['n826'] = net.net('n826',  charge_storage=True,  parent=self)
        self.netlist['n83'] = net.net('n83', pullup_str=100,   parent=self)
        self.netlist['n830'] = net.net('n830', pullup_str=100,   parent=self)
        self.netlist['n831'] = net.net('n831', pullup_str=100,   parent=self)
        self.netlist['n834'] = net.net('n834', pullup_str=100,   parent=self)
        self.netlist['n835'] = net.net('n835',  charge_storage=True,  parent=self)
        self.netlist['n836'] = net.net('n836',  charge_storage=True,  parent=self)
        self.netlist['n837'] = net.net('n837', pullup_str=100,   parent=self)
        self.netlist['n838'] = net.net('n838', pullup_str=100,   parent=self)
        self.netlist['n839'] = net.net('n839', pullup_str=100,   parent=self)
        self.netlist['n84'] = net.net('n84', pullup_str=100,   parent=self)
        self.netlist['n840'] = net.net('n840', pullup_str=100,   parent=self)
        self.netlist['n841'] = net.net('n841', pullup_str=100,   parent=self)
        self.netlist['n842'] = net.net('n842', pullup_str=100,   parent=self)
        self.netlist['n844'] = net.net('n844', pullup_str=100,   parent=self)
        self.netlist['n845'] = net.net('n845', pullup_str=100,   parent=self)
        self.netlist['n846'] = net.net('n846', pullup_str=100,   parent=self)
        self.netlist['n847'] = net.net('n847', pullup_str=100,   parent=self)
        self.netlist['n849'] = net.net('n849', pullup_str=100,   parent=self)
        self.netlist['n850'] = net.net('n850', pullup_str=100,   parent=self)
        self.netlist['n851'] = net.net('n851', pullup_str=100,   parent=self)
        self.netlist['n852'] = net.net('n852', pullup_str=100,   parent=self)
        self.netlist['n853'] = net.net('n853', pullup_str=100,   parent=self)
        self.netlist['n854'] = net.net('n854', pullup_str=100,   parent=self)
        self.netlist['n855'] = net.net('n855',  charge_storage=True,  parent=self)
        self.netlist['n856'] = net.net('n856',  charge_storage=True,  parent=self)
        self.netlist['n857'] = net.net('n857', pullup_str=100,   parent=self)
        self.netlist['n86'] = net.net('n86',  charge_storage=True,  parent=self)
        self.netlist['n860'] = net.net('n860', pullup_str=100,   parent=self)
        self.netlist['n861'] = net.net('n861', pullup_str=100,   parent=self)
        self.netlist['n862'] = net.net('n862', pullup_str=100,   parent=self)
        self.netlist['n863'] = net.net('n863',  charge_storage=True,  parent=self)
        self.netlist['n864'] = net.net('n864',  charge_storage=True,  parent=self)
        self.netlist['n865'] = net.net('n865',  charge_storage=True,  parent=self)
        self.netlist['n866'] = net.net('n866',  charge_storage=True,  parent=self)
        self.netlist['n867'] = net.net('n867', pullup_str=100,   parent=self)
        self.netlist['n868'] = net.net('n868',  charge_storage=True,  parent=self)
        self.netlist['n869'] = net.net('n869',  charge_storage=True,  parent=self)
        self.netlist['n87'] = net.net('n87',  charge_storage=True,  parent=self)
        self.netlist['n871'] = net.net('n871', pullup_str=100,   parent=self)
        self.netlist['n875'] = net.net('n875', pullup_str=100,   parent=self)
        self.netlist['n876'] = net.net('n876', pullup_str=100,   parent=self)
        self.netlist['n877'] = net.net('n877', pullup_str=100,   parent=self)
        self.netlist['n878'] = net.net('n878',  charge_storage=True,  parent=self)
        self.netlist['n88'] = net.net('n88',  charge_storage=True,  parent=self)
        self.netlist['n880'] = net.net('n880', pullup_str=100,   parent=self)
        self.netlist['n881'] = net.net('n881',  charge_storage=True,  parent=self)
        self.netlist['n882'] = net.net('n882', pullup_str=100,   parent=self)
        self.netlist['n883'] = net.net('n883', pullup_str=100,   parent=self)
        self.netlist['n884'] = net.net('n884', pullup_str=100,   parent=self)
        self.netlist['n885'] = net.net('n885', pullup_str=100,   parent=self)
        self.netlist['n886'] = net.net('n886',  charge_storage=True,  parent=self)
        self.netlist['n888'] = net.net('n888', pullup_str=100,   parent=self)
        self.netlist['n889'] = net.net('n889', pullup_str=100,   parent=self)
        self.netlist['n891'] = net.net('n891',  charge_storage=True,  parent=self)
        self.netlist['n896'] = net.net('n896', pullup_str=100,   parent=self)
        self.netlist['n897'] = net.net('n897',  charge_storage=True,  parent=self)
        self.netlist['n9'] = net.net('n9',  charge_storage=True,  parent=self)
        self.netlist['n90'] = net.net('n90', pullup_str=100,   parent=self)
        self.netlist['n901'] = net.net('n901', pullup_str=100,   parent=self)
        self.netlist['n902'] = net.net('n902',  charge_storage=True,  parent=self)
        self.netlist['n903'] = net.net('n903',  charge_storage=True,  parent=self)
        self.netlist['n904'] = net.net('n904', pullup_str=100,   parent=self)
        self.netlist['n905'] = net.net('n905', pullup_str=100,   parent=self)
        self.netlist['n906'] = net.net('n906', pullup_str=100,   parent=self)
        self.netlist['n907'] = net.net('n907',  charge_storage=True,  parent=self)
        self.netlist['n91'] = net.net('n91', pullup_str=100,   parent=self)
        self.netlist['n911'] = net.net('n911',  charge_storage=True,  parent=self)
        self.netlist['n912'] = net.net('n912',  charge_storage=True,  parent=self)
        self.netlist['n913'] = net.net('n913', pullup_str=100,   parent=self)
        self.netlist['n914'] = net.net('n914',  charge_storage=True,  parent=self)
        self.netlist['n916'] = net.net('n916', pullup_str=100,   parent=self)
        self.netlist['n917'] = net.net('n917', pullup_str=100,   parent=self)
        self.netlist['n918'] = net.net('n918', pullup_str=100,   parent=self)
        self.netlist['n919'] = net.net('n919', pullup_str=100,   parent=self)
        self.netlist['n92'] = net.net('n92',  charge_storage=True,  parent=self)
        self.netlist['n920'] = net.net('n920', pullup_str=100,   parent=self)
        self.netlist['n922'] = net.net('n922',  charge_storage=True,  parent=self)
        self.netlist['n923'] = net.net('n923', pullup_str=100,   parent=self)
        self.netlist['n924'] = net.net('n924',  charge_storage=True,  parent=self)
        self.netlist['n925'] = net.net('n925', pullup_str=100,   parent=self)
        self.netlist['n927'] = net.net('n927',  charge_storage=True,  parent=self)
        self.netlist['n928'] = net.net('n928', pullup_str=100,   parent=self)
        self.netlist['n929'] = net.net('n929', pullup_str=100,   parent=self)
        self.netlist['n93'] = net.net('n93', pullup_str=100,   parent=self)
        self.netlist['n930'] = net.net('n930', pullup_str=100,   parent=self)
        self.netlist['n931'] = net.net('n931', pullup_str=100,   parent=self)
        self.netlist['n932'] = net.net('n932', pullup_str=100,   parent=self)
        self.netlist['n933'] = net.net('n933', pullup_str=100,   parent=self)
        self.netlist['n934'] = net.net('n934', pullup_str=100,   parent=self)
        self.netlist['n935'] = net.net('n935', pullup_str=100,   parent=self)
        self.netlist['n936'] = net.net('n936', pullup_str=100,   parent=self)
        self.netlist['n937'] = net.net('n937', pullup_str=100,   parent=self)
        self.netlist['n939'] = net.net('n939',  charge_storage=True,  parent=self)
        self.netlist['n94'] = net.net('n94',  charge_storage=True,  parent=self)
        self.netlist['n941'] = net.net('n941',  charge_storage=True,  parent=self)
        self.netlist['n942'] = net.net('n942',  charge_storage=True,  parent=self)
        self.netlist['n944'] = net.net('n944', pullup_str=100,   parent=self)
        self.netlist['n946'] = net.net('n946', pullup_str=100,   parent=self)
        self.netlist['n947'] = net.net('n947', pullup_str=100,   parent=self)
        self.netlist['n949'] = net.net('n949',  charge_storage=True,  parent=self)
        self.netlist['n95'] = net.net('n95',  charge_storage=True,  parent=self)
        self.netlist['n950'] = net.net('n950', pullup_str=100,   parent=self)
        self.netlist['n951'] = net.net('n951', pullup_str=100,   parent=self)
        self.netlist['n952'] = net.net('n952', pullup_str=100,   parent=self)
        self.netlist['n953'] = net.net('n953', pullup_str=100,   parent=self)
        self.netlist['n954'] = net.net('n954', pullup_str=100,   parent=self)
        self.netlist['n956'] = net.net('n956', pullup_str=100,   parent=self)
        self.netlist['n957'] = net.net('n957',  charge_storage=True,  parent=self)
        self.netlist['n958'] = net.net('n958', pullup_str=100,   parent=self)
        self.netlist['n959'] = net.net('n959', pullup_str=100,   parent=self)
        self.netlist['n961'] = net.net('n961', pullup_str=100,   parent=self)
        self.netlist['n962'] = net.net('n962', pullup_str=100,   parent=self)
        self.netlist['n963'] = net.net('n963',  charge_storage=True,  parent=self)
        self.netlist['n964'] = net.net('n964', pullup_str=100,   parent=self)
        self.netlist['n965'] = net.net('n965', pullup_str=100,   parent=self)
        self.netlist['n966'] = net.net('n966', pullup_str=100,   parent=self)
        self.netlist['n968'] = net.net('n968',  charge_storage=True,  parent=self)
        self.netlist['n969'] = net.net('n969', pullup_str=100,   parent=self)
        self.netlist['n970'] = net.net('n970',  charge_storage=True,  parent=self)
        self.netlist['n972'] = net.net('n972',  charge_storage=True,  parent=self)
        self.netlist['n973'] = net.net('n973', pullup_str=100,   parent=self)
        self.netlist['n975'] = net.net('n975', pullup_str=100,   parent=self)
        self.netlist['n979'] = net.net('n979', pullup_str=100,   parent=self)
        self.netlist['n980'] = net.net('n980', pullup_str=100,   parent=self)
        self.netlist['n982'] = net.net('n982',  charge_storage=True,  parent=self)
        self.netlist['n983'] = net.net('n983', pullup_str=100,   parent=self)
        self.netlist['n985'] = net.net('n985', pullup_str=100,   parent=self)
        self.netlist['n986'] = net.net('n986', pullup_str=100,   parent=self)
        self.netlist['n988'] = net.net('n988', pullup_str=100,   parent=self)
        self.netlist['n990'] = net.net('n990', pullup_str=100,   parent=self)
        self.netlist['n992'] = net.net('n992', pullup_str=100,   parent=self)
        self.netlist['n993'] = net.net('n993',  charge_storage=True,  parent=self)
        self.netlist['n994'] = net.net('n994',  charge_storage=True,  parent=self)
        self.netlist['n995'] = net.net('n995', pullup_str=100,   parent=self)
        self.netlist['n998'] = net.net('n998', pullup_str=100,   parent=self)
        self.netlist['n999'] = net.net('n999',  charge_storage=True,  parent=self)
        self.port['nmi'].netconn.charge_storage=True
        self.netlist['nnT2BR'] = net.net('nnT2BR', pullup_str=100,   parent=self)
        self.netlist['notRdy0'] = net.net('notRdy0',  charge_storage=True,  parent=self)
        self.netlist['notRnWprepad'] = net.net('notRnWprepad', pullup_str=100,   parent=self)
        self.netlist['notalu0'] = net.net('notalu0',  charge_storage=True,  parent=self)
        self.netlist['notalu1'] = net.net('notalu1',  charge_storage=True,  parent=self)
        self.netlist['notalu2'] = net.net('notalu2',  charge_storage=True,  parent=self)
        self.netlist['notalu3'] = net.net('notalu3',  charge_storage=True,  parent=self)
        self.netlist['notalu4'] = net.net('notalu4',  charge_storage=True,  parent=self)
        self.netlist['notalu5'] = net.net('notalu5',  charge_storage=True,  parent=self)
        self.netlist['notalu6'] = net.net('notalu6',  charge_storage=True,  parent=self)
        self.netlist['notalu7'] = net.net('notalu7',  charge_storage=True,  parent=self)
        self.netlist['notalucin'] = net.net('notalucin', pullup_str=100,   parent=self)
        self.netlist['notalucout'] = net.net('notalucout', pullup_str=100,   parent=self)
        self.netlist['notaluvout'] = net.net('notaluvout', pullup_str=100,   parent=self)
        self.netlist['notdor0'] = net.net('notdor0',  charge_storage=True,  parent=self)
        self.netlist['notdor1'] = net.net('notdor1',  charge_storage=True,  parent=self)
        self.netlist['notdor2'] = net.net('notdor2',  charge_storage=True,  parent=self)
        self.netlist['notdor3'] = net.net('notdor3',  charge_storage=True,  parent=self)
        self.netlist['notdor4'] = net.net('notdor4',  charge_storage=True,  parent=self)
        self.netlist['notdor5'] = net.net('notdor5',  charge_storage=True,  parent=self)
        self.netlist['notdor6'] = net.net('notdor6',  charge_storage=True,  parent=self)
        self.netlist['notdor7'] = net.net('notdor7',  charge_storage=True,  parent=self)
        self.netlist['notidl0'] = net.net('notidl0',  charge_storage=True,  parent=self)
        self.netlist['notidl1'] = net.net('notidl1',  charge_storage=True,  parent=self)
        self.netlist['notidl2'] = net.net('notidl2',  charge_storage=True,  parent=self)
        self.netlist['notidl3'] = net.net('notidl3',  charge_storage=True,  parent=self)
        self.netlist['notidl4'] = net.net('notidl4',  charge_storage=True,  parent=self)
        self.netlist['notidl5'] = net.net('notidl5',  charge_storage=True,  parent=self)
        self.netlist['notidl6'] = net.net('notidl6',  charge_storage=True,  parent=self)
        self.netlist['notidl7'] = net.net('notidl7',  charge_storage=True,  parent=self)
        self.netlist['notir0'] = net.net('notir0', pullup_str=100,   parent=self)
        self.netlist['notir1'] = net.net('notir1', pullup_str=100,   parent=self)
        self.netlist['notir2'] = net.net('notir2', pullup_str=100,   parent=self)
        self.netlist['notir3'] = net.net('notir3', pullup_str=100,   parent=self)
        self.netlist['notir4'] = net.net('notir4', pullup_str=100,   parent=self)
        self.netlist['notir5'] = net.net('notir5', pullup_str=100,   parent=self)
        self.netlist['notir6'] = net.net('notir6', pullup_str=100,   parent=self)
        self.netlist['notir7'] = net.net('notir7', pullup_str=100,   parent=self)
        self.netlist['nots0'] = net.net('nots0',  charge_storage=True,  parent=self)
        self.netlist['nots1'] = net.net('nots1',  charge_storage=True,  parent=self)
        self.netlist['nots2'] = net.net('nots2',  charge_storage=True,  parent=self)
        self.netlist['nots3'] = net.net('nots3',  charge_storage=True,  parent=self)
        self.netlist['nots4'] = net.net('nots4',  charge_storage=True,  parent=self)
        self.netlist['nots5'] = net.net('nots5',  charge_storage=True,  parent=self)
        self.netlist['nots6'] = net.net('nots6',  charge_storage=True,  parent=self)
        self.netlist['nots7'] = net.net('nots7',  charge_storage=True,  parent=self)
        self.netlist['notx0'] = net.net('notx0', pullup_str=100,   parent=self)
        self.netlist['notx1'] = net.net('notx1', pullup_str=100,   parent=self)
        self.netlist['notx2'] = net.net('notx2', pullup_str=100,   parent=self)
        self.netlist['notx3'] = net.net('notx3', pullup_str=100,   parent=self)
        self.netlist['notx4'] = net.net('notx4', pullup_str=100,   parent=self)
        self.netlist['notx5'] = net.net('notx5', pullup_str=100,   parent=self)
        self.netlist['notx6'] = net.net('notx6', pullup_str=100,   parent=self)
        self.netlist['notx7'] = net.net('notx7', pullup_str=100,   parent=self)
        self.netlist['noty0'] = net.net('noty0', pullup_str=100,   parent=self)
        self.netlist['noty1'] = net.net('noty1', pullup_str=100,   parent=self)
        self.netlist['noty2'] = net.net('noty2', pullup_str=100,   parent=self)
        self.netlist['noty3'] = net.net('noty3', pullup_str=100,   parent=self)
        self.netlist['noty4'] = net.net('noty4', pullup_str=100,   parent=self)
        self.netlist['noty5'] = net.net('noty5', pullup_str=100,   parent=self)
        self.netlist['noty6'] = net.net('noty6', pullup_str=100,   parent=self)
        self.netlist['noty7'] = net.net('noty7', pullup_str=100,   parent=self)
        self.netlist['p0'] = net.net('p0',  charge_storage=True,  parent=self)
        self.netlist['p1'] = net.net('p1',  charge_storage=True,  parent=self)
        self.netlist['p2'] = net.net('p2',  charge_storage=True,  parent=self)
        self.netlist['p3'] = net.net('p3',  charge_storage=True,  parent=self)
        self.netlist['pch0'] = net.net('pch0',  charge_storage=True,  parent=self)
        self.netlist['pch1'] = net.net('pch1',  charge_storage=True,  parent=self)
        self.netlist['pch2'] = net.net('pch2',  charge_storage=True,  parent=self)
        self.netlist['pch3'] = net.net('pch3',  charge_storage=True,  parent=self)
        self.netlist['pch4'] = net.net('pch4',  charge_storage=True,  parent=self)
        self.netlist['pch5'] = net.net('pch5',  charge_storage=True,  parent=self)
        self.netlist['pch6'] = net.net('pch6',  charge_storage=True,  parent=self)
        self.netlist['pch7'] = net.net('pch7',  charge_storage=True,  parent=self)
        self.netlist['pchp0'] = net.net('pchp0', pullup_str=100,   parent=self)
        self.netlist['pchp1'] = net.net('pchp1', pullup_str=100,   parent=self)
        self.netlist['pchp2'] = net.net('pchp2', pullup_str=100,   parent=self)
        self.netlist['pchp3'] = net.net('pchp3', pullup_str=100,   parent=self)
        self.netlist['pchp4'] = net.net('pchp4', pullup_str=100,   parent=self)
        self.netlist['pchp5'] = net.net('pchp5', pullup_str=100,   parent=self)
        self.netlist['pchp6'] = net.net('pchp6', pullup_str=100,   parent=self)
        self.netlist['pchp7'] = net.net('pchp7', pullup_str=100,   parent=self)
        self.netlist['pcl0'] = net.net('pcl0',  charge_storage=True,  parent=self)
        self.netlist['pcl1'] = net.net('pcl1',  charge_storage=True,  parent=self)
        self.netlist['pcl2'] = net.net('pcl2',  charge_storage=True,  parent=self)
        self.netlist['pcl3'] = net.net('pcl3',  charge_storage=True,  parent=self)
        self.netlist['pcl4'] = net.net('pcl4',  charge_storage=True,  parent=self)
        self.netlist['pcl5'] = net.net('pcl5',  charge_storage=True,  parent=self)
        self.netlist['pcl6'] = net.net('pcl6',  charge_storage=True,  parent=self)
        self.netlist['pcl7'] = net.net('pcl7',  charge_storage=True,  parent=self)
        self.netlist['pclp0'] = net.net('pclp0', pullup_str=100,   parent=self)
        self.netlist['pclp1'] = net.net('pclp1', pullup_str=100,   parent=self)
        self.netlist['pclp2'] = net.net('pclp2', pullup_str=100,   parent=self)
        self.netlist['pclp3'] = net.net('pclp3', pullup_str=100,   parent=self)
        self.netlist['pclp4'] = net.net('pclp4', pullup_str=100,   parent=self)
        self.netlist['pclp5'] = net.net('pclp5', pullup_str=100,   parent=self)
        self.netlist['pclp6'] = net.net('pclp6', pullup_str=100,   parent=self)
        self.netlist['pclp7'] = net.net('pclp7', pullup_str=100,   parent=self)
        self.netlist['pd0'] = net.net('pd0',  charge_storage=True,  parent=self)
        self.netlist['pd1'] = net.net('pd1',  charge_storage=True,  parent=self)
        self.netlist['pd2'] = net.net('pd2',  charge_storage=True,  parent=self)
        self.netlist['pd3'] = net.net('pd3',  charge_storage=True,  parent=self)
        self.netlist['pd4'] = net.net('pd4',  charge_storage=True,  parent=self)
        self.netlist['pd5'] = net.net('pd5',  charge_storage=True,  parent=self)
        self.netlist['pd6'] = net.net('pd6',  charge_storage=True,  parent=self)
        self.netlist['pd7'] = net.net('pd7',  charge_storage=True,  parent=self)
        self.netlist['pipeT2out'] = net.net('pipeT2out',  charge_storage=True,  parent=self)
        self.netlist['pipeT3out'] = net.net('pipeT3out',  charge_storage=True,  parent=self)
        self.netlist['pipeT4out'] = net.net('pipeT4out',  charge_storage=True,  parent=self)
        self.netlist['pipeT5out'] = net.net('pipeT5out',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK01'] = net.net('pipeUNK01',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK02'] = net.net('pipeUNK02',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK03'] = net.net('pipeUNK03',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK04'] = net.net('pipeUNK04',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK05'] = net.net('pipeUNK05',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK06'] = net.net('pipeUNK06',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK08'] = net.net('pipeUNK08',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK09'] = net.net('pipeUNK09',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK10'] = net.net('pipeUNK10',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK11'] = net.net('pipeUNK11',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK12'] = net.net('pipeUNK12',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK13'] = net.net('pipeUNK13',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK14'] = net.net('pipeUNK14',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK15'] = net.net('pipeUNK15',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK16'] = net.net('pipeUNK16',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK17'] = net.net('pipeUNK17',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK18'] = net.net('pipeUNK18',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK19'] = net.net('pipeUNK19',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK20'] = net.net('pipeUNK20',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK21'] = net.net('pipeUNK21',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK22'] = net.net('pipeUNK22',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK23'] = net.net('pipeUNK23',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK26'] = net.net('pipeUNK26',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK27'] = net.net('pipeUNK27',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK28'] = net.net('pipeUNK28',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK29'] = net.net('pipeUNK29',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK30'] = net.net('pipeUNK30',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK31'] = net.net('pipeUNK31',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK32'] = net.net('pipeUNK32',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK33'] = net.net('pipeUNK33',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK34'] = net.net('pipeUNK34',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK35'] = net.net('pipeUNK35',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK36'] = net.net('pipeUNK36',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK37'] = net.net('pipeUNK37',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK39'] = net.net('pipeUNK39',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK40'] = net.net('pipeUNK40',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK41'] = net.net('pipeUNK41',  charge_storage=True,  parent=self)
        self.netlist['pipeUNK42'] = net.net('pipeUNK42',  charge_storage=True,  parent=self)
        self.netlist['pipeVectorA0'] = net.net('pipeVectorA0',  charge_storage=True,  parent=self)
        self.netlist['pipeVectorA1'] = net.net('pipeVectorA1',  charge_storage=True,  parent=self)
        self.netlist['pipeVectorA2'] = net.net('pipeVectorA2',  charge_storage=True,  parent=self)
        self.netlist['pipedpc28'] = net.net('pipedpc28',  charge_storage=True,  parent=self)
        self.netlist['pipephi2Reset0'] = net.net('pipephi2Reset0',  charge_storage=True,  parent=self)
        self.netlist['pipephi2Reset0x'] = net.net('pipephi2Reset0x',  charge_storage=True,  parent=self)
        self.port['rdy'].netconn.pullup_str=100
        self.port['res'].netconn.charge_storage=True
        self.port['rw'].netconn.charge_storage=True
        self.netlist['s0'] = net.net('s0',  charge_storage=True,  parent=self)
        self.netlist['s1'] = net.net('s1',  charge_storage=True,  parent=self)
        self.netlist['s2'] = net.net('s2',  charge_storage=True,  parent=self)
        self.netlist['s3'] = net.net('s3',  charge_storage=True,  parent=self)
        self.netlist['s4'] = net.net('s4',  charge_storage=True,  parent=self)
        self.netlist['s5'] = net.net('s5',  charge_storage=True,  parent=self)
        self.netlist['s6'] = net.net('s6',  charge_storage=True,  parent=self)
        self.netlist['s7'] = net.net('s7',  charge_storage=True,  parent=self)
        self.netlist['sb1'] = net.net('sb1',  charge_storage=True,  parent=self)
        self.netlist['sb2'] = net.net('sb2',  charge_storage=True,  parent=self)
        self.netlist['sb3'] = net.net('sb3',  charge_storage=True,  parent=self)
        self.netlist['sb5'] = net.net('sb5',  charge_storage=True,  parent=self)
        self.netlist['sb6'] = net.net('sb6',  charge_storage=True,  parent=self)
        self.netlist['sb7'] = net.net('sb7',  charge_storage=True,  parent=self)
        self.port['so'].netconn.pullup_str=100
        self.port['sync'].netconn.charge_storage=True
        self.netlist['t2'] = net.net('t2', pullup_str=100,   parent=self)
        self.netlist['t3'] = net.net('t3', pullup_str=100,   parent=self)
        self.netlist['t4'] = net.net('t4', pullup_str=100,   parent=self)
        self.netlist['t5'] = net.net('t5', pullup_str=100,   parent=self)
        self.netlist['vcc'] = net.supply1('vcc')
        self.netlist['x0'] = net.net('x0',  charge_storage=True,  parent=self)
        self.netlist['x1'] = net.net('x1',  charge_storage=True,  parent=self)
        self.netlist['x2'] = net.net('x2',  charge_storage=True,  parent=self)
        self.netlist['x3'] = net.net('x3',  charge_storage=True,  parent=self)
        self.netlist['x4'] = net.net('x4',  charge_storage=True,  parent=self)
        self.netlist['x5'] = net.net('x5',  charge_storage=True,  parent=self)
        self.netlist['x6'] = net.net('x6',  charge_storage=True,  parent=self)
        self.netlist['x7'] = net.net('x7',  charge_storage=True,  parent=self)
        self.netlist['y0'] = net.net('y0',  charge_storage=True,  parent=self)
        self.netlist['y1'] = net.net('y1',  charge_storage=True,  parent=self)
        self.netlist['y2'] = net.net('y2',  charge_storage=True,  parent=self)
        self.netlist['y3'] = net.net('y3',  charge_storage=True,  parent=self)
        self.netlist['y4'] = net.net('y4',  charge_storage=True,  parent=self)
        self.netlist['y5'] = net.net('y5',  charge_storage=True,  parent=self)
        self.netlist['y6'] = net.net('y6',  charge_storage=True,  parent=self)
        self.netlist['y7'] = net.net('y7',  charge_storage=True,  parent=self)
        ## Component declarations
        self.gatelist.extend([
            NMOS("t3488", [self.netlist['n1111'],self.netlist['n941'],self.netlist['pipeUNK10']], isweak=False, parent=self),
            NMOS("t3489", [self.netlist['n250'],self.netlist['n155'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t3484", [self.netlist['n1716'],self.port['vss'].netconn,self.netlist['n218']], isweak=False, parent=self),
            NMOS("t3485", [self.netlist['n688'],self.netlist['n1594'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3486", [self.netlist['RESP'],self.port['vss'].netconn,self.netlist['n1395']], isweak=False, parent=self),
            NMOS("t3481", [self.netlist['n547'],self.netlist['n486'],self.netlist['n1571']], isweak=False, parent=self),
            NMOS("t3482", [self.port['vss'].netconn,self.netlist['n817'],self.netlist['n1571']], isweak=False, parent=self),
            NMOS("t776", [self.port['vss'].netconn,self.netlist['n528'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t777", [self.port['vss'].netconn,self.netlist['n309'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t774", [self.port['vss'].netconn,self.netlist['n1589'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t775", [self.port['vss'].netconn,self.netlist['n446'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t772", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t773", [self.port['vss'].netconn,self.netlist['n932'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t770", [self.port['vss'].netconn,self.netlist['n791'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t771", [self.port['vss'].netconn,self.netlist['n352'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t778", [self.port['vss'].netconn,self.netlist['n1430'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t779", [self.port['vss'].netconn,self.netlist['n1646'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t174", [self.netlist['n11'],self.port['vss'].netconn,self.netlist['n4']], isweak=False, parent=self),
            NMOS("t175", [self.port['vss'].netconn,self.netlist['n1380'],self.netlist['n819']], isweak=False, parent=self),
            NMOS("t2579", [self.port['vss'].netconn,self.netlist['n557'],self.netlist['n410']], isweak=False, parent=self),
            NMOS("t177", [self.port['vss'].netconn,self.netlist['n818'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t170", [self.netlist['n210'],self.netlist['n1513'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t171", [self.netlist['n1706'],self.netlist['n1500'],self.netlist['n379']], isweak=False, parent=self),
            NMOS("t172", [self.netlist['n1345'],self.port['vss'].netconn,self.netlist['n379']], isweak=False, parent=self),
            NMOS("t173", [self.netlist['n1508'],self.netlist['n1101'],self.netlist['n813']], isweak=False, parent=self),
            NMOS("t3008", [self.port['vss'].netconn,self.netlist['n1164'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3009", [self.port['vss'].netconn,self.netlist['n995'],self.netlist['n312']], isweak=False, parent=self),
            NMOS("t2571", [self.netlist['n431'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2570", [self.port['vcc'].netconn,self.netlist['dpc10_ADLADD'],self.netlist['n1541']], isweak=False, parent=self),
            NMOS("t2577", [self.netlist['n1511'],self.port['vss'].netconn,self.netlist['pipeUNK29']], isweak=False, parent=self),
            NMOS("t179", [self.netlist['n1130'],self.port['vss'].netconn,self.netlist['n1002']], isweak=False, parent=self),
            NMOS("t2574", [self.netlist['n1072'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1958", [self.netlist['n957'],self.netlist['n143'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t1959", [self.netlist['n1654'],self.port['vss'].netconn,self.netlist['n947']], isweak=False, parent=self),
            NMOS("t2683", [self.netlist['idb7'],self.netlist['alub7'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t2682", [self.netlist['n243'],self.port['vss'].netconn,self.netlist['idb1']], isweak=False, parent=self),
            NMOS("t2685", [self.port['vss'].netconn,self.netlist['n60'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2684", [self.netlist['idb6'],self.netlist['alub6'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t2687", [self.port['vss'].netconn,self.netlist['n271'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2686", [self.port['vss'].netconn,self.netlist['n84'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1950", [self.netlist['n877'],self.port['vss'].netconn,self.netlist['n933']], isweak=False, parent=self),
            NMOS("t1951", [self.netlist['n1406'],self.netlist['n1657'],self.netlist['n523']], isweak=False, parent=self),
            NMOS("t1952", [self.netlist['n1659'],self.netlist['n875'],self.netlist['n523']], isweak=False, parent=self),
            NMOS("t1953", [self.netlist['n743'],self.port['vss'].netconn,self.netlist['n523']], isweak=False, parent=self),
            NMOS("t615", [self.netlist['n1355'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1955", [self.port['vss'].netconn,self.netlist['n708'],self.netlist['n1230']], isweak=False, parent=self),
            NMOS("t1956", [self.netlist['dpc11_SBADD'],self.port['vcc'].netconn,self.netlist['n1230']], isweak=False, parent=self),
            NMOS("t1957", [self.netlist['n1398'],self.netlist['n304'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t2371", [self.netlist['n694'],self.netlist['adl1'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t2370", [self.netlist['sb7'],self.netlist['n1592'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t2373", [self.port['vss'].netconn,self.netlist['pchp0'],self.netlist['n780']], isweak=False, parent=self),
            NMOS("t2372", [self.netlist['n642'],self.netlist['n707'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2375", [self.port['vss'].netconn,self.netlist['n1512'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2374", [self.netlist['dpc34_PCLC'],self.port['vss'].netconn,self.netlist['n379']], isweak=False, parent=self),
            NMOS("t2377", [self.port['vss'].netconn,self.netlist['n1173'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2376", [self.netlist['n382'],self.port['vss'].netconn,self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2379", [self.port['vss'].netconn,self.netlist['n76'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2378", [self.port['vss'].netconn,self.netlist['n1543'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t3178", [self.netlist['pclp0'],self.netlist['pcl0'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t3179", [self.netlist['pclp3'],self.netlist['pcl3'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t3174", [self.netlist['pclp4'],self.netlist['pcl4'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t3175", [self.netlist['pclp7'],self.netlist['pcl7'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t3176", [self.netlist['pclp6'],self.netlist['pcl6'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t3177", [self.netlist['pclp1'],self.netlist['pcl1'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t3170", [self.port['vss'].netconn,self.netlist['n623'],self.netlist['n143']], isweak=False, parent=self),
            NMOS("t3171", [self.port['vss'].netconn,self.netlist['n1347'],self.netlist['n782']], isweak=False, parent=self),
            NMOS("t3172", [self.port['vss'].netconn,self.netlist['n934'],self.netlist['n366']], isweak=False, parent=self),
            NMOS("t3173", [self.netlist['pclp5'],self.netlist['pcl5'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t1317", [self.netlist['n1650'],self.port['vss'].netconn,self.port['so'].netconn], isweak=False, parent=self),
            NMOS("t505", [self.netlist['n572'],self.port['vss'].netconn,self.netlist['pipeUNK21']], isweak=False, parent=self),
            NMOS("t504", [self.port['vss'].netconn,self.netlist['n1092'],self.netlist['n118']], isweak=False, parent=self),
            NMOS("t507", [self.port['vss'].netconn,self.port['ab0'].netconn,self.netlist['n1100']], isweak=False, parent=self),
            NMOS("t506", [self.port['vss'].netconn,self.netlist['n61'],self.netlist['sb6']], isweak=False, parent=self),
            NMOS("t501", [self.netlist['n634'],self.port['vss'].netconn,self.netlist['n1676']], isweak=False, parent=self),
            NMOS("t500", [self.port['vss'].netconn,self.netlist['n1347'],self.netlist['n1396']], isweak=False, parent=self),
            NMOS("t503", [self.netlist['n310'],self.netlist['notir0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t502", [self.port['vcc'].netconn,self.netlist['n86'],self.netlist['n1676']], isweak=False, parent=self),
            NMOS("t2645", [self.netlist['idl3'],self.port['vss'].netconn,self.netlist['notidl3']], isweak=False, parent=self),
            NMOS("t2199", [self.netlist['sb2'],self.netlist['adh2'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t2198", [self.netlist['sb3'],self.netlist['adh3'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t1339", [self.netlist['n964'],self.port['vss'].netconn,self.netlist['n1533']], isweak=False, parent=self),
            NMOS("t2195", [self.netlist['n1247'],self.port['vss'].netconn,self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2194", [self.port['vss'].netconn,self.netlist['n38'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2197", [self.netlist['dasb4'],self.netlist['adh4'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t2196", [self.port['vss'].netconn,self.netlist['n882'],self.netlist['n1252']], isweak=False, parent=self),
            NMOS("t2191", [self.netlist['adh6'],self.netlist['sb6'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t2190", [self.netlist['sb7'],self.netlist['adh7'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t2193", [self.netlist['dasb0'],self.netlist['adh0'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t2192", [self.netlist['dasb0'],self.netlist['y0'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t2753", [self.netlist['n1110'],self.netlist['pipeUNK01'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2752", [self.netlist['dpc30_ADHPCH'],self.port['vcc'].netconn,self.netlist['n21']], isweak=False, parent=self),
            NMOS("t2751", [self.port['vss'].netconn,self.netlist['n228'],self.netlist['n21']], isweak=False, parent=self),
            NMOS("t2750", [self.port['vss'].netconn,self.netlist['DC78'],self.netlist['n1201']], isweak=False, parent=self),
            NMOS("t2209", [self.port['vss'].netconn,self.netlist['dpc20_ADDSB06'],self.netlist['n75']], isweak=False, parent=self),
            NMOS("t2208", [self.netlist['n102'],self.port['vcc'].netconn,self.netlist['n834']], isweak=False, parent=self),
            NMOS("t2979", [self.netlist['n1086'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2978", [self.port['vss'].netconn,self.netlist['n1721'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2205", [self.netlist['n1072'],self.port['vss'].netconn,self.netlist['dor0']], isweak=False, parent=self),
            NMOS("t2204", [self.port['vss'].netconn,self.netlist['noty6'],self.netlist['y6']], isweak=False, parent=self),
            NMOS("t2759", [self.port['vss'].netconn,self.netlist['n783'],self.netlist['pcl2']], isweak=False, parent=self),
            NMOS("t2206", [self.netlist['n769'],self.port['vss'].netconn,self.netlist['dor0']], isweak=False, parent=self),
            NMOS("t2201", [self.netlist['n762'],self.port['vss'].netconn,self.netlist['n761']], isweak=False, parent=self),
            NMOS("t2200", [self.netlist['n970'],self.netlist['n233'],self.netlist['n761']], isweak=False, parent=self),
            NMOS("t2203", [self.netlist['n1293'],self.port['vss'].netconn,self.netlist['n840']], isweak=False, parent=self),
            NMOS("t2970", [self.port['vss'].netconn,self.netlist['n1337'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3000", [self.port['vss'].netconn,self.netlist['n1646'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t969", [self.port['vss'].netconn,self.netlist['n388'],self.netlist['n623']], isweak=False, parent=self),
            NMOS("t1408", [self.netlist['n694'],self.port['vss'].netconn,self.netlist['nots1']], isweak=False, parent=self),
            NMOS("t1409", [self.netlist['n849'],self.port['vss'].netconn,self.netlist['n321']], isweak=False, parent=self),
            NMOS("t1406", [self.port['vss'].netconn,self.netlist['n604'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1407", [self.netlist['n599'],self.netlist['n533'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1404", [self.netlist['n998'],self.port['vss'].netconn,self.netlist['nots3']], isweak=False, parent=self),
            NMOS("t1405", [self.port['vss'].netconn,self.netlist['n1145'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1402", [self.netlist['notir7'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t176", [self.port['vcc'].netconn,self.netlist['dpc19_ADDSB7'],self.netlist['n714']], isweak=False, parent=self),
            NMOS("t1400", [self.netlist['n93'],self.port['vss'].netconn,self.port['db0'].netconn], isweak=False, parent=self),
            NMOS("t1401", [self.port['vss'].netconn,self.netlist['n419'],self.netlist['a2']], isweak=False, parent=self),
            NMOS("t2995", [self.netlist['n446'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1239", [self.port['vss'].netconn,self.netlist['n324'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t2997", [self.netlist['n309'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2578", [self.netlist['n814'],self.netlist['n344'],self.netlist['n410']], isweak=False, parent=self),
            NMOS("t2991", [self.port['vss'].netconn,self.netlist['n352'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2990", [self.port['vss'].netconn,self.netlist['n791'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2993", [self.port['vss'].netconn,self.netlist['n932'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1995", [self.netlist['n1422'],self.port['vss'].netconn,self.netlist['pipeUNK09']], isweak=False, parent=self),
            NMOS("t3004", [self.netlist['n1569'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2999", [self.port['vss'].netconn,self.netlist['n1292'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2998", [self.port['vss'].netconn,self.netlist['n1430'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3005", [self.netlist['n950'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1082", [self.netlist['alua6'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t1083", [self.netlist['alua5'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t1080", [self.netlist['alua1'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t1081", [self.netlist['alua4'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t1086", [self.port['vss'].netconn,self.netlist['n105'],self.netlist['notalucin']], isweak=False, parent=self),
            NMOS("t3006", [self.port['vss'].netconn,self.netlist['n1050'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1084", [self.netlist['n510'],self.port['vss'].netconn,self.netlist['n1052']], isweak=False, parent=self),
            NMOS("t1085", [self.netlist['n134'],self.port['vss'].netconn,self.netlist['n1052']], isweak=False, parent=self),
            NMOS("t1990", [self.netlist['n298'],self.port['vss'].netconn,self.netlist['n23']], isweak=False, parent=self),
            NMOS("t1088", [self.port['db2'].netconn,self.port['db2'].netconn,self.netlist['n37']], isweak=False, parent=self),
            NMOS("t1089", [self.port['vss'].netconn,self.port['db2'].netconn,self.netlist['n37']], isweak=False, parent=self),
            NMOS("t707", [self.netlist['n262'],self.netlist['n1189'],self.netlist['n1714']], isweak=False, parent=self),
            NMOS("t1335", [self.port['vcc'].netconn,self.netlist['n210'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t981", [self.port['vss'].netconn,self.netlist['n1347'],self.netlist['n979']], isweak=False, parent=self),
            NMOS("t980", [self.netlist['n1106'],self.netlist['n1103'],self.netlist['n258']], isweak=False, parent=self),
            NMOS("t983", [self.netlist['n1671'],self.port['vss'].netconn,self.netlist['pd2']], isweak=False, parent=self),
            NMOS("t982", [self.netlist['n1464'],self.port['vss'].netconn,self.netlist['n370']], isweak=False, parent=self),
            NMOS("t985", [self.netlist['n434'],self.port['vss'].netconn,self.netlist['n790']], isweak=False, parent=self),
            NMOS("t1992", [self.port['vss'].netconn,self.netlist['n1093'],self.netlist['n968']], isweak=False, parent=self),
            NMOS("t1314", [self.port['vss'].netconn,self.netlist['n939'],self.netlist['n647']], isweak=False, parent=self),
            NMOS("t1315", [self.netlist['n138'],self.netlist['n825'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t989", [self.netlist['pclp0'],self.netlist['idb0'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t988", [self.port['vss'].netconn,self.netlist['n320'],self.netlist['sb1']], isweak=False, parent=self),
            NMOS("t1318", [self.port['vss'].netconn,self.netlist['n1270'],self.netlist['n509']], isweak=False, parent=self),
            NMOS("t1319", [self.netlist['n390'],self.port['vss'].netconn,self.netlist['n653']], isweak=False, parent=self),
            NMOS("t1046", [self.netlist['pchp2'],self.port['vss'].netconn,self.netlist['n114']], isweak=False, parent=self),
            NMOS("t3002", [self.port['vss'].netconn,self.netlist['n1476'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t178", [self.netlist['n1107'],self.port['vss'].netconn,self.netlist['n1520']], isweak=False, parent=self),
            NMOS("t1512", [self.netlist['n313'],self.netlist['n350'],self.netlist['alub3']], isweak=False, parent=self),
            NMOS("t2576", [self.port['vss'].netconn,self.netlist['n1189'],self.netlist['pipeUNK29']], isweak=False, parent=self),
            NMOS("t1538", [self.port['vss'].netconn,self.netlist['n253'],self.netlist['pipeUNK42']], isweak=False, parent=self),
            NMOS("t1513", [self.port['vss'].netconn,self.netlist['n649'],self.netlist['alub3']], isweak=False, parent=self),
            NMOS("t1532", [self.netlist['dpc7_SS'],self.port['vss'].netconn,self.netlist['n71']], isweak=False, parent=self),
            NMOS("t1042", [self.port['vss'].netconn,self.netlist['n279'],self.netlist['n954']], isweak=False, parent=self),
            NMOS("t1530", [self.netlist['dasb5'],self.port['vss'].netconn,self.netlist['n1629']], isweak=False, parent=self),
            NMOS("t1531", [self.netlist['abl2'],self.port['vss'].netconn,self.netlist['n707']], isweak=False, parent=self),
            NMOS("t1536", [self.port['db2'].netconn,self.port['vcc'].netconn,self.netlist['n520']], isweak=False, parent=self),
            NMOS("t1534", [self.port['vss'].netconn,self.netlist['n1719'],self.netlist['a5']], isweak=False, parent=self),
            NMOS("t1535", [self.port['vss'].netconn,self.netlist['n1717'],self.netlist['n60']], isweak=False, parent=self),
            NMOS("t1516", [self.port['vcc'].netconn,self.netlist['n826'],self.netlist['abh0']], isweak=False, parent=self),
            NMOS("t705", [self.netlist['notalu5'],self.netlist['n277'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1041", [self.netlist['n514'],self.netlist['n494'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3419", [self.port['vss'].netconn,self.netlist['n811'],self.netlist['alucout']], isweak=False, parent=self),
            NMOS("t1693", [self.netlist['n1662'],self.port['vss'].netconn,self.netlist['n1124']], isweak=False, parent=self),
            NMOS("t3418", [self.netlist['n610'],self.netlist['n696'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1160", [self.netlist['n624'],self.netlist['alub0'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t1163", [self.netlist['n924'],self.netlist['n1425'],self.netlist['C23']], isweak=False, parent=self),
            NMOS("t1162", [self.port['vss'].netconn,self.netlist['n1003'],self.netlist['C23']], isweak=False, parent=self),
            NMOS("t1165", [self.netlist['n458'],self.netlist['alub2'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t1164", [self.netlist['n478'],self.netlist['alub4'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t1626", [self.netlist['n1588'],self.port['vss'].netconn,self.port['db5'].netconn], isweak=False, parent=self),
            NMOS("t1627", [self.netlist['n1417'],self.port['vss'].netconn,self.netlist['n747']], isweak=False, parent=self),
            NMOS("t1624", [self.netlist['notalu1'],self.netlist['n250'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1625", [self.netlist['n864'],self.netlist['n825'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t1622", [self.port['vss'].netconn,self.netlist['n1347'],self.netlist['n550']], isweak=False, parent=self),
            NMOS("t1623", [self.netlist['n816'],self.netlist['n1137'],self.netlist['n790']], isweak=False, parent=self),
            NMOS("t1620", [self.netlist['n132'],self.netlist['pipeUNK26'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1621", [self.netlist['n1307'],self.netlist['n1254'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1694", [self.netlist['n1401'],self.port['vss'].netconn,self.netlist['n1269']], isweak=False, parent=self),
            NMOS("t1628", [self.netlist['n1309'],self.port['vss'].netconn,self.netlist['n1460']], isweak=False, parent=self),
            NMOS("t1629", [self.port['vss'].netconn,self.netlist['n201'],self.netlist['n1174']], isweak=False, parent=self),
            NMOS("t3096", [self.netlist['n1430'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t839", [self.netlist['n446'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t3506", [self.netlist['n586'],self.port['vss'].netconn,self.netlist['n1619']], isweak=False, parent=self),
            NMOS("t189", [self.port['vss'].netconn,self.netlist['aluvout'],self.netlist['n408']], isweak=False, parent=self),
            NMOS("t188", [self.port['vss'].netconn,self.netlist['n169'],self.netlist['n1624']], isweak=False, parent=self),
            NMOS("t181", [self.netlist['n101'],self.netlist['n1141'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t180", [self.netlist['n805'],self.netlist['n779'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t183", [self.netlist['n379'],self.netlist['n1480'],self.netlist['n1581']], isweak=False, parent=self),
            NMOS("t182", [self.netlist['notaluvout'],self.netlist['n408'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t185", [self.port['vss'].netconn,self.netlist['idl6'],self.netlist['notidl6']], isweak=False, parent=self),
            NMOS("t184", [self.netlist['n191'],self.port['vss'].netconn,self.netlist['n347']], isweak=False, parent=self),
            NMOS("t1197", [self.netlist['n944'],self.netlist['pipeUNK37'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2572", [self.port['ab15'].netconn,self.port['vcc'].netconn,self.netlist['n1639']], isweak=False, parent=self),
            NMOS("t349", [self.netlist['notir0'],self.port['vss'].netconn,self.netlist['ir0']], isweak=False, parent=self),
            NMOS("t348", [self.port['vss'].netconn,self.netlist['n1133'],self.netlist['ir0']], isweak=False, parent=self),
            NMOS("t347", [self.netlist['n980'],self.port['vss'].netconn,self.netlist['n1381']], isweak=False, parent=self),
            NMOS("t346", [self.port['vss'].netconn,self.netlist['n80'],self.netlist['n1130']], isweak=False, parent=self),
            NMOS("t345", [self.port['vcc'].netconn,self.netlist['dpc26_ACDB'],self.netlist['n525']], isweak=False, parent=self),
            NMOS("t344", [self.port['vss'].netconn,self.netlist['n800'],self.netlist['n525']], isweak=False, parent=self),
            NMOS("t2258", [self.port['vss'].netconn,self.netlist['n937'],self.netlist['pcl0']], isweak=False, parent=self),
            NMOS("t342", [self.netlist['n1055'],self.port['vss'].netconn,self.netlist['n1708']], isweak=False, parent=self),
            NMOS("t341", [self.netlist['n1000'],self.port['vss'].netconn,self.netlist['n575']], isweak=False, parent=self),
            NMOS("t340", [self.port['vss'].netconn,self.netlist['n861'],self.netlist['n1452']], isweak=False, parent=self),
            NMOS("t2681", [self.netlist['n947'],self.port['vss'].netconn,self.netlist['a3']], isweak=False, parent=self),
            NMOS("t1810", [self.port['vss'].netconn,self.netlist['n1204'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1816", [self.port['vss'].netconn,self.netlist['n285'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t3361", [self.netlist['n1307'],self.netlist['n524'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t3360", [self.port['vss'].netconn,self.netlist['n886'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3363", [self.netlist['n364'],self.netlist['n738'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t3362", [self.netlist['n28'],self.netlist['n577'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t3365", [self.port['vss'].netconn,self.netlist['n1094'],self.netlist['adl5']], isweak=False, parent=self),
            NMOS("t3364", [self.netlist['n1513'],self.netlist['n463'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t3367", [self.port['vss'].netconn,self.netlist['n261'],self.netlist['n461']], isweak=False, parent=self),
            NMOS("t3366", [self.netlist['n1712'],self.port['vss'].netconn,self.netlist['n264']], isweak=False, parent=self),
            NMOS("t3369", [self.netlist['clearIR'],self.netlist['n380'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t3368", [self.port['vss'].netconn,self.netlist['n726'],self.netlist['n461']], isweak=False, parent=self),
            NMOS("t613", [self.port['vss'].netconn,self.netlist['n1273'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t612", [self.port['vss'].netconn,self.netlist['n403'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1954", [self.netlist['n513'],self.port['vss'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t614", [self.netlist['n1337'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t72", [self.netlist['sb6'],self.netlist['y6'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t73", [self.netlist['n785'],self.netlist['n920'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t70", [self.netlist['n1622'],self.port['vss'].netconn,self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t1427", [self.port['vss'].netconn,self.netlist['n1259'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t76", [self.port['vcc'].netconn,self.port['clk2out'].netconn,self.netlist['n127']], isweak=False, parent=self),
            NMOS("t77", [self.netlist['dasb4'],self.netlist['y4'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t74", [self.port['vss'].netconn,self.netlist['n748'],self.netlist['n1318']], isweak=False, parent=self),
            NMOS("t75", [self.port['vcc'].netconn,self.netlist['n304'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t78", [self.netlist['n790'],self.port['vss'].netconn,self.netlist['n53']], isweak=False, parent=self),
            NMOS("t79", [self.netlist['dpc8_nDBADD'],self.port['vss'].netconn,self.netlist['n763']], isweak=False, parent=self),
            NMOS("t761", [self.port['vss'].netconn,self.netlist['n487'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2565", [self.port['vss'].netconn,self.netlist['n1254'],self.netlist['abl6']], isweak=False, parent=self),
            NMOS("t2566", [self.port['vss'].netconn,self.netlist['n1195'],self.netlist['abl6']], isweak=False, parent=self),
            NMOS("t2567", [self.netlist['n1191'],self.port['vcc'].netconn,self.netlist['abl6']], isweak=False, parent=self),
            NMOS("t2560", [self.port['vcc'].netconn,self.port['ab3'].netconn,self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t764", [self.port['vss'].netconn,self.netlist['n1478'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t767", [self.port['vss'].netconn,self.netlist['n1557'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t766", [self.port['vss'].netconn,self.netlist['n1210'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t769", [self.port['vss'].netconn,self.netlist['n1052'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t768", [self.port['vss'].netconn,self.netlist['n259'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2568", [self.port['vss'].netconn,self.netlist['n300'],self.netlist['n389']], isweak=False, parent=self),
            NMOS("t2569", [self.netlist['n491'],self.port['vss'].netconn,self.netlist['n1541']], isweak=False, parent=self),
            NMOS("t167", [self.netlist['n373'],self.port['vcc'].netconn,self.netlist['dor5']], isweak=False, parent=self),
            NMOS("t166", [self.port['ab11'].netconn,self.port['vcc'].netconn,self.netlist['n1296']], isweak=False, parent=self),
            NMOS("t165", [self.netlist['n739'],self.netlist['n711'],self.netlist['n761']], isweak=False, parent=self),
            NMOS("t164", [self.port['vss'].netconn,self.netlist['n914'],self.netlist['n715']], isweak=False, parent=self),
            NMOS("t163", [self.port['vss'].netconn,self.netlist['n426'],self.netlist['n715']], isweak=False, parent=self),
            NMOS("t162", [self.port['vss'].netconn,self.netlist['n952'],self.netlist['n272']], isweak=False, parent=self),
            NMOS("t161", [self.port['vss'].netconn,self.netlist['n1366'],self.netlist['pipeT3out']], isweak=False, parent=self),
            NMOS("t160", [self.netlist['n70'],self.port['vss'].netconn,self.netlist['n1134']], isweak=False, parent=self),
            NMOS("t2893", [self.netlist['n1035'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t169", [self.netlist['n812'],self.port['vss'].netconn,self.netlist['n646']], isweak=False, parent=self),
            NMOS("t168", [self.netlist['n264'],self.port['vss'].netconn,self.netlist['n1312']], isweak=False, parent=self),
            NMOS("t2270", [self.port['vcc'].netconn,self.netlist['idb5'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t7", [self.port['clk0'].netconn,self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t1", [self.port['ab13'].netconn,self.port['vcc'].netconn,self.netlist['n1608']], isweak=False, parent=self),
            NMOS("t2273", [self.port['vss'].netconn,self.netlist['n1716'],self.netlist['n660']], isweak=False, parent=self),
            NMOS("t2274", [self.port['vss'].netconn,self.netlist['n1708'],self.netlist['n660']], isweak=False, parent=self),
            NMOS("t2275", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n594']], isweak=False, parent=self),
            NMOS("t2692", [self.port['vss'].netconn,self.netlist['n804'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2693", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2690", [self.port['vss'].netconn,self.netlist['n784'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2691", [self.port['vss'].netconn,self.netlist['n204'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2696", [self.port['vss'].netconn,self.netlist['n1204'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t0", [self.netlist['n217'],self.port['vss'].netconn,self.netlist['pipeVectorA0']], isweak=False, parent=self),
            NMOS("t2694", [self.port['vss'].netconn,self.netlist['n1428'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2695", [self.port['vss'].netconn,self.netlist['n492'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2698", [self.port['vss'].netconn,self.netlist['n342'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2699", [self.port['vss'].netconn,self.netlist['n857'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2246", [self.port['vss'].netconn,self.netlist['n795'],self.netlist['n1649']], isweak=False, parent=self),
            NMOS("t2366", [self.netlist['n1654'],self.netlist['sb3'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t2367", [self.netlist['n1344'],self.netlist['dasb4'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t2364", [self.netlist['n929'],self.netlist['sb1'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t2365", [self.netlist['sb2'],self.netlist['n1618'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t2368", [self.netlist['n831'],self.netlist['sb5'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t1909", [self.netlist['n1614'],self.port['vss'].netconn,self.netlist['pipeUNK03']], isweak=False, parent=self),
            NMOS("t3109", [self.port['vss'].netconn,self.netlist['n1294'],self.netlist['n540']], isweak=False, parent=self),
            NMOS("t3108", [self.netlist['n365'],self.port['vss'].netconn,self.netlist['n540']], isweak=False, parent=self),
            NMOS("t3101", [self.netlist['n1164'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3100", [self.netlist['n1226'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3103", [self.port['vss'].netconn,self.port['ab6'].netconn,self.netlist['n1254']], isweak=False, parent=self),
            NMOS("t3102", [self.port['vss'].netconn,self.netlist['n1497'],self.netlist['pipeUNK41']], isweak=False, parent=self),
            NMOS("t3107", [self.port['vss'].netconn,self.netlist['n302'],self.netlist['n540']], isweak=False, parent=self),
            NMOS("t3070", [self.netlist['n1664'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t2078", [self.netlist['n1134'],self.port['vss'].netconn,self.netlist['VEC1']], isweak=False, parent=self),
            NMOS("t1908", [self.port['vss'].netconn,self.netlist['n1723'],self.netlist['pipeUNK03']], isweak=False, parent=self),
            NMOS("t3072", [self.netlist['n665'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t570", [self.netlist['dpc17_SUMS'],self.port['vcc'].netconn,self.netlist['n772']], isweak=False, parent=self),
            NMOS("t571", [self.netlist['n496'],self.port['vss'].netconn,self.netlist['s5']], isweak=False, parent=self),
            NMOS("t572", [self.port['vss'].netconn,self.netlist['pclp2'],self.netlist['n1079']], isweak=False, parent=self),
            NMOS("t573", [self.port['vss'].netconn,self.netlist['dpc23_SBAC'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t574", [self.port['vss'].netconn,self.netlist['n625'],self.netlist['n459']], isweak=False, parent=self),
            NMOS("t575", [self.port['vss'].netconn,self.netlist['n830'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t576", [self.port['vss'].netconn,self.port['irq'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t577", [self.netlist['n580'],self.netlist['n566'],self.netlist['n755']], isweak=False, parent=self),
            NMOS("t578", [self.port['vcc'].netconn,self.netlist['n520'],self.netlist['dor2']], isweak=False, parent=self),
            NMOS("t579", [self.netlist['n17'],self.port['vss'].netconn,self.netlist['n732']], isweak=False, parent=self),
            NMOS("t1768", [self.port['vss'].netconn,self.netlist['n269'],self.netlist['AxB7']], isweak=False, parent=self),
            NMOS("t2075", [self.port['vss'].netconn,self.netlist['n1315'],self.netlist['abh0']], isweak=False, parent=self),
            NMOS("t3001", [self.port['vss'].netconn,self.netlist['n1114'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2188", [self.netlist['n1547'],self.port['vss'].netconn,self.netlist['n743']], isweak=False, parent=self),
            NMOS("t2189", [self.netlist['n1694'],self.port['vss'].netconn,self.netlist['notx2']], isweak=False, parent=self),
            NMOS("t2186", [self.netlist['n875'],self.port['vss'].netconn,self.netlist['n743']], isweak=False, parent=self),
            NMOS("t2187", [self.netlist['n609'],self.netlist['n545'],self.netlist['n743']], isweak=False, parent=self),
            NMOS("t2184", [self.port['vss'].netconn,self.netlist['n1194'],self.netlist['p3']], isweak=False, parent=self),
            NMOS("t2185", [self.port['vss'].netconn,self.netlist['n988'],self.netlist['n350']], isweak=False, parent=self),
            NMOS("t2182", [self.port['vss'].netconn,self.netlist['n620'],self.netlist['n1293']], isweak=False, parent=self),
            NMOS("t2183", [self.port['vss'].netconn,self.netlist['n1122'],self.netlist['n936']], isweak=False, parent=self),
            NMOS("t2180", [self.port['vss'].netconn,self.netlist['n321'],self.netlist['n398']], isweak=False, parent=self),
            NMOS("t2181", [self.port['vss'].netconn,self.netlist['n692'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t2968", [self.port['vss'].netconn,self.netlist['n857'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2969", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2748", [self.netlist['VEC1'],self.port['vss'].netconn,self.netlist['n698']], isweak=False, parent=self),
            NMOS("t2749", [self.port['vss'].netconn,self.netlist['n1371'],self.netlist['n846']], isweak=False, parent=self),
            NMOS("t2218", [self.netlist['n722'],self.netlist['n336'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2219", [self.netlist['n1318'],self.netlist['n304'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2216", [self.netlist['n296'],self.netlist['n1063'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2745", [self.netlist['idb3'],self.netlist['pclp3'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t2746", [self.netlist['idb1'],self.netlist['pclp1'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t2215", [self.netlist['n1071'],self.netlist['n350'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2212", [self.netlist['n957'],self.netlist['n1628'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2213", [self.netlist['n250'],self.netlist['n841'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2742", [self.netlist['n387'],self.port['vss'].netconn,self.netlist['n853']], isweak=False, parent=self),
            NMOS("t2743", [self.port['vss'].netconn,self.netlist['n670'],self.netlist['n519']], isweak=False, parent=self),
            NMOS("t889", [self.netlist['n347'],self.port['vss'].netconn,self.netlist['n1385']], isweak=False, parent=self),
            NMOS("t1439", [self.port['vss'].netconn,self.netlist['n1524'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1438", [self.port['vss'].netconn,self.netlist['n145'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1433", [self.port['vss'].netconn,self.netlist['n822'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t881", [self.port['vss'].netconn,self.netlist['pchp4'],self.netlist['n820']], isweak=False, parent=self),
            NMOS("t882", [self.port['vss'].netconn,self.netlist['n917'],self.netlist['n383']], isweak=False, parent=self),
            NMOS("t883", [self.netlist['n386'],self.port['vss'].netconn,self.netlist['pcl5']], isweak=False, parent=self),
            NMOS("t884", [self.port['vss'].netconn,self.netlist['n1649'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1436", [self.netlist['n1504'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1435", [self.netlist['n1342'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t887", [self.netlist['n147'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t2986", [self.port['vss'].netconn,self.netlist['n660'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2987", [self.netlist['n1557'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2984", [self.port['vss'].netconn,self.netlist['n1478'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2985", [self.port['vss'].netconn,self.netlist['n594'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2982", [self.port['vss'].netconn,self.netlist['n1239'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2983", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2980", [self.netlist['n487'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2981", [self.netlist['n579'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2988", [self.netlist['n259'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2989", [self.netlist['n1052'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3003", [self.netlist['n1226'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t408", [self.port['vss'].netconn,self.netlist['n807'],self.netlist['n330']], isweak=False, parent=self),
            NMOS("t409", [self.netlist['n1716'],self.port['vss'].netconn,self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t404", [self.netlist['n1281'],self.port['vss'].netconn,self.port['db3'].netconn], isweak=False, parent=self),
            NMOS("t405", [self.netlist['C56'],self.port['vss'].netconn,self.netlist['n427']], isweak=False, parent=self),
            NMOS("t406", [self.netlist['C67'],self.netlist['n112'],self.netlist['n427']], isweak=False, parent=self),
            NMOS("t407", [self.netlist['n462'],self.netlist['n878'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t401", [self.netlist['n1463'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t402", [self.netlist['n845'],self.netlist['p2'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t403", [self.port['vss'].netconn,self.netlist['n1358'],self.netlist['n1109']], isweak=False, parent=self),
            NMOS("t1983", [self.netlist['dpc21_ADDADL'],self.port['vss'].netconn,self.netlist['n1033']], isweak=False, parent=self),
            NMOS("t1982", [self.port['vss'].netconn,self.netlist['n457'],self.netlist['idb3']], isweak=False, parent=self),
            NMOS("t1981", [self.netlist['n819'],self.port['vss'].netconn,self.netlist['pipephi2Reset0']], isweak=False, parent=self),
            NMOS("t1980", [self.port['vss'].netconn,self.netlist['n212'],self.netlist['adh4']], isweak=False, parent=self),
            NMOS("t1987", [self.netlist['n1069'],self.port['vss'].netconn,self.netlist['n1274']], isweak=False, parent=self),
            NMOS("t1986", [self.netlist['n55'],self.netlist['n11'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1985", [self.netlist['sb3'],self.netlist['y3'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t1984", [self.netlist['adl7'],self.netlist['pcl7'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t974", [self.netlist['abl0'],self.port['vss'].netconn,self.netlist['n153']], isweak=False, parent=self),
            NMOS("t975", [self.port['vss'].netconn,self.netlist['n1352'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t976", [self.port['vss'].netconn,self.netlist['n104'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t1988", [self.netlist['n1274'],self.netlist['n913'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1323", [self.port['vss'].netconn,self.netlist['n1560'],self.netlist['n1055']], isweak=False, parent=self),
            NMOS("t1322", [self.netlist['n9'],self.port['vcc'].netconn,self.netlist['n866']], isweak=False, parent=self),
            NMOS("t1321", [self.port['vss'].netconn,self.netlist['n1365'],self.netlist['n862']], isweak=False, parent=self),
            NMOS("t1320", [self.netlist['n1455'],self.port['vss'].netconn,self.netlist['n179']], isweak=False, parent=self),
            NMOS("t1507", [self.netlist['a0'],self.netlist['n146'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1506", [self.port['vss'].netconn,self.netlist['n467'],self.netlist['n470']], isweak=False, parent=self),
            NMOS("t1505", [self.netlist['sb2'],self.netlist['n1491'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t1504", [self.netlist['n570'],self.port['vss'].netconn,self.netlist['n647']], isweak=False, parent=self),
            NMOS("t1051", [self.netlist['n153'],self.netlist['n246'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t1050", [self.netlist['n1196'],self.port['vss'].netconn,self.netlist['n522']], isweak=False, parent=self),
            NMOS("t1053", [self.port['vss'].netconn,self.netlist['n1601'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1052", [self.netlist['n790'],self.port['vss'].netconn,self.netlist['n691']], isweak=False, parent=self),
            NMOS("t1059", [self.port['vss'].netconn,self.netlist['n303'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1058", [self.port['vss'].netconn,self.netlist['n1381'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1509", [self.port['vss'].netconn,self.netlist['n513'],self.netlist['n885']], isweak=False, parent=self),
            NMOS("t1508", [self.netlist['n1531'],self.netlist['sb3'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t3322", [self.netlist['n1441'],self.port['vss'].netconn,self.netlist['n1277']], isweak=False, parent=self),
            NMOS("t1255", [self.port['vss'].netconn,self.netlist['n1196'],self.netlist['n1228']], isweak=False, parent=self),
            NMOS("t2299", [self.netlist['n1381'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t836", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t1189", [self.netlist['n1227'],self.port['vss'].netconn,self.netlist['n526']], isweak=False, parent=self),
            NMOS("t1188", [self.netlist['n284'],self.port['vss'].netconn,self.netlist['n1392']], isweak=False, parent=self),
            NMOS("t1183", [self.netlist['n1709'],self.netlist['x1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1182", [self.port['vcc'].netconn,self.netlist['n1479'],self.netlist['abl1']], isweak=False, parent=self),
            NMOS("t1181", [self.netlist['n842'],self.port['vss'].netconn,self.netlist['abl1']], isweak=False, parent=self),
            NMOS("t1180", [self.port['vss'].netconn,self.netlist['n66'],self.netlist['abl1']], isweak=False, parent=self),
            NMOS("t1187", [self.netlist['n346'],self.netlist['n297'],self.netlist['n1392']], isweak=False, parent=self),
            NMOS("t1186", [self.port['vss'].netconn,self.netlist['n1705'],self.netlist['n467']], isweak=False, parent=self),
            NMOS("t1185", [self.netlist['n645'],self.netlist['n562'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1184", [self.netlist['adl1'],self.port['vss'].netconn,self.netlist['n686']], isweak=False, parent=self),
            NMOS("t1613", [self.netlist['notalucout'],self.port['vss'].netconn,self.netlist['n560']], isweak=False, parent=self),
            NMOS("t1612", [self.netlist['n1185'],self.port['vss'].netconn,self.netlist['n1137']], isweak=False, parent=self),
            NMOS("t1611", [self.port['vss'].netconn,self.netlist['n46'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1617", [self.netlist['n180'],self.port['vss'].netconn,self.netlist['n1716']], isweak=False, parent=self),
            NMOS("t1616", [self.netlist['notidl3'],self.netlist['n896'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1615", [self.netlist['x4'],self.netlist['n436'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1614", [self.port['vss'].netconn,self.netlist['n274'],self.netlist['n860']], isweak=False, parent=self),
            NMOS("t3007", [self.port['vss'].netconn,self.netlist['n1419'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1619", [self.netlist['Pout7'],self.port['vss'].netconn,self.netlist['n1045']], isweak=False, parent=self),
            NMOS("t1618", [self.port['vss'].netconn,self.netlist['n588'],self.port['db7'].netconn], isweak=False, parent=self),
            NMOS("t1020", [self.port['vss'].netconn,self.netlist['n161'],self.netlist['n1113']], isweak=False, parent=self),
            NMOS("t1929", [self.port['vss'].netconn,self.netlist['n1499'],self.netlist['n1450']], isweak=False, parent=self),
            NMOS("t1928", [self.port['vss'].netconn,self.netlist['ir5'],self.netlist['n1609']], isweak=False, parent=self),
            NMOS("t916", [self.netlist['n630'],self.port['vss'].netconn,self.netlist['n726']], isweak=False, parent=self),
            NMOS("t917", [self.netlist['n1191'],self.port['vss'].netconn,self.netlist['n1195']], isweak=False, parent=self),
            NMOS("t666", [self.netlist['n579'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t915", [self.netlist['pipedpc28'],self.netlist['n1225'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3069", [self.netlist['n985'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t660", [self.netlist['n1420'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t1920", [self.netlist['n901'],self.port['vss'].netconn,self.netlist['alu1']], isweak=False, parent=self),
            NMOS("t1905", [self.netlist['n648'],self.port['vss'].netconn,self.netlist['DBNeg']], isweak=False, parent=self),
            NMOS("t372", [self.netlist['alub0'],self.netlist['adl0'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t373", [self.netlist['n1054'],self.port['vss'].netconn,self.netlist['RESG']], isweak=False, parent=self),
            NMOS("t370", [self.port['vss'].netconn,self.netlist['n424'],self.netlist['n198']], isweak=False, parent=self),
            NMOS("t371", [self.netlist['n1604'],self.netlist['n1717'],self.netlist['n335']], isweak=False, parent=self),
            NMOS("t374", [self.netlist['sb1'],self.netlist['n694'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t375", [self.port['ab13'].netconn,self.port['vss'].netconn,self.netlist['n869']], isweak=False, parent=self),
            NMOS("t1332", [self.netlist['n262'],self.netlist['n1598'],self.netlist['n1511']], isweak=False, parent=self),
            NMOS("t331", [self.netlist['n1596'],self.port['vss'].netconn,self.netlist['n1602']], isweak=False, parent=self),
            NMOS("t1134", [self.netlist['n1658'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t2757", [self.netlist['n1225'],self.netlist['n1121'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2756", [self.port['vss'].netconn,self.netlist['n1178'],self.netlist['pipeUNK30']], isweak=False, parent=self),
            NMOS("t282", [self.netlist['n1151'],self.port['vss'].netconn,self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t2547", [self.netlist['pchp7'],self.netlist['adh7'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t2755", [self.port['vss'].netconn,self.netlist['n661'],self.netlist['pipeUNK14']], isweak=False, parent=self),
            NMOS("t2754", [self.port['vss'].netconn,self.netlist['alu7'],self.netlist['notalu7']], isweak=False, parent=self),
            NMOS("t3372", [self.netlist['abh1'],self.port['vss'].netconn,self.netlist['n907']], isweak=False, parent=self),
            NMOS("t3373", [self.netlist['adl1'],self.netlist['pcl1'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t3370", [self.port['vss'].netconn,self.netlist['n238'],self.netlist['pipeUNK35']], isweak=False, parent=self),
            NMOS("t3371", [self.netlist['n1354'],self.netlist['n623'],self.netlist['n1628']], isweak=False, parent=self),
            NMOS("t3376", [self.netlist['pcl2'],self.netlist['adl2'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t3377", [self.netlist['adl5'],self.netlist['pcl5'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t3374", [self.netlist['pcl0'],self.netlist['adl0'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t3375", [self.netlist['adl3'],self.netlist['pcl3'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t3378", [self.netlist['pcl4'],self.netlist['adl4'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t3379", [self.netlist['pcl6'],self.netlist['adl6'],self.netlist['dpc40_ADLPCL']], isweak=False, parent=self),
            NMOS("t2207", [self.netlist['n1170'],self.port['vss'].netconn,self.netlist['n755']], isweak=False, parent=self),
            NMOS("t1881", [self.netlist['n663'],self.netlist['n1209'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3338", [self.netlist['n1109'],self.port['vss'].netconn,self.netlist['n1464']], isweak=False, parent=self),
            NMOS("t1886", [self.port['vss'].netconn,self.netlist['n1339'],self.netlist['n799']], isweak=False, parent=self),
            NMOS("t3339", [self.netlist['n703'],self.netlist['n227'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1887", [self.port['db3'].netconn,self.port['vss'].netconn,self.netlist['n643']], isweak=False, parent=self),
            NMOS("t3336", [self.port['vss'].netconn,self.netlist['n62'],self.port['db7'].netconn], isweak=False, parent=self),
            NMOS("t2971", [self.netlist['n1381'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3441", [self.port['vss'].netconn,self.netlist['INTG'],self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t2202", [self.netlist['DC34'],self.port['vss'].netconn,self.netlist['n1201']], isweak=False, parent=self),
            NMOS("t288", [self.netlist['s1'],self.netlist['n694'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t3335", [self.netlist['n384'],self.port['vss'].netconn,self.netlist['n1412']], isweak=False, parent=self),
            NMOS("t3252", [self.port['vss'].netconn,self.netlist['n552'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3445", [self.netlist['n1526'],self.port['vss'].netconn,self.netlist['n680']], isweak=False, parent=self),
            NMOS("t2511", [self.netlist['n1621'],self.port['vss'].netconn,self.netlist['idb3']], isweak=False, parent=self),
            NMOS("t2510", [self.port['vss'].netconn,self.netlist['n732'],self.netlist['n1161']], isweak=False, parent=self),
            NMOS("t2513", [self.netlist['n347'],self.port['vss'].netconn,self.netlist['n607']], isweak=False, parent=self),
            NMOS("t2512", [self.netlist['n182'],self.port['vss'].netconn,self.netlist['n646']], isweak=False, parent=self),
            NMOS("t798", [self.netlist['n552'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2514", [self.netlist['n1298'],self.netlist['n1267'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2517", [self.netlist['n1682'],self.port['vss'].netconn,self.netlist['n901']], isweak=False, parent=self),
            NMOS("t2516", [self.netlist['n643'],self.port['vcc'].netconn,self.netlist['n1613']], isweak=False, parent=self),
            NMOS("t794", [self.netlist['n318'],self.netlist['pipeUNK14'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2518", [self.netlist['n1362'],self.port['vss'].netconn,self.netlist['n901']], isweak=False, parent=self),
            NMOS("t796", [self.port['vss'].netconn,self.netlist['n271'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t3447", [self.netlist['n1427'],self.port['vss'].netconn,self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t790", [self.netlist['n1016'],self.netlist['n416'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t791", [self.netlist['alu2'],self.port['vss'].netconn,self.netlist['notalu2']], isweak=False, parent=self),
            NMOS("t792", [self.netlist['n1330'],self.netlist['n586'],self.netlist['BRtaken']], isweak=False, parent=self),
            NMOS("t152", [self.port['vss'].netconn,self.netlist['n604'],self.netlist['n1582']], isweak=False, parent=self),
            NMOS("t153", [self.port['vss'].netconn,self.netlist['n1010'],self.netlist['pch0']], isweak=False, parent=self),
            NMOS("t150", [self.netlist['n605'],self.port['vss'].netconn,self.netlist['n787']], isweak=False, parent=self),
            NMOS("t151", [self.netlist['dpc1_SBY'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t156", [self.port['vss'].netconn,self.netlist['n1264'],self.netlist['n453']], isweak=False, parent=self),
            NMOS("t157", [self.port['vss'].netconn,self.netlist['abl7'],self.netlist['n28']], isweak=False, parent=self),
            NMOS("t154", [self.port['vcc'].netconn,self.port['db1'].netconn,self.netlist['n798']], isweak=False, parent=self),
            NMOS("t158", [self.netlist['n1548'],self.port['vss'].netconn,self.netlist['adl6']], isweak=False, parent=self),
            NMOS("t159", [self.port['vss'].netconn,self.netlist['n1225'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t1403", [self.netlist['n1688'],self.port['vss'].netconn,self.netlist['n1304']], isweak=False, parent=self),
            NMOS("t2093", [self.netlist['n1677'],self.port['vss'].netconn,self.netlist['abh4']], isweak=False, parent=self),
            NMOS("t2429", [self.netlist['n1559'],self.port['vss'].netconn,self.netlist['alua5']], isweak=False, parent=self),
            NMOS("t2428", [self.port['vss'].netconn,self.netlist['n1508'],self.netlist['n46']], isweak=False, parent=self),
            NMOS("t2994", [self.port['vss'].netconn,self.netlist['n1589'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2357", [self.port['ab15'].netconn,self.port['vss'].netconn,self.netlist['n659']], isweak=False, parent=self),
            NMOS("t2424", [self.port['vss'].netconn,self.netlist['dpc13_ORS'],self.netlist['n1255']], isweak=False, parent=self),
            NMOS("t2427", [self.netlist['n1369'],self.port['vss'].netconn,self.netlist['n897']], isweak=False, parent=self),
            NMOS("t2426", [self.netlist['n1457'],self.port['vss'].netconn,self.netlist['n781']], isweak=False, parent=self),
            NMOS("t2353", [self.port['db7'].netconn,self.port['vcc'].netconn,self.netlist['n298']], isweak=False, parent=self),
            NMOS("t2352", [self.netlist['n272'],self.port['vss'].netconn,self.netlist['n0']], isweak=False, parent=self),
            NMOS("t2351", [self.netlist['n1631'],self.netlist['n868'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2350", [self.netlist['n479'],self.port['vss'].netconn,self.netlist['n739']], isweak=False, parent=self),
            NMOS("t3118", [self.netlist['sb2'],self.netlist['n1694'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t2996", [self.netlist['n528'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2541", [self.netlist['n83'],self.port['vss'].netconn,self.netlist['n1400']], isweak=False, parent=self),
            NMOS("t3112", [self.port['vss'].netconn,self.netlist['n1159'],self.netlist['n1580']], isweak=False, parent=self),
            NMOS("t3113", [self.netlist['n1550'],self.netlist['n845'],self.netlist['n1573']], isweak=False, parent=self),
            NMOS("t3110", [self.netlist['n506'],self.port['vss'].netconn,self.netlist['n236']], isweak=False, parent=self),
            NMOS("t3111", [self.port['vss'].netconn,self.netlist['n1656'],self.netlist['n1580']], isweak=False, parent=self),
            NMOS("t3116", [self.netlist['sb6'],self.netlist['n1724'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t3117", [self.netlist['dpc15_ANDS'],self.port['vss'].netconn,self.netlist['n1256']], isweak=False, parent=self),
            NMOS("t3114", [self.port['vss'].netconn,self.netlist['n959'],self.netlist['n430']], isweak=False, parent=self),
            NMOS("t3115", [self.netlist['sb5'],self.netlist['n578'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t2992", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t563", [self.netlist['n1616'],self.netlist['n299'],self.netlist['n1614']], isweak=False, parent=self),
            NMOS("t562", [self.port['vss'].netconn,self.netlist['n628'],self.netlist['n55']], isweak=False, parent=self),
            NMOS("t561", [self.port['vss'].netconn,self.netlist['n176'],self.netlist['n10']], isweak=False, parent=self),
            NMOS("t560", [self.netlist['n224'],self.port['vss'].netconn,self.netlist['dor2']], isweak=False, parent=self),
            NMOS("t567", [self.port['vss'].netconn,self.netlist['n122'],self.netlist['n1459']], isweak=False, parent=self),
            NMOS("t566", [self.netlist['n1134'],self.port['vss'].netconn,self.netlist['VEC0']], isweak=False, parent=self),
            NMOS("t565", [self.netlist['n1697'],self.port['vss'].netconn,self.netlist['n664']], isweak=False, parent=self),
            NMOS("t564", [self.netlist['n335'],self.port['vss'].netconn,self.netlist['n925']], isweak=False, parent=self),
            NMOS("t569", [self.netlist['n1305'],self.port['vss'].netconn,self.netlist['n772']], isweak=False, parent=self),
            NMOS("t568", [self.port['vss'].netconn,self.netlist['n1030'],self.netlist['n1459']], isweak=False, parent=self),
            NMOS("t1876", [self.netlist['adl7'],self.netlist['n1147'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t2739", [self.netlist['n1695'],self.netlist['n1318'],self.netlist['alub7']], isweak=False, parent=self),
            NMOS("t2738", [self.port['vss'].netconn,self.netlist['n41'],self.netlist['n1441']], isweak=False, parent=self),
            NMOS("t2229", [self.port['vss'].netconn,self.netlist['dpc40_ADLPCL'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2228", [self.port['vss'].netconn,self.netlist['n929'],self.netlist['n1549']], isweak=False, parent=self),
            NMOS("t2731", [self.netlist['n578'],self.netlist['x5'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2730", [self.port['vss'].netconn,self.netlist['n806'],self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t2221", [self.port['vcc'].netconn,self.netlist['adl1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2220", [self.netlist['n569'],self.netlist['n1205'],self.netlist['n233']], isweak=False, parent=self),
            NMOS("t2735", [self.port['vss'].netconn,self.netlist['n914'],self.netlist['n1316']], isweak=False, parent=self),
            NMOS("t2734", [self.netlist['n426'],self.netlist['n1386'],self.netlist['n1316']], isweak=False, parent=self),
            NMOS("t2737", [self.netlist['n780'],self.netlist['n1229'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2736", [self.netlist['adl0'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t899", [self.port['vss'].netconn,self.netlist['n860'],self.netlist['AxB3']], isweak=False, parent=self),
            NMOS("t898", [self.port['vss'].netconn,self.netlist['n136'],self.netlist['AxB3']], isweak=False, parent=self),
            NMOS("t893", [self.port['vss'].netconn,self.netlist['n486'],self.netlist['n817']], isweak=False, parent=self),
            NMOS("t892", [self.netlist['n188'],self.netlist['pipeT4out'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t891", [self.port['vss'].netconn,self.netlist['n1180'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t890", [self.netlist['n1087'],self.netlist['n1132'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t897", [self.port['vss'].netconn,self.netlist['dpc9_DBADD'],self.netlist['n225']], isweak=False, parent=self),
            NMOS("t896", [self.port['vss'].netconn,self.netlist['n635'],self.netlist['abh6']], isweak=False, parent=self),
            NMOS("t895", [self.port['vss'].netconn,self.netlist['n1523'],self.netlist['abh6']], isweak=False, parent=self),
            NMOS("t894", [self.netlist['n963'],self.port['vcc'].netconn,self.netlist['abh6']], isweak=False, parent=self),
            NMOS("t1087", [self.netlist['n942'],self.port['vss'].netconn,self.netlist['notalucin']], isweak=False, parent=self),
            NMOS("t419", [self.netlist['n92'],self.netlist['n1667'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t418", [self.netlist['n1383'],self.port['vss'].netconn,self.netlist['idb5']], isweak=False, parent=self),
            NMOS("t417", [self.netlist['nots6'],self.netlist['n1187'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t416", [self.port['vcc'].netconn,self.netlist['sb6'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t415", [self.netlist['adh6'],self.netlist['pch6'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t414", [self.netlist['adh7'],self.netlist['pch7'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t413", [self.netlist['adh4'],self.netlist['pch4'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t412", [self.netlist['adh5'],self.netlist['pch5'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t411", [self.netlist['adh2'],self.netlist['pch2'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t410", [self.netlist['adh3'],self.netlist['pch3'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t1338", [self.netlist['sb1'],self.netlist['x1'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t2644", [self.netlist['n1172'],self.port['vss'].netconn,self.netlist['n646']], isweak=False, parent=self),
            NMOS("t1998", [self.netlist['n1090'],self.port['vss'].netconn,self.netlist['n157']], isweak=False, parent=self),
            NMOS("t2640", [self.netlist['alu5'],self.port['vss'].netconn,self.netlist['notalu5']], isweak=False, parent=self),
            NMOS("t2643", [self.netlist['dpc3_SBX'],self.port['vcc'].netconn,self.netlist['n625']], isweak=False, parent=self),
            NMOS("t968", [self.netlist['n1707'],self.netlist['n319'],self.netlist['n623']], isweak=False, parent=self),
            NMOS("t967", [self.port['vss'].netconn,self.netlist['n218'],self.netlist['n368']], isweak=False, parent=self),
            NMOS("t966", [self.port['vss'].netconn,self.netlist['DBZ'],self.netlist['idb6']], isweak=False, parent=self),
            NMOS("t1996", [self.netlist['n118'],self.port['vss'].netconn,self.netlist['n334']], isweak=False, parent=self),
            NMOS("t1997", [self.port['vss'].netconn,self.netlist['n619'],self.netlist['n700']], isweak=False, parent=self),
            NMOS("t1334", [self.port['vss'].netconn,self.netlist['n1633'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1991", [self.netlist['n1501'],self.port['vcc'].netconn,self.netlist['n23']], isweak=False, parent=self),
            NMOS("t961", [self.port['vcc'].netconn,self.netlist['idb3'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t960", [self.netlist['n1710'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t1510", [self.netlist['n37'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1047", [self.netlist['y7'],self.netlist['n1251'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1044", [self.netlist['n1427'],self.port['vss'].netconn,self.netlist['n236']], isweak=False, parent=self),
            NMOS("t1045", [self.netlist['n1464'],self.port['vss'].netconn,self.netlist['n271']], isweak=False, parent=self),
            NMOS("t1514", [self.netlist['n798'],self.port['vss'].netconn,self.netlist['n288']], isweak=False, parent=self),
            NMOS("t1515", [self.netlist['n794'],self.port['vcc'].netconn,self.netlist['n288']], isweak=False, parent=self),
            NMOS("t1040", [self.netlist['n1267'],self.port['vss'].netconn,self.netlist['adh1']], isweak=False, parent=self),
            NMOS("t1517", [self.port['vss'].netconn,self.netlist['n625'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t1518", [self.netlist['n34'],self.port['vss'].netconn,self.netlist['s3']], isweak=False, parent=self),
            NMOS("t1519", [self.netlist['pchp6'],self.port['vss'].netconn,self.netlist['n751']], isweak=False, parent=self),
            NMOS("t2798", [self.netlist['n1383'],self.netlist['alub5'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t1048", [self.netlist['n1519'],self.port['vss'].netconn,self.netlist['adl4']], isweak=False, parent=self),
            NMOS("t1049", [self.netlist['n1447'],self.netlist['n262'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3304", [self.port['vss'].netconn,self.netlist['n1419'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t1194", [self.port['vss'].netconn,self.netlist['abh3'],self.netlist['n92']], isweak=False, parent=self),
            NMOS("t1195", [self.netlist['DBZ'],self.port['vss'].netconn,self.netlist['idb1']], isweak=False, parent=self),
            NMOS("t1196", [self.port['vss'].netconn,self.netlist['n851'],self.netlist['n1294']], isweak=False, parent=self),
            NMOS("t3129", [self.netlist['n1599'],self.port['vss'].netconn,self.port['irq'].netconn], isweak=False, parent=self),
            NMOS("t1190", [self.netlist['n1464'],self.port['vss'].netconn,self.netlist['n552']], isweak=False, parent=self),
            NMOS("t1191", [self.netlist['C34'],self.port['vss'].netconn,self.netlist['n1425']], isweak=False, parent=self),
            NMOS("t1192", [self.netlist['C45'],self.netlist['n1310'],self.netlist['n1425']], isweak=False, parent=self),
            NMOS("t1193", [self.netlist['n1617'],self.port['vss'].netconn,self.netlist['n117']], isweak=False, parent=self),
            NMOS("t249", [self.netlist['sb6'],self.netlist['s6'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t1198", [self.netlist['n1106'],self.port['vss'].netconn,self.netlist['n1658']], isweak=False, parent=self),
            NMOS("t1199", [self.netlist['notdor6'],self.netlist['n1684'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1424", [self.netlist['n1428'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1425", [self.netlist['n492'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1426", [self.netlist['n1204'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t2105", [self.netlist['n1686'],self.netlist['dasb3'],self.netlist['n345']], isweak=False, parent=self),
            NMOS("t1420", [self.port['vss'].netconn,self.netlist['n1512'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1421", [self.port['vss'].netconn,self.netlist['n84'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1422", [self.netlist['n1623'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1423", [self.netlist['n403'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1316", [self.port['vss'].netconn,self.netlist['n717'],self.netlist['pipephi2Reset0x']], isweak=False, parent=self),
            NMOS("t1428", [self.netlist['n342'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1429", [self.netlist['n1355'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t984", [self.port['vss'].netconn,self.netlist['n911'],self.netlist['n1343']], isweak=False, parent=self),
            NMOS("t987", [self.netlist['n1106'],self.port['vss'].netconn,self.netlist['n1543']], isweak=False, parent=self),
            NMOS("t2639", [self.port['vss'].netconn,self.netlist['DBZ'],self.netlist['idb2']], isweak=False, parent=self),
            NMOS("t1043", [self.port['vss'].netconn,self.netlist['n367'],self.netlist['n954']], isweak=False, parent=self),
            NMOS("t986", [self.netlist['n70'],self.port['vss'].netconn,self.netlist['n1054']], isweak=False, parent=self),
            NMOS("t1608", [self.netlist['Pout2'],self.port['vss'].netconn,self.netlist['n334']], isweak=False, parent=self),
            NMOS("t1609", [self.port['vss'].netconn,self.netlist['n643'],self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t821", [self.netlist['n303'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t1604", [self.netlist['alurawcout'],self.netlist['n560'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1605", [self.port['vss'].netconn,self.netlist['n1517'],self.netlist['n572']], isweak=False, parent=self),
            NMOS("t1606", [self.netlist['n1525'],self.netlist['n1348'],self.netlist['n693']], isweak=False, parent=self),
            NMOS("t1607", [self.port['vss'].netconn,self.netlist['n169'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t1600", [self.netlist['dasb2'],self.netlist['n1656'],self.netlist['n613']], isweak=False, parent=self),
            NMOS("t1601", [self.netlist['n1159'],self.port['vss'].netconn,self.netlist['n613']], isweak=False, parent=self),
            NMOS("t1602", [self.netlist['idb7'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1603", [self.netlist['n1452'],self.netlist['VEC1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2702", [self.port['vss'].netconn,self.netlist['n1168'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t750", [self.port['vss'].netconn,self.netlist['n776'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t745", [self.port['vss'].netconn,self.netlist['n1259'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t751", [self.port['vss'].netconn,self.netlist['n157'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2109", [self.netlist['n1193'],self.port['vss'].netconn,self.netlist['n815']], isweak=False, parent=self),
            NMOS("t2557", [self.netlist['n381'],self.netlist['n1062'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2703", [self.port['vss'].netconn,self.netlist['n1721'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1351", [self.port['vss'].netconn,self.netlist['n793'],self.netlist['pipeUNK13']], isweak=False, parent=self),
            NMOS("t2556", [self.netlist['n700'],self.port['vss'].netconn,self.netlist['n1201']], isweak=False, parent=self),
            NMOS("t1934", [self.netlist['n471'],self.port['vcc'].netconn,self.netlist['n466']], isweak=False, parent=self),
            NMOS("t755", [self.port['vss'].netconn,self.netlist['n4'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2553", [self.netlist['pchp1'],self.netlist['adh1'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t2552", [self.netlist['pchp2'],self.netlist['adh2'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t2704", [self.port['vss'].netconn,self.netlist['n487'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1935", [self.port['vss'].netconn,self.netlist['n384'],self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t1859", [self.netlist['dasb4'],self.netlist['idb4'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t3439", [self.netlist['n578'],self.port['vss'].netconn,self.netlist['notx5']], isweak=False, parent=self),
            NMOS("t2705", [self.port['vss'].netconn,self.netlist['n579'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t3438", [self.netlist['dpc19_ADDSB7'],self.port['vss'].netconn,self.netlist['n906']], isweak=False, parent=self),
            NMOS("t365", [self.netlist['n605'],self.port['vss'].netconn,self.netlist['n1081']], isweak=False, parent=self),
            NMOS("t364", [self.port['vss'].netconn,self.port['db1'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t367", [self.netlist['notRdy0'],self.port['vcc'].netconn,self.netlist['n424']], isweak=False, parent=self),
            NMOS("t366", [self.netlist['n1198'],self.port['vss'].netconn,self.netlist['pipeUNK01']], isweak=False, parent=self),
            NMOS("t361", [self.port['vss'].netconn,self.netlist['n1692'],self.netlist['n253']], isweak=False, parent=self),
            NMOS("t360", [self.port['vss'].netconn,self.netlist['n279'],self.netlist['n253']], isweak=False, parent=self),
            NMOS("t363", [self.port['vss'].netconn,self.netlist['n906'],self.netlist['n1333']], isweak=False, parent=self),
            NMOS("t362", [self.netlist['cclk'],self.port['vcc'].netconn,self.netlist['n1129']], isweak=False, parent=self),
            NMOS("t369", [self.port['vss'].netconn,self.netlist['notRdy0'],self.netlist['n198']], isweak=False, parent=self),
            NMOS("t368", [self.netlist['n1178'],self.port['vss'].netconn,self.netlist['pipeUNK31']], isweak=False, parent=self),
            NMOS("t2706", [self.port['vss'].netconn,self.netlist['n1239'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t3389", [self.netlist['n695'],self.netlist['n1341'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2710", [self.port['vss'].netconn,self.netlist['n1478'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t619", [self.port['vss'].netconn,self.netlist['n179'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1539", [self.port['vss'].netconn,self.netlist['dpc14_SRS'],self.netlist['n1552']], isweak=False, parent=self),
            NMOS("t2707", [self.port['vss'].netconn,self.netlist['n285'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t618", [self.netlist['n257'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2641", [self.netlist['n1573'],self.port['vss'].netconn,self.netlist['idb2']], isweak=False, parent=self),
            NMOS("t589", [self.netlist['n1095'],self.netlist['idb4'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t3349", [self.port['vss'].netconn,self.netlist['n1260'],self.netlist['n598']], isweak=False, parent=self),
            NMOS("t3348", [self.port['vss'].netconn,self.netlist['noty5'],self.netlist['y5']], isweak=False, parent=self),
            NMOS("t3347", [self.netlist['alua7'],self.netlist['sb7'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t3346", [self.netlist['n954'],self.port['vss'].netconn,self.netlist['pipeUNK08']], isweak=False, parent=self),
            NMOS("t3345", [self.netlist['n507'],self.port['vss'].netconn,self.netlist['n1049']], isweak=False, parent=self),
            NMOS("t3344", [self.netlist['n839'],self.port['vss'].netconn,self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3342", [self.netlist['idl4'],self.netlist['n1095'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3341", [self.netlist['nots7'],self.netlist['n548'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3340", [self.port['vcc'].netconn,self.netlist['sb5'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t14", [self.netlist['n346'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2554", [self.netlist['pchp0'],self.netlist['adh0'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t16", [self.port['vss'].netconn,self.netlist['n508'],self.netlist['n1540']], isweak=False, parent=self),
            NMOS("t17", [self.netlist['n1082'],self.netlist['p0'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t10", [self.netlist['n220'],self.port['vss'].netconn,self.netlist['n190']], isweak=False, parent=self),
            NMOS("t11", [self.port['vcc'].netconn,self.netlist['n1247'],self.netlist['n38']], isweak=False, parent=self),
            NMOS("t12", [self.port['vss'].netconn,self.netlist['n189'],self.netlist['alua1']], isweak=False, parent=self),
            NMOS("t13", [self.netlist['n155'],self.port['vss'].netconn,self.netlist['alua1']], isweak=False, parent=self),
            NMOS("t18", [self.netlist['n212'],self.netlist['n1451'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t19", [self.netlist['dpc23_SBAC'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1848", [self.netlist['a7'],self.netlist['dasb7'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1858", [self.netlist['idb3'],self.netlist['sb3'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t2502", [self.netlist['n824'],self.port['vss'].netconn,self.netlist['n487']], isweak=False, parent=self),
            NMOS("t913", [self.port['vss'].netconn,self.netlist['n1330'],self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t2500", [self.netlist['n1082'],self.netlist['n1692'],self.netlist['n270']], isweak=False, parent=self),
            NMOS("t2501", [self.port['vss'].netconn,self.netlist['n1668'],self.netlist['adh0']], isweak=False, parent=self),
            NMOS("t2506", [self.netlist['n1486'],self.netlist['n126'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2507", [self.port['vss'].netconn,self.netlist['n152'],self.netlist['n788']], isweak=False, parent=self),
            NMOS("t2504", [self.netlist['n1621'],self.netlist['alub3'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t2505", [self.port['vss'].netconn,self.netlist['n1619'],self.netlist['n182']], isweak=False, parent=self),
            NMOS("t787", [self.port['vss'].netconn,self.netlist['n607'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t786", [self.port['vss'].netconn,self.netlist['n1050'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2508", [self.netlist['n1492'],self.port['vss'].netconn,self.netlist['pipeUNK02']], isweak=False, parent=self),
            NMOS("t784", [self.port['vss'].netconn,self.netlist['n1665'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t783", [self.port['vss'].netconn,self.netlist['n950'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t782", [self.port['vss'].netconn,self.netlist['n1569'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t781", [self.port['vss'].netconn,self.netlist['n1226'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t780", [self.port['vss'].netconn,self.netlist['n1476'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t633", [self.netlist['n1114'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1121", [self.netlist['n597'],self.netlist['n1339'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t149", [self.netlist['dpc20_ADDSB06'],self.port['vcc'].netconn,self.netlist['n154']], isweak=False, parent=self),
            NMOS("t148", [self.netlist['n75'],self.port['vss'].netconn,self.netlist['n154']], isweak=False, parent=self),
            NMOS("t1973", [self.port['vss'].netconn,self.netlist['n1270'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t145", [self.port['vss'].netconn,self.netlist['n789'],self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t144", [self.port['vss'].netconn,self.netlist['n397'],self.netlist['n1420']], isweak=False, parent=self),
            NMOS("t147", [self.netlist['n624'],self.port['vss'].netconn,self.netlist['idb0']], isweak=False, parent=self),
            NMOS("t146", [self.port['vss'].netconn,self.netlist['n884'],self.netlist['AxB3']], isweak=False, parent=self),
            NMOS("t141", [self.netlist['notx5'],self.port['vss'].netconn,self.netlist['x5']], isweak=False, parent=self),
            NMOS("t140", [self.netlist['n1083'],self.netlist['n1590'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t143", [self.port['vss'].netconn,self.netlist['n1455'],self.netlist['n1420']], isweak=False, parent=self),
            NMOS("t142", [self.netlist['idl2'],self.netlist['n1424'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3299", [self.port['vss'].netconn,self.netlist['n1114'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3298", [self.port['vss'].netconn,self.netlist['n1292'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t630", [self.netlist['n1478'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t3018", [self.netlist['DBZ'],self.port['vss'].netconn,self.netlist['idb3']], isweak=False, parent=self),
            NMOS("t3291", [self.port['vss'].netconn,self.netlist['n791'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t637", [self.netlist['n1491'],self.netlist['y2'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3293", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3292", [self.port['vss'].netconn,self.netlist['n352'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3295", [self.port['vss'].netconn,self.netlist['n446'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3294", [self.port['vss'].netconn,self.netlist['n932'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3297", [self.port['vss'].netconn,self.netlist['n1430'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3296", [self.port['vss'].netconn,self.netlist['n528'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t635", [self.port['vss'].netconn,self.netlist['n1226'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2551", [self.netlist['pchp3'],self.netlist['adh3'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t639", [self.netlist['n299'],self.port['vss'].netconn,self.netlist['n587']], isweak=False, parent=self),
            NMOS("t2711", [self.port['vss'].netconn,self.netlist['n1210'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2348", [self.netlist['n360'],self.netlist['n795'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2349", [self.netlist['n1554'],self.netlist['dasb6'],self.netlist['n739']], isweak=False, parent=self),
            NMOS("t964", [self.netlist['n137'],self.port['vss'].netconn,self.netlist['n1120']], isweak=False, parent=self),
            NMOS("t3124", [self.netlist['n570'],self.port['vss'].netconn,self.netlist['n1144']], isweak=False, parent=self),
            NMOS("t3123", [self.netlist['n831'],self.port['vss'].netconn,self.netlist['n1719']], isweak=False, parent=self),
            NMOS("t3122", [self.netlist['n37'],self.port['vcc'].netconn,self.netlist['n224']], isweak=False, parent=self),
            NMOS("t3121", [self.netlist['n520'],self.port['vss'].netconn,self.netlist['n224']], isweak=False, parent=self),
            NMOS("t3120", [self.netlist['dasb4'],self.netlist['n436'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t2436", [self.port['vss'].netconn,self.netlist['n1352'],self.netlist['n335']], isweak=False, parent=self),
            NMOS("t2550", [self.netlist['pchp4'],self.netlist['adh4'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t2434", [self.netlist['n1572'],self.port['vss'].netconn,self.netlist['n701']], isweak=False, parent=self),
            NMOS("t2435", [self.netlist['n193'],self.port['vss'].netconn,self.netlist['n701']], isweak=False, parent=self),
            NMOS("t2432", [self.port['vss'].netconn,self.netlist['dpc40_ADLPCL'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t2433", [self.port['vss'].netconn,self.netlist['n152'],self.netlist['n630']], isweak=False, parent=self),
            NMOS("t2346", [self.port['vss'].netconn,self.netlist['noty0'],self.netlist['y0']], isweak=False, parent=self),
            NMOS("t2431", [self.netlist['n510'],self.port['vss'].netconn,self.netlist['n434']], isweak=False, parent=self),
            NMOS("t481", [self.port['vcc'].netconn,self.netlist['n1417'],self.netlist['n670']], isweak=False, parent=self),
            NMOS("t2700", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2701", [self.port['vss'].netconn,self.netlist['n776'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2179", [self.netlist['cp1'],self.port['vcc'].netconn,self.netlist['n1399']], isweak=False, parent=self),
            NMOS("t1879", [self.netlist['n1238'],self.port['vss'].netconn,self.netlist['n1295']], isweak=False, parent=self),
            NMOS("t1878", [self.port['vss'].netconn,self.netlist['n1115'],self.netlist['n620']], isweak=False, parent=self),
            NMOS("t558", [self.netlist['n345'],self.netlist['n1584'],self.netlist['n8']], isweak=False, parent=self),
            NMOS("t559", [self.netlist['n37'],self.port['vss'].netconn,self.netlist['dor2']], isweak=False, parent=self),
            NMOS("t556", [self.netlist['notidl0'],self.netlist['n718'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t557", [self.port['vss'].netconn,self.netlist['n165'],self.netlist['n1236']], isweak=False, parent=self),
            NMOS("t550", [self.port['vss'].netconn,self.netlist['n1130'],self.netlist['n1109']], isweak=False, parent=self),
            NMOS("t551", [self.port['vss'].netconn,self.port['clk1out'].netconn,self.netlist['n1417']], isweak=False, parent=self),
            NMOS("t2234", [self.port['vss'].netconn,self.netlist['n1110'],self.netlist['n756']], isweak=False, parent=self),
            NMOS("t2235", [self.netlist['idb0'],self.netlist['n146'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2236", [self.netlist['idb1'],self.netlist['n929'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2237", [self.netlist['idb2'],self.netlist['n1618'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2230", [self.port['vss'].netconn,self.netlist['dpc39_PCLPCL'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2231", [self.netlist['n132'],self.port['vss'].netconn,self.netlist['n31']], isweak=False, parent=self),
            NMOS("t2232", [self.port['vss'].netconn,self.netlist['n1583'],self.netlist['n918']], isweak=False, parent=self),
            NMOS("t2233", [self.netlist['n112'],self.port['vss'].netconn,self.netlist['n336']], isweak=False, parent=self),
            NMOS("t1855", [self.netlist['idb0'],self.netlist['dasb0'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t1854", [self.port['vss'].netconn,self.netlist['n19'],self.netlist['n1708']], isweak=False, parent=self),
            NMOS("t1857", [self.netlist['sb2'],self.netlist['idb2'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t2255", [self.netlist['alua2'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t2238", [self.netlist['idb3'],self.netlist['n1654'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t1850", [self.port['vss'].netconn,self.netlist['RnWstretched'],self.netlist['n251']], isweak=False, parent=self),
            NMOS("t2708", [self.port['vss'].netconn,self.netlist['n1524'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2728", [self.netlist['idb5'],self.netlist['alub5'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t2729", [self.netlist['idb4'],self.netlist['alub4'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t610", [self.netlist['n552'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2709", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2722", [self.port['vss'].netconn,self.netlist['n219'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2723", [self.port['vss'].netconn,self.netlist['n1385'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2720", [self.port['vss'].netconn,self.netlist['n1569'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2721", [self.port['vss'].netconn,self.netlist['n1710'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2726", [self.netlist['idb3'],self.netlist['alub3'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t2727", [self.netlist['alub2'],self.netlist['idb2'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t2724", [self.netlist['idl7'],self.netlist['n1147'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2725", [self.netlist['idb1'],self.netlist['alub1'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t1297", [self.port['vss'].netconn,self.netlist['n1239'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1296", [self.port['vss'].netconn,self.netlist['n1721'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1295", [self.port['vss'].netconn,self.netlist['n1168'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1294", [self.port['vss'].netconn,self.netlist['n354'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1293", [self.port['vss'].netconn,self.netlist['n257'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1292", [self.port['vss'].netconn,self.netlist['n342'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1291", [self.netlist['n58'],self.port['vss'].netconn,self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1290", [self.port['vss'].netconn,self.netlist['n1204'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1299", [self.port['vss'].netconn,self.netlist['n447'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1298", [self.netlist['n461'],self.port['vss'].netconn,self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t2621", [self.netlist['n1639'],self.port['vss'].netconn,self.netlist['n1153']], isweak=False, parent=self),
            NMOS("t428", [self.netlist['n1012'],self.netlist['n366'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t429", [self.port['vss'].netconn,self.netlist['abh4'],self.netlist['n668']], isweak=False, parent=self),
            NMOS("t422", [self.port['vss'].netconn,self.port['clk2out'].netconn,self.netlist['n135']], isweak=False, parent=self),
            NMOS("t420", [self.netlist['n1683'],self.netlist['n1090'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t421", [self.netlist['n1018'],self.port['vss'].netconn,self.netlist['n762']], isweak=False, parent=self),
            NMOS("t426", [self.port['vcc'].netconn,self.netlist['adh4'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2319", [self.netlist['n716'],self.port['vss'].netconn,self.netlist['n681']], isweak=False, parent=self),
            NMOS("t2620", [self.netlist['n395'],self.port['vss'].netconn,self.netlist['pipeT4out']], isweak=False, parent=self),
            NMOS("t2656", [self.netlist['n17'],self.netlist['n554'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2657", [self.netlist['n1615'],self.port['vss'].netconn,self.netlist['pipeT5out']], isweak=False, parent=self),
            NMOS("t2654", [self.netlist['n5'],self.port['vss'].netconn,self.netlist['a0']], isweak=False, parent=self),
            NMOS("t959", [self.netlist['n1665'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t2652", [self.netlist['n385'],self.port['vss'].netconn,self.netlist['n604']], isweak=False, parent=self),
            NMOS("t2653", [self.port['vss'].netconn,self.netlist['n522'],self.netlist['n1145']], isweak=False, parent=self),
            NMOS("t2650", [self.netlist['n1213'],self.port['vss'].netconn,self.netlist['n609']], isweak=False, parent=self),
            NMOS("t2651", [self.port['vcc'].netconn,self.netlist['n1325'],self.netlist['dor0']], isweak=False, parent=self),
            NMOS("t952", [self.netlist['n1243'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t953", [self.netlist['n822'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t950", [self.netlist['n1664'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t951", [self.netlist['n1482'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t956", [self.port['vss'].netconn,self.netlist['n1155'],self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t957", [self.netlist['n301'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t2658", [self.port['vss'].netconn,self.port['ab11'].netconn,self.netlist['n359']], isweak=False, parent=self),
            NMOS("t3153", [self.port['vss'].netconn,self.netlist['n639'],self.netlist['n130']], isweak=False, parent=self),
            NMOS("t1073", [self.netlist['dpc10_ADLADD'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1072", [self.netlist['dpc11_SBADD'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1071", [self.netlist['dpc12_0ADD'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1070", [self.port['vss'].netconn,self.netlist['n219'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1077", [self.port['vss'].netconn,self.netlist['dpc6_SBS'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1076", [self.netlist['dpc7_SS'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1075", [self.netlist['dpc8_nDBADD'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1074", [self.netlist['dpc9_DBADD'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1079", [self.netlist['n792'],self.netlist['n851'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1078", [self.netlist['alua0'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t1932", [self.netlist['n1073'],self.netlist['n1326'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2099", [self.port['vss'].netconn,self.netlist['alurawcout'],self.netlist['n1327']], isweak=False, parent=self),
            NMOS("t2310", [self.port['vss'].netconn,self.netlist['n309'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1450", [self.port['vss'].netconn,self.netlist['n612'],self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1453", [self.netlist['pipeUNK19'],self.netlist['n586'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1452", [self.netlist['pipeUNK20'],self.netlist['n14'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1455", [self.netlist['n1487'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t2315", [self.netlist['n301'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1457", [self.port['vss'].netconn,self.netlist['n1428'],self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1456", [self.netlist['n1031'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1459", [self.netlist['n342'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1458", [self.netlist['n58'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1056", [self.port['vss'].netconn,self.netlist['n764'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t2314", [self.netlist['n1569'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t617", [self.netlist['n575'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1679", [self.port['db3'].netconn,self.port['vcc'].netconn,self.netlist['n42']], isweak=False, parent=self),
            NMOS("t1678", [self.netlist['n266'],self.netlist['n1037'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2717", [self.port['vss'].netconn,self.netlist['n446'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1671", [self.netlist['n272'],self.port['vss'].netconn,self.netlist['n646']], isweak=False, parent=self),
            NMOS("t1670", [self.port['rdy'].netconn,self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t1673", [self.netlist['n1455'],self.port['vss'].netconn,self.netlist['n131']], isweak=False, parent=self),
            NMOS("t1672", [self.netlist['n1293'],self.port['vss'].netconn,self.netlist['n1174']], isweak=False, parent=self),
            NMOS("t1675", [self.netlist['dpc31_PCHPCH'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1674", [self.port['vss'].netconn,self.netlist['dpc26_ACDB'],self.netlist['n800']], isweak=False, parent=self),
            NMOS("t1677", [self.netlist['n1387'],self.netlist['adl5'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t1278", [self.netlist['n933'],self.netlist['n1407'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t616", [self.netlist['n787'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2716", [self.port['vss'].netconn,self.netlist['n352'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1276", [self.netlist['dpc23_SBAC'],self.port['vss'].netconn,self.netlist['n1047']], isweak=False, parent=self),
            NMOS("t2715", [self.port['vss'].netconn,self.netlist['n259'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1705", [self.netlist['n1133'],self.port['vss'].netconn,self.netlist['ir1']], isweak=False, parent=self),
            NMOS("t1704", [self.netlist['n1581'],self.netlist['n1275'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1707", [self.netlist['n1353'],self.netlist['n1128'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t1706", [self.netlist['notir1'],self.port['vss'].netconn,self.netlist['ir1']], isweak=False, parent=self),
            NMOS("t1701", [self.port['vcc'].netconn,self.port['ab12'].netconn,self.netlist['n475']], isweak=False, parent=self),
            NMOS("t1700", [self.netlist['n236'],self.port['vss'].netconn,self.netlist['n1708']], isweak=False, parent=self),
            NMOS("t1703", [self.netlist['n1472'],self.netlist['D1x1'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1702", [self.port['vss'].netconn,self.netlist['D1x1'],self.netlist['INTG']], isweak=False, parent=self),
            NMOS("t1709", [self.netlist['n1105'],self.port['vss'].netconn,self.netlist['n1399']], isweak=False, parent=self),
            NMOS("t1708", [self.netlist['n1037'],self.port['vss'].netconn,self.netlist['n1086']], isweak=False, parent=self),
            NMOS("t1927", [self.port['vss'].netconn,self.netlist['n1081'],self.netlist['n1560']], isweak=False, parent=self),
            NMOS("t62", [self.port['vss'].netconn,self.netlist['n860'],self.netlist['n1003']], isweak=False, parent=self),
            NMOS("t311", [self.port['vss'].netconn,self.netlist['n127'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t312", [self.port['vss'].netconn,self.port['sync'].netconn,self.netlist['n445']], isweak=False, parent=self),
            NMOS("t317", [self.port['vss'].netconn,self.netlist['abh2'],self.netlist['n768']], isweak=False, parent=self),
            NMOS("t318", [self.port['vss'].netconn,self.netlist['n1215'],self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t319", [self.netlist['n547'],self.port['vss'].netconn,self.netlist['AxB5']], isweak=False, parent=self),
            NMOS("t765", [self.port['vss'].netconn,self.netlist['n594'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2628", [self.netlist['n11'],self.port['vss'].netconn,self.netlist['n1396']], isweak=False, parent=self),
            NMOS("t3119", [self.netlist['sb3'],self.netlist['n242'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t1921", [self.netlist['n1723'],self.netlist['n299'],self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t686", [self.port['vss'].netconn,self.netlist['n180'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t838", [self.netlist['n1589'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t932", [self.netlist['n699'],self.port['vss'].netconn,self.netlist['alu2']], isweak=False, parent=self),
            NMOS("t3358", [self.netlist['notidl2'],self.netlist['n1199'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3359", [self.netlist['pipeUNK34'],self.netlist['n824'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t685", [self.port['vss'].netconn,self.netlist['n1154'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t228", [self.netlist['n355'],self.port['vss'].netconn,self.netlist['n621']], isweak=False, parent=self),
            NMOS("t229", [self.netlist['n251'],self.port['vss'].netconn,self.netlist['n1035']], isweak=False, parent=self),
            NMOS("t3350", [self.netlist['ir0'],self.port['vss'].netconn,self.netlist['n310']], isweak=False, parent=self),
            NMOS("t225", [self.netlist['n124'],self.port['vss'].netconn,self.netlist['n1061']], isweak=False, parent=self),
            NMOS("t226", [self.netlist['s0'],self.netlist['n332'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t227", [self.port['vcc'].netconn,self.netlist['idb0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t220", [self.netlist['n1371'],self.port['vss'].netconn,self.netlist['n201']], isweak=False, parent=self),
            NMOS("t221", [self.netlist['n272'],self.port['vss'].netconn,self.netlist['n273']], isweak=False, parent=self),
            NMOS("t222", [self.port['vss'].netconn,self.netlist['n307'],self.netlist['n846']], isweak=False, parent=self),
            NMOS("t3357", [self.netlist['n1531'],self.port['vss'].netconn,self.netlist['noty3']], isweak=False, parent=self),
            NMOS("t2171", [self.port['vss'].netconn,self.netlist['n1259'],self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2503", [self.netlist['n583'],self.netlist['alub1'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t528", [self.netlist['alu6'],self.netlist['adl6'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t29", [self.port['vss'].netconn,self.netlist['n1616'],self.netlist['pipeUNK05']], isweak=False, parent=self),
            NMOS("t831", [self.netlist['n1557'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t830", [self.netlist['n594'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t21", [self.netlist['nots0'],self.netlist['n983'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t20", [self.netlist['n272'],self.netlist['n1162'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t23", [self.netlist['n395'],self.netlist['n472'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t22", [self.netlist['n468'],self.netlist['n1615'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t25", [self.port['vss'].netconn,self.netlist['n1100'],self.netlist['abl0']], isweak=False, parent=self),
            NMOS("t24", [self.netlist['p3'],self.netlist['n1495'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t27", [self.port['vcc'].netconn,self.netlist['n855'],self.netlist['abl0']], isweak=False, parent=self),
            NMOS("t26", [self.netlist['n1660'],self.port['vss'].netconn,self.netlist['abl0']], isweak=False, parent=self),
            NMOS("t832", [self.netlist['n259'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t789", [self.port['vss'].netconn,self.netlist['ir2'],self.netlist['n1300']], isweak=False, parent=self),
            NMOS("t835", [self.port['vss'].netconn,self.netlist['n352'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t788", [self.port['vss'].netconn,self.netlist['n219'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1922", [self.port['vcc'].netconn,self.port['ab2'].netconn,self.netlist['n1152']], isweak=False, parent=self),
            NMOS("t834", [self.netlist['n791'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t837", [self.netlist['n932'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2539", [self.port['vss'].netconn,self.netlist['n930'],self.netlist['n1276']], isweak=False, parent=self),
            NMOS("t2538", [self.netlist['n1416'],self.port['vss'].netconn,self.netlist['idb6']], isweak=False, parent=self),
            NMOS("t2537", [self.netlist['adl2'],self.port['vss'].netconn,self.netlist['n1193']], isweak=False, parent=self),
            NMOS("t2536", [self.netlist['n133'],self.port['vss'].netconn,self.netlist['n1404']], isweak=False, parent=self),
            NMOS("t2535", [self.netlist['n289'],self.netlist['n635'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t520", [self.netlist['idl1'],self.netlist['n87'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2533", [self.port['vss'].netconn,self.netlist['n975'],self.netlist['n854']], isweak=False, parent=self),
            NMOS("t2532", [self.netlist['adl3'],self.netlist['pclp3'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t2531", [self.netlist['pclp2'],self.netlist['adl2'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t2530", [self.netlist['adl1'],self.netlist['pclp1'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t138", [self.netlist['n1559'],self.netlist['n477'],self.netlist['alub5']], isweak=False, parent=self),
            NMOS("t2775", [self.netlist['dpc26_ACDB'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2509", [self.port['vss'].netconn,self.netlist['n378'],self.netlist['n1357']], isweak=False, parent=self),
            NMOS("t1209", [self.netlist['sb5'],self.netlist['alu5'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t130", [self.netlist['dpc38_PCLADL'],self.port['vcc'].netconn,self.netlist['n1369']], isweak=False, parent=self),
            NMOS("t131", [self.netlist['n816'],self.port['vss'].netconn,self.netlist['n925']], isweak=False, parent=self),
            NMOS("t132", [self.netlist['sb7'],self.netlist['n721'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t133", [self.netlist['sb6'],self.netlist['n618'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t134", [self.port['vss'].netconn,self.netlist['n1043'],self.netlist['n818']], isweak=False, parent=self),
            NMOS("t135", [self.netlist['dpc40_ADLPCL'],self.port['vcc'].netconn,self.netlist['n818']], isweak=False, parent=self),
            NMOS("t136", [self.netlist['dasb4'],self.netlist['n3'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t137", [self.port['vss'].netconn,self.netlist['n1426'],self.netlist['n270']], isweak=False, parent=self),
            NMOS("t3288", [self.port['vss'].netconn,self.netlist['n660'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2952", [self.port['vss'].netconn,self.netlist['n1664'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3282", [self.port['vss'].netconn,self.netlist['n1239'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2955", [self.netlist['n286'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3280", [self.port['vss'].netconn,self.netlist['n487'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3281", [self.port['vss'].netconn,self.netlist['n579'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3286", [self.port['vss'].netconn,self.netlist['n1210'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3287", [self.port['vss'].netconn,self.netlist['n461'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3284", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2770", [self.netlist['n1249'],self.netlist['n626'],self.netlist['DBNeg']], isweak=False, parent=self),
            NMOS("t2957", [self.netlist['n370'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2956", [self.netlist['n271'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2890", [self.netlist['pchp1'],self.port['vss'].netconn,self.netlist['n113']], isweak=False, parent=self),
            NMOS("t2675", [self.port['vss'].netconn,self.netlist['n172'],self.netlist['abl5']], isweak=False, parent=self),
            NMOS("t2892", [self.port['vss'].netconn,self.netlist['n1687'],self.netlist['idb0']], isweak=False, parent=self),
            NMOS("t3130", [self.netlist['pipeUNK15'],self.netlist['n1391'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3131", [self.netlist['n1255'],self.port['vss'].netconn,self.netlist['n531']], isweak=False, parent=self),
            NMOS("t3132", [self.netlist['dpc13_ORS'],self.port['vcc'].netconn,self.netlist['n531']], isweak=False, parent=self),
            NMOS("t3133", [self.netlist['n298'],self.port['vcc'].netconn,self.netlist['dor7']], isweak=False, parent=self),
            NMOS("t3134", [self.netlist['n999'],self.netlist['n668'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3135", [self.netlist['n907'],self.netlist['n1298'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t3136", [self.netlist['n1404'],self.netlist['n1106'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3137", [self.netlist['idl5'],self.port['vss'].netconn,self.netlist['notidl5']], isweak=False, parent=self),
            NMOS("t2403", [self.port['vss'].netconn,self.netlist['n594'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2670", [self.netlist['n368'],self.port['vss'].netconn,self.netlist['n528']], isweak=False, parent=self),
            NMOS("t2401", [self.port['vss'].netconn,self.netlist['n1074'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2400", [self.port['vss'].netconn,self.netlist['n1086'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2407", [self.netlist['n791'],self.port['vss'].netconn,self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2406", [self.port['vss'].netconn,self.netlist['n1052'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2405", [self.port['vss'].netconn,self.netlist['n447'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2778", [self.netlist['n66'],self.port['vcc'].netconn,self.netlist['n842']], isweak=False, parent=self),
            NMOS("t2896", [self.port['vss'].netconn,self.netlist['n587'],self.netlist['pipeUNK12']], isweak=False, parent=self),
            NMOS("t2673", [self.port['vss'].netconn,self.netlist['n696'],self.netlist['n217']], isweak=False, parent=self),
            NMOS("t2393", [self.port['vss'].netconn,self.netlist['n1324'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2392", [self.port['vss'].netconn,self.netlist['n257'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2391", [self.port['vss'].netconn,self.netlist['n1381'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2390", [self.port['vss'].netconn,self.netlist['n1520'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2397", [self.port['vss'].netconn,self.netlist['n1396'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2396", [self.port['vss'].netconn,self.netlist['n4'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2395", [self.netlist['n131'],self.port['vss'].netconn,self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2394", [self.port['vss'].netconn,self.netlist['n179'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2399", [self.port['vss'].netconn,self.netlist['n354'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2398", [self.port['vss'].netconn,self.netlist['n167'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t549", [self.netlist['notalu3'],self.netlist['n1071'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t548", [self.netlist['n193'],self.port['vss'].netconn,self.netlist['C12']], isweak=False, parent=self),
            NMOS("t541", [self.netlist['n237'],self.netlist['n1641'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t540", [self.netlist['dpc29_0ADH17'],self.port['vss'].netconn,self.netlist['n1635']], isweak=False, parent=self),
            NMOS("t543", [self.netlist['n845'],self.netlist['n1426'],self.netlist['n1662']], isweak=False, parent=self),
            NMOS("t542", [self.netlist['n409'],self.netlist['n724'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t545", [self.netlist['n916'],self.netlist['n387'],self.netlist['n206']], isweak=False, parent=self),
            NMOS("t544", [self.netlist['n80'],self.port['vss'].netconn,self.netlist['n267']], isweak=False, parent=self),
            NMOS("t547", [self.netlist['n1572'],self.netlist['n22'],self.netlist['C12']], isweak=False, parent=self),
            NMOS("t546", [self.netlist['n1071'],self.netlist['n649'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t2241", [self.netlist['idb6'],self.netlist['n326'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2240", [self.netlist['idb5'],self.netlist['n831'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2243", [self.port['vss'].netconn,self.netlist['n540'],self.netlist['pd4']], isweak=False, parent=self),
            NMOS("t2242", [self.netlist['idb7'],self.netlist['n1592'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2245", [self.port['vss'].netconn,self.netlist['n1568'],self.netlist['n1345']], isweak=False, parent=self),
            NMOS("t2244", [self.netlist['n1685'],self.netlist['n1542'],self.netlist['n1345']], isweak=False, parent=self),
            NMOS("t2247", [self.netlist['n1533'],self.netlist['n1180'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1849", [self.netlist['n1028'],self.port['vss'].netconn,self.netlist['n251']], isweak=False, parent=self),
            NMOS("t1846", [self.netlist['a5'],self.netlist['dasb5'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1847", [self.netlist['a6'],self.netlist['dasb6'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1844", [self.netlist['a3'],self.netlist['dasb3'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1845", [self.netlist['a4'],self.netlist['dasb4'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1842", [self.netlist['a1'],self.netlist['dasb1'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1843", [self.netlist['dasb2'],self.netlist['a2'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t1840", [self.port['vss'].netconn,self.netlist['n1691'],self.netlist['alub2']], isweak=False, parent=self),
            NMOS("t1841", [self.netlist['a0'],self.netlist['dasb0'],self.netlist['dpc23_SBAC']], isweak=False, parent=self),
            NMOS("t2087", [self.port['vss'].netconn,self.netlist['n368'],self.netlist['n932']], isweak=False, parent=self),
            NMOS("t2086", [self.port['vss'].netconn,self.netlist['n556'],self.netlist['a4']], isweak=False, parent=self),
            NMOS("t2085", [self.netlist['pipeUNK04'],self.netlist['n1194'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2084", [self.port['vss'].netconn,self.netlist['n470'],self.netlist['n646']], isweak=False, parent=self),
            NMOS("t2083", [self.port['vss'].netconn,self.port['db0'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t2082", [self.netlist['n385'],self.netlist['pipeUNK30'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2081", [self.netlist['n912'],self.port['vss'].netconn,self.netlist['VEC1']], isweak=False, parent=self),
            NMOS("t2080", [self.netlist['n160'],self.port['vss'].netconn,self.netlist['n781']], isweak=False, parent=self),
            NMOS("t2089", [self.port['vss'].netconn,self.netlist['n291'],self.netlist['n1121']], isweak=False, parent=self),
            NMOS("t2088", [self.netlist['n1352'],self.port['vss'].netconn,self.netlist['n932']], isweak=False, parent=self),
            NMOS("t1280", [self.netlist['n928'],self.port['vss'].netconn,self.netlist['n667']], isweak=False, parent=self),
            NMOS("t1281", [self.netlist['NMIP'],self.netlist['n891'],self.netlist['n284']], isweak=False, parent=self),
            NMOS("t1282", [self.port['vss'].netconn,self.netlist['n1070'],self.netlist['pch1']], isweak=False, parent=self),
            NMOS("t1283", [self.port['vss'].netconn,self.netlist['n60'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1284", [self.port['vss'].netconn,self.netlist['n1512'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1285", [self.port['vss'].netconn,self.netlist['n1173'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1286", [self.port['vss'].netconn,self.netlist['n258'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1287", [self.port['vss'].netconn,self.netlist['n245'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1288", [self.port['vss'].netconn,self.netlist['n682'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1289", [self.port['vss'].netconn,self.netlist['n492'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1856", [self.netlist['idb1'],self.netlist['sb1'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t1014", [self.netlist['n1075'],self.netlist['pd4'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t435", [self.port['vcc'].netconn,self.netlist['n635'],self.netlist['n1523']], isweak=False, parent=self),
            NMOS("t434", [self.port['vss'].netconn,self.netlist['n963'],self.netlist['n1523']], isweak=False, parent=self),
            NMOS("t437", [self.netlist['dpc32_PCHADH'],self.port['vcc'].netconn,self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t436", [self.port['vss'].netconn,self.netlist['n1413'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t431", [self.netlist['n15'],self.netlist['n474'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t430", [self.port['vss'].netconn,self.netlist['n21'],self.netlist['n1162']], isweak=False, parent=self),
            NMOS("t433", [self.netlist['n1035'],self.port['vss'].netconn,self.netlist['n962']], isweak=False, parent=self),
            NMOS("t432", [self.netlist['dasb0'],self.netlist['n1169'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t439", [self.port['vcc'].netconn,self.netlist['n639'],self.netlist['n220']], isweak=False, parent=self),
            NMOS("t438", [self.netlist['n130'],self.port['vss'].netconn,self.netlist['n220']], isweak=False, parent=self),
            NMOS("t496", [self.netlist['n942'],self.netlist['C01'],self.netlist['n1628']], isweak=False, parent=self),
            NMOS("t945", [self.netlist['n428'],self.netlist['n1558'],self.netlist['n16']], isweak=False, parent=self),
            NMOS("t944", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n341']], isweak=False, parent=self),
            NMOS("t947", [self.port['so'].netconn,self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t946", [self.netlist['n591'],self.netlist['n252'],self.netlist['n691']], isweak=False, parent=self),
            NMOS("t941", [self.netlist['n277'],self.netlist['n1469'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t940", [self.netlist['n296'],self.netlist['n308'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t943", [self.netlist['n177'],self.netlist['n304'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t2877", [self.netlist['n264'],self.netlist['n799'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t949", [self.netlist['n786'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t948", [self.port['vss'].netconn,self.netlist['n1053'],self.netlist['Pout3']], isweak=False, parent=self),
            NMOS("t2667", [self.netlist['n1638'],self.port['vss'].netconn,self.port['db6'].netconn], isweak=False, parent=self),
            NMOS("t2666", [self.port['vss'].netconn,self.netlist['n1107'],self.netlist['n1204']], isweak=False, parent=self),
            NMOS("t2665", [self.port['vss'].netconn,self.netlist['n191'],self.netlist['n790']], isweak=False, parent=self),
            NMOS("t2888", [self.port['vss'].netconn,self.netlist['n811'],self.netlist['n838']], isweak=False, parent=self),
            NMOS("t2887", [self.netlist['n1460'],self.port['vss'].netconn,self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t2886", [self.port['vss'].netconn,self.netlist['n1671'],self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t2669", [self.netlist['n465'],self.port['vss'].netconn,self.netlist['n206']], isweak=False, parent=self),
            NMOS("t2668", [self.netlist['n836'],self.netlist['n768'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t2883", [self.netlist['n465'],self.netlist['n430'],self.netlist['n771']], isweak=False, parent=self),
            NMOS("t2882", [self.netlist['n1446'],self.port['vss'].netconn,self.netlist['n771']], isweak=False, parent=self),
            NMOS("t2881", [self.netlist['n241'],self.port['vss'].netconn,self.netlist['n745']], isweak=False, parent=self),
            NMOS("t2880", [self.netlist['n252'],self.port['vss'].netconn,self.netlist['n301']], isweak=False, parent=self),
            NMOS("t604", [self.port['vss'].netconn,self.netlist['n1658'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1068", [self.port['vss'].netconn,self.netlist['n950'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1069", [self.netlist['n607'],self.port['vss'].netconn,self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1064", [self.port['vss'].netconn,self.netlist['n309'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1065", [self.port['vss'].netconn,self.netlist['n1646'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1066", [self.port['vss'].netconn,self.netlist['n904'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1067", [self.port['vss'].netconn,self.netlist['n1476'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1060", [self.port['vss'].netconn,self.netlist['n285'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1061", [self.port['vss'].netconn,self.netlist['n594'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1062", [self.port['vss'].netconn,self.netlist['n1052'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t1063", [self.port['vss'].netconn,self.netlist['n1589'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t2865", [self.port['vss'].netconn,self.netlist['n1554'],self.netlist['n61']], isweak=False, parent=self),
            NMOS("t2864", [self.netlist['pipeT2out'],self.netlist['n1575'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2867", [self.port['vss'].netconn,self.netlist['notx4'],self.netlist['x4']], isweak=False, parent=self),
            NMOS("t2866", [self.netlist['n479'],self.port['vss'].netconn,self.netlist['n61']], isweak=False, parent=self),
            NMOS("t2861", [self.netlist['n941'],self.port['vss'].netconn,self.netlist['pipeUNK09']], isweak=False, parent=self),
            NMOS("t2860", [self.netlist['n301'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2259", [self.netlist['n526'],self.netlist['n1500'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2862", [self.port['vss'].netconn,self.netlist['n25'],self.netlist['n256']], isweak=False, parent=self),
            NMOS("t2869", [self.port['vss'].netconn,self.netlist['dor4'],self.netlist['notdor4']], isweak=False, parent=self),
            NMOS("t2868", [self.port['vss'].netconn,self.netlist['dasb6'],self.netlist['n479']], isweak=False, parent=self),
            NMOS("t605", [self.port['vss'].netconn,self.netlist['n245'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2128", [self.port['vss'].netconn,self.netlist['n374'],self.port['db6'].netconn], isweak=False, parent=self),
            NMOS("t1442", [self.netlist['n1155'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1443", [self.netlist['n301'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1440", [self.port['vss'].netconn,self.netlist['n1210'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1441", [self.port['vss'].netconn,self.netlist['n461'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1446", [self.netlist['n944'],self.port['vss'].netconn,self.netlist['n759']], isweak=False, parent=self),
            NMOS("t1447", [self.netlist['n343'],self.netlist['n1300'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t1444", [self.netlist['n1385'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1445", [self.port['db3'].netconn,self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t493", [self.port['vss'].netconn,self.netlist['n1480'],self.netlist['n1472']], isweak=False, parent=self),
            NMOS("t1448", [self.netlist['n664'],self.port['vss'].netconn,self.netlist['n1006']], isweak=False, parent=self),
            NMOS("t1449", [self.netlist['n330'],self.netlist['IRQP'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2961", [self.port['vss'].netconn,self.netlist['n784'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2149", [self.port['vcc'].netconn,self.netlist['adl6'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1668", [self.netlist['n1107'],self.port['vss'].netconn,self.netlist['n1428']], isweak=False, parent=self),
            NMOS("t1669", [self.netlist['n604'],self.port['vss'].netconn,self.netlist['n1428']], isweak=False, parent=self),
            NMOS("t1662", [self.port['vss'].netconn,self.netlist['n620'],self.netlist['n1371']], isweak=False, parent=self),
            NMOS("t1663", [self.port['vss'].netconn,self.netlist['n51'],self.netlist['Pout3']], isweak=False, parent=self),
            NMOS("t1660", [self.port['vss'].netconn,self.netlist['n476'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t1661", [self.netlist['n1213'],self.port['vss'].netconn,self.netlist['n453']], isweak=False, parent=self),
            NMOS("t1667", [self.port['vss'].netconn,self.netlist['n1541'],self.netlist['n1477']], isweak=False, parent=self),
            NMOS("t1664", [self.netlist['n334'],self.port['vss'].netconn,self.netlist['p2']], isweak=False, parent=self),
            NMOS("t1665", [self.netlist['n605'],self.port['vss'].netconn,self.netlist['n1002']], isweak=False, parent=self),
            NMOS("t2962", [self.port['vss'].netconn,self.netlist['n764'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2963", [self.netlist['n1582'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1716", [self.netlist['INTG'],self.netlist['n50'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1717", [self.port['vss'].netconn,self.netlist['n36'],self.netlist['n600']], isweak=False, parent=self),
            NMOS("t1714", [self.netlist['n611'],self.port['vss'].netconn,self.netlist['n43']], isweak=False, parent=self),
            NMOS("t1715", [self.netlist['n1106'],self.port['vss'].netconn,self.netlist['n245']], isweak=False, parent=self),
            NMOS("t1712", [self.port['db0'].netconn,self.port['vcc'].netconn,self.netlist['n1325']], isweak=False, parent=self),
            NMOS("t1710", [self.netlist['n972'],self.port['vss'].netconn,self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1711", [self.netlist['AxB1'],self.port['vss'].netconn,self.netlist['n936']], isweak=False, parent=self),
            NMOS("t3079", [self.netlist['n324'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t1718", [self.netlist['n1048'],self.port['vss'].netconn,self.netlist['n1721']], isweak=False, parent=self),
            NMOS("t1719", [self.netlist['n935'],self.netlist['n1636'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2437", [self.port['rw'].netconn,self.port['vss'].netconn,self.netlist['n1696']], isweak=False, parent=self),
            NMOS("t935", [self.port['vcc'].netconn,self.netlist['dpc14_SRS'],self.netlist['n1593']], isweak=False, parent=self),
            NMOS("t2884", [self.netlist['n766'],self.netlist['n474'],self.netlist['n1184']], isweak=False, parent=self),
            NMOS("t3127", [self.netlist['n538'],self.port['vss'].netconn,self.netlist['n1599']], isweak=False, parent=self),
            NMOS("t301", [self.port['db5'].netconn,self.port['vss'].netconn,self.netlist['n612']], isweak=False, parent=self),
            NMOS("t300", [self.port['vss'].netconn,self.netlist['n1724'],self.netlist['notx6']], isweak=False, parent=self),
            NMOS("t1479", [self.netlist['n889'],self.port['vss'].netconn,self.netlist['n1114']], isweak=False, parent=self),
            NMOS("t3126", [self.netlist['fetch'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t309", [self.netlist['n417'],self.port['vss'].netconn,self.netlist['n445']], isweak=False, parent=self),
            NMOS("t308", [self.netlist['n317'],self.port['vss'].netconn,self.netlist['n445']], isweak=False, parent=self),
            NMOS("t3125", [self.port['vss'].netconn,self.netlist['notir5'],self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t844", [self.port['vss'].netconn,self.netlist['n1292'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2050", [self.netlist['n1296'],self.port['vss'].netconn,self.netlist['n1346']], isweak=False, parent=self),
            NMOS("t845", [self.netlist['n1646'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t736", [self.port['vss'].netconn,self.netlist['n784'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t936", [self.netlist['n957'],self.netlist['n1525'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t846", [self.netlist['n1114'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t737", [self.port['vss'].netconn,self.netlist['n764'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2966", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t847", [self.netlist['n1476'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t734", [self.port['vss'].netconn,self.netlist['n1612'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t840", [self.netlist['n528'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t735", [self.port['vss'].netconn,self.netlist['n1487'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t841", [self.netlist['n309'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2340", [self.netlist['notalu2'],self.netlist['n740'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t842", [self.netlist['n1430'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2341", [self.netlist['n1000'],self.port['vss'].netconn,self.netlist['n1466']], isweak=False, parent=self),
            NMOS("t937", [self.netlist['n953'],self.netlist['n250'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t843", [self.port['vss'].netconn,self.netlist['n691'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2342", [self.port['vss'].netconn,self.netlist['n753'],self.netlist['n1257']], isweak=False, parent=self),
            NMOS("t2967", [self.port['vss'].netconn,self.netlist['n1520'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1125", [self.netlist['n509'],self.netlist['n442'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2343", [self.port['vss'].netconn,self.netlist['n711'],self.netlist['n1257']], isweak=False, parent=self),
            NMOS("t1656", [self.netlist['n113'],self.port['vss'].netconn,self.netlist['n126']], isweak=False, parent=self),
            NMOS("t2344", [self.netlist['n569'],self.port['vss'].netconn,self.netlist['n1257']], isweak=False, parent=self),
            NMOS("t1655", [self.port['vss'].netconn,self.netlist['n1720'],self.netlist['dor5']], isweak=False, parent=self),
            NMOS("t2345", [self.port['vss'].netconn,self.netlist['n440'],self.netlist['n24']], isweak=False, parent=self),
            NMOS("t1654", [self.port['vss'].netconn,self.netlist['n612'],self.netlist['dor5']], isweak=False, parent=self),
            NMOS("t2430", [self.netlist['n1632'],self.port['vss'].netconn,self.netlist['alua5']], isweak=False, parent=self),
            NMOS("t239", [self.netlist['n689'],self.port['vss'].netconn,self.netlist['n370']], isweak=False, parent=self),
            NMOS("t238", [self.netlist['n1147'],self.netlist['adh7'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t237", [self.netlist['n1014'],self.netlist['adh6'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t236", [self.netlist['n1387'],self.netlist['adh5'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t235", [self.netlist['n1095'],self.netlist['adh4'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t234", [self.netlist['n1661'],self.netlist['adh3'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t233", [self.netlist['n1424'],self.netlist['adh2'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t232", [self.netlist['n87'],self.netlist['adh1'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t231", [self.netlist['n719'],self.netlist['adh0'],self.netlist['n41']], isweak=False, parent=self),
            NMOS("t1120", [self.port['vss'].netconn,self.netlist['pclp5'],self.netlist['n1326']], isweak=False, parent=self),
            NMOS("t1123", [self.port['vss'].netconn,self.netlist['n436'],self.netlist['notx4']], isweak=False, parent=self),
            NMOS("t343", [self.netlist['dpc17_SUMS'],self.port['vss'].netconn,self.netlist['n1305']], isweak=False, parent=self),
            NMOS("t1650", [self.netlist['n1169'],self.port['vss'].netconn,self.netlist['notx0']], isweak=False, parent=self),
            NMOS("t939", [self.netlist['n1071'],self.netlist['n884'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t38", [self.port['vss'].netconn,self.netlist['n510'],self.netlist['n347']], isweak=False, parent=self),
            NMOS("t39", [self.netlist['n883'],self.netlist['n1667'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t36", [self.port['vcc'].netconn,self.netlist['dasb4'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t37", [self.netlist['nots4'],self.netlist['n973'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t34", [self.netlist['y6'],self.netlist['n518'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t35", [self.netlist['n31'],self.port['vss'].netconn,self.netlist['p0']], isweak=False, parent=self),
            NMOS("t32", [self.netlist['n1378'],self.netlist['n928'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t33", [self.netlist['n74'],self.netlist['n1309'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t30", [self.netlist['n375'],self.netlist['n651'],self.netlist['C34']], isweak=False, parent=self),
            NMOS("t31", [self.netlist['n65'],self.port['vss'].netconn,self.netlist['C34']], isweak=False, parent=self),
            NMOS("t624", [self.netlist['n1396'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2528", [self.netlist['adl7'],self.netlist['pclp7'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t2529", [self.netlist['pclp0'],self.netlist['adl0'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t2520", [self.netlist['notRnWprepad'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t2521", [self.netlist['n1718'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t2522", [self.netlist['n837'],self.port['vss'].netconn,self.netlist['n1623']], isweak=False, parent=self),
            NMOS("t2523", [self.port['vcc'].netconn,self.port['clk1out'].netconn,self.netlist['n747']], isweak=False, parent=self),
            NMOS("t2524", [self.netlist['n1715'],self.port['vss'].netconn,self.netlist['n358']], isweak=False, parent=self),
            NMOS("t2525", [self.netlist['pclp4'],self.netlist['adl4'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t2526", [self.netlist['adl5'],self.netlist['pclp5'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t2527", [self.netlist['pclp6'],self.netlist['adl6'],self.netlist['dpc38_PCLADL']], isweak=False, parent=self),
            NMOS("t129", [self.netlist['n1462'],self.port['vss'].netconn,self.netlist['n1369']], isweak=False, parent=self),
            NMOS("t128", [self.netlist['sb2'],self.netlist['n1389'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t2629", [self.netlist['n327'],self.netlist['pipeUNK09'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t123", [self.netlist['n514'],self.netlist['n429'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t122", [self.port['vss'].netconn,self.netlist['n1358'],self.netlist['n917']], isweak=False, parent=self),
            NMOS("t121", [self.netlist['pclp7'],self.port['vss'].netconn,self.netlist['n536']], isweak=False, parent=self),
            NMOS("t120", [self.port['vss'].netconn,self.netlist['n692'],self.netlist['n460']], isweak=False, parent=self),
            NMOS("t127", [self.netlist['sb3'],self.netlist['n998'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t126", [self.netlist['n393'],self.netlist['n1179'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t125", [self.netlist['n1570'],self.netlist['n430'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t124", [self.netlist['n1268'],self.port['vss'].netconn,self.netlist['DBZ']], isweak=False, parent=self),
            NMOS("t2147", [self.netlist['notidl7'],self.netlist['n588'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t631", [self.netlist['n594'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1883", [self.netlist['n171'],self.netlist['n28'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2414", [self.port['vss'].netconn,self.netlist['n1114'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2415", [self.port['vss'].netconn,self.netlist['n1226'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2416", [self.port['vss'].netconn,self.netlist['n1006'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2417", [self.port['vss'].netconn,self.netlist['n1164'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2410", [self.port['vss'].netconn,self.netlist['n1589'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2411", [self.port['vss'].netconn,self.netlist['n309'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2412", [self.port['vss'].netconn,self.netlist['n1430'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2413", [self.port['vss'].netconn,self.netlist['n1292'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2418", [self.port['vss'].netconn,self.netlist['n950'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2419", [self.port['vss'].netconn,self.netlist['n281'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2885", [self.netlist['n410'],self.port['vss'].netconn,self.netlist['n1184']], isweak=False, parent=self),
            NMOS("t3383", [self.netlist['n312'],self.port['vss'].netconn,self.port['res'].netconn], isweak=False, parent=self),
            NMOS("t3382", [self.port['vss'].netconn,self.netlist['dpc27_SBADH'],self.netlist['n1271']], isweak=False, parent=self),
            NMOS("t3381", [self.netlist['DBZ'],self.port['vss'].netconn,self.netlist['idb0']], isweak=False, parent=self),
            NMOS("t3380", [self.netlist['n1185'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t3387", [self.port['vss'].netconn,self.netlist['n252'],self.netlist['n950']], isweak=False, parent=self),
            NMOS("t3386", [self.netlist['n743'],self.port['vss'].netconn,self.netlist['n499']], isweak=False, parent=self),
            NMOS("t3385", [self.netlist['n1659'],self.port['vss'].netconn,self.netlist['n499']], isweak=False, parent=self),
            NMOS("t3384", [self.netlist['sb2'],self.netlist['alu2'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t3435", [self.port['vss'].netconn,self.netlist['n432'],self.netlist['sb3']], isweak=False, parent=self),
            NMOS("t3434", [self.port['vcc'].netconn,self.netlist['dpc39_PCLPCL'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3437", [self.netlist['n714'],self.port['vss'].netconn,self.netlist['n906']], isweak=False, parent=self),
            NMOS("t3388", [self.netlist['n618'],self.port['vss'].netconn,self.netlist['nots6']], isweak=False, parent=self),
            NMOS("t3431", [self.port['vss'].netconn,self.netlist['n1196'],self.netlist['n934']], isweak=False, parent=self),
            NMOS("t3430", [self.port['vss'].netconn,self.netlist['n1691'],self.netlist['alua2']], isweak=False, parent=self),
            NMOS("t3433", [self.netlist['n1518'],self.port['vss'].netconn,self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3432", [self.netlist['n1585'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2388", [self.port['vss'].netconn,self.netlist['n1057'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2389", [self.port['vss'].netconn,self.netlist['n58'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2384", [self.port['vss'].netconn,self.netlist['n1482'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2385", [self.port['vss'].netconn,self.netlist['n552'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2386", [self.port['vss'].netconn,self.netlist['n1487'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2387", [self.port['vss'].netconn,self.netlist['n764'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2380", [self.port['vss'].netconn,self.netlist['n245'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2381", [self.port['vss'].netconn,self.netlist['n786'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2382", [self.port['vss'].netconn,self.netlist['n1664'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2383", [self.port['vss'].netconn,self.netlist['n682'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2648", [self.netlist['C12'],self.port['vss'].netconn,self.netlist['n1122']], isweak=False, parent=self),
            NMOS("t636", [self.port['vss'].netconn,self.netlist['n1419'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t625", [self.netlist['n167'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2252", [self.netlist['n994'],self.port['vss'].netconn,self.netlist['abh2']], isweak=False, parent=self),
            NMOS("t2253", [self.netlist['n347'],self.port['vss'].netconn,self.netlist['n219']], isweak=False, parent=self),
            NMOS("t2250", [self.netlist['n1545'],self.port['vcc'].netconn,self.netlist['abh2']], isweak=False, parent=self),
            NMOS("t2251", [self.netlist['n1034'],self.port['vss'].netconn,self.netlist['abh2']], isweak=False, parent=self),
            NMOS("t2256", [self.netlist['n582'],self.port['vss'].netconn,self.netlist['n610']], isweak=False, parent=self),
            NMOS("t2257", [self.netlist['sb7'],self.netlist['n1251'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t2254", [self.netlist['adh1'],self.netlist['sb1'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t1915", [self.netlist['n17'],self.port['vss'].netconn,self.netlist['n964']], isweak=False, parent=self),
            NMOS("t1873", [self.netlist['n774'],self.port['vss'].netconn,self.netlist['n1419']], isweak=False, parent=self),
            NMOS("t1872", [self.netlist['n454'],self.port['vss'].netconn,self.netlist['n616']], isweak=False, parent=self),
            NMOS("t1871", [self.netlist['n742'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1870", [self.netlist['abl3'],self.port['vss'].netconn,self.netlist['n825']], isweak=False, parent=self),
            NMOS("t1877", [self.netlist['n922'],self.port['vss'].netconn,self.netlist['n620']], isweak=False, parent=self),
            NMOS("t1916", [self.netlist['clock1'],self.port['vss'].netconn,self.netlist['n964']], isweak=False, parent=self),
            NMOS("t1875", [self.port['vss'].netconn,self.netlist['dor6'],self.netlist['notdor6']], isweak=False, parent=self),
            NMOS("t1874", [self.port['vss'].netconn,self.netlist['n1258'],self.netlist['n390']], isweak=False, parent=self),
            NMOS("t2090", [self.netlist['n733'],self.port['vss'].netconn,self.netlist['noty5']], isweak=False, parent=self),
            NMOS("t2091", [self.netlist['n66'],self.netlist['n107'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2092", [self.port['vcc'].netconn,self.netlist['n475'],self.netlist['abh4']], isweak=False, parent=self),
            NMOS("t656", [self.port['vss'].netconn,self.netlist['n546'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t2094", [self.netlist['n999'],self.port['vss'].netconn,self.netlist['abh4']], isweak=False, parent=self),
            NMOS("t2095", [self.netlist['notalu0'],self.netlist['n957'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2096", [self.port['vss'].netconn,self.netlist['n1506'],self.netlist['C01']], isweak=False, parent=self),
            NMOS("t2097", [self.netlist['n1122'],self.netlist['n1510'],self.netlist['C01']], isweak=False, parent=self),
            NMOS("t2098", [self.netlist['n1175'],self.port['vss'].netconn,self.netlist['n1447']], isweak=False, parent=self),
            NMOS("t1910", [self.netlist['n903'],self.netlist['n1631'],self.netlist['n1184']], isweak=False, parent=self),
            NMOS("t1911", [self.port['vcc'].netconn,self.netlist['adh2'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1279", [self.netlist['notalu4'],self.netlist['n296'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1912", [self.netlist['n1172'],self.netlist['n1085'],self.netlist['n372']], isweak=False, parent=self),
            NMOS("t1275", [self.port['vss'].netconn,self.netlist['dpc35_PCHC'],self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t1274", [self.port['vss'].netconn,self.netlist['n311'],self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t1277", [self.port['vss'].netconn,self.netlist['n35'],self.netlist['n796']], isweak=False, parent=self),
            NMOS("t1913", [self.netlist['n1290'],self.netlist['n912'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1271", [self.netlist['pipeUNK12'],self.netlist['n340'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1270", [self.netlist['n1353'],self.netlist['n254'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1273", [self.netlist['n206'],self.netlist['n430'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t1272", [self.netlist['C23'],self.netlist['n433'],self.netlist['n681']], isweak=False, parent=self),
            NMOS("t440", [self.netlist['n102'],self.port['vss'].netconn,self.netlist['n400']], isweak=False, parent=self),
            NMOS("t441", [self.netlist['n1696'],self.port['vcc'].netconn,self.netlist['n400']], isweak=False, parent=self),
            NMOS("t442", [self.netlist['n1696'],self.port['vss'].netconn,self.netlist['n834']], isweak=False, parent=self),
            NMOS("t443", [self.netlist['n400'],self.port['vss'].netconn,self.netlist['n834']], isweak=False, parent=self),
            NMOS("t444", [self.port['vss'].netconn,self.netlist['notx7'],self.netlist['x7']], isweak=False, parent=self),
            NMOS("t445", [self.port['vss'].netconn,self.netlist['n656'],self.netlist['n604']], isweak=False, parent=self),
            NMOS("t634", [self.netlist['n1476'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t447", [self.netlist['n1012'],self.port['vss'].netconn,self.netlist['n1246']], isweak=False, parent=self),
            NMOS("t448", [self.netlist['n949'],self.port['vss'].netconn,self.netlist['dpc35_PCHC']], isweak=False, parent=self),
            NMOS("t449", [self.netlist['n1406'],self.port['vss'].netconn,self.netlist['dpc35_PCHC']], isweak=False, parent=self),
            NMOS("t1468", [self.netlist['n607'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t930", [self.netlist['n1040'],self.port['vss'].netconn,self.netlist['n383']], isweak=False, parent=self),
            NMOS("t687", [self.netlist['n1367'],self.port['vss'].netconn,self.netlist['n1202']], isweak=False, parent=self),
            NMOS("t684", [self.netlist['n1081'],self.netlist['pipeUNK32'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t933", [self.netlist['n1495'],self.netlist['n1445'],self.netlist['n270']], isweak=False, parent=self),
            NMOS("t682", [self.netlist['n389'],self.netlist['pipeUNK31'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t683", [self.netlist['n249'],self.port['vss'].netconn,self.netlist['pcl3']], isweak=False, parent=self),
            NMOS("t680", [self.port['vss'].netconn,self.netlist['n1164'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t681", [self.netlist['pipeUNK33'],self.netlist['n473'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t938", [self.netlist['n740'],self.netlist['n701'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t659", [self.netlist['n179'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t688", [self.netlist['n57'],self.port['vss'].netconn,self.netlist['n1202']], isweak=False, parent=self),
            NMOS("t689", [self.netlist['n620'],self.port['vss'].netconn,self.netlist['n307']], isweak=False, parent=self),
            NMOS("t2898", [self.netlist['n1109'],self.port['vss'].netconn,self.netlist['n902']], isweak=False, parent=self),
            NMOS("t872", [self.netlist['n10'],self.port['vss'].netconn,self.netlist['n1721']], isweak=False, parent=self),
            NMOS("t2678", [self.port['vss'].netconn,self.netlist['n43'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2674", [self.port['vss'].netconn,self.netlist['n210'],self.netlist['abl5']], isweak=False, parent=self),
            NMOS("t2891", [self.netlist['n759'],self.netlist['notRnWprepad'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2676", [self.port['vcc'].netconn,self.netlist['n1633'],self.netlist['abl5']], isweak=False, parent=self),
            NMOS("t2677", [self.port['vss'].netconn,self.netlist['n1618'],self.netlist['n419']], isweak=False, parent=self),
            NMOS("t2894", [self.netlist['ir7'],self.port['vss'].netconn,self.netlist['n541']], isweak=False, parent=self),
            NMOS("t2895", [self.netlist['sb1'],self.netlist['alu1'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t2672", [self.netlist['n143'],self.port['vss'].netconn,self.netlist['alua0']], isweak=False, parent=self),
            NMOS("t2897", [self.netlist['dasb0'],self.netlist['alu0'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t1019", [self.port['vss'].netconn,self.netlist['n1716'],self.netlist['n510']], isweak=False, parent=self),
            NMOS("t1018", [self.netlist['n716'],self.netlist['n701'],self.netlist['n110']], isweak=False, parent=self),
            NMOS("t1011", [self.port['vss'].netconn,self.netlist['n674'],self.netlist['n25']], isweak=False, parent=self),
            NMOS("t1010", [self.netlist['notir6'],self.netlist['n1675'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1013", [self.netlist['n1281'],self.netlist['pd3'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1012", [self.netlist['pd5'],self.netlist['n1588'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1015", [self.netlist['a1'],self.netlist['n929'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3442", [self.port['db6'].netconn,self.port['vcc'].netconn,self.netlist['n7']], isweak=False, parent=self),
            NMOS("t1017", [self.netlist['notidl6'],self.netlist['n1638'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1016", [self.netlist['n1223'],self.port['vss'].netconn,self.netlist['n688']], isweak=False, parent=self),
            NMOS("t2876", [self.port['vss'].netconn,self.netlist['n570'],self.netlist['AxB5']], isweak=False, parent=self),
            NMOS("t1388", [self.netlist['alu0'],self.port['vss'].netconn,self.netlist['notalu0']], isweak=False, parent=self),
            NMOS("t2874", [self.netlist['n523'],self.netlist['n949'],self.netlist['n83']], isweak=False, parent=self),
            NMOS("t2875", [self.netlist['n1406'],self.port['vss'].netconn,self.netlist['n83']], isweak=False, parent=self),
            NMOS("t2872", [self.port['vss'].netconn,self.netlist['n1433'],self.netlist['n840']], isweak=False, parent=self),
            NMOS("t2873", [self.netlist['n381'],self.port['vcc'].netconn,self.netlist['n1315']], isweak=False, parent=self),
            NMOS("t2870", [self.netlist['n134'],self.port['vss'].netconn,self.netlist['n259']], isweak=False, parent=self),
            NMOS("t2871", [self.port['vss'].netconn,self.netlist['dor3'],self.netlist['notdor3']], isweak=False, parent=self),
            NMOS("t1381", [self.port['vss'].netconn,self.netlist['n1388'],self.netlist['AxB1']], isweak=False, parent=self),
            NMOS("t1380", [self.port['vss'].netconn,self.netlist['n1517'],self.netlist['n853']], isweak=False, parent=self),
            NMOS("t1383", [self.port['vss'].netconn,self.netlist['n1584'],self.netlist['n876']], isweak=False, parent=self),
            NMOS("t1382", [self.port['vss'].netconn,self.netlist['n295'],self.netlist['AxB1']], isweak=False, parent=self),
            NMOS("t1385", [self.port['vss'].netconn,self.netlist['n326'],self.netlist['n1356']], isweak=False, parent=self),
            NMOS("t1384", [self.netlist['idb6'],self.netlist['pclp6'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t2878", [self.netlist['n264'],self.netlist['n1693'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2879", [self.port['vss'].netconn,self.netlist['n46'],self.netlist['n992']], isweak=False, parent=self),
            NMOS("t592", [self.netlist['n1147'],self.netlist['idb7'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t593", [self.port['vss'].netconn,self.netlist['n1368'],self.netlist['NMIL']], isweak=False, parent=self),
            NMOS("t590", [self.netlist['n1387'],self.netlist['idb5'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t591", [self.netlist['n1014'],self.netlist['idb6'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t848", [self.netlist['n1226'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t849", [self.netlist['n1569'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t594", [self.port['ab7'].netconn,self.port['vcc'].netconn,self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1478", [self.netlist['n646'],self.port['vss'].netconn,self.netlist['n17']], isweak=False, parent=self),
            NMOS("t1477", [self.netlist['clock1'],self.port['vcc'].netconn,self.netlist['n17']], isweak=False, parent=self),
            NMOS("t1476", [self.netlist['n907'],self.netlist['n676'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1475", [self.netlist['dpc9_DBADD'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1474", [self.port['vss'].netconn,self.netlist['n992'],self.netlist['n595']], isweak=False, parent=self),
            NMOS("t1473", [self.port['vss'].netconn,self.netlist['n239'],self.netlist['n595']], isweak=False, parent=self),
            NMOS("t1472", [self.netlist['n543'],self.port['vss'].netconn,self.netlist['n339']], isweak=False, parent=self),
            NMOS("t1471", [self.netlist['dpc15_ANDS'],self.port['vcc'].netconn,self.netlist['n91']], isweak=False, parent=self),
            NMOS("t1470", [self.netlist['n1256'],self.port['vss'].netconn,self.netlist['n91']], isweak=False, parent=self),
            NMOS("t1657", [self.port['vss'].netconn,self.netlist['n1391'],self.netlist['n750']], isweak=False, parent=self),
            NMOS("t1124", [self.port['vss'].netconn,self.netlist['n809'],self.netlist['pd1']], isweak=False, parent=self),
            NMOS("t1127", [self.netlist['n1601'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1126", [self.netlist['n564'],self.port['vss'].netconn,self.netlist['noty0']], isweak=False, parent=self),
            NMOS("t1653", [self.netlist['n1149'],self.netlist['n1368'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1652", [self.netlist['pipeUNK16'],self.netlist['n31'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1651", [self.netlist['n531'],self.port['vss'].netconn,self.netlist['n95']], isweak=False, parent=self),
            NMOS("t1122", [self.netlist['n834'],self.port['vss'].netconn,self.netlist['n402']], isweak=False, parent=self),
            NMOS("t1129", [self.netlist['n1173'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1128", [self.netlist['n382'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1659", [self.netlist['n532'],self.port['vss'].netconn,self.netlist['n1217']], isweak=False, parent=self),
            NMOS("t1658", [self.netlist['n1610'],self.port['vss'].netconn,self.netlist['AxB3']], isweak=False, parent=self),
            NMOS("t1495", [self.port['vss'].netconn,self.netlist['n924'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t3080", [self.netlist['n712'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t1496", [self.netlist['cp1'],self.port['vss'].netconn,self.netlist['n1105']], isweak=False, parent=self),
            NMOS("t1491", [self.port['vss'].netconn,self.netlist['n643'],self.netlist['dor3']], isweak=False, parent=self),
            NMOS("t1490", [self.netlist['n595'],self.port['vss'].netconn,self.netlist['n354']], isweak=False, parent=self),
            NMOS("t1493", [self.netlist['n1134'],self.netlist['n1431'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1492", [self.port['vss'].netconn,self.netlist['n1613'],self.netlist['dor3']], isweak=False, parent=self),
            NMOS("t2977", [self.port['vss'].netconn,self.netlist['n303'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3082", [self.netlist['n575'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3083", [self.netlist['n1466'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3084", [self.netlist['n776'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3085", [self.netlist['n822'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3086", [self.netlist['n131'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t2487", [self.netlist['adh5'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t3087", [self.netlist['n1420'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t2338", [self.port['vss'].netconn,self.netlist['n161'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3446", [self.netlist['n760'],self.netlist['n629'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t785", [self.port['vss'].netconn,self.netlist['n1710'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1723", [self.netlist['n998'],self.netlist['adl3'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t1722", [self.netlist['n3'],self.netlist['adl4'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t1721", [self.netlist['n280'],self.netlist['adl5'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t1720", [self.port['vss'].netconn,self.netlist['n503'],self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t1727", [self.netlist['adl7'],self.netlist['n721'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t1726", [self.port['vss'].netconn,self.netlist['n553'],self.netlist['n1662']], isweak=False, parent=self),
            NMOS("t1725", [self.port['vss'].netconn,self.netlist['n1004'],self.netlist['n1408']], isweak=False, parent=self),
            NMOS("t2975", [self.port['vss'].netconn,self.netlist['n131'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1729", [self.netlist['abl1'],self.port['vss'].netconn,self.netlist['n107']], isweak=False, parent=self),
            NMOS("t1728", [self.port['vss'].netconn,self.netlist['n1347'],self.netlist['n862']], isweak=False, parent=self),
            NMOS("t2489", [self.port['vss'].netconn,self.netlist['n550'],self.netlist['n1228']], isweak=False, parent=self),
            NMOS("t2336", [self.netlist['adh3'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2974", [self.port['vss'].netconn,self.netlist['n257'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3283", [self.port['vss'].netconn,self.netlist['n1524'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2740", [self.netlist['n1398'],self.port['vss'].netconn,self.netlist['alub7']], isweak=False, parent=self),
            NMOS("t338", [self.port['vss'].netconn,self.netlist['pclp0'],self.netlist['n1227']], isweak=False, parent=self),
            NMOS("t339", [self.port['vss'].netconn,self.netlist['n182'],self.netlist['n0']], isweak=False, parent=self),
            NMOS("t336", [self.netlist['n1605'],self.netlist['n1183'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t337", [self.netlist['n793'],self.netlist['n1181'],self.netlist['n1595']], isweak=False, parent=self),
            NMOS("t334", [self.netlist['pipeUNK36'],self.netlist['n261'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t335", [self.netlist['n323'],self.netlist['n959'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t332", [self.port['vss'].netconn,self.netlist['n442'],self.netlist['n182']], isweak=False, parent=self),
            NMOS("t333", [self.netlist['n798'],self.port['vcc'].netconn,self.netlist['dor1']], isweak=False, parent=self),
            NMOS("t330", [self.port['vss'].netconn,self.netlist['n335'],self.netlist['n347']], isweak=False, parent=self),
            NMOS("t3243", [self.port['vss'].netconn,self.netlist['n1543'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2973", [self.netlist['n157'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2801", [self.port['vss'].netconn,self.netlist['n1294'],self.netlist['n1605']], isweak=False, parent=self),
            NMOS("t2555", [self.netlist['n779'],self.netlist['n605'],self.netlist['n1440']], isweak=False, parent=self),
            NMOS("t1461", [self.netlist['n579'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t2800", [self.netlist['n423'],self.netlist['alub7'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t2972", [self.netlist['n776'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t71", [self.port['vss'].netconn,self.netlist['n667'],self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t1462", [self.netlist['n120'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t2809", [self.netlist['n809'],self.port['vss'].netconn,self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t202", [self.netlist['n813'],self.port['vss'].netconn,self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t203", [self.netlist['n720'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t200", [self.netlist['n1203'],self.port['vss'].netconn,self.netlist['n1135']], isweak=False, parent=self),
            NMOS("t201", [self.netlist['n1629'],self.port['vss'].netconn,self.netlist['n1135']], isweak=False, parent=self),
            NMOS("t204", [self.netlist['n1371'],self.port['vss'].netconn,self.netlist['n1045']], isweak=False, parent=self),
            NMOS("t205", [self.port['ab12'].netconn,self.port['vss'].netconn,self.netlist['n999']], isweak=False, parent=self),
            NMOS("t1463", [self.netlist['n677'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t942", [self.netlist['n722'],self.netlist['n1459'],self.netlist['dpc16_EORS']], isweak=False, parent=self),
            NMOS("t1464", [self.netlist['n447'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t2153", [self.port['vcc'].netconn,self.netlist['dpc8_nDBADD'],self.netlist['n1534']], isweak=False, parent=self),
            NMOS("t116", [self.netlist['DC34'],self.netlist['n972'],self.netlist['n1610']], isweak=False, parent=self),
            NMOS("t117", [self.netlist['n1497'],self.netlist['n653'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t114", [self.netlist['n1145'],self.port['vss'].netconn,self.netlist['n403']], isweak=False, parent=self),
            NMOS("t115", [self.port['vss'].netconn,self.netlist['dor1'],self.netlist['notdor1']], isweak=False, parent=self),
            NMOS("t112", [self.port['vss'].netconn,self.netlist['alua3'],self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t113", [self.netlist['n365'],self.port['vss'].netconn,self.netlist['n1410']], isweak=False, parent=self),
            NMOS("t110", [self.port['vss'].netconn,self.netlist['n1346'],self.netlist['abh3']], isweak=False, parent=self),
            NMOS("t111", [self.port['vss'].netconn,self.netlist['n359'],self.netlist['abh3']], isweak=False, parent=self),
            NMOS("t118", [self.port['vss'].netconn,self.netlist['abh7'],self.netlist['n429']], isweak=False, parent=self),
            NMOS("t119", [self.netlist['n10'],self.port['vss'].netconn,self.netlist['n467']], isweak=False, parent=self),
            NMOS("t1465", [self.netlist['n660'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t2152", [self.netlist['n763'],self.port['vss'].netconn,self.netlist['n1534']], isweak=False, parent=self),
            NMOS("t3285", [self.port['vss'].netconn,self.netlist['n1478'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t1466", [self.netlist['n1430'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1259", [self.port['vss'].netconn,self.netlist['AxB5'],self.netlist['n1632']], isweak=False, parent=self),
            NMOS("t2326", [self.netlist['n863'],self.port['vcc'].netconn,self.netlist['n1566']], isweak=False, parent=self),
            NMOS("t2461", [self.port['vss'].netconn,self.netlist['n1469'],self.netlist['AxB5']], isweak=False, parent=self),
            NMOS("t2460", [self.netlist['n100'],self.port['vss'].netconn,self.netlist['n1018']], isweak=False, parent=self),
            NMOS("t2463", [self.netlist['n368'],self.port['vss'].netconn,self.netlist['n1430']], isweak=False, parent=self),
            NMOS("t2462", [self.netlist['n778'],self.port['vss'].netconn,self.netlist['n231']], isweak=False, parent=self),
            NMOS("t2464", [self.port['vss'].netconn,self.netlist['n911'],self.netlist['n877']], isweak=False, parent=self),
            NMOS("t2467", [self.netlist['n602'],self.port['vss'].netconn,self.netlist['n133']], isweak=False, parent=self),
            NMOS("t2466", [self.netlist['n847'],self.port['vss'].netconn,self.netlist['n300']], isweak=False, parent=self),
            NMOS("t2469", [self.port['vss'].netconn,self.netlist['n1201'],self.netlist['n709']], isweak=False, parent=self),
            NMOS("t2468", [self.netlist['dpc2_XSB'],self.port['vcc'].netconn,self.netlist['n133']], isweak=False, parent=self),
            NMOS("t1467", [self.port['vss'].netconn,self.netlist['n904'],self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1258", [self.port['vss'].netconn,self.netlist['n1236'],self.netlist['n1632']], isweak=False, parent=self),
            NMOS("t760", [self.port['vss'].netconn,self.netlist['n1074'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t763", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t622", [self.netlist['n1342'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t762", [self.port['vss'].netconn,self.netlist['n579'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t3398", [self.netlist['n334'],self.netlist['pipeUNK17'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3399", [self.port['vcc'].netconn,self.port['ab1'].netconn,self.netlist['n1479']], isweak=False, parent=self),
            NMOS("t3428", [self.port['vss'].netconn,self.netlist['AxB3'],self.netlist['n649']], isweak=False, parent=self),
            NMOS("t3429", [self.port['vss'].netconn,self.netlist['n452'],self.netlist['alua2']], isweak=False, parent=self),
            NMOS("t3426", [self.port['vss'].netconn,self.netlist['n570'],self.netlist['n122']], isweak=False, parent=self),
            NMOS("t3427", [self.port['vss'].netconn,self.netlist['n1313'],self.netlist['n649']], isweak=False, parent=self),
            NMOS("t3396", [self.port['vss'].netconn,self.netlist['n152'],self.netlist['n1002']], isweak=False, parent=self),
            NMOS("t3397", [self.netlist['n1407'],self.port['vss'].netconn,self.netlist['n572']], isweak=False, parent=self),
            NMOS("t3422", [self.port['vss'].netconn,self.netlist['n1501'],self.netlist['dor7']], isweak=False, parent=self),
            NMOS("t3423", [self.port['vss'].netconn,self.netlist['n23'],self.netlist['dor7']], isweak=False, parent=self),
            NMOS("t3392", [self.port['vss'].netconn,self.port['ab2'].netconn,self.netlist['n642']], isweak=False, parent=self),
            NMOS("t3421", [self.netlist['n936'],self.port['vss'].netconn,self.netlist['n841']], isweak=False, parent=self),
            NMOS("t427", [self.port['vcc'].netconn,self.netlist['adl5'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1864", [self.port['vss'].netconn,self.netlist['n1144'],self.netlist['n1571']], isweak=False, parent=self),
            NMOS("t1865", [self.netlist['Pout3'],self.port['vss'].netconn,self.netlist['n1194']], isweak=False, parent=self),
            NMOS("t1866", [self.netlist['n1178'],self.port['vss'].netconn,self.netlist['pipeUNK33']], isweak=False, parent=self),
            NMOS("t1867", [self.netlist['n398'],self.netlist['n824'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1860", [self.netlist['sb5'],self.netlist['idb5'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t1861", [self.netlist['sb6'],self.netlist['idb6'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t1862", [self.netlist['idb7'],self.netlist['sb7'],self.netlist['dpc25_SBDB']], isweak=False, parent=self),
            NMOS("t1863", [self.netlist['n1124'],self.netlist['n1065'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1868", [self.port['vss'].netconn,self.netlist['n728'],self.netlist['VEC0']], isweak=False, parent=self),
            NMOS("t1869", [self.netlist['DC34'],self.netlist['n972'],self.netlist['n388']], isweak=False, parent=self),
            NMOS("t2444", [self.port['vss'].netconn,self.netlist['n925'],self.netlist['n517']], isweak=False, parent=self),
            NMOS("t2269", [self.netlist['n734'],self.port['vss'].netconn,self.netlist['n1540']], isweak=False, parent=self),
            NMOS("t2268", [self.netlist['n1519'],self.netlist['n738'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2267", [self.netlist['n1185'],self.port['vss'].netconn,self.netlist['pipeUNK36']], isweak=False, parent=self),
            NMOS("t2266", [self.netlist['n445'],self.port['vss'].netconn,self.netlist['n862']], isweak=False, parent=self),
            NMOS("t2265", [self.netlist['n824'],self.port['vss'].netconn,self.netlist['n579']], isweak=False, parent=self),
            NMOS("t2264", [self.port['vss'].netconn,self.netlist['n499'],self.netlist['pch5']], isweak=False, parent=self),
            NMOS("t2263", [self.netlist['sb5'],self.netlist['n733'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t2262", [self.netlist['sb6'],self.netlist['n518'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t2261", [self.port['vss'].netconn,self.netlist['n603'],self.netlist['n47']], isweak=False, parent=self),
            NMOS("t2260", [self.netlist['dasb4'],self.netlist['n658'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t2655", [self.netlist['n1717'],self.port['vss'].netconn,self.netlist['n1512']], isweak=False, parent=self),
            NMOS("t2069", [self.port['vss'].netconn,self.netlist['n1215'],self.netlist['n238']], isweak=False, parent=self),
            NMOS("t2068", [self.port['vss'].netconn,self.netlist['n1578'],self.netlist['n1431']], isweak=False, parent=self),
            NMOS("t2065", [self.netlist['n267'],self.port['vss'].netconn,self.netlist['n785']], isweak=False, parent=self),
            NMOS("t2067", [self.netlist['dasb2'],self.port['vss'].netconn,self.netlist['n1159']], isweak=False, parent=self),
            NMOS("t2066", [self.port['vcc'].netconn,self.netlist['RnWstretched'],self.netlist['n1028']], isweak=False, parent=self),
            NMOS("t2063", [self.netlist['AxB7'],self.port['vss'].netconn,self.netlist['n748']], isweak=False, parent=self),
            NMOS("t2285", [self.netlist['n786'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2284", [self.port['vss'].netconn,self.netlist['n1658'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2287", [self.netlist['n1612'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2286", [self.netlist['n1664'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2281", [self.netlist['n460'],self.netlist['n616'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2280", [self.netlist['dpc24_ACSB'],self.port['vcc'].netconn,self.netlist['n628']], isweak=False, parent=self),
            NMOS("t2283", [self.netlist['n76'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2282", [self.netlist['n1233'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1266", [self.netlist['n169'],self.netlist['pipeUNK29'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1267", [self.port['vss'].netconn,self.netlist['n1714'],self.netlist['pipeUNK26']], isweak=False, parent=self),
            NMOS("t1264", [self.netlist['notdor0'],self.netlist['n1687'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1265", [self.netlist['n1625'],self.netlist['n299'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2289", [self.port['vss'].netconn,self.netlist['n244'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2288", [self.netlist['n784'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1260", [self.port['vss'].netconn,self.netlist['n1498'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t1261", [self.port['vss'].netconn,self.netlist['n903'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t452", [self.netlist['n1129'],self.port['vss'].netconn,self.netlist['n358']], isweak=False, parent=self),
            NMOS("t451", [self.netlist['notRnWprepad'],self.netlist['n402'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t450", [self.netlist['idb0'],self.netlist['alub0'],self.netlist['dpc9_DBADD']], isweak=False, parent=self),
            NMOS("t457", [self.netlist['notidl5'],self.netlist['n568'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2940", [self.netlist['n1380'],self.netlist['n666'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t455", [self.netlist['sb7'],self.netlist['n871'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t454", [self.netlist['n1113'],self.netlist['n1717'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t459", [self.port['vss'].netconn,self.netlist['n990'],self.netlist['abl3']], isweak=False, parent=self),
            NMOS("t458", [self.port['vss'].netconn,self.netlist['n138'],self.netlist['abl3']], isweak=False, parent=self),
            NMOS("t2012", [self.port['vss'].netconn,self.netlist['dpc37_PCLDB'],self.netlist['n1323']], isweak=False, parent=self),
            NMOS("t1331", [self.netlist['a5'],self.netlist['n831'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t923", [self.netlist['n1085'],self.netlist['n1365'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t690", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n784']], isweak=False, parent=self),
            NMOS("t693", [self.port['vss'].netconn,self.netlist['n1026'],self.netlist['abl7']], isweak=False, parent=self),
            NMOS("t692", [self.port['vss'].netconn,self.netlist['n171'],self.netlist['abl7']], isweak=False, parent=self),
            NMOS("t695", [self.netlist['n8'],self.port['vss'].netconn,self.netlist['n551']], isweak=False, parent=self),
            NMOS("t926", [self.netlist['notdor3'],self.netlist['n457'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t697", [self.port['vss'].netconn,self.port['nmi'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t924", [self.netlist['n92'],self.netlist['n359'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t699", [self.port['vss'].netconn,self.netlist['dpc10_ADLADD'],self.netlist['n491']], isweak=False, parent=self),
            NMOS("t698", [self.port['vss'].netconn,self.netlist['n1275'],self.netlist['pipeUNK19']], isweak=False, parent=self),
            NMOS("t929", [self.port['vss'].netconn,self.netlist['dor2'],self.netlist['notdor2']], isweak=False, parent=self),
            NMOS("t2609", [self.netlist['n1594'],self.netlist['n656'],self.netlist['n779']], isweak=False, parent=self),
            NMOS("t2608", [self.port['vss'].netconn,self.netlist['n1006'],self.netlist['n1050']], isweak=False, parent=self),
            NMOS("t1884", [self.port['vss'].netconn,self.netlist['dpc10_ADLADD'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t954", [self.port['vss'].netconn,self.netlist['n1324'],self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t2601", [self.netlist['n537'],self.netlist['n862'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2600", [self.netlist['notidl1'],self.netlist['n213'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2603", [self.port['vss'].netconn,self.netlist['n1685'],self.netlist['n1166']], isweak=False, parent=self),
            NMOS("t2602", [self.netlist['notdor7'],self.netlist['n789'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2605", [self.netlist['n855'],self.port['vss'].netconn,self.netlist['n1660']], isweak=False, parent=self),
            NMOS("t2604", [self.port['vss'].netconn,self.netlist['n1568'],self.netlist['n1166']], isweak=False, parent=self),
            NMOS("t2607", [self.netlist['n1712'],self.port['vss'].netconn,self.netlist['n1134']], isweak=False, parent=self),
            NMOS("t2606", [self.port['vcc'].netconn,self.netlist['n1100'],self.netlist['n1660']], isweak=False, parent=self),
            NMOS("t2146", [self.netlist['x0'],self.netlist['n1169'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1008", [self.netlist['n902'],self.netlist['notRdy0'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1009", [self.port['vss'].netconn,self.netlist['notir2'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3081", [self.netlist['n787'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t1002", [self.port['vss'].netconn,self.netlist['n295'],self.netlist['n1506']], isweak=False, parent=self),
            NMOS("t1003", [self.netlist['n7'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1000", [self.port['vss'].netconn,self.netlist['n771'],self.netlist['n1110']], isweak=False, parent=self),
            NMOS("t1001", [self.netlist['n1388'],self.netlist['n965'],self.netlist['n1506']], isweak=False, parent=self),
            NMOS("t1006", [self.port['vss'].netconn,self.netlist['n920'],self.netlist['pipeUNK27']], isweak=False, parent=self),
            NMOS("t1007", [self.port['vss'].netconn,self.netlist['n651'],self.netlist['n65']], isweak=False, parent=self),
            NMOS("t1005", [self.netlist['n466'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t2843", [self.netlist['n1623'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2842", [self.netlist['n784'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t1398", [self.port['vss'].netconn,self.netlist['n636'],self.netlist['n1239']], isweak=False, parent=self),
            NMOS("t1399", [self.netlist['n106'],self.netlist['n732'],self.netlist['n792']], isweak=False, parent=self),
            NMOS("t2847", [self.netlist['n257'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2846", [self.netlist['n1355'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2845", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2844", [self.netlist['n403'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t1392", [self.netlist['pd2'],self.netlist['n111'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1393", [self.netlist['pd7'],self.netlist['n62'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2849", [self.netlist['n1086'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t1391", [self.netlist['n698'],self.netlist['n1290'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1397", [self.netlist['alu1'],self.port['vss'].netconn,self.netlist['notalu1']], isweak=False, parent=self),
            NMOS("t1394", [self.netlist['pd6'],self.netlist['n374'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1395", [self.port['vss'].netconn,self.netlist['n888'],self.netlist['IRQP']], isweak=False, parent=self),
            NMOS("t628", [self.port['vss'].netconn,self.netlist['n1721'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2115", [self.netlist['n671'],self.netlist['n1718'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2114", [self.port['vss'].netconn,self.netlist['n1030'],self.netlist['n757']], isweak=False, parent=self),
            NMOS("t2117", [self.netlist['n1069'],self.port['vss'].netconn,self.netlist['n1024']], isweak=False, parent=self),
            NMOS("t2116", [self.port['vss'].netconn,self.netlist['n1130'],self.netlist['n192']], isweak=False, parent=self),
            NMOS("t2111", [self.port['vss'].netconn,self.netlist['n667'],self.netlist['pd5']], isweak=False, parent=self),
            NMOS("t588", [self.netlist['n1661'],self.netlist['idb3'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t859", [self.port['vss'].netconn,self.netlist['n1610'],self.netlist['n216']], isweak=False, parent=self),
            NMOS("t858", [self.port['vss'].netconn,self.netlist['n516'],self.netlist['n216']], isweak=False, parent=self),
            NMOS("t857", [self.netlist['n802'],self.netlist['n566'],self.netlist['n243']], isweak=False, parent=self),
            NMOS("t584", [self.netlist['n511'],self.port['vss'].netconn,self.netlist['pipeUNK17']], isweak=False, parent=self),
            NMOS("t855", [self.netlist['n846'],self.port['vss'].netconn,self.netlist['n840']], isweak=False, parent=self),
            NMOS("t586", [self.netlist['n87'],self.netlist['idb1'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t581", [self.netlist['n1679'],self.netlist['notRdy0'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t580", [self.netlist['clock1'],self.port['vss'].netconn,self.netlist['n732']], isweak=False, parent=self),
            NMOS("t583", [self.port['vss'].netconn,self.netlist['n1327'],self.netlist['n748']], isweak=False, parent=self),
            NMOS("t582", [self.netlist['n1215'],self.netlist['n223'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1136", [self.netlist['n245'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1641", [self.netlist['sb1'],self.netlist['y1'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t1642", [self.netlist['n504'],self.netlist['n137'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t1135", [self.netlist['n1540'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1132", [self.netlist['n1543'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1645", [self.port['vss'].netconn,self.netlist['n1433'],self.netlist['n90']], isweak=False, parent=self),
            NMOS("t1646", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n120']], isweak=False, parent=self),
            NMOS("t1131", [self.port['vss'].netconn,self.netlist['n1562'],self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1648", [self.port['vss'].netconn,self.netlist['n404'],self.netlist['alub4']], isweak=False, parent=self),
            NMOS("t1649", [self.netlist['n1352'],self.port['vss'].netconn,self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t1460", [self.port['vss'].netconn,self.netlist['n1381'],self.netlist['t3']], isweak=False, parent=self),
            NMOS("t1138", [self.netlist['n786'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1177", [self.netlist['n384'],self.port['vss'].netconn,self.netlist['n946']], isweak=False, parent=self),
            NMOS("t1486", [self.port['vss'].netconn,self.netlist['n1322'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1487", [self.port['vss'].netconn,self.netlist['n735'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1484", [self.netlist['n1424'],self.netlist['adl2'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t1485", [self.netlist['n719'],self.netlist['adl0'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t1482", [self.netlist['n1095'],self.netlist['adl4'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t1483", [self.netlist['n87'],self.netlist['adl1'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t1480", [self.port['vss'].netconn,self.netlist['n327'],self.netlist['n1226']], isweak=False, parent=self),
            NMOS("t1481", [self.netlist['n1661'],self.netlist['adl3'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t1488", [self.netlist['n471'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1336", [self.port['vss'].netconn,self.netlist['n678'],self.netlist['n1357']], isweak=False, parent=self),
            NMOS("t2950", [self.port['vss'].netconn,self.netlist['n1233'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t934", [self.netlist['n1552'],self.port['vss'].netconn,self.netlist['n1593']], isweak=False, parent=self),
            NMOS("t1337", [self.netlist['n1600'],self.port['vss'].netconn,self.netlist['idb3']], isweak=False, parent=self),
            NMOS("t1738", [self.netlist['n19'],self.port['vss'].netconn,self.netlist['n770']], isweak=False, parent=self),
            NMOS("t1739", [self.port['vcc'].netconn,self.netlist['sb1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t795", [self.netlist['n1466'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t1735", [self.netlist['idl7'],self.port['vss'].netconn,self.netlist['notidl7']], isweak=False, parent=self),
            NMOS("t1730", [self.netlist['n1151'],self.netlist['n182'],self.netlist['n236']], isweak=False, parent=self),
            NMOS("t1731", [self.netlist['pchp3'],self.port['vss'].netconn,self.netlist['n124']], isweak=False, parent=self),
            NMOS("t1732", [self.netlist['n1215'],self.netlist['n1528'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1733", [self.netlist['n109'],self.netlist['n1161'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t329", [self.netlist['dasb0'],self.netlist['n564'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t328", [self.port['vss'].netconn,self.netlist['n388'],self.netlist['AxB1']], isweak=False, parent=self),
            NMOS("t321", [self.netlist['adl2'],self.netlist['alu2'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t320", [self.port['vss'].netconn,self.netlist['n817'],self.netlist['AxB5']], isweak=False, parent=self),
            NMOS("t323", [self.netlist['alu0'],self.netlist['adl0'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t322", [self.netlist['alu1'],self.netlist['adl1'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t325", [self.netlist['n501'],self.port['vss'].netconn,self.netlist['RESP']], isweak=False, parent=self),
            NMOS("t324", [self.netlist['n1464'],self.port['vss'].netconn,self.netlist['n784']], isweak=False, parent=self),
            NMOS("t327", [self.port['vss'].netconn,self.netlist['n261'],self.netlist['n447']], isweak=False, parent=self),
            NMOS("t326", [self.netlist['n913'],self.port['vss'].netconn,self.netlist['n1699']], isweak=False, parent=self),
            NMOS("t2129", [self.netlist['idb3'],self.netlist['Pout3'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t3290", [self.port['vss'].netconn,self.netlist['n259'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2697", [self.port['vss'].netconn,self.netlist['n1259'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t215", [self.port['vss'].netconn,self.netlist['n206'],self.netlist['alucout']], isweak=False, parent=self),
            NMOS("t214", [self.netlist['n1717'],self.port['vss'].netconn,self.netlist['n1173']], isweak=False, parent=self),
            NMOS("t217", [self.netlist['n1033'],self.port['vss'].netconn,self.netlist['n241']], isweak=False, parent=self),
            NMOS("t216", [self.netlist['n1106'],self.port['vss'].netconn,self.netlist['n76']], isweak=False, parent=self),
            NMOS("t213", [self.netlist['n876'],self.port['vss'].netconn,self.netlist['n867']], isweak=False, parent=self),
            NMOS("t212", [self.netlist['n29'],self.netlist['pipeUNK22'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t219", [self.netlist['n886'],self.netlist['n975'],self.netlist['n995']], isweak=False, parent=self),
            NMOS("t218", [self.netlist['dpc21_ADDADL'],self.port['vcc'].netconn,self.netlist['n241']], isweak=False, parent=self),
            NMOS("t3097", [self.netlist['n1646'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t1201", [self.port['vss'].netconn,self.netlist['n1566'],self.netlist['n1221']], isweak=False, parent=self),
            NMOS("t1809", [self.port['vss'].netconn,self.netlist['n1582'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t2951", [self.port['vss'].netconn,self.netlist['n1658'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1454", [self.netlist['n60'],self.port['vss'].netconn,self.netlist['t3']], isweak=False, parent=self),
            NMOS("t2347", [self.netlist['n1107'],self.port['vss'].netconn,self.netlist['n58']], isweak=False, parent=self),
            NMOS("t2363", [self.netlist['n146'],self.netlist['dasb0'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t101", [self.netlist['n207'],self.port['vss'].netconn,self.netlist['n810']], isweak=False, parent=self),
            NMOS("t100", [self.port['vss'].netconn,self.netlist['n371'],self.netlist['n555']], isweak=False, parent=self),
            NMOS("t103", [self.port['vss'].netconn,self.netlist['noty1'],self.netlist['y1']], isweak=False, parent=self),
            NMOS("t102", [self.port['vss'].netconn,self.netlist['n501'],self.netlist['n819']], isweak=False, parent=self),
            NMOS("t105", [self.port['vss'].netconn,self.netlist['n202'],self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t104", [self.port['ab14'].netconn,self.port['vcc'].netconn,self.netlist['n963']], isweak=False, parent=self),
            NMOS("t107", [self.port['vss'].netconn,self.netlist['n1563'],self.netlist['n1342']], isweak=False, parent=self),
            NMOS("t3098", [self.netlist['n1155'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t109", [self.netlist['n1296'],self.port['vcc'].netconn,self.netlist['abh3']], isweak=False, parent=self),
            NMOS("t108", [self.port['vss'].netconn,self.netlist['n844'],self.netlist['n786']], isweak=False, parent=self),
            NMOS("t3095", [self.netlist['n528'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t57", [self.netlist['n1400'],self.port['vss'].netconn,self.netlist['pch4']], isweak=False, parent=self),
            NMOS("t3093", [self.netlist['n0'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3092", [self.netlist['n579'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3091", [self.netlist['n1504'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3090", [self.netlist['n303'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3259", [self.port['vss'].netconn,self.netlist['n1428'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3258", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3255", [self.port['vss'].netconn,self.netlist['n784'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3254", [self.port['vss'].netconn,self.netlist['n1487'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3257", [self.port['vss'].netconn,self.netlist['n804'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3256", [self.port['vss'].netconn,self.netlist['n1582'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3251", [self.port['vss'].netconn,self.netlist['n370'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3250", [self.port['vss'].netconn,self.netlist['n271'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3253", [self.port['vss'].netconn,self.netlist['n1612'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t1204", [self.netlist['n1560'],self.port['vss'].netconn,self.netlist['n1355']], isweak=False, parent=self),
            NMOS("t3353", [self.netlist['adl7'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1640", [self.netlist['n242'],self.port['vss'].netconn,self.netlist['notx3']], isweak=False, parent=self),
            NMOS("t2369", [self.netlist['sb6'],self.netlist['n326'],self.netlist['dpc24_ACSB']], isweak=False, parent=self),
            NMOS("t2472", [self.netlist['n1075'],self.port['vss'].netconn,self.port['db4'].netconn], isweak=False, parent=self),
            NMOS("t2473", [self.netlist['n1007'],self.port['vss'].netconn,self.netlist['dpc34_PCLC']], isweak=False, parent=self),
            NMOS("t2470", [self.port['vss'].netconn,self.netlist['notx0'],self.netlist['x0']], isweak=False, parent=self),
            NMOS("t2471", [self.netlist['n1293'],self.port['vss'].netconn,self.netlist['n318']], isweak=False, parent=self),
            NMOS("t2476", [self.netlist['pchp7'],self.netlist['pch7'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2477", [self.netlist['pchp4'],self.netlist['pch4'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2474", [self.port['vss'].netconn,self.netlist['n176'],self.netlist['n236']], isweak=False, parent=self),
            NMOS("t2475", [self.netlist['pchp6'],self.netlist['pch6'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2478", [self.netlist['pchp5'],self.netlist['pch5'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2479", [self.netlist['pchp2'],self.netlist['pch2'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t3066", [self.port['vss'].netconn,self.netlist['dpc38_PCLADL'],self.netlist['n1462']], isweak=False, parent=self),
            NMOS("t3067", [self.port['vss'].netconn,self.netlist['BRtaken'],self.netlist['n1115']], isweak=False, parent=self),
            NMOS("t1142", [self.netlist['n665'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t2049", [self.port['vss'].netconn,self.netlist['n1412'],self.netlist['n1455']], isweak=False, parent=self),
            NMOS("t3355", [self.port['vss'].netconn,self.netlist['pclp1'],self.netlist['n1102']], isweak=False, parent=self),
            NMOS("t2048", [self.port['vss'].netconn,self.netlist['n726'],self.netlist['n0']], isweak=False, parent=self),
            NMOS("t2586", [self.port['vcc'].netconn,self.netlist['n869'],self.netlist['n1423']], isweak=False, parent=self),
            NMOS("t632", [self.netlist['n1292'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t3410", [self.port['vss'].netconn,self.port['db1'].netconn,self.netlist['n794']], isweak=False, parent=self),
            NMOS("t3417", [self.netlist['pipeUNK03'],self.netlist['n1155'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1811", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t2043", [self.netlist['n1649'],self.port['vss'].netconn,self.netlist['n857']], isweak=False, parent=self),
            NMOS("t1813", [self.port['vss'].netconn,self.netlist['n1086'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1812", [self.port['vss'].netconn,self.netlist['n157'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1815", [self.port['vss'].netconn,self.netlist['n1239'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1814", [self.port['vss'].netconn,self.netlist['n487'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1817", [self.port['vss'].netconn,self.netlist['n1524'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t2590", [self.netlist['abl4'],self.port['vss'].netconn,self.netlist['n364']], isweak=False, parent=self),
            NMOS("t1819", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1818", [self.port['vss'].netconn,self.netlist['n273'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t2041", [self.netlist['n1058'],self.port['vss'].netconn,self.netlist['n271']], isweak=False, parent=self),
            NMOS("t2278", [self.netlist['notir4'],self.netlist['n927'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2279", [self.port['vss'].netconn,self.netlist['n1335'],self.netlist['n628']], isweak=False, parent=self),
            NMOS("t2592", [self.netlist['n296'],self.netlist['n404'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t8", [self.netlist['n1199'],self.port['vss'].netconn,self.port['db2'].netconn], isweak=False, parent=self),
            NMOS("t9", [self.netlist['n1548'],self.netlist['n524'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t6", [self.netlist['n1514'],self.netlist['n289'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t2271", [self.netlist['n629'],self.port['vss'].netconn,self.netlist['n50']], isweak=False, parent=self),
            NMOS("t2272", [self.netlist['pipeUNK39'],self.netlist['n440'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t5", [self.netlist['n1319'],self.port['vss'].netconn,self.port['db1'].netconn], isweak=False, parent=self),
            NMOS("t2", [self.netlist['alucout'],self.port['vss'].netconn,self.netlist['notalucout']], isweak=False, parent=self),
            NMOS("t3", [self.netlist['cclk'],self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t2276", [self.netlist['pclp4'],self.port['vss'].netconn,self.netlist['n39']], isweak=False, parent=self),
            NMOS("t2277", [self.port['db7'].netconn,self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t3075", [self.netlist['n1612'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3074", [self.netlist['n271'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3077", [self.netlist['n244'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3076", [self.netlist['n1487'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3071", [self.netlist['n682'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3068", [self.netlist['n1658'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3073", [self.netlist['n286'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t2079", [self.netlist['pipeVectorA0'],self.netlist['n728'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2076", [self.port['vss'].netconn,self.netlist['n381'],self.netlist['abh0']], isweak=False, parent=self),
            NMOS("t2077", [self.netlist['n1045'],self.netlist['pipeUNK13'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2074", [self.netlist['n1069'],self.netlist['n1177'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2044", [self.netlist['n1377'],self.port['vss'].netconn,self.netlist['n857']], isweak=False, parent=self),
            NMOS("t2072", [self.port['vss'].netconn,self.netlist['dpc34_PCLC'],self.netlist['n232']], isweak=False, parent=self),
            NMOS("t2073", [self.netlist['n1316'],self.port['vss'].netconn,self.netlist['n232']], isweak=False, parent=self),
            NMOS("t2070", [self.port['vss'].netconn,self.netlist['dpc0_YSB'],self.netlist['n969']], isweak=False, parent=self),
            NMOS("t2071", [self.netlist['n585'],self.port['vss'].netconn,self.netlist['n232']], isweak=False, parent=self),
            NMOS("t2296", [self.port['vss'].netconn,self.netlist['n1355'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2297", [self.port['vss'].netconn,self.netlist['n787'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2294", [self.port['vss'].netconn,self.netlist['n857'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2295", [self.netlist['n1337'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2292", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2293", [self.port['vss'].netconn,self.netlist['n324'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2290", [self.port['vss'].netconn,self.netlist['n1623'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2291", [self.netlist['n764'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1253", [self.port['vss'].netconn,self.netlist['Pout0'],self.netlist['n31']], isweak=False, parent=self),
            NMOS("t1252", [self.netlist['n1275'],self.port['vss'].netconn,self.netlist['n778']], isweak=False, parent=self),
            NMOS("t1251", [self.netlist['n191'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1250", [self.port['vss'].netconn,self.netlist['n1665'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1257", [self.netlist['pipephi2Reset0x'],self.netlist['RESP'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1256", [self.port['vcc'].netconn,self.port['ab9'].netconn,self.netlist['n1140']], isweak=False, parent=self),
            NMOS("t2298", [self.netlist['n575'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1254", [self.netlist['n42'],self.port['vcc'].netconn,self.netlist['dor3']], isweak=False, parent=self),
            NMOS("t1328", [self.netlist['NMIL'],self.port['vss'].netconn,self.netlist['n882']], isweak=False, parent=self),
            NMOS("t468", [self.netlist['n964'],self.port['vss'].netconn,self.netlist['n554']], isweak=False, parent=self),
            NMOS("t469", [self.port['vss'].netconn,self.netlist['n1304'],self.netlist['n787']], isweak=False, parent=self),
            NMOS("t466", [self.port['vcc'].netconn,self.netlist['dpc7_SS'],self.netlist['n35']], isweak=False, parent=self),
            NMOS("t467", [self.port['vss'].netconn,self.netlist['n1180'],self.netlist['n554']], isweak=False, parent=self),
            NMOS("t464", [self.port['vss'].netconn,self.netlist['t5'],self.netlist['n378']], isweak=False, parent=self),
            NMOS("t465", [self.port['vss'].netconn,self.netlist['n71'],self.netlist['n35']], isweak=False, parent=self),
            NMOS("t462", [self.netlist['n182'],self.port['vss'].netconn,self.netlist['n1655']], isweak=False, parent=self),
            NMOS("t463", [self.port['vss'].netconn,self.netlist['n1356'],self.netlist['a6']], isweak=False, parent=self),
            NMOS("t460", [self.port['vcc'].netconn,self.netlist['n1041'],self.netlist['abl3']], isweak=False, parent=self),
            NMOS("t461", [self.netlist['n1214'],self.port['vss'].netconn,self.netlist['pipeUNK11']], isweak=False, parent=self),
            NMOS("t668", [self.netlist['n259'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t669", [self.netlist['n517'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t918", [self.port['vcc'].netconn,self.netlist['n1254'],self.netlist['n1195']], isweak=False, parent=self),
            NMOS("t919", [self.port['vss'].netconn,self.netlist['n1055'],self.netlist['n771']], isweak=False, parent=self),
            NMOS("t664", [self.port['vss'].netconn,self.netlist['n1504'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t665", [self.port['vss'].netconn,self.netlist['n487'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t914", [self.port['vss'].netconn,self.netlist['n721'],self.netlist['nots7']], isweak=False, parent=self),
            NMOS("t667", [self.netlist['n145'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t912", [self.netlist['n1534'],self.port['vss'].netconn,self.netlist['n43']], isweak=False, parent=self),
            NMOS("t661", [self.netlist['n4'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t662", [self.port['vss'].netconn,self.netlist['n167'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t663", [self.port['vss'].netconn,self.netlist['n303'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t2618", [self.port['vss'].netconn,self.netlist['dor7'],self.netlist['notdor7']], isweak=False, parent=self),
            NMOS("t2619", [self.netlist['n1703'],self.port['vss'].netconn,self.netlist['pipeT4out']], isweak=False, parent=self),
            NMOS("t2612", [self.netlist['n1196'],self.port['vss'].netconn,self.netlist['n1689']], isweak=False, parent=self),
            NMOS("t2613", [self.netlist['n826'],self.port['vss'].netconn,self.netlist['n1315']], isweak=False, parent=self),
            NMOS("t2610", [self.netlist['NMIP'],self.port['vss'].netconn,self.netlist['n297']], isweak=False, parent=self),
            NMOS("t2611", [self.netlist['n1344'],self.port['vss'].netconn,self.netlist['n556']], isweak=False, parent=self),
            NMOS("t2616", [self.netlist['y5'],self.netlist['n733'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2614", [self.port['vss'].netconn,self.netlist['n1202'],self.netlist['n1265']], isweak=False, parent=self),
            NMOS("t2615", [self.port['vss'].netconn,self.netlist['dpc35_PCHC'],self.netlist['n1265']], isweak=False, parent=self),
            NMOS("t2953", [self.port['vss'].netconn,self.netlist['n1482'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2858", [self.netlist['n309'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2859", [self.netlist['n1569'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2854", [self.netlist['n517'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2855", [self.netlist['n352'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2856", [self.netlist['n750'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2857", [self.netlist['n932'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2850", [self.netlist['n487'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2851", [self.netlist['n145'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2852", [self.netlist['n1478'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2853", [self.port['vss'].netconn,self.netlist['n1557'],self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t1325", [self.netlist['n1019'],self.port['vss'].netconn,self.netlist['n1622']], isweak=False, parent=self),
            NMOS("t2106", [self.netlist['n1097'],self.port['vss'].netconn,self.netlist['n345']], isweak=False, parent=self),
            NMOS("t2107", [self.netlist['n767'],self.port['vss'].netconn,self.netlist['noty1']], isweak=False, parent=self),
            NMOS("t868", [self.netlist['n1217'],self.port['vss'].netconn,self.netlist['AxB7']], isweak=False, parent=self),
            NMOS("t869", [self.netlist['n1157'],self.port['vss'].netconn,self.netlist['n291']], isweak=False, parent=self),
            NMOS("t2100", [self.port['vss'].netconn,self.netlist['n1154'],self.netlist['n959']], isweak=False, parent=self),
            NMOS("t2101", [self.port['ab7'].netconn,self.port['vss'].netconn,self.netlist['n171']], isweak=False, parent=self),
            NMOS("t862", [self.netlist['n107'],self.netlist['n416'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t863", [self.netlist['dpc35_PCHC'],self.port['vss'].netconn,self.netlist['n1007']], isweak=False, parent=self),
            NMOS("t860", [self.netlist['n1046'],self.port['vss'].netconn,self.netlist['adl7']], isweak=False, parent=self),
            NMOS("t861", [self.port['vss'].netconn,self.netlist['n389'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t866", [self.port['vss'].netconn,self.netlist['noty2'],self.netlist['y2']], isweak=False, parent=self),
            NMOS("t867", [self.netlist['n1013'],self.port['vss'].netconn,self.netlist['AxB7']], isweak=False, parent=self),
            NMOS("t2108", [self.netlist['idl5'],self.netlist['n1387'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t865", [self.netlist['n707'],self.netlist['n1636'],self.netlist['n639']], isweak=False, parent=self),
            NMOS("t1103", [self.netlist['x6'],self.netlist['n1724'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1102", [self.netlist['n1649'],self.port['vss'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t1101", [self.port['vcc'].netconn,self.netlist['adl3'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1100", [self.port['vss'].netconn,self.netlist['n591'],self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t1107", [self.netlist['n250'],self.netlist['n965'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1106", [self.netlist['n957'],self.netlist['n371'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1105", [self.netlist['dpc25_SBDB'],self.port['vss'].netconn,self.netlist['n1238']], isweak=False, parent=self),
            NMOS("t1104", [self.netlist['n1598'],self.port['vss'].netconn,self.netlist['pipeUNK28']], isweak=False, parent=self),
            NMOS("t1324", [self.port['vss'].netconn,self.netlist['n269'],self.netlist['n1038']], isweak=False, parent=self),
            NMOS("t1109", [self.netlist['n1071'],self.netlist['n274'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1108", [self.netlist['n740'],self.netlist['n22'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t958", [self.netlist['n950'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t1037", [self.netlist['n1620'],self.netlist['n1590'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t1036", [self.netlist['n1094'],self.netlist['n463'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1035", [self.port['vcc'].netconn,self.netlist['n1467'],self.netlist['n358']], isweak=False, parent=self),
            NMOS("t1034", [self.netlist['n769'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t480", [self.netlist['n1170'],self.port['vss'].netconn,self.netlist['n781']], isweak=False, parent=self),
            NMOS("t1032", [self.netlist['n1325'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t482", [self.port['ab10'].netconn,self.port['vss'].netconn,self.netlist['n994']], isweak=False, parent=self),
            NMOS("t489", [self.netlist['n518'],self.port['vss'].netconn,self.netlist['noty6']], isweak=False, parent=self),
            NMOS("t1039", [self.netlist['n1275'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1038", [self.netlist['n1368'],self.port['vss'].netconn,self.netlist['n645']], isweak=False, parent=self),
            NMOS("t2248", [self.netlist['n983'],self.port['vss'].netconn,self.netlist['s0']], isweak=False, parent=self),
            NMOS("t1749", [self.netlist['dpc27_SBADH'],self.port['vcc'].netconn,self.netlist['n1596']], isweak=False, parent=self),
            NMOS("t1748", [self.port['vss'].netconn,self.netlist['n1271'],self.netlist['n1596']], isweak=False, parent=self),
            NMOS("t1741", [self.netlist['n1211'],self.netlist['n897'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1740", [self.netlist['n265'],self.netlist['n182'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1743", [self.netlist['n1354'],self.port['vss'].netconn,self.netlist['notalucin']], isweak=False, parent=self),
            NMOS("t1742", [self.port['vss'].netconn,self.netlist['n368'],self.netlist['n446']], isweak=False, parent=self),
            NMOS("t1745", [self.port['vss'].netconn,self.netlist['n1635'],self.netlist['n966']], isweak=False, parent=self),
            NMOS("t1744", [self.netlist['fetch'],self.port['vss'].netconn,self.netlist['n1214']], isweak=False, parent=self),
            NMOS("t1747", [self.port['vss'].netconn,self.netlist['n770'],self.netlist['n559']], isweak=False, parent=self),
            NMOS("t1746", [self.netlist['dpc29_0ADH17'],self.port['vcc'].netconn,self.netlist['n966']], isweak=False, parent=self),
            NMOS("t1938", [self.netlist['n521'],self.netlist['n1358'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1939", [self.netlist['Pout1'],self.port['vss'].netconn,self.netlist['n318']], isweak=False, parent=self),
            NMOS("t1936", [self.port['vss'].netconn,self.netlist['n22'],self.netlist['n193']], isweak=False, parent=self),
            NMOS("t900", [self.port['vss'].netconn,self.netlist['n1021'],self.netlist['n155']], isweak=False, parent=self),
            NMOS("t903", [self.port['vss'].netconn,self.netlist['n1686'],self.netlist['n432']], isweak=False, parent=self),
            NMOS("t902", [self.netlist['n1555'],self.port['vss'].netconn,self.netlist['n440']], isweak=False, parent=self),
            NMOS("t673", [self.port['vss'].netconn,self.netlist['n691'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t2671", [self.port['vss'].netconn,self.netlist['n316'],self.netlist['alua0']], isweak=False, parent=self),
            NMOS("t904", [self.port['vss'].netconn,self.netlist['n1097'],self.netlist['n432']], isweak=False, parent=self),
            NMOS("t1930", [self.netlist['n1712'],self.port['vss'].netconn,self.netlist['RESG']], isweak=False, parent=self),
            NMOS("t1330", [self.port['vss'].netconn,self.netlist['n1619'],self.netlist['n1448']], isweak=False, parent=self),
            NMOS("t2130", [self.netlist['idb6'],self.netlist['Pout6'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t1931", [self.netlist['n566'],self.netlist['n661'],self.netlist['n1170']], isweak=False, parent=self),
            NMOS("t611", [self.port['vss'].netconn,self.netlist['n1623'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1219", [self.netlist['n404'],self.port['vss'].netconn,self.netlist['alua4']], isweak=False, parent=self),
            NMOS("t260", [self.netlist['n1674'],self.netlist['n931'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t261", [self.netlist['n1450'],self.netlist['n1526'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t262", [self.port['vss'].netconn,self.netlist['n638'],self.netlist['n1273']], isweak=False, parent=self),
            NMOS("t263", [self.netlist['n154'],self.port['vss'].netconn,self.netlist['n512']], isweak=False, parent=self),
            NMOS("t264", [self.port['vss'].netconn,self.netlist['dpc6_SBS'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t265", [self.netlist['n1448'],self.port['vss'].netconn,self.netlist['n1427']], isweak=False, parent=self),
            NMOS("t266", [self.netlist['n1357'],self.port['vss'].netconn,self.netlist['n223']], isweak=False, parent=self),
            NMOS("t267", [self.netlist['n1002'],self.port['vss'].netconn,self.netlist['n1219']], isweak=False, parent=self),
            NMOS("t268", [self.netlist['Pout0'],self.netlist['idb0'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t269", [self.netlist['n1477'],self.netlist['n604'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2960", [self.port['vss'].netconn,self.netlist['n1487'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2840", [self.netlist['n370'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t3308", [self.netlist['pipeVectorA2'],self.netlist['n1712'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2217", [self.netlist['n477'],self.netlist['n277'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2214", [self.netlist['n740'],self.netlist['n681'],self.netlist['dpc15_ANDS']], isweak=False, parent=self),
            NMOS("t2747", [self.netlist['pclp7'],self.netlist['idb7'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t2964", [self.netlist['n1031'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2965", [self.netlist['n804'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3303", [self.port['vss'].netconn,self.netlist['n1050'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2210", [self.port['vss'].netconn,self.netlist['n1571'],self.netlist['C45']], isweak=False, parent=self),
            NMOS("t3302", [self.port['vss'].netconn,self.netlist['n1665'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2211", [self.netlist['n165'],self.netlist['n427'],self.netlist['C45']], isweak=False, parent=self),
            NMOS("t297", [self.netlist['n1605'],self.port['vss'].netconn,self.netlist['n1410']], isweak=False, parent=self),
            NMOS("t1216", [self.netlist['n608'],self.port['vss'].netconn,self.netlist['n1272']], isweak=False, parent=self),
            NMOS("t3307", [self.port['vss'].netconn,self.netlist['n1006'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t290", [self.netlist['abl6'],self.port['vss'].netconn,self.netlist['n1307']], isweak=False, parent=self),
            NMOS("t3088", [self.netlist['n4'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3089", [self.netlist['n167'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t293", [self.netlist['dpc32_PCHADH'],self.port['vss'].netconn,self.netlist['n1413']], isweak=False, parent=self),
            NMOS("t89", [self.netlist['n1158'],self.port['vss'].netconn,self.netlist['n783']], isweak=False, parent=self),
            NMOS("t88", [self.port['vss'].netconn,self.netlist['n835'],self.netlist['n311']], isweak=False, parent=self),
            NMOS("t87", [self.port['vss'].netconn,self.netlist['n856'],self.netlist['n311']], isweak=False, parent=self),
            NMOS("t86", [self.netlist['notidl4'],self.netlist['n490'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t85", [self.netlist['n1646'],self.netlist['n1673'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t84", [self.netlist['pipeUNK06'],self.netlist['n513'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t83", [self.netlist['Pout2'],self.netlist['idb2'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t82", [self.netlist['idb7'],self.netlist['Pout7'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t81", [self.netlist['n1463'],self.port['vss'].netconn,self.netlist['dor4']], isweak=False, parent=self),
            NMOS("t80", [self.netlist['n147'],self.port['vss'].netconn,self.netlist['dor4']], isweak=False, parent=self),
            NMOS("t3248", [self.port['vss'].netconn,self.netlist['n682'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3249", [self.port['vss'].netconn,self.netlist['n1482'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3246", [self.port['vss'].netconn,self.netlist['n786'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3247", [self.port['vss'].netconn,self.netlist['n1664'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3244", [self.port['vss'].netconn,self.netlist['n76'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3245", [self.port['vss'].netconn,self.netlist['n245'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3242", [self.port['vss'].netconn,self.netlist['n84'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t1312", [self.port['vss'].netconn,self.netlist['dpc26_ACDB'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t3240", [self.port['vss'].netconn,self.netlist['n382'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3241", [self.port['vss'].netconn,self.netlist['n1173'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t880", [self.netlist['n458'],self.port['vss'].netconn,self.netlist['idb2']], isweak=False, parent=self),
            NMOS("t1432", [self.port['vss'].netconn,self.netlist['n1243'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1431", [self.netlist['n575'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1430", [self.netlist['n787'],self.port['vss'].netconn,self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1437", [self.port['vss'].netconn,self.netlist['n1168'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1313", [self.port['vss'].netconn,self.netlist['n1039'],self.netlist['pipeUNK40']], isweak=False, parent=self),
            NMOS("t885", [self.netlist['n1366'],self.netlist['n472'],self.netlist['n16']], isweak=False, parent=self),
            NMOS("t886", [self.netlist['n850'],self.port['vss'].netconn,self.netlist['pipeUNK18']], isweak=False, parent=self),
            NMOS("t2449", [self.port['vss'].netconn,self.netlist['n1595'],self.netlist['n754']], isweak=False, parent=self),
            NMOS("t2448", [self.netlist['n1181'],self.netlist['n648'],self.netlist['n754']], isweak=False, parent=self),
            NMOS("t2446", [self.netlist['n1711'],self.netlist['nots1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2445", [self.port['vss'].netconn,self.netlist['n139'],self.netlist['n934']], isweak=False, parent=self),
            NMOS("t1434", [self.port['vss'].netconn,self.netlist['n1420'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t2443", [self.port['vss'].netconn,self.netlist['n506'],self.netlist['n192']], isweak=False, parent=self),
            NMOS("t2442", [self.port['vss'].netconn,self.netlist['adh0'],self.netlist['dpc28_0ADH0']], isweak=False, parent=self),
            NMOS("t3155", [self.netlist['n851'],self.netlist['n1515'],self.netlist['n1019']], isweak=False, parent=self),
            NMOS("t3404", [self.netlist['notx3'],self.port['vss'].netconn,self.netlist['x3']], isweak=False, parent=self),
            NMOS("t3405", [self.port['vss'].netconn,self.netlist['n14'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t3406", [self.netlist['n593'],self.port['vss'].netconn,self.netlist['n355']], isweak=False, parent=self),
            NMOS("t3407", [self.netlist['dpc4_SSB'],self.port['vcc'].netconn,self.netlist['n355']], isweak=False, parent=self),
            NMOS("t1310", [self.port['vss'].netconn,self.netlist['n1474'],self.netlist['idb1']], isweak=False, parent=self),
            NMOS("t3408", [self.port['vss'].netconn,self.netlist['n814'],self.netlist['n392']], isweak=False, parent=self),
            NMOS("t3409", [self.port['vss'].netconn,self.netlist['n557'],self.netlist['n392']], isweak=False, parent=self),
            NMOS("t1311", [self.port['vss'].netconn,self.netlist['dpc30_ADHPCH'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1802", [self.netlist['n501'],self.netlist['pipeUNK35'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1803", [self.port['vss'].netconn,self.netlist['n1512'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1801", [self.netlist['n1276'],self.netlist['notRdy0'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1806", [self.port['vss'].netconn,self.netlist['n788'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1807", [self.port['vss'].netconn,self.netlist['n1057'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1804", [self.port['vss'].netconn,self.netlist['n258'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1805", [self.port['vss'].netconn,self.netlist['n84'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1808", [self.port['vss'].netconn,self.netlist['n204'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1882", [self.netlist['n69'],self.netlist['n1181'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t714", [self.port['vss'].netconn,self.netlist['n1290'],self.netlist['n1126']], isweak=False, parent=self),
            NMOS("t715", [self.netlist['n986'],self.netlist['n1556'],self.netlist['n699']], isweak=False, parent=self),
            NMOS("t716", [self.port['vss'].netconn,self.netlist['n867'],self.netlist['n699']], isweak=False, parent=self),
            NMOS("t717", [self.port['vss'].netconn,self.netlist['n1649'],self.netlist['n1057']], isweak=False, parent=self),
            NMOS("t710", [self.netlist['n1541'],self.port['vss'].netconn,self.netlist['n43']], isweak=False, parent=self),
            NMOS("t955", [self.netlist['n1646'],self.port['vss'].netconn,self.netlist['clock2']], isweak=False, parent=self),
            NMOS("t712", [self.netlist['n11'],self.port['vss'].netconn,self.netlist['n167']], isweak=False, parent=self),
            NMOS("t713", [self.netlist['n1395'],self.netlist['n854'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t718", [self.netlist['n1538'],self.port['vss'].netconn,self.netlist['n1070']], isweak=False, parent=self),
            NMOS("t719", [self.port['vss'].netconn,self.netlist['dpc35_PCHC'],self.netlist['n1070']], isweak=False, parent=self),
            NMOS("t2599", [self.netlist['n905'],self.netlist['n1681'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t2598", [self.port['vcc'].netconn,self.netlist['idb6'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3064", [self.port['vss'].netconn,self.netlist['n935'],self.netlist['adl2']], isweak=False, parent=self),
            NMOS("t3065", [self.netlist['n146'],self.port['vss'].netconn,self.netlist['n5']], isweak=False, parent=self),
            NMOS("t3062", [self.netlist['dasb7'],self.port['vss'].netconn,self.netlist['n260']], isweak=False, parent=self),
            NMOS("t3063", [self.port['vss'].netconn,self.netlist['dasb1'],self.netlist['n735']], isweak=False, parent=self),
            NMOS("t3061", [self.netlist['n720'],self.port['vss'].netconn,self.netlist['pipeUNK34']], isweak=False, parent=self),
            NMOS("t2591", [self.netlist['n18'],self.netlist['n468'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2042", [self.netlist['n24'],self.netlist['n1039'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2593", [self.port['vss'].netconn,self.netlist['n1649'],self.netlist['n389']], isweak=False, parent=self),
            NMOS("t2040", [self.netlist['dpc5_SADL'],self.port['vss'].netconn,self.netlist['n196']], isweak=False, parent=self),
            NMOS("t2595", [self.netlist['n277'],self.netlist['n1632'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t2046", [self.port['vss'].netconn,self.netlist['notalucout'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t2045", [self.netlist['n190'],self.netlist['n1101'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2596", [self.netlist['n378'],self.port['vss'].netconn,self.netlist['n18']], isweak=False, parent=self),
            NMOS("t2594", [self.netlist['n1464'],self.port['vss'].netconn,self.netlist['n1487']], isweak=False, parent=self),
            NMOS("t2741", [self.netlist['n20'],self.port['vss'].netconn,self.netlist['n1316']], isweak=False, parent=self),
            NMOS("t2919", [self.netlist['n869'],self.netlist['n1128'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2918", [self.netlist['pchp7'],self.netlist['idb7'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2915", [self.netlist['idb4'],self.netlist['pchp4'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2914", [self.netlist['idb3'],self.netlist['pchp3'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2917", [self.netlist['pchp6'],self.netlist['idb6'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2916", [self.netlist['idb5'],self.netlist['pchp5'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2911", [self.netlist['idb0'],self.netlist['pchp0'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2910", [self.netlist['n345'],self.netlist['n1279'],self.netlist['n986']], isweak=False, parent=self),
            NMOS("t2913", [self.netlist['pchp2'],self.netlist['idb2'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t2912", [self.netlist['pchp1'],self.netlist['idb1'],self.netlist['dpc33_PCHDB']], isweak=False, parent=self),
            NMOS("t479", [self.netlist['n1197'],self.port['vss'].netconn,self.netlist['n174']], isweak=False, parent=self),
            NMOS("t478", [self.netlist['DC78'],self.netlist['n164'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1880", [self.netlist['dpc25_SBDB'],self.port['vcc'].netconn,self.netlist['n1295']], isweak=False, parent=self),
            NMOS("t471", [self.netlist['n104'],self.port['vss'].netconn,self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t470", [self.port['vss'].netconn,self.netlist['n1347'],self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t473", [self.netlist['n1061'],self.netlist['n207'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t472", [self.netlist['n343'],self.netlist['n571'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t475", [self.netlist['n958'],self.port['vss'].netconn,self.port['rdy'].netconn], isweak=False, parent=self),
            NMOS("t474", [self.netlist['n1004'],self.netlist['n473'],self.netlist['n980']], isweak=False, parent=self),
            NMOS("t477", [self.port['vss'].netconn,self.netlist['n863'],self.netlist['n1240']], isweak=False, parent=self),
            NMOS("t2597", [self.netlist['n379'],self.netlist['n1480'],self.netlist['n1570']], isweak=False, parent=self),
            NMOS("t2627", [self.netlist['n174'],self.port['vss'].netconn,self.netlist['n1459']], isweak=False, parent=self),
            NMOS("t2626", [self.netlist['n1390'],self.port['vss'].netconn,self.netlist['n1459']], isweak=False, parent=self),
            NMOS("t2625", [self.netlist['n1269'],self.netlist['nnT2BR'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2624", [self.netlist['n1550'],self.port['vss'].netconn,self.netlist['n781']], isweak=False, parent=self),
            NMOS("t2623", [self.port['vss'].netconn,self.netlist['n761'],self.netlist['alu5']], isweak=False, parent=self),
            NMOS("t2622", [self.port['vcc'].netconn,self.netlist['n659'],self.netlist['n1153']], isweak=False, parent=self),
            NMOS("t679", [self.port['vss'].netconn,self.netlist['n840'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t678", [self.port['vss'].netconn,self.netlist['n1665'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t901", [self.port['vss'].netconn,self.netlist['AxB1'],self.netlist['n155']], isweak=False, parent=self),
            NMOS("t1937", [self.port['vss'].netconn,self.netlist['abh6'],self.netlist['n289']], isweak=False, parent=self),
            NMOS("t675", [self.netlist['n1114'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t674", [self.netlist['n1646'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t905", [self.port['ab14'].netconn,self.port['vss'].netconn,self.netlist['n635']], isweak=False, parent=self),
            NMOS("t1933", [self.netlist['n7'],self.port['vss'].netconn,self.netlist['n466']], isweak=False, parent=self),
            NMOS("t671", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t670", [self.port['vss'].netconn,self.netlist['n352'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t878", [self.netlist['n300'],self.port['vss'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t2829", [self.port['vss'].netconn,self.netlist['notx2'],self.netlist['x2']], isweak=False, parent=self),
            NMOS("t2828", [self.port['vss'].netconn,self.netlist['dpc34_PCLC'],self.netlist['n249']], isweak=False, parent=self),
            NMOS("t2821", [self.netlist['n1280'],self.port['vss'].netconn,self.netlist['n335']], isweak=False, parent=self),
            NMOS("t2820", [self.netlist['n813'],self.port['vss'].netconn,self.netlist['n440']], isweak=False, parent=self),
            NMOS("t2823", [self.port['vss'].netconn,self.netlist['n851'],self.netlist['n302']], isweak=False, parent=self),
            NMOS("t2822", [self.port['vss'].netconn,self.netlist['n1549'],self.netlist['a1']], isweak=False, parent=self),
            NMOS("t2825", [self.netlist['n506'],self.netlist['n1602'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2824", [self.netlist['n94'],self.netlist['n1650'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2827", [self.port['vss'].netconn,self.netlist['n163'],self.netlist['n249']], isweak=False, parent=self),
            NMOS("t2826", [self.netlist['n853'],self.port['vss'].netconn,self.netlist['n770']], isweak=False, parent=self),
            NMOS("t875", [self.port['vss'].netconn,self.netlist['n725'],self.netlist['n599']], isweak=False, parent=self),
            NMOS("t874", [self.netlist['n1278'],self.port['vss'].netconn,self.netlist['n462']], isweak=False, parent=self),
            NMOS("t877", [self.port['vcc'].netconn,self.netlist['dpc1_SBY'],self.netlist['n692']], isweak=False, parent=self),
            NMOS("t876", [self.port['vss'].netconn,self.netlist['n441'],self.netlist['n692']], isweak=False, parent=self),
            NMOS("t871", [self.port['vss'].netconn,self.netlist['n1225'],self.netlist['n1524']], isweak=False, parent=self),
            NMOS("t870", [self.netlist['n1564'],self.port['vcc'].netconn,self.netlist['n291']], isweak=False, parent=self),
            NMOS("t873", [self.netlist['n1488'],self.port['vss'].netconn,self.netlist['n278']], isweak=False, parent=self),
            NMOS("t2132", [self.netlist['n1082'],self.netlist['n186'],self.netlist['n507']], isweak=False, parent=self),
            NMOS("t879", [self.port['vss'].netconn,self.netlist['INTG'],self.netlist['n760']], isweak=False, parent=self),
            NMOS("t2131", [self.port['vss'].netconn,self.netlist['n279'],self.netlist['n507']], isweak=False, parent=self),
            NMOS("t2785", [self.netlist['n86'],self.netlist['n364'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2133", [self.netlist['notdor5'],self.netlist['n961'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1245", [self.port['vss'].netconn,self.netlist['n167'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1246", [self.port['vss'].netconn,self.netlist['n1074'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1247", [self.port['vss'].netconn,self.netlist['n1246'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1240", [self.netlist['n1466'],self.port['vss'].netconn,self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1241", [self.port['vss'].netconn,self.netlist['n546'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t2135", [self.netlist['n1367'],self.netlist['n293'],self.netlist['n200']], isweak=False, parent=self),
            NMOS("t2134", [self.netlist['n1486'],self.port['vss'].netconn,self.netlist['n200']], isweak=False, parent=self),
            NMOS("t2137", [self.port['vss'].netconn,self.netlist['n1501'],self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t2139", [self.netlist['n1509'],self.netlist['n952'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1248", [self.port['vss'].netconn,self.netlist['n53'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1249", [self.port['vss'].netconn,self.netlist['n691'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t2136", [self.netlist['n57'],self.port['vss'].netconn,self.netlist['n200']], isweak=False, parent=self),
            NMOS("t3017", [self.netlist['n1410'],self.port['vss'].netconn,self.netlist['pd7']], isweak=False, parent=self),
            NMOS("t1118", [self.netlist['sb3'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1329", [self.port['vss'].netconn,self.netlist['n306'],self.netlist['n725']], isweak=False, parent=self),
            NMOS("t3016", [self.port['vcc'].netconn,self.netlist['n994'],self.netlist['n1034']], isweak=False, parent=self),
            NMOS("t1114", [self.netlist['notdor2'],self.netlist['n1376'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1115", [self.netlist['n327'],self.port['vss'].netconn,self.netlist['n1569']], isweak=False, parent=self),
            NMOS("t1116", [self.port['vss'].netconn,self.netlist['AxB3'],self.netlist['n988']], isweak=False, parent=self),
            NMOS("t1243", [self.port['vss'].netconn,self.netlist['n179'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1110", [self.netlist['n296'],self.netlist['n651'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1111", [self.netlist['n277'],self.netlist['n486'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1112", [self.netlist['n1197'],self.netlist['n722'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1113", [self.netlist['n532'],self.netlist['n304'],self.netlist['dpc17_SUMS']], isweak=False, parent=self),
            NMOS("t1327", [self.netlist['n1491'],self.port['vss'].netconn,self.netlist['noty2']], isweak=False, parent=self),
            NMOS("t748", [self.port['vss'].netconn,self.netlist['n1337'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1326", [self.port['vss'].netconn,self.netlist['n1294'],self.netlist['n1622']], isweak=False, parent=self),
            NMOS("t1333", [self.netlist['idb1'],self.netlist['Pout1'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t1989", [self.netlist['n604'],self.port['vss'].netconn,self.netlist['n1311']], isweak=False, parent=self),
            NMOS("t977", [self.port['vss'].netconn,self.netlist['n812'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t2548", [self.netlist['pchp6'],self.netlist['adh6'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t970", [self.port['vss'].netconn,self.netlist['n1368'],self.netlist['n1578']], isweak=False, parent=self),
            NMOS("t2549", [self.netlist['pchp5'],self.netlist['adh5'],self.netlist['dpc32_PCHADH']], isweak=False, parent=self),
            NMOS("t1885", [self.port['vss'].netconn,self.netlist['n252'],self.netlist['n1710']], isweak=False, parent=self),
            NMOS("t971", [self.netlist['n476'],self.port['vss'].netconn,self.netlist['n1027']], isweak=False, parent=self),
            NMOS("t497", [self.netlist['n877'],self.port['vss'].netconn,self.netlist['n506']], isweak=False, parent=self),
            NMOS("t2546", [self.port['vss'].netconn,self.netlist['n6'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t1022", [self.netlist['dpc8_nDBADD'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1023", [self.port['db6'].netconn,self.port['db6'].netconn,self.netlist['n471']], isweak=False, parent=self),
            NMOS("t1024", [self.port['db6'].netconn,self.port['vss'].netconn,self.netlist['n471']], isweak=False, parent=self),
            NMOS("t492", [self.port['vss'].netconn,self.netlist['n747'],self.netlist['n670']], isweak=False, parent=self),
            NMOS("t491", [self.netlist['n880'],self.port['vss'].netconn,self.netlist['adh6']], isweak=False, parent=self),
            NMOS("t490", [self.netlist['n721'],self.netlist['s7'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t711", [self.netlist['n91'],self.port['vss'].netconn,self.netlist['n1529']], isweak=False, parent=self),
            NMOS("t973", [self.port['vss'].netconn,self.netlist['n104'],self.netlist['n1589']], isweak=False, parent=self),
            NMOS("t741", [self.port['vss'].netconn,self.netlist['n804'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t499", [self.netlist['n1084'],self.netlist['n722'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t498", [self.netlist['n1642'],self.netlist['n1278'],self.netlist['n824']], isweak=False, parent=self),
            NMOS("t1055", [self.port['vss'].netconn,self.netlist['n665'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t2545", [self.netlist['n536'],self.netlist['n484'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1054", [self.port['vss'].netconn,self.netlist['n258'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t2014", [self.port['vss'].netconn,self.netlist['n1215'],self.netlist['n1185']], isweak=False, parent=self),
            NMOS("t3181", [self.netlist['sb5'],self.netlist['adh5'],self.netlist['dpc27_SBADH']], isweak=False, parent=self),
            NMOS("t1057", [self.port['vss'].netconn,self.netlist['n1057'],self.netlist['notir2']], isweak=False, parent=self),
            NMOS("t2015", [self.port['vss'].netconn,self.netlist['n1433'],self.netlist['n201']], isweak=False, parent=self),
            NMOS("t1759", [self.netlist['n267'],self.port['vss'].netconn,self.netlist['n1175']], isweak=False, parent=self),
            NMOS("t3019", [self.port['vss'].netconn,self.netlist['n1558'],self.netlist['pipeT2out']], isweak=False, parent=self),
            NMOS("t1752", [self.netlist['idl6'],self.netlist['n1014'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1503", [self.netlist['n815'],self.port['vss'].netconn,self.netlist['pipeVectorA2']], isweak=False, parent=self),
            NMOS("t1750", [self.netlist['adl2'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1751", [self.netlist['n114'],self.netlist['n1402'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1756", [self.port['vss'].netconn,self.netlist['clock2'],self.netlist['n1533']], isweak=False, parent=self),
            NMOS("t1757", [self.port['db5'].netconn,self.port['vcc'].netconn,self.netlist['n373']], isweak=False, parent=self),
            NMOS("t1754", [self.port['vss'].netconn,self.netlist['n1044'],self.netlist['n31']], isweak=False, parent=self),
            NMOS("t1119", [self.netlist['n2'],self.port['vss'].netconn,self.netlist['pipeUNK39']], isweak=False, parent=self),
            NMOS("t852", [self.netlist['n1174'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t1501", [self.netlist['n545'],self.port['vss'].netconn,self.netlist['n1488']], isweak=False, parent=self),
            NMOS("t3180", [self.netlist['pclp2'],self.netlist['pcl2'],self.netlist['dpc39_PCLPCL']], isweak=False, parent=self),
            NMOS("t1687", [self.port['vss'].netconn,self.netlist['n1244'],self.netlist['n1562']], isweak=False, parent=self),
            NMOS("t1117", [self.netlist['nots3'],self.netlist['n34'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3424", [self.port['vss'].netconn,self.netlist['dpc0_YSB'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t3425", [self.port['vss'].netconn,self.netlist['n1230'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t3391", [self.netlist['sb7'],self.netlist['s7'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t3420", [self.port['vss'].netconn,self.netlist['n1440'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t273", [self.netlist['n406'],self.netlist['n371'],self.netlist['n105']], isweak=False, parent=self),
            NMOS("t272", [self.netlist['t2'],self.port['vss'].netconn,self.netlist['n1575']], isweak=False, parent=self),
            NMOS("t271", [self.port['vss'].netconn,self.netlist['n818'],self.netlist['n265']], isweak=False, parent=self),
            NMOS("t270", [self.netlist['n1082'],self.netlist['n367'],self.netlist['n206']], isweak=False, parent=self),
            NMOS("t277", [self.port['vss'].netconn,self.netlist['n267'],self.netlist['n544']], isweak=False, parent=self),
            NMOS("t276", [self.netlist['dpc37_PCLDB'],self.port['vcc'].netconn,self.netlist['n631']], isweak=False, parent=self),
            NMOS("t275", [self.netlist['n1323'],self.port['vss'].netconn,self.netlist['n631']], isweak=False, parent=self),
            NMOS("t274", [self.netlist['n555'],self.port['vss'].netconn,self.netlist['n105']], isweak=False, parent=self),
            NMOS("t279", [self.netlist['adl4'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t278", [self.port['vss'].netconn,self.netlist['n616'],self.netlist['n1482']], isweak=False, parent=self),
            NMOS("t3230", [self.netlist['n1084'],self.port['vss'].netconn,self.netlist['alua6']], isweak=False, parent=self),
            NMOS("t864", [self.netlist['n754'],self.port['vss'].netconn,self.netlist['n1673']], isweak=False, parent=self),
            NMOS("t1502", [self.netlist['n1547'],self.port['vss'].netconn,self.netlist['n1488']], isweak=False, parent=self),
            NMOS("t350", [self.port['vss'].netconn,self.port['ab1'].netconn,self.netlist['n66']], isweak=False, parent=self),
            NMOS("t99", [self.netlist['n1343'],self.port['vss'].netconn,self.netlist['n152']], isweak=False, parent=self),
            NMOS("t90", [self.netlist['dpc34_PCLC'],self.port['vss'].netconn,self.netlist['n783']], isweak=False, parent=self),
            NMOS("t91", [self.netlist['n1253'],self.port['vss'].netconn,self.netlist['n783']], isweak=False, parent=self),
            NMOS("t92", [self.port['vss'].netconn,self.port['ab8'].netconn,self.netlist['n381']], isweak=False, parent=self),
            NMOS("t3279", [self.port['vss'].netconn,self.netlist['n1074'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3278", [self.port['vss'].netconn,self.netlist['n1086'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3273", [self.port['vss'].netconn,self.netlist['n4'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3272", [self.port['vss'].netconn,self.netlist['n131'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3271", [self.port['vss'].netconn,self.netlist['n179'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2959", [self.port['vss'].netconn,self.netlist['n1612'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t3277", [self.port['vss'].netconn,self.netlist['n1721'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3276", [self.port['vss'].netconn,self.netlist['n1168'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3275", [self.port['vss'].netconn,self.netlist['n167'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3274", [self.port['vss'].netconn,self.netlist['n1396'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2688", [self.port['vss'].netconn,self.netlist['n370'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t608", [self.netlist['n665'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t609", [self.netlist['n271'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2458", [self.netlist['n1153'],self.port['vss'].netconn,self.netlist['abh7']], isweak=False, parent=self),
            NMOS("t2459", [self.port['vss'].netconn,self.netlist['n659'],self.netlist['abh7']], isweak=False, parent=self),
            NMOS("t3183", [self.netlist['n254'],self.port['vss'].netconn,self.netlist['adh5']], isweak=False, parent=self),
            NMOS("t3182", [self.netlist['adl6'],self.netlist['n618'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t3185", [self.netlist['n1158'],self.netlist['n515'],self.netlist['n1542']], isweak=False, parent=self),
            NMOS("t3184", [self.netlist['n1038'],self.port['vss'].netconn,self.netlist['n336']], isweak=False, parent=self),
            NMOS("t3187", [self.port['vss'].netconn,self.netlist['dpc12_0ADD'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t607", [self.netlist['n682'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2450", [self.netlist['adh1'],self.netlist['pch1'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t2451", [self.netlist['n1178'],self.netlist['n590'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2452", [self.netlist['abh5'],self.port['vss'].netconn,self.netlist['n1128']], isweak=False, parent=self),
            NMOS("t2453", [self.netlist['adh0'],self.netlist['pch0'],self.netlist['dpc30_ADHPCH']], isweak=False, parent=self),
            NMOS("t2454", [self.port['vss'].netconn,self.netlist['n617'],self.netlist['abh1']], isweak=False, parent=self),
            NMOS("t2455", [self.port['vss'].netconn,self.netlist['n676'],self.netlist['abh1']], isweak=False, parent=self),
            NMOS("t2456", [self.netlist['n1192'],self.netlist['n751'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2457", [self.netlist['n1639'],self.port['vcc'].netconn,self.netlist['abh7']], isweak=False, parent=self),
            NMOS("t3471", [self.port['vss'].netconn,self.netlist['dpc34_PCLC'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t3470", [self.port['vss'].netconn,self.netlist['n1166'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t3473", [self.port['vss'].netconn,self.port['db0'].netconn,self.netlist['n1072']], isweak=False, parent=self),
            NMOS("t3472", [self.port['vss'].netconn,self.netlist['n1107'],self.netlist['n492']], isweak=False, parent=self),
            NMOS("t1021", [self.port['vss'].netconn,self.netlist['n1382'],self.netlist['n861']], isweak=False, parent=self),
            NMOS("t1943", [self.port['vss'].netconn,self.netlist['n1089'],self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t495", [self.netlist['n1083'],self.port['vss'].netconn,self.netlist['n1587']], isweak=False, parent=self),
            NMOS("t603", [self.netlist['n76'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t494", [self.port['vss'].netconn,self.netlist['n1294'],self.netlist['n1587']], isweak=False, parent=self),
            NMOS("t600", [self.netlist['n382'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t963", [self.netlist['s0'],self.netlist['dasb0'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t1940", [self.port['vcc'].netconn,self.port['ab10'].netconn,self.netlist['n1545']], isweak=False, parent=self),
            NMOS("t2304", [self.netlist['n1246'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2758", [self.port['vss'].netconn,self.netlist['dpc11_SBADD'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1839", [self.netlist['n452'],self.netlist['n681'],self.netlist['alub2']], isweak=False, parent=self),
            NMOS("t962", [self.netlist['x2'],self.netlist['n1694'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1837", [self.netlist['n1303'],self.netlist['n508'],self.netlist['n335']], isweak=False, parent=self),
            NMOS("t1836", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n0']], isweak=False, parent=self),
            NMOS("t1835", [self.port['vss'].netconn,self.netlist['n1684'],self.netlist['idb6']], isweak=False, parent=self),
            NMOS("t1834", [self.netlist['n270'],self.port['vss'].netconn,self.netlist['n503']], isweak=False, parent=self),
            NMOS("t1833", [self.netlist['n1272'],self.netlist['notRdy0'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1832", [self.netlist['n310'],self.netlist['n724'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t1831", [self.netlist['n119'],self.netlist['n237'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t1830", [self.port['vss'].netconn,self.netlist['n1006'],self.netlist['ir0']], isweak=False, parent=self),
            NMOS("t2054", [self.netlist['n104'],self.port['vss'].netconn,self.netlist['n847']], isweak=False, parent=self),
            NMOS("t706", [self.port['vss'].netconn,self.netlist['n1257'],self.netlist['notalucout']], isweak=False, parent=self),
            NMOS("t2056", [self.port['ab9'].netconn,self.port['vss'].netconn,self.netlist['n676']], isweak=False, parent=self),
            NMOS("t704", [self.netlist['n696'],self.netlist['n911'],self.netlist['n79']], isweak=False, parent=self),
            NMOS("t703", [self.port['vss'].netconn,self.netlist['DBZ'],self.netlist['idb4']], isweak=False, parent=self),
            NMOS("t2051", [self.port['vcc'].netconn,self.netlist['n359'],self.netlist['n1346']], isweak=False, parent=self),
            NMOS("t2052", [self.netlist['n1455'],self.port['vss'].netconn,self.netlist['n1324']], isweak=False, parent=self),
            NMOS("t2053", [self.netlist['sb7'],self.netlist['alu7'],self.netlist['dpc19_ADDSB7']], isweak=False, parent=self),
            NMOS("t709", [self.netlist['n351'],self.port['vss'].netconn,self.netlist['idb6']], isweak=False, parent=self),
            NMOS("t708", [self.port['vss'].netconn,self.netlist['n177'],self.netlist['AxB7']], isweak=False, parent=self),
            NMOS("t3053", [self.netlist['n339'],self.netlist['n632'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3052", [self.port['vss'].netconn,self.netlist['D1x1'],self.netlist['RESG']], isweak=False, parent=self),
            NMOS("t3051", [self.netlist['n1629'],self.port['vss'].netconn,self.netlist['n753']], isweak=False, parent=self),
            NMOS("t3050", [self.netlist['n1203'],self.netlist['dasb5'],self.netlist['n753']], isweak=False, parent=self),
            NMOS("t3509", [self.port['vss'].netconn,self.netlist['n810'],self.netlist['n923']], isweak=False, parent=self),
            NMOS("t3056", [self.netlist['n953'],self.port['vss'].netconn,self.netlist['AxB1']], isweak=False, parent=self),
            NMOS("t3055", [self.netlist['dpc16_EORS'],self.port['vcc'].netconn,self.netlist['n1364']], isweak=False, parent=self),
            NMOS("t3054", [self.netlist['n108'],self.port['vss'].netconn,self.netlist['n1364']], isweak=False, parent=self),
            NMOS("t2582", [self.netlist['n678'],self.netlist['pipeT3out'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2583", [self.netlist['n533'],self.port['vss'].netconn,self.netlist['pipeUNK22']], isweak=False, parent=self),
            NMOS("t2580", [self.netlist['n375'],self.port['vss'].netconn,self.netlist['n308']], isweak=False, parent=self),
            NMOS("t2581", [self.netlist['n65'],self.port['vss'].netconn,self.netlist['n308']], isweak=False, parent=self),
            NMOS("t3501", [self.port['vcc'].netconn,self.netlist['n642'],self.netlist['n951']], isweak=False, parent=self),
            NMOS("t2587", [self.netlist['n836'],self.netlist['n168'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2584", [self.netlist['n474'],self.port['vss'].netconn,self.netlist['n410']], isweak=False, parent=self),
            NMOS("t3502", [self.port['vcc'].netconn,self.netlist['sb2'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2249", [self.netlist['n580'],self.port['vss'].netconn,self.netlist['n1268']], isweak=False, parent=self),
            NMOS("t2908", [self.netlist['n1000'],self.netlist['n1408'],self.netlist['n1044']], isweak=False, parent=self),
            NMOS("t2909", [self.netlist['pipeUNK10'],self.netlist['n1379'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2906", [self.netlist['n1587'],self.port['vss'].netconn,self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t2907", [self.netlist['n540'],self.port['vss'].netconn,self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t2904", [self.port['vss'].netconn,self.netlist['dpc34_PCLC'],self.netlist['n1643']], isweak=False, parent=self),
            NMOS("t2905", [self.netlist['n410'],self.port['vss'].netconn,self.netlist['n1643']], isweak=False, parent=self),
            NMOS("t2902", [self.port['vcc'].netconn,self.netlist['dpc23_SBAC'],self.netlist['n830']], isweak=False, parent=self),
            NMOS("t2903", [self.netlist['n766'],self.port['vss'].netconn,self.netlist['n1643']], isweak=False, parent=self),
            NMOS("t2900", [self.netlist['n1289'],self.port['vss'].netconn,self.netlist['n902']], isweak=False, parent=self),
            NMOS("t2901", [self.port['vss'].netconn,self.netlist['n1047'],self.netlist['n830']], isweak=False, parent=self),
            NMOS("t224", [self.netlist['n380'],self.port['vss'].netconn,self.netlist['D1x1']], isweak=False, parent=self),
            NMOS("t3351", [self.port['vss'].netconn,self.netlist['n494'],self.netlist['adh7']], isweak=False, parent=self),
            NMOS("t3352", [self.port['vcc'].netconn,self.netlist['adh6'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2630", [self.netlist['pipeUNK08'],self.netlist['n252'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2631", [self.netlist['n1579'],self.netlist['notRnWprepad'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2632", [self.netlist['n566'],self.netlist['p1'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t649", [self.port['vss'].netconn,self.netlist['n665'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t2634", [self.netlist['n581'],self.netlist['n306'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2635", [self.port['vss'].netconn,self.netlist['n1564'],self.netlist['n1157']], isweak=False, parent=self),
            NMOS("t2636", [self.netlist['NMIL'],self.port['vss'].netconn,self.netlist['n562']], isweak=False, parent=self),
            NMOS("t2637", [self.port['vss'].netconn,self.netlist['dor5'],self.netlist['notdor5']], isweak=False, parent=self),
            NMOS("t642", [self.netlist['n1173'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t3354", [self.port['vss'].netconn,self.netlist['n501'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t640", [self.port['vss'].netconn,self.netlist['n1466'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t641", [self.port['vss'].netconn,self.netlist['n1601'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t646", [self.netlist['n245'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t647", [self.port['vss'].netconn,self.netlist['n985'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t644", [self.netlist['n1543'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t645", [self.netlist['n1540'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t3356", [self.netlist['n192'],self.netlist['n239'],self.netlist['n1048']], isweak=False, parent=self),
            NMOS("t223", [self.netlist['n541'],self.netlist['n1183'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t1349", [self.netlist['n796'],self.netlist['n396'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1348", [self.netlist['VEC0'],self.port['vss'].netconn,self.netlist['n689']], isweak=False, parent=self),
            NMOS("t1345", [self.port['vss'].netconn,self.netlist['n726'],self.netlist['n677']], isweak=False, parent=self),
            NMOS("t1344", [self.port['vcc'].netconn,self.netlist['n1105'],self.netlist['n1715']], isweak=False, parent=self),
            NMOS("t1347", [self.netlist['n329'],self.port['vss'].netconn,self.netlist['pcl1']], isweak=False, parent=self),
            NMOS("t1346", [self.port['vss'].netconn,self.netlist['noty4'],self.netlist['y4']], isweak=False, parent=self),
            NMOS("t1341", [self.netlist['alua7'],self.port['vss'].netconn,self.netlist['dpc12_0ADD']], isweak=False, parent=self),
            NMOS("t1340", [self.port['vss'].netconn,self.netlist['n149'],self.netlist['alu6']], isweak=False, parent=self),
            NMOS("t1307", [self.netlist['n168'],self.port['vss'].netconn,self.netlist['adh2']], isweak=False, parent=self),
            NMOS("t2838", [self.netlist['n786'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2839", [self.netlist['n1482'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2832", [self.netlist['n1173'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2833", [self.netlist['n1233'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2830", [self.netlist['n1601'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2831", [self.netlist['n382'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2836", [self.netlist['n1540'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2837", [self.port['vss'].netconn,self.netlist['n245'],self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2834", [self.netlist['n1543'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2835", [self.netlist['n76'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t800", [self.netlist['n1487'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t801", [self.netlist['n784'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t802", [self.netlist['n244'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t803", [self.netlist['n1623'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t804", [self.port['vss'].netconn,self.netlist['n764'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t805", [self.port['vss'].netconn,self.netlist['n403'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t806", [self.netlist['n1582'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t807", [self.netlist['n1031'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t808", [self.netlist['n804'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t809", [self.netlist['n1311'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t1231", [self.port['vss'].netconn,self.netlist['n1543'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1230", [self.netlist['n1562'],self.port['vss'].netconn,self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1233", [self.port['vss'].netconn,self.netlist['n1540'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1232", [self.port['vss'].netconn,self.netlist['n76'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1235", [self.port['vss'].netconn,self.netlist['n985'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1234", [self.port['vss'].netconn,self.netlist['n245'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1237", [self.port['vss'].netconn,self.netlist['n682'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t1236", [self.port['vss'].netconn,self.netlist['n786'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t2124", [self.netlist['n482'],self.netlist['n1459'],self.netlist['n336']], isweak=False, parent=self),
            NMOS("t2125", [self.port['vss'].netconn,self.port['res'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t2126", [self.netlist['n221'],self.port['vss'].netconn,self.netlist['n1579']], isweak=False, parent=self),
            NMOS("t2127", [self.netlist['idb4'],self.netlist['Pout4'],self.netlist['H1x1']], isweak=False, parent=self),
            NMOS("t2120", [self.netlist['n358'],self.port['vss'].netconn,self.port['clk0'].netconn], isweak=False, parent=self),
            NMOS("t2121", [self.netlist['n1090'],self.port['vss'].netconn,self.netlist['n1222']], isweak=False, parent=self),
            NMOS("t2122", [self.netlist['n1717'],self.port['vss'].netconn,self.netlist['n382']], isweak=False, parent=self),
            NMOS("t2123", [self.netlist['dasb0'],self.netlist['x0'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t1169", [self.port['vcc'].netconn,self.netlist['n135'],self.netlist['n519']], isweak=False, parent=self),
            NMOS("t1168", [self.netlist['n127'],self.port['vss'].netconn,self.netlist['n519']], isweak=False, parent=self),
            NMOS("t1699", [self.netlist['dpc5_SADL'],self.port['vcc'].netconn,self.netlist['n543']], isweak=False, parent=self),
            NMOS("t1698", [self.port['vss'].netconn,self.netlist['n196'],self.netlist['n543']], isweak=False, parent=self),
            NMOS("t1161", [self.netlist['n79'],self.port['vss'].netconn,self.netlist['n236']], isweak=False, parent=self),
            NMOS("t1692", [self.port['vss'].netconn,self.netlist['n14'],self.netlist['n671']], isweak=False, parent=self),
            NMOS("t1691", [self.port['vss'].netconn,self.netlist['n1358'],self.netlist['n245']], isweak=False, parent=self),
            NMOS("t1690", [self.netlist['n226'],self.netlist['n1093'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1697", [self.port['vss'].netconn,self.netlist['n1593'],self.netlist['n226']], isweak=False, parent=self),
            NMOS("t1696", [self.netlist['n1451'],self.netlist['n668'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t1695", [self.netlist['n1249'],self.port['vss'].netconn,self.netlist['n1269']], isweak=False, parent=self),
            NMOS("t1166", [self.port['vss'].netconn,self.netlist['n753'],self.netlist['n811']], isweak=False, parent=self),
            NMOS("t1753", [self.netlist['n1495'],self.netlist['n1546'],self.netlist['n1600']], isweak=False, parent=self),
            NMOS("t1268", [self.port['vss'].netconn,self.netlist['n1103'],self.netlist['n1244']], isweak=False, parent=self),
            NMOS("t28", [self.netlist['DBZ'],self.port['vss'].netconn,self.netlist['idb5']], isweak=False, parent=self),
            NMOS("t1269", [self.port['vss'].netconn,self.netlist['n620'],self.netlist['n1433']], isweak=False, parent=self),
            NMOS("t1589", [self.netlist['n302'],self.port['vss'].netconn,self.netlist['n409']], isweak=False, parent=self),
            NMOS("t1588", [self.netlist['notalu6'],self.netlist['n722'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1587", [self.port['vcc'].netconn,self.netlist['dasb0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1586", [self.netlist['n1720'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1584", [self.netlist['n373'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1583", [self.netlist['n608'],self.netlist['n559'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1582", [self.netlist['n347'],self.port['vss'].netconn,self.netlist['n904']], isweak=False, parent=self),
            NMOS("t1581", [self.port['vss'].netconn,self.netlist['n1380'],self.netlist['n1154']], isweak=False, parent=self),
            NMOS("t1580", [self.netlist['dpc28_0ADH0'],self.port['vss'].netconn,self.netlist['pipedpc28']], isweak=False, parent=self),
            NMOS("t1767", [self.netlist['n1099'],self.netlist['n1102'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1766", [self.netlist['n512'],self.netlist['n1130'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1765", [self.netlist['n745'],self.netlist['n674'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1764", [self.netlist['n1179'],self.port['vss'].netconn,self.netlist['C34']], isweak=False, parent=self),
            NMOS("t1763", [self.netlist['n619'],self.netlist['n695'],self.netlist['C34']], isweak=False, parent=self),
            NMOS("t1762", [self.port['vss'].netconn,self.netlist['n1056'],self.netlist['n761']], isweak=False, parent=self),
            NMOS("t1761", [self.port['vss'].netconn,self.netlist['n882'],self.netlist['n597']], isweak=False, parent=self),
            NMOS("t1760", [self.port['vcc'].netconn,self.netlist['idb2'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1262", [self.port['vss'].netconn,self.netlist['ir3'],self.netlist['n1620']], isweak=False, parent=self),
            NMOS("t1769", [self.netlist['n298'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1263", [self.netlist['n862'],self.netlist['pipeUNK11'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1565", [self.port['vss'].netconn,self.netlist['n959'],self.netlist['pipeUNK20']], isweak=False, parent=self),
            NMOS("t1567", [self.netlist['n42'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1566", [self.netlist['n1592'],self.port['vss'].netconn,self.netlist['n128']], isweak=False, parent=self),
            NMOS("t1561", [self.port['ab5'].netconn,self.port['vss'].netconn,self.netlist['n210']], isweak=False, parent=self),
            NMOS("t1560", [self.port['vss'].netconn,self.netlist['n482'],self.netlist['n803']], isweak=False, parent=self),
            NMOS("t3149", [self.port['vcc'].netconn,self.netlist['n634'],self.netlist['abl4']], isweak=False, parent=self),
            NMOS("t1569", [self.netlist['n1613'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1999", [self.netlist['n1467'],self.port['vss'].netconn,self.netlist['n1129']], isweak=False, parent=self),
            NMOS("t3148", [self.netlist['n1676'],self.port['vss'].netconn,self.netlist['abl4']], isweak=False, parent=self),
            NMOS("t456", [self.netlist['adh1'],self.port['vcc'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2766", [self.netlist['n513'],self.port['vss'].netconn,self.netlist['n954']], isweak=False, parent=self),
            NMOS("t2542", [self.port['vss'].netconn,self.netlist['n611'],self.netlist['n1509']], isweak=False, parent=self),
            NMOS("t978", [self.netlist['n962'],self.port['vss'].netconn,self.netlist['n1585']], isweak=False, parent=self),
            NMOS("t1994", [self.netlist['n781'],self.port['vss'].netconn,self.netlist['pipeUNK09']], isweak=False, parent=self),
            NMOS("t248", [self.netlist['sb5'],self.netlist['s5'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t922", [self.netlist['n372'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t246", [self.netlist['n316'],self.netlist['n1628'],self.netlist['alub0']], isweak=False, parent=self),
            NMOS("t247", [self.netlist['n143'],self.port['vss'].netconn,self.netlist['alub0']], isweak=False, parent=self),
            NMOS("t244", [self.netlist['n1087'],self.port['vss'].netconn,self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t245", [self.port['vss'].netconn,self.netlist['n1178'],self.netlist['pipeUNK32']], isweak=False, parent=self),
            NMOS("t242", [self.netlist['pipeVectorA1'],self.netlist['n1117'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t243", [self.netlist['notdor4'],self.netlist['n797'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t240", [self.netlist['n1534'],self.port['vss'].netconn,self.netlist['n805']], isweak=False, parent=self),
            NMOS("t241", [self.netlist['a6'],self.netlist['n326'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t920", [self.port['vss'].netconn,self.netlist['n251'],self.netlist['n221']], isweak=False, parent=self),
            NMOS("t979", [self.port['vss'].netconn,self.netlist['n1489'],self.netlist['n1398']], isweak=False, parent=self),
            NMOS("t927", [self.netlist['dpc31_PCHPCH'],self.port['vss'].netconn,self.netlist['n255']], isweak=False, parent=self),
            NMOS("t694", [self.netlist['n322'],self.port['vcc'].netconn,self.netlist['abl7']], isweak=False, parent=self),
            NMOS("t925", [self.netlist['n756'],self.netlist['n626'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t696", [self.netlist['notir3'],self.netlist['n1620'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t525", [self.port['vss'].netconn,self.netlist['n916'],self.netlist['n1517']], isweak=False, parent=self),
            NMOS("t2848", [self.netlist['n179'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t512", [self.netlist['n3'],self.port['vss'].netconn,self.netlist['nots4']], isweak=False, parent=self),
            NMOS("t2169", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['t4']], isweak=False, parent=self),
            NMOS("t3264", [self.port['vss'].netconn,self.netlist['n342'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3265", [self.port['vss'].netconn,self.netlist['n857'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3266", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3267", [self.port['vss'].netconn,self.netlist['n776'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3260", [self.port['vss'].netconn,self.netlist['n492'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3261", [self.port['vss'].netconn,self.netlist['n1204'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3262", [self.port['vss'].netconn,self.netlist['n1520'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3263", [self.port['vss'].netconn,self.netlist['n1259'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3268", [self.port['vss'].netconn,self.netlist['n157'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3269", [self.port['vss'].netconn,self.netlist['n257'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t398", [self.netlist['adh1'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t399", [self.netlist['n1076'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t2534", [self.netlist['n1500'],self.port['vss'].netconn,self.netlist['n1345']], isweak=False, parent=self),
            NMOS("t2767", [self.netlist['n322'],self.port['vss'].netconn,self.netlist['n1026']], isweak=False, parent=self),
            NMOS("t390", [self.netlist['n16'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t391", [self.port['vss'].netconn,self.netlist['n213'],self.port['db1'].netconn], isweak=False, parent=self),
            NMOS("t392", [self.netlist['n686'],self.port['vss'].netconn,self.netlist['pipeVectorA1']], isweak=False, parent=self),
            NMOS("t393", [self.netlist['n280'],self.port['vss'].netconn,self.netlist['nots5']], isweak=False, parent=self),
            NMOS("t394", [self.netlist['a3'],self.netlist['n1654'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t395", [self.netlist['n1062'],self.netlist['n705'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t396", [self.port['vss'].netconn,self.netlist['n6'],self.netlist['n521']], isweak=False, parent=self),
            NMOS("t397", [self.netlist['n417'],self.port['vcc'].netconn,self.netlist['n317']], isweak=False, parent=self),
            NMOS("t2110", [self.netlist['n1065'],self.port['vss'].netconn,self.netlist['n1292']], isweak=False, parent=self),
            NMOS("t2941", [self.port['vss'].netconn,self.netlist['n334'],self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t2946", [self.port['vss'].netconn,self.netlist['n1710'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2947", [self.netlist['n1601'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2944", [self.port['vss'].netconn,self.netlist['n1705'],self.netlist['n630']], isweak=False, parent=self),
            NMOS("t139", [self.netlist['n1632'],self.port['vss'].netconn,self.netlist['alub5']], isweak=False, parent=self),
            NMOS("t2945", [self.port['vss'].netconn,self.netlist['dpc39_PCLPCL'],self.netlist['n1518']], isweak=False, parent=self),
            NMOS("t3192", [self.netlist['n160'],self.port['vss'].netconn,self.netlist['n934']], isweak=False, parent=self),
            NMOS("t3193", [self.port['vss'].netconn,self.netlist['n1689'],self.netlist['n837']], isweak=False, parent=self),
            NMOS("t3191", [self.netlist['n515'],self.port['vss'].netconn,self.netlist['n1253']], isweak=False, parent=self),
            NMOS("t3196", [self.netlist['n423'],self.port['vss'].netconn,self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t3197", [self.netlist['n774'],self.netlist['pipeUNK02'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3194", [self.netlist['alucin'],self.port['vss'].netconn,self.netlist['n590']], isweak=False, parent=self),
            NMOS("t3195", [self.netlist['dasb0'],self.netlist['n332'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t3198", [self.netlist['n968'],self.netlist['n934'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3199", [self.netlist['n415'],self.netlist['n1196'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1238", [self.port['vss'].netconn,self.netlist['n244'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t3463", [self.netlist['n1568'],self.netlist['n1099'],self.netlist['n1542']], isweak=False, parent=self),
            NMOS("t3466", [self.netlist['n1471'],self.port['vss'].netconn,self.netlist['D1x1']], isweak=False, parent=self),
            NMOS("t3467", [self.port['vss'].netconn,self.netlist['n392'],self.netlist['n386']], isweak=False, parent=self),
            NMOS("t3464", [self.netlist['n1498'],self.netlist['n1184'],self.netlist['n1253']], isweak=False, parent=self),
            NMOS("t3465", [self.port['vss'].netconn,self.netlist['n903'],self.netlist['n1253']], isweak=False, parent=self),
            NMOS("t3468", [self.port['vss'].netconn,self.netlist['dpc34_PCLC'],self.netlist['n386']], isweak=False, parent=self),
            NMOS("t3469", [self.netlist['n1565'],self.netlist['n700'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2112", [self.port['vss'].netconn,self.netlist['notx1'],self.netlist['x1']], isweak=False, parent=self),
            NMOS("t3456", [self.netlist['n604'],self.netlist['n1118'],self.netlist['n638']], isweak=False, parent=self),
            NMOS("t3455", [self.netlist['notRnWprepad'],self.port['vss'].netconn,self.netlist['RESG']], isweak=False, parent=self),
            NMOS("t3454", [self.netlist['n1027'],self.netlist['n1649'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1828", [self.netlist['noty7'],self.port['vss'].netconn,self.netlist['y7']], isweak=False, parent=self),
            NMOS("t1829", [self.netlist['notir1'],self.netlist['n119'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1993", [self.netlist['n1020'],self.netlist['n1705'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1820", [self.port['vss'].netconn,self.netlist['n932'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1821", [self.port['vss'].netconn,self.netlist['n309'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1822", [self.port['vss'].netconn,self.netlist['n219'],self.netlist['t2']], isweak=False, parent=self),
            NMOS("t1823", [self.netlist['n1091'],self.netlist['n1360'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1824", [self.netlist['n1106'],self.port['vss'].netconn,self.netlist['n84']], isweak=False, parent=self),
            NMOS("t1825", [self.netlist['n1262'],self.port['vss'].netconn,self.netlist['n1679']], isweak=False, parent=self),
            NMOS("t1826", [self.netlist['n504'],self.netlist['pipeUNK41'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1827", [self.netlist['n1574'],self.netlist['n1228'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t732", [self.port['vss'].netconn,self.netlist['n370'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t733", [self.port['vss'].netconn,self.netlist['n552'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t730", [self.port['vss'].netconn,self.netlist['n286'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t731", [self.port['vss'].netconn,self.netlist['n271'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2025", [self.port['vss'].netconn,self.netlist['n202'],self.netlist['n646']], isweak=False, parent=self),
            NMOS("t2024", [self.netlist['n1343'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t2027", [self.netlist['n739'],self.netlist['n1080'],self.netlist['n1056']], isweak=False, parent=self),
            NMOS("t2026", [self.netlist['n881'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2029", [self.port['vss'].netconn,self.netlist['n631'],self.netlist['n878']], isweak=False, parent=self),
            NMOS("t2028", [self.port['vcc'].netconn,self.netlist['adh7'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t738", [self.port['vss'].netconn,self.netlist['n1057'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t739", [self.port['vss'].netconn,self.netlist['n1582'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t3078", [self.netlist['n1520'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t3289", [self.port['vss'].netconn,self.netlist['n1557'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3048", [self.port['vss'].netconn,self.netlist['n363'],self.netlist['n537']], isweak=False, parent=self),
            NMOS("t3049", [self.port['vss'].netconn,self.netlist['n731'],self.netlist['n993']], isweak=False, parent=self),
            NMOS("t3046", [self.port['vss'].netconn,self.netlist['n1376'],self.netlist['idb2']], isweak=False, parent=self),
            NMOS("t3047", [self.netlist['n125'],self.port['vss'].netconn,self.netlist['n365']], isweak=False, parent=self),
            NMOS("t2939", [self.port['vss'].netconn,self.netlist['n717'],self.netlist['n1132']], isweak=False, parent=self),
            NMOS("t2938", [self.netlist['n1345'],self.port['vss'].netconn,self.netlist['n937']], isweak=False, parent=self),
            NMOS("t1755", [self.netlist['n979'],self.port['vss'].netconn,self.netlist['n905']], isweak=False, parent=self),
            NMOS("t2933", [self.netlist['dpc1_SBY'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2932", [self.port['vss'].netconn,self.netlist['dpc2_XSB'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2931", [self.netlist['dpc3_SBX'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2930", [self.netlist['n1221'],self.netlist['n104'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2937", [self.netlist['dpc34_PCLC'],self.port['vss'].netconn,self.netlist['n937']], isweak=False, parent=self),
            NMOS("t2936", [self.netlist['n1706'],self.port['vss'].netconn,self.netlist['n937']], isweak=False, parent=self),
            NMOS("t2935", [self.netlist['n420'],self.netlist['n47'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2934", [self.netlist['dpc0_YSB'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t655", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t654", [self.netlist['n804'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t657", [self.port['vss'].netconn,self.netlist['n776'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t1917", [self.netlist['n535'],self.port['vss'].netconn,self.netlist['n663']], isweak=False, parent=self),
            NMOS("t651", [self.netlist['n271'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t650", [self.netlist['n286'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t653", [self.netlist['n403'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t652", [self.netlist['n370'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t2689", [self.port['vss'].netconn,self.netlist['n1612'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t1918", [self.port['vss'].netconn,self.netlist['n1286'],self.netlist['n470']], isweak=False, parent=self),
            NMOS("t658", [self.netlist['n257'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t972", [self.port['vss'].netconn,self.netlist['n368'],self.netlist['n1589']], isweak=False, parent=self),
            NMOS("t1494", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n1478']], isweak=False, parent=self),
            NMOS("t2841", [self.netlist['n552'],self.port['vss'].netconn,self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t2483", [self.netlist['n1411'],self.netlist['n515'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2482", [self.netlist['pchp1'],self.netlist['pch1'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2481", [self.netlist['pchp0'],self.netlist['pch0'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2480", [self.netlist['pchp3'],self.netlist['pch3'],self.netlist['dpc31_PCHPCH']], isweak=False, parent=self),
            NMOS("t2339", [self.netlist['n332'],self.port['vss'].netconn,self.netlist['nots0']], isweak=False, parent=self),
            NMOS("t2486", [self.netlist['adh2'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t2485", [self.netlist['adh3'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t2484", [self.port['vss'].netconn,self.netlist['n616'],self.netlist['n665']], isweak=False, parent=self),
            NMOS("t2335", [self.port['vss'].netconn,self.netlist['n1130'],self.netlist['n862']], isweak=False, parent=self),
            NMOS("t2334", [self.netlist['pclp4'],self.netlist['idb4'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t2337", [self.port['vss'].netconn,self.netlist['n133'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2488", [self.netlist['adh4'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t2331", [self.port['vss'].netconn,self.netlist['n838'],self.netlist['n581']], isweak=False, parent=self),
            NMOS("t2330", [self.port['vss'].netconn,self.netlist['n835'],self.netlist['dpc34_PCLC']], isweak=False, parent=self),
            NMOS("t2333", [self.port['vss'].netconn,self.netlist['n134'],self.netlist['n1557']], isweak=False, parent=self),
            NMOS("t2332", [self.netlist['n1563'],self.netlist['n11'],self.netlist['n397']], isweak=False, parent=self),
            NMOS("t2807", [self.netlist['n200'],self.port['vss'].netconn,self.netlist['n919']], isweak=False, parent=self),
            NMOS("t2806", [self.netlist['n1538'],self.netlist['n1486'],self.netlist['n919']], isweak=False, parent=self),
            NMOS("t2805", [self.netlist['n835'],self.netlist['n1229'],self.netlist['n919']], isweak=False, parent=self),
            NMOS("t2804", [self.netlist['x7'],self.netlist['n871'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2803", [self.port['vss'].netconn,self.netlist['n1449'],self.netlist['n958']], isweak=False, parent=self),
            NMOS("t2802", [self.port['vss'].netconn,self.netlist['ir4'],self.netlist['n927']], isweak=False, parent=self),
            NMOS("t1358", [self.port['db5'].netconn,self.port['vss'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t1359", [self.netlist['DC78'],self.netlist['n1030'],self.netlist['n269']], isweak=False, parent=self),
            NMOS("t1356", [self.netlist['n1397'],self.port['vss'].netconn,self.netlist['n1601']], isweak=False, parent=self),
            NMOS("t1357", [self.netlist['dpc24_ACSB'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1354", [self.port['vss'].netconn,self.netlist['n1312'],self.netlist['n1693']], isweak=False, parent=self),
            NMOS("t1355", [self.port['vss'].netconn,self.netlist['n1604'],self.netlist['n1601']], isweak=False, parent=self),
            NMOS("t1352", [self.netlist['n109'],self.port['vss'].netconn,self.netlist['n1380']], isweak=False, parent=self),
            NMOS("t1353", [self.netlist['n405'],self.port['vss'].netconn,self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t1350", [self.netlist['n1100'],self.netlist['n153'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2808", [self.port['vss'].netconn,self.netlist['n1655'],self.netlist['n1211']], isweak=False, parent=self),
            NMOS("t1390", [self.netlist['n466'],self.port['vss'].netconn,self.netlist['dor6']], isweak=False, parent=self),
            NMOS("t813", [self.netlist['n1381'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t812", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t811", [self.netlist['n857'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t810", [self.netlist['n1520'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t817", [self.netlist['n1243'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t816", [self.netlist['n157'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t815", [self.netlist['n776'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t814", [self.netlist['n546'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t819", [self.port['vss'].netconn,self.netlist['n131'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t818", [self.netlist['n1324'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t1222", [self.port['vss'].netconn,self.netlist['ir6'],self.netlist['n1675']], isweak=False, parent=self),
            NMOS("t1223", [self.netlist['n1091'],self.netlist['n363'],self.netlist['n16']], isweak=False, parent=self),
            NMOS("t1220", [self.port['vss'].netconn,self.netlist['n21'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t1221", [self.netlist['n944'],self.port['vss'].netconn,self.netlist['n1449']], isweak=False, parent=self),
            NMOS("t1226", [self.port['vss'].netconn,self.netlist['n550'],self.netlist['n384']], isweak=False, parent=self),
            NMOS("t1227", [self.netlist['n598'],self.netlist['n176'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1224", [self.netlist['n1717'],self.port['vss'].netconn,self.netlist['n1233']], isweak=False, parent=self),
            NMOS("t1225", [self.port['vss'].netconn,self.netlist['n885'],self.netlist['n384']], isweak=False, parent=self),
            NMOS("t2151", [self.netlist['n297'],self.port['vss'].netconn,self.netlist['NMIP']], isweak=False, parent=self),
            NMOS("t2150", [self.netlist['n14'],self.port['vss'].netconn,self.netlist['RESP']], isweak=False, parent=self),
            NMOS("t1228", [self.netlist['a7'],self.netlist['n1592'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1229", [self.netlist['n891'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2155", [self.netlist['n1322'],self.netlist['dasb1'],self.netlist['n36']], isweak=False, parent=self),
            NMOS("t2154", [self.port['vss'].netconn,self.netlist['n1045'],self.netlist['n69']], isweak=False, parent=self),
            NMOS("t2157", [self.port['sync'].netconn,self.port['vcc'].netconn,self.netlist['n417']], isweak=False, parent=self),
            NMOS("t2156", [self.netlist['n735'],self.port['vss'].netconn,self.netlist['n36']], isweak=False, parent=self),
            NMOS("t1178", [self.netlist['n128'],self.port['vss'].netconn,self.netlist['a7']], isweak=False, parent=self),
            NMOS("t1179", [self.port['vss'].netconn,self.netlist['n275'],self.netlist['n773']], isweak=False, parent=self),
            NMOS("t1172", [self.port['vss'].netconn,self.netlist['n1348'],self.netlist['n1628']], isweak=False, parent=self),
            NMOS("t1173", [self.netlist['n468'],self.netlist['n1703'],self.netlist['n16']], isweak=False, parent=self),
            NMOS("t1170", [self.port['vss'].netconn,self.netlist['n1575'],self.netlist['n1360']], isweak=False, parent=self),
            NMOS("t1171", [self.netlist['n252'],self.port['vss'].netconn,self.netlist['n1155']], isweak=False, parent=self),
            NMOS("t1176", [self.netlist['abl5'],self.port['vss'].netconn,self.netlist['n1513']], isweak=False, parent=self),
            NMOS("t677", [self.netlist['n1226'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t1174", [self.port['vss'].netconn,self.netlist['n366'],self.netlist['n1074']], isweak=False, parent=self),
            NMOS("t1175", [self.netlist['n1583'],self.netlist['n308'],self.netlist['n1063']], isweak=False, parent=self),
            NMOS("t676", [self.netlist['n1476'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t1598", [self.port['vss'].netconn,self.netlist['n844'],self.netlist['n1664']], isweak=False, parent=self),
            NMOS("t1599", [self.netlist['sb2'],self.netlist['y2'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t1590", [self.netlist['n957'],self.netlist['n841'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1591", [self.netlist['n681'],self.netlist['n250'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1592", [self.netlist['n740'],self.netlist['n350'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1593", [self.netlist['n1063'],self.netlist['n1071'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1594", [self.netlist['n477'],self.netlist['n296'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1595", [self.netlist['n336'],self.netlist['n277'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1596", [self.netlist['n1318'],self.netlist['n722'],self.netlist['dpc14_SRS']], isweak=False, parent=self),
            NMOS("t1597", [self.netlist['n875'],self.netlist['n469'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1771", [self.netlist['n23'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1772", [self.port['vss'].netconn,self.netlist['n1279'],self.netlist['n600']], isweak=False, parent=self),
            NMOS("t1773", [self.netlist['n969'],self.port['vss'].netconn,self.netlist['n161']], isweak=False, parent=self),
            NMOS("t1774", [self.netlist['dpc0_YSB'],self.port['vcc'].netconn,self.netlist['n161']], isweak=False, parent=self),
            NMOS("t1775", [self.port['vss'].netconn,self.netlist['n715'],self.netlist['n641']], isweak=False, parent=self),
            NMOS("t1776", [self.port['vss'].netconn,self.netlist['dpc34_PCLC'],self.netlist['n641']], isweak=False, parent=self),
            NMOS("t1777", [self.netlist['dpc7_SS'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1778", [self.netlist['n604'],self.port['vss'].netconn,self.netlist['n804']], isweak=False, parent=self),
            NMOS("t1779", [self.netlist['sb5'],self.netlist['y5'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t1576", [self.netlist['n1531'],self.netlist['y3'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1577", [self.netlist['n629'],self.netlist['n202'],self.netlist['n480']], isweak=False, parent=self),
            NMOS("t1574", [self.netlist['n880'],self.netlist['n1514'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1575", [self.port['vss'].netconn,self.netlist['dpc11_SBADD'],self.netlist['n708']], isweak=False, parent=self),
            NMOS("t1572", [self.port['vss'].netconn,self.netlist['n1304'],self.netlist['n673']], isweak=False, parent=self),
            NMOS("t1573", [self.port['vss'].netconn,self.netlist['n39'],self.netlist['n15']], isweak=False, parent=self),
            NMOS("t1570", [self.netlist['notalucin'],self.port['vss'].netconn,self.netlist['alucin']], isweak=False, parent=self),
            NMOS("t1571", [self.netlist['y4'],self.netlist['n658'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1578", [self.netlist['n1606'],self.netlist['n472'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1579", [self.netlist['n90'],self.netlist['pipeUNK05'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1301", [self.port['vss'].netconn,self.netlist['n1292'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t2642", [self.port['vss'].netconn,self.netlist['n662'],self.netlist['n625']], isweak=False, parent=self),
            NMOS("t743", [self.port['vss'].netconn,self.netlist['n1428'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t997", [self.netlist['n927'],self.netlist['n703'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t994", [self.port['vss'].netconn,self.netlist['n340'],self.netlist['n1164']], isweak=False, parent=self),
            NMOS("t1684", [self.netlist['n1046'],self.netlist['n577'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1685", [self.netlist['n956'],self.port['vss'].netconn,self.netlist['n476']], isweak=False, parent=self),
            NMOS("t1686", [self.port['vcc'].netconn,self.netlist['dpc12_0ADD'],self.netlist['n476']], isweak=False, parent=self),
            NMOS("t1302", [self.port['vss'].netconn,self.netlist['n1114'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1681", [self.netlist['n973'],self.port['vss'].netconn,self.netlist['s4']], isweak=False, parent=self),
            NMOS("t1682", [self.netlist['Pout4'],self.port['vss'].netconn,self.netlist['n1471']], isweak=False, parent=self),
            NMOS("t1683", [self.netlist['n621'],self.netlist['n1586'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1305", [self.port['vss'].netconn,self.netlist['n281'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1688", [self.port['vss'].netconn,self.netlist['n1351'],self.netlist['n1562']], isweak=False, parent=self),
            NMOS("t1689", [self.port['vss'].netconn,self.netlist['n961'],self.netlist['idb5']], isweak=False, parent=self),
            NMOS("t1244", [self.port['vss'].netconn,self.netlist['n1396'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t742", [self.port['vss'].netconn,self.netlist['n1311'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2113", [self.port['vss'].netconn,self.netlist['n830'],self.netlist['n1505']], isweak=False, parent=self),
            NMOS("t2033", [self.port['vss'].netconn,self.netlist['n571'],self.netlist['n1671']], isweak=False, parent=self),
            NMOS("t1306", [self.port['vss'].netconn,self.netlist['n1164'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t2409", [self.port['vss'].netconn,self.netlist['n932'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t585", [self.netlist['n719'],self.netlist['idb0'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t2408", [self.port['vss'].netconn,self.netlist['n750'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t856", [self.netlist['notRnWprepad'],self.port['vss'].netconn,self.netlist['n1131']], isweak=False, parent=self),
            NMOS("t2036", [self.netlist['n1294'],self.port['vss'].netconn,self.netlist['n1671']], isweak=False, parent=self),
            NMOS("t587", [self.netlist['n1424'],self.netlist['idb2'],self.netlist['n863']], isweak=False, parent=self),
            NMOS("t2037", [self.port['vss'].netconn,self.netlist['idl4'],self.netlist['notidl4']], isweak=False, parent=self),
            NMOS("t672", [self.port['vss'].netconn,self.netlist['n528'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t2119", [self.port['vss'].netconn,self.netlist['abh0'],self.netlist['n1062']], isweak=False, parent=self),
            NMOS("t2035", [self.port['vss'].netconn,self.netlist['n1019'],self.netlist['n1671']], isweak=False, parent=self),
            NMOS("t2118", [self.netlist['pipeUNK21'],self.netlist['n1231'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t851", [self.port['vss'].netconn,self.netlist['n1050'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2402", [self.netlist['n273'],self.port['vss'].netconn,self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t1387", [self.port['vss'].netconn,self.netlist['n516'],self.netlist['n1691']], isweak=False, parent=self),
            NMOS("t850", [self.netlist['n1665'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t740", [self.port['vss'].netconn,self.netlist['n1031'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t259", [self.netlist['x3'],self.netlist['n242'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t258", [self.port['vss'].netconn,self.netlist['n1425'],self.netlist['DC34']], isweak=False, parent=self),
            NMOS("t1137", [self.netlist['n985'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t251", [self.netlist['s4'],self.netlist['dasb4'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t250", [self.netlist['sb3'],self.netlist['s3'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t253", [self.netlist['sb2'],self.netlist['s2'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t252", [self.netlist['sb1'],self.netlist['s1'],self.netlist['dpc6_SBS']], isweak=False, parent=self),
            NMOS("t255", [self.netlist['n406'],self.port['vss'].netconn,self.netlist['n1525']], isweak=False, parent=self),
            NMOS("t254", [self.port['vss'].netconn,self.netlist['n802'],self.netlist['n781']], isweak=False, parent=self),
            NMOS("t257", [self.port['vss'].netconn,self.netlist['n427'],self.netlist['n647']], isweak=False, parent=self),
            NMOS("t256", [self.netlist['n555'],self.port['vss'].netconn,self.netlist['n1525']], isweak=False, parent=self),
            NMOS("t1643", [self.port['vss'].netconn,self.netlist['n1649'],self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t1644", [self.port['vss'].netconn,self.netlist['n300'],self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t2404", [self.port['vss'].netconn,self.netlist['n677'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t1133", [self.netlist['n76'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1130", [self.netlist['n1233'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1647", [self.netlist['n185'],self.netlist['n1063'],self.netlist['alub4']], isweak=False, parent=self),
            NMOS("t2649", [self.netlist['n433'],self.port['vss'].netconn,self.netlist['n1122']], isweak=False, parent=self),
            NMOS("t746", [self.port['vss'].netconn,self.netlist['n857'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t3211", [self.netlist['pipeUNK18'],self.netlist['n19'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3210", [self.netlist['alub3'],self.netlist['adl3'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t3213", [self.port['vss'].netconn,self.netlist['n1286'],self.netlist['n930']], isweak=False, parent=self),
            NMOS("t3212", [self.netlist['n1179'],self.port['vss'].netconn,self.netlist['n725']], isweak=False, parent=self),
            NMOS("t3215", [self.port['vss'].netconn,self.port['db6'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t3214", [self.netlist['n718'],self.port['vss'].netconn,self.port['db0'].netconn], isweak=False, parent=self),
            NMOS("t3217", [self.netlist['n111'],self.port['vss'].netconn,self.port['db2'].netconn], isweak=False, parent=self),
            NMOS("t3216", [self.netlist['a2'],self.netlist['n1618'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3219", [self.port['vss'].netconn,self.netlist['n896'],self.port['db3'].netconn], isweak=False, parent=self),
            NMOS("t3218", [self.netlist['notalu7'],self.netlist['n304'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1139", [self.port['vss'].netconn,self.netlist['n1664'],self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t389", [self.netlist['n1091'],self.netlist['n12'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t388", [self.netlist['n428'],self.netlist['n1456'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t382", [self.port['db4'].netconn,self.port['vcc'].netconn,self.netlist['n1076']], isweak=False, parent=self),
            NMOS("t387", [self.netlist['n939'],self.netlist['n757'],self.netlist['n1144']], isweak=False, parent=self),
            NMOS("t386", [self.netlist['n544'],self.port['vss'].netconn,self.netlist['n244']], isweak=False, parent=self),
            NMOS("t385", [self.netlist['sb5'],self.netlist['n280'],self.netlist['dpc4_SSB']], isweak=False, parent=self),
            NMOS("t384", [self.netlist['n641'],self.port['vss'].netconn,self.netlist['pcl7']], isweak=False, parent=self),
            NMOS("t1242", [self.port['vss'].netconn,self.netlist['n1324'],self.netlist['notir1']], isweak=False, parent=self),
            NMOS("t744", [self.port['vss'].netconn,self.netlist['n1520'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1533", [self.netlist['sb7'],self.netlist['x7'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t3329", [self.port['vss'].netconn,self.netlist['n1080'],self.netlist['n811']], isweak=False, parent=self),
            NMOS("t3328", [self.netlist['RESP'],self.netlist['pipephi2Reset0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3458", [self.port['ab4'].netconn,self.port['vcc'].netconn,self.netlist['n634']], isweak=False, parent=self),
            NMOS("t3457", [self.port['vss'].netconn,self.netlist['n396'],self.netlist['n1358']], isweak=False, parent=self),
            NMOS("t3324", [self.netlist['n781'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t3327", [self.port['vss'].netconn,self.netlist['n467'],self.netlist['n134']], isweak=False, parent=self),
            NMOS("t3326", [self.port['vss'].netconn,self.netlist['n930'],self.netlist['n134']], isweak=False, parent=self),
            NMOS("t3321", [self.netlist['alu3'],self.port['vss'].netconn,self.netlist['notalu3']], isweak=False, parent=self),
            NMOS("t3320", [self.netlist['n186'],self.port['vss'].netconn,self.netlist['n1224']], isweak=False, parent=self),
            NMOS("t3323", [self.netlist['n41'],self.port['vcc'].netconn,self.netlist['n1277']], isweak=False, parent=self),
            NMOS("t3450", [self.port['vss'].netconn,self.port['ab3'].netconn,self.netlist['n138']], isweak=False, parent=self),
            NMOS("t2032", [self.netlist['n1333'],self.netlist['n80'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t620", [self.port['vss'].netconn,self.netlist['n131'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2030", [self.netlist['n1185'],self.port['vss'].netconn,self.netlist['n916']], isweak=False, parent=self),
            NMOS("t2031", [self.netlist['n272'],self.port['vss'].netconn,self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t729", [self.port['vss'].netconn,self.netlist['n1482'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t728", [self.port['vss'].netconn,self.netlist['n1664'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2034", [self.netlist['n302'],self.port['vss'].netconn,self.netlist['n1671']], isweak=False, parent=self),
            NMOS("t621", [self.port['vss'].netconn,self.netlist['n1420'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t725", [self.port['vss'].netconn,self.netlist['n76'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t724", [self.port['vss'].netconn,self.netlist['n1543'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t727", [self.port['vss'].netconn,self.netlist['n786'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t726", [self.port['vss'].netconn,self.netlist['n1658'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t721", [self.port['vss'].netconn,self.netlist['n382'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t720", [self.netlist['n200'],self.port['vss'].netconn,self.netlist['n1070']], isweak=False, parent=self),
            NMOS("t723", [self.port['vss'].netconn,self.netlist['n84'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t722", [self.port['vss'].netconn,self.netlist['n1233'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t3038", [self.port['vss'].netconn,self.port['db4'].netconn,self.netlist['n147']], isweak=False, parent=self),
            NMOS("t623", [self.netlist['n4'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t3031", [self.port['vss'].netconn,self.netlist['n1454'],self.netlist['n852']], isweak=False, parent=self),
            NMOS("t3030", [self.netlist['Pout6'],self.port['vss'].netconn,self.netlist['n90']], isweak=False, parent=self),
            NMOS("t3033", [self.netlist['n1555'],self.netlist['n1107'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t3032", [self.port['vss'].netconn,self.netlist['n260'],self.netlist['n852']], isweak=False, parent=self),
            NMOS("t3035", [self.netlist['n1072'],self.port['vcc'].netconn,self.netlist['n769']], isweak=False, parent=self),
            NMOS("t3034", [self.netlist['n1325'],self.port['vss'].netconn,self.netlist['n769']], isweak=False, parent=self),
            NMOS("t3037", [self.port['db4'].netconn,self.port['db4'].netconn,self.netlist['n147']], isweak=False, parent=self),
            NMOS("t3036", [self.netlist['n1643'],self.port['vss'].netconn,self.netlist['pcl4']], isweak=False, parent=self),
            NMOS("t1967", [self.netlist['n110'],self.port['vss'].netconn,self.netlist['n1691']], isweak=False, parent=self),
            NMOS("t627", [self.port['vss'].netconn,self.netlist['n1504'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1961", [self.netlist['n332'],self.netlist['adl0'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t1960", [self.netlist['n232'],self.port['vss'].netconn,self.netlist['pcl6']], isweak=False, parent=self),
            NMOS("t1963", [self.netlist['n1190'],self.port['vss'].netconn,self.netlist['s2']], isweak=False, parent=self),
            NMOS("t1962", [self.port['vss'].netconn,self.netlist['n1622'],self.netlist['pd0']], isweak=False, parent=self),
            NMOS("t1965", [self.netlist['BRtaken'],self.netlist['n922'],self.netlist['n270']], isweak=False, parent=self),
            NMOS("t1964", [self.netlist['notir2'],self.netlist['n1300'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t626", [self.netlist['n303'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1966", [self.port['vss'].netconn,self.netlist['n1115'],self.netlist['n270']], isweak=False, parent=self),
            NMOS("t1969", [self.port['vss'].netconn,self.netlist['pclp3'],self.netlist['n868']], isweak=False, parent=self),
            NMOS("t629", [self.port['vss'].netconn,self.netlist['n1074'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2000", [self.port['ab5'].netconn,self.port['vcc'].netconn,self.netlist['n1633']], isweak=False, parent=self),
            NMOS("t3145", [self.port['vss'].netconn,self.netlist['dpc3_SBX'],self.netlist['n662']], isweak=False, parent=self),
            NMOS("t3144", [self.netlist['n155'],self.port['vss'].netconn,self.netlist['alub1']], isweak=False, parent=self),
            NMOS("t3147", [self.port['vss'].netconn,self.netlist['n86'],self.netlist['abl4']], isweak=False, parent=self),
            NMOS("t3146", [self.netlist['n33'],self.port['vss'].netconn,self.netlist['n469']], isweak=False, parent=self),
            NMOS("t3141", [self.netlist['n1649'],self.port['vss'].netconn,self.netlist['n712']], isweak=False, parent=self),
            NMOS("t2499", [self.netlist['n1378'],self.netlist['n1609'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t2328", [self.port['vss'].netconn,self.netlist['irline3'],self.netlist['n1133']], isweak=False, parent=self),
            NMOS("t3142", [self.netlist['sb1'],self.netlist['n767'],self.netlist['dpc0_YSB']], isweak=False, parent=self),
            NMOS("t2494", [self.netlist['n1058'],self.netlist['n632'],self.netlist['n1289']], isweak=False, parent=self),
            NMOS("t2495", [self.netlist['n198'],self.port['vss'].netconn,self.netlist['pipeUNK37']], isweak=False, parent=self),
            NMOS("t2324", [self.netlist['n1505'],self.netlist['n1455'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2497", [self.netlist['n1092'],self.port['vss'].netconn,self.netlist['n888']], isweak=False, parent=self),
            NMOS("t2490", [self.netlist['adh7'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t2491", [self.netlist['adh6'],self.port['vss'].netconn,self.netlist['dpc29_0ADH17']], isweak=False, parent=self),
            NMOS("t2320", [self.netlist['idb5'],self.netlist['pclp5'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t2321", [self.port['vss'].netconn,self.netlist['n693'],self.netlist['n143']], isweak=False, parent=self),
            NMOS("t2810", [self.netlist['n1410'],self.port['vss'].netconn,self.netlist['clearIR']], isweak=False, parent=self),
            NMOS("t2811", [self.netlist['n1668'],self.netlist['n705'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1369", [self.port['vss'].netconn,self.netlist['idl0'],self.netlist['notidl0']], isweak=False, parent=self),
            NMOS("t1368", [self.port['vss'].netconn,self.netlist['n677'],self.netlist['n791']], isweak=False, parent=self),
            NMOS("t2814", [self.netlist['n1457'],self.port['vss'].netconn,self.netlist['n1492']], isweak=False, parent=self),
            NMOS("t2815", [self.netlist['n525'],self.port['vss'].netconn,self.netlist['n266']], isweak=False, parent=self),
            NMOS("t2816", [self.netlist['n188'],self.port['vss'].netconn,self.netlist['n1357']], isweak=False, parent=self),
            NMOS("t2817", [self.netlist['n123'],self.netlist['n246'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1363", [self.port['vss'].netconn,self.netlist['n970'],self.netlist['n149']], isweak=False, parent=self),
            NMOS("t2819", [self.netlist['adl0'],self.port['vss'].netconn,self.netlist['n217']], isweak=False, parent=self),
            NMOS("t1361", [self.netlist['n336'],self.netlist['n1483'],self.netlist['alub6']], isweak=False, parent=self),
            NMOS("t1360", [self.port['vss'].netconn,self.netlist['n1721'],self.netlist['n603']], isweak=False, parent=self),
            NMOS("t1367", [self.port['vss'].netconn,self.netlist['n273'],self.netlist['n791']], isweak=False, parent=self),
            NMOS("t1366", [self.port['vss'].netconn,self.netlist['n965'],self.netlist['n295']], isweak=False, parent=self),
            NMOS("t1365", [self.netlist['n478'],self.port['vss'].netconn,self.netlist['idb4']], isweak=False, parent=self),
            NMOS("t1364", [self.netlist['n762'],self.port['vss'].netconn,self.netlist['n149']], isweak=False, parent=self),
            NMOS("t2714", [self.port['vss'].netconn,self.netlist['n1557'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2976", [self.port['vss'].netconn,self.netlist['n4'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2713", [self.port['vss'].netconn,self.netlist['n660'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2712", [self.port['vss'].netconn,self.netlist['n461'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t538", [self.netlist['n1691'],self.netlist['n740'],self.netlist['dpc13_ORS']], isweak=False, parent=self),
            NMOS("t539", [self.netlist['n29'],self.netlist['n51'],self.netlist['n787']], isweak=False, parent=self),
            NMOS("t828", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t829", [self.netlist['n1478'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t534", [self.port['vss'].netconn,self.netlist['n1041'],self.netlist['n990']], isweak=False, parent=self),
            NMOS("t535", [self.port['vcc'].netconn,self.netlist['n138'],self.netlist['n990']], isweak=False, parent=self),
            NMOS("t824", [self.netlist['n1074'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t537", [self.netlist['dasb3'],self.port['vss'].netconn,self.netlist['n1097']], isweak=False, parent=self),
            NMOS("t530", [self.netlist['n356'],self.netlist['n207'],self.netlist['n293']], isweak=False, parent=self),
            NMOS("t531", [self.port['vss'].netconn,self.netlist['n810'],self.netlist['n293']], isweak=False, parent=self),
            NMOS("t532", [self.netlist['n1106'],self.netlist['n734'],self.netlist['n335']], isweak=False, parent=self),
            NMOS("t533", [self.port['vss'].netconn,self.netlist['n330'],self.netlist['n807']], isweak=False, parent=self),
            NMOS("t2924", [self.port['vss'].netconn,self.netlist['n1210'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2925", [self.port['vss'].netconn,self.netlist['n1385'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2926", [self.port['vss'].netconn,self.netlist['n370'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2927", [self.port['vss'].netconn,self.netlist['n784'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2920", [self.port['vss'].netconn,self.netlist['n772'],self.netlist['n1674']], isweak=False, parent=self),
            NMOS("t2921", [self.port['vss'].netconn,self.netlist['n446'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2922", [self.port['vss'].netconn,self.netlist['n528'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2923", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t1217", [self.netlist['n123'],self.port['vss'].netconn,self.netlist['adl0']], isweak=False, parent=self),
            NMOS("t2143", [self.port['vss'].netconn,self.netlist['dpc16_EORS'],self.netlist['n108']], isweak=False, parent=self),
            NMOS("t2140", [self.port['vss'].netconn,self.netlist['dor0'],self.netlist['notdor0']], isweak=False, parent=self),
            NMOS("t2141", [self.port['vss'].netconn,self.netlist['n1245'],self.netlist['aluvout']], isweak=False, parent=self),
            NMOS("t1213", [self.port['vss'].netconn,self.netlist['n1352'],self.netlist['n352']], isweak=False, parent=self),
            NMOS("t1212", [self.port['vss'].netconn,self.netlist['n1391'],self.netlist['n352']], isweak=False, parent=self),
            NMOS("t2144", [self.port['vss'].netconn,self.netlist['n1446'],self.netlist['n850']], isweak=False, parent=self),
            NMOS("t2145", [self.port['vss'].netconn,self.netlist['n430'],self.netlist['n850']], isweak=False, parent=self),
            NMOS("t2719", [self.port['vss'].netconn,self.netlist['n904'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2718", [self.port['vss'].netconn,self.netlist['n528'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t598", [self.netlist['n1233'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t2498", [self.netlist['n74'],self.netlist['n1675'],self.netlist['fetch']], isweak=False, parent=self),
            NMOS("t3140", [self.netlist['n1464'],self.port['vss'].netconn,self.netlist['n1612']], isweak=False, parent=self),
            NMOS("t230", [self.port['vss'].netconn,self.netlist['n188'],self.netlist['n1606']], isweak=False, parent=self),
            NMOS("t1789", [self.netlist['n1316'],self.port['vss'].netconn,self.netlist['n344']], isweak=False, parent=self),
            NMOS("t1788", [self.netlist['n585'],self.netlist['n20'],self.netlist['n344']], isweak=False, parent=self),
            NMOS("t1785", [self.netlist['n490'],self.port['vss'].netconn,self.port['db4'].netconn], isweak=False, parent=self),
            NMOS("t1784", [self.port['vss'].netconn,self.netlist['n1587'],self.netlist['pd3']], isweak=False, parent=self),
            NMOS("t1787", [self.port['ab8'].netconn,self.port['vcc'].netconn,self.netlist['n826']], isweak=False, parent=self),
            NMOS("t1786", [self.netlist['n557'],self.netlist['n1073'],self.netlist['n344']], isweak=False, parent=self),
            NMOS("t1781", [self.netlist['dpc40_ADLPCL'],self.port['vss'].netconn,self.netlist['n1043']], isweak=False, parent=self),
            NMOS("t1780", [self.netlist['H1x1'],self.port['vss'].netconn,self.netlist['pipeUNK15']], isweak=False, parent=self),
            NMOS("t1783", [self.port['vss'].netconn,self.netlist['n1257'],self.netlist['n1218']], isweak=False, parent=self),
            NMOS("t1782", [self.netlist['sb7'],self.netlist['y7'],self.netlist['dpc1_SBY']], isweak=False, parent=self),
            NMOS("t1543", [self.netlist['n803'],self.port['vss'].netconn,self.netlist['n1084']], isweak=False, parent=self),
            NMOS("t1542", [self.port['vss'].netconn,self.netlist['n854'],self.netlist['n975']], isweak=False, parent=self),
            NMOS("t1541", [self.port['vss'].netconn,self.netlist['n678'],self.netlist['n644']], isweak=False, parent=self),
            NMOS("t1540", [self.port['vss'].netconn,self.netlist['n797'],self.netlist['idb4']], isweak=False, parent=self),
            NMOS("t1547", [self.netlist['n982'],self.netlist['n1689'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1546", [self.port['vss'].netconn,self.netlist['n260'],self.netlist['n1205']], isweak=False, parent=self),
            NMOS("t1545", [self.netlist['dasb7'],self.netlist['n1454'],self.netlist['n1205']], isweak=False, parent=self),
            NMOS("t2327", [self.netlist['n864'],self.netlist['n1507'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1549", [self.netlist['n88'],self.netlist['n522'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1548", [self.port['vcc'].netconn,self.netlist['sb7'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2325", [self.port['vss'].netconn,self.netlist['n1240'],self.netlist['n1566']], isweak=False, parent=self),
            NMOS("t2322", [self.port['vss'].netconn,self.netlist['C01'],self.netlist['n143']], isweak=False, parent=self),
            NMOS("t2323", [self.netlist['n604'],self.port['vss'].netconn,self.netlist['n1031']], isweak=False, parent=self),
            NMOS("t1147", [self.netlist['n787'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1146", [self.netlist['n1355'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1145", [self.netlist['n1337'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1144", [self.netlist['n324'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1143", [self.netlist['n286'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t2492", [self.port['vss'].netconn,self.netlist['n1230'],self.netlist['n360']], isweak=False, parent=self),
            NMOS("t1141", [self.netlist['n1482'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1140", [self.netlist['n682'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t2493", [self.port['vss'].netconn,self.netlist['n1118'],self.netlist['n204']], isweak=False, parent=self),
            NMOS("t1149", [self.netlist['n179'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1148", [self.netlist['n257'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t3270", [self.port['vss'].netconn,self.netlist['n1324'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t2812", [self.port['vss'].netconn,self.netlist['n1211'],self.netlist['n273']], isweak=False, parent=self),
            NMOS("t1979", [self.netlist['n1040'],self.netlist['n782'],self.netlist['n1303']], isweak=False, parent=self),
            NMOS("t1734", [self.netlist['n1198'],self.netlist['n626'],self.netlist['n1401']], isweak=False, parent=self),
            NMOS("t2813", [self.netlist['n1445'],self.port['vss'].netconn,self.netlist['n1492']], isweak=False, parent=self),
            NMOS("t3143", [self.netlist['n189'],self.netlist['n841'],self.netlist['alub1']], isweak=False, parent=self),
            NMOS("t2818", [self.port['vcc'].netconn,self.netlist['n7'],self.netlist['dor6']], isweak=False, parent=self),
            NMOS("t1362", [self.netlist['n1084'],self.port['vss'].netconn,self.netlist['alub6']], isweak=False, parent=self),
            NMOS("t599", [self.netlist['n286'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t752", [self.port['vss'].netconn,self.netlist['n1324'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1676", [self.netlist['n1014'],self.netlist['adl6'],self.netlist['n1564']], isweak=False, parent=self),
            NMOS("t49", [self.netlist['dasb4'],self.netlist['alua4'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t48", [self.netlist['sb3'],self.netlist['alua3'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t43", [self.port['vss'].netconn,self.netlist['n25'],self.netlist['n192']], isweak=False, parent=self),
            NMOS("t42", [self.netlist['n409'],self.port['vss'].netconn,self.netlist['n1622']], isweak=False, parent=self),
            NMOS("t41", [self.port['vss'].netconn,self.netlist['n307'],self.netlist['n1174']], isweak=False, parent=self),
            NMOS("t40", [self.port['vss'].netconn,self.netlist['n1456'],self.netlist['pipeT3out']], isweak=False, parent=self),
            NMOS("t47", [self.netlist['alua2'],self.netlist['sb2'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t46", [self.netlist['alua1'],self.netlist['sb1'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t45", [self.netlist['n767'],self.netlist['y1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t44", [self.netlist['alu4'],self.port['vss'].netconn,self.netlist['notalu4']], isweak=False, parent=self),
            NMOS("t3202", [self.netlist['n669'],self.port['vss'].netconn,self.netlist['n303']], isweak=False, parent=self),
            NMOS("t3203", [self.netlist['alub6'],self.netlist['adl6'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t3200", [self.netlist['n1688'],self.netlist['n680'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3201", [self.port['vss'].netconn,self.netlist['n106'],self.netlist['n1528']], isweak=False, parent=self),
            NMOS("t3206", [self.netlist['alub1'],self.netlist['adl1'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t3207", [self.netlist['alub4'],self.netlist['adl4'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t3204", [self.netlist['alub7'],self.netlist['adl7'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t3208", [self.netlist['adl5'],self.netlist['alub5'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t3209", [self.netlist['VEC0'],self.netlist['n1126'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t993", [self.netlist['pclp2'],self.netlist['idb2'],self.netlist['dpc37_PCLDB']], isweak=False, parent=self),
            NMOS("t1469", [self.netlist['n150'],self.netlist['n613'],self.netlist['n1682']], isweak=False, parent=self),
            NMOS("t853", [self.netlist['n1310'],self.port['vss'].netconn,self.netlist['n1063']], isweak=False, parent=self),
            NMOS("t3448", [self.port['vss'].netconn,self.netlist['n852'],self.netlist['sb7']], isweak=False, parent=self),
            NMOS("t283", [self.netlist['s6'],self.netlist['n618'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t280", [self.netlist['n1364'],self.port['vss'].netconn,self.netlist['n101']], isweak=False, parent=self),
            NMOS("t281", [self.netlist['n844'],self.port['vss'].netconn,self.netlist['n985']], isweak=False, parent=self),
            NMOS("t286", [self.netlist['s3'],self.netlist['n998'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t287", [self.netlist['s2'],self.netlist['n1389'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t284", [self.netlist['s5'],self.netlist['n280'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t285", [self.netlist['s4'],self.netlist['n3'],self.netlist['dpc7_SS']], isweak=False, parent=self),
            NMOS("t3440", [self.port['vss'].netconn,self.netlist['n462'],self.netlist['n1338']], isweak=False, parent=self),
            NMOS("t3337", [self.netlist['n720'],self.netlist['n1338'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3334", [self.netlist['n1264'],self.netlist['n1209'],self.netlist['n609']], isweak=False, parent=self),
            NMOS("t289", [self.netlist['n883'],self.port['vss'].netconn,self.netlist['adh3']], isweak=False, parent=self),
            NMOS("t3332", [self.netlist['n1641'],self.port['vss'].netconn,self.netlist['n809']], isweak=False, parent=self),
            NMOS("t3333", [self.netlist['n1547'],self.netlist['n1192'],self.netlist['n609']], isweak=False, parent=self),
            NMOS("t3330", [self.netlist['n100'],self.netlist['n1205'],self.netlist['n811']], isweak=False, parent=self),
            NMOS("t3331", [self.port['vcc'].netconn,self.netlist['idb1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t826", [self.netlist['n487'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t827", [self.port['vss'].netconn,self.netlist['n579'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2515", [self.netlist['n42'],self.port['vss'].netconn,self.netlist['n1613']], isweak=False, parent=self),
            NMOS("t536", [self.netlist['n1575'],self.port['vss'].netconn,self.netlist['n1357']], isweak=False, parent=self),
            NMOS("t799", [self.netlist['n1612'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t825", [self.netlist['n1246'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t822", [self.netlist['n1504'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t3186", [self.netlist['n1253'],self.port['vss'].netconn,self.netlist['n1542']], isweak=False, parent=self),
            NMOS("t823", [self.netlist['n1086'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2519", [self.netlist['n378'],self.netlist['pipeT5out'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t820", [self.port['vss'].netconn,self.netlist['n1396'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2799", [self.netlist['n351'],self.netlist['alub6'],self.netlist['dpc8_nDBADD']], isweak=False, parent=self),
            NMOS("t3188", [self.netlist['idl1'],self.port['vss'].netconn,self.netlist['notidl1']], isweak=False, parent=self),
            NMOS("t2797", [self.netlist['n658'],self.port['vss'].netconn,self.netlist['noty4']], isweak=False, parent=self),
            NMOS("t2796", [self.netlist['n819'],self.port['vss'].netconn,self.netlist['pipeUNK23']], isweak=False, parent=self),
            NMOS("t2795", [self.port['vss'].netconn,self.netlist['n637'],self.netlist['C67']], isweak=False, parent=self),
            NMOS("t2794", [self.netlist['n1489'],self.netlist['notaluvout'],self.netlist['C67']], isweak=False, parent=self),
            NMOS("t2793", [self.netlist['dpc2_XSB'],self.port['vss'].netconn,self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t2792", [self.port['vss'].netconn,self.netlist['n252'],self.netlist['n1665']], isweak=False, parent=self),
            NMOS("t2791", [self.netlist['dpc24_ACSB'],self.port['vss'].netconn,self.netlist['n1335']], isweak=False, parent=self),
            NMOS("t2790", [self.netlist['n431'],self.netlist['n807'],self.netlist['n1599']], isweak=False, parent=self),
            NMOS("t758", [self.port['vss'].netconn,self.netlist['n303'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t759", [self.port['vss'].netconn,self.netlist['n1086'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t797", [self.port['vss'].netconn,self.netlist['n370'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t2559", [self.netlist['n1352'],self.port['vss'].netconn,self.netlist['n1642']], isweak=False, parent=self),
            NMOS("t2558", [self.port['vss'].netconn,self.netlist['n1129'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2009", [self.netlist['notir7'],self.netlist['n541'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2008", [self.port['vss'].netconn,self.netlist['n821'],self.netlist['n1067']], isweak=False, parent=self),
            NMOS("t2007", [self.port['vss'].netconn,self.netlist['AxB5'],self.netlist['n647']], isweak=False, parent=self),
            NMOS("t2006", [self.port['vss'].netconn,self.netlist['n867'],self.netlist['n901']], isweak=False, parent=self),
            NMOS("t2005", [self.port['vss'].netconn,self.netlist['n1556'],self.netlist['n901']], isweak=False, parent=self),
            NMOS("t753", [self.port['vss'].netconn,self.netlist['n179'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t754", [self.port['vss'].netconn,self.netlist['n131'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2148", [self.port['vcc'].netconn,self.netlist['adh5'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t756", [self.port['vss'].netconn,self.netlist['n1396'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t757", [self.port['vss'].netconn,self.netlist['n167'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t3028", [self.port['vss'].netconn,self.netlist['n1510'],self.netlist['n1021']], isweak=False, parent=self),
            NMOS("t3029", [self.port['vss'].netconn,self.netlist['n365'],self.netlist['n809']], isweak=False, parent=self),
            NMOS("t3022", [self.port['vss'].netconn,self.netlist['n551'],self.netlist['n393']], isweak=False, parent=self),
            NMOS("t3023", [self.netlist['n1085'],self.netlist['pipeUNK23'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3020", [self.netlist['n12'],self.port['vss'].netconn,self.netlist['pipeT2out']], isweak=False, parent=self),
            NMOS("t3021", [self.netlist['n1016'],self.port['vss'].netconn,self.netlist['adl1']], isweak=False, parent=self),
            NMOS("t3026", [self.netlist['n532'],self.netlist['n1013'],self.netlist['n592']], isweak=False, parent=self),
            NMOS("t3027", [self.netlist['n1217'],self.port['vss'].netconn,self.netlist['n592']], isweak=False, parent=self),
            NMOS("t3024", [self.netlist['pipeUNK28'],self.netlist['n1175'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3025", [self.port['vss'].netconn,self.netlist['n1312'],self.netlist['n1291']], isweak=False, parent=self),
            NMOS("t2889", [self.netlist['notir4'],self.port['vss'].netconn,self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1218", [self.netlist['n185'],self.port['vss'].netconn,self.netlist['alua4']], isweak=False, parent=self),
            NMOS("t1972", [self.port['vss'].netconn,self.netlist['n1681'],self.netlist['n546']], isweak=False, parent=self),
            NMOS("t2142", [self.netlist['n1644'],self.port['vss'].netconn,self.netlist['pipeUNK04']], isweak=False, parent=self),
            NMOS("t1970", [self.port['vss'].netconn,self.netlist['n794'],self.netlist['dor1']], isweak=False, parent=self),
            NMOS("t1971", [self.port['vss'].netconn,self.netlist['n288'],self.netlist['dor1']], isweak=False, parent=self),
            NMOS("t1976", [self.netlist['n1197'],self.netlist['n1390'],self.netlist['C56']], isweak=False, parent=self),
            NMOS("t1977", [self.netlist['n174'],self.port['vss'].netconn,self.netlist['C56']], isweak=False, parent=self),
            NMOS("t1974", [self.port['vss'].netconn,self.netlist['dpc39_PCLPCL'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1975", [self.netlist['ir1'],self.port['vss'].netconn,self.netlist['n119']], isweak=False, parent=self),
            NMOS("t1978", [self.port['vss'].netconn,self.netlist['t4'],self.netlist['n188']], isweak=False, parent=self),
            NMOS("t638", [self.netlist['n272'],self.port['vss'].netconn,self.netlist['n236']], isweak=False, parent=self),
            NMOS("t1215", [self.netlist['n845'],self.netlist['n511'],self.netlist['n553']], isweak=False, parent=self),
            NMOS("t1214", [self.netlist['n1657'],self.netlist['n820'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2928", [self.port['vss'].netconn,self.netlist['n776'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t2239", [self.netlist['n1344'],self.netlist['idb4'],self.netlist['dpc26_ACDB']], isweak=False, parent=self),
            NMOS("t2929", [self.port['vss'].netconn,self.netlist['n1168'],self.netlist['t5']], isweak=False, parent=self),
            NMOS("t3156", [self.port['vss'].netconn,self.netlist['n231'],self.netlist['n1019']], isweak=False, parent=self),
            NMOS("t3157", [self.port['vss'].netconn,self.netlist['pclp6'],self.netlist['n731']], isweak=False, parent=self),
            NMOS("t3154", [self.port['vss'].netconn,self.netlist['n104'],self.netlist['n275']], isweak=False, parent=self),
            NMOS("t2318", [self.port['vss'].netconn,self.netlist['n1419'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t3152", [self.netlist['n216'],self.port['vss'].netconn,self.netlist['n681']], isweak=False, parent=self),
            NMOS("t1211", [self.netlist['sb3'],self.netlist['alu3'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t3150", [self.netlist['n1709'],self.port['vss'].netconn,self.netlist['notx1']], isweak=False, parent=self),
            NMOS("t3151", [self.netlist['n1389'],self.port['vss'].netconn,self.netlist['nots2']], isweak=False, parent=self),
            NMOS("t2313", [self.netlist['n1155'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2312", [self.port['vss'].netconn,self.netlist['n1292'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2311", [self.port['vss'].netconn,self.netlist['n53'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t1210", [self.netlist['alu4'],self.netlist['dasb4'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t2317", [self.netlist['n1710'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2316", [self.netlist['n950'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t3158", [self.netlist['n1120'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t3159", [self.netlist['n2'],self.netlist['n1039'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t691", [self.netlist['n278'],self.port['vss'].netconn,self.netlist['pch6']], isweak=False, parent=self),
            NMOS("t2177", [self.port['vss'].netconn,self.netlist['n1569'],self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2176", [self.netlist['n1589'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2175", [self.netlist['n352'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2174", [self.netlist['n461'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2173", [self.netlist['n341'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2172", [self.netlist['n354'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t529", [self.netlist['n57'],self.netlist['n1402'],self.netlist['n293']], isweak=False, parent=self),
            NMOS("t2170", [self.port['vss'].netconn,self.netlist['n492'],self.netlist['t4']], isweak=False, parent=self),
            NMOS("t527", [self.netlist['alu5'],self.netlist['adl5'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t526", [self.netlist['adl7'],self.netlist['alu7'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t833", [self.netlist['n1052'],self.port['vss'].netconn,self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t524", [self.port['vss'].netconn,self.netlist['n568'],self.port['db5'].netconn], isweak=False, parent=self),
            NMOS("t523", [self.netlist['n459'],self.netlist['n844'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t522", [self.netlist['alu4'],self.netlist['adl4'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t521", [self.netlist['alu3'],self.netlist['adl3'],self.netlist['dpc21_ADDADL']], isweak=False, parent=self),
            NMOS("t2178", [self.port['vss'].netconn,self.netlist['n281'],self.netlist['t4']], isweak=False, parent=self),
            NMOS("t1208", [self.netlist['sb6'],self.netlist['alu6'],self.netlist['dpc20_ADDSB06']], isweak=False, parent=self),
            NMOS("t2774", [self.port['vss'].netconn,self.netlist['C45'],self.netlist['n404']], isweak=False, parent=self),
            NMOS("t2777", [self.netlist['n1479'],self.port['vss'].netconn,self.netlist['n842']], isweak=False, parent=self),
            NMOS("t2776", [self.netlist['dpc24_ACSB'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2771", [self.netlist['n191'],self.netlist['pipeUNK40'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2954", [self.port['vss'].netconn,self.netlist['n665'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2773", [self.port['vss'].netconn,self.netlist['n918'],self.netlist['n404']], isweak=False, parent=self),
            NMOS("t2772", [self.netlist['n1455'],self.port['vss'].netconn,self.netlist['n822']], isweak=False, parent=self),
            NMOS("t1200", [self.port['vss'].netconn,self.netlist['n388'],self.netlist['n516']], isweak=False, parent=self),
            NMOS("t2958", [self.port['vss'].netconn,self.netlist['n552'],self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1202", [self.netlist['n1044'],self.port['vss'].netconn,self.netlist['n812']], isweak=False, parent=self),
            NMOS("t1203", [self.netlist['n1131'],self.netlist['n1352'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2779", [self.netlist['n1140'],self.port['vcc'].netconn,self.netlist['abh1']], isweak=False, parent=self),
            NMOS("t1205", [self.netlist['n95'],self.netlist['n1375'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1206", [self.netlist['n1529'],self.netlist['n1089'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1207", [self.netlist['n946'],self.netlist['n454'],self.netlist['n844']], isweak=False, parent=self),
            NMOS("t1374", [self.netlist['n1649'],self.port['vss'].netconn,self.netlist['n1109']], isweak=False, parent=self),
            NMOS("t1375", [self.netlist['n318'],self.port['vss'].netconn,self.netlist['p1']], isweak=False, parent=self),
            NMOS("t1376", [self.netlist['n881'],self.netlist['n330'],self.netlist['n538']], isweak=False, parent=self),
            NMOS("t1377", [self.netlist['n1223'],self.port['vss'].netconn,self.netlist['n43']], isweak=False, parent=self),
            NMOS("t1372", [self.netlist['n966'],self.port['vss'].netconn,self.netlist['n1683']], isweak=False, parent=self),
            NMOS("t1373", [self.port['vss'].netconn,self.netlist['dpc1_SBY'],self.netlist['n441']], isweak=False, parent=self),
            NMOS("t1378", [self.port['vss'].netconn,self.netlist['dpc6_SBS'],self.netlist['n282']], isweak=False, parent=self),
            NMOS("t1379", [self.netlist['pchp5'],self.port['vss'].netconn,self.netlist['n33']], isweak=False, parent=self),
            NMOS("t2863", [self.netlist['n1059'],self.netlist['n633'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1798", [self.netlist['n264'],self.port['vss'].netconn,self.netlist['n1149']], isweak=False, parent=self),
            NMOS("t1799", [self.netlist['n1218'],self.port['vss'].netconn,self.netlist['n1565']], isweak=False, parent=self),
            NMOS("t1796", [self.netlist['n160'],self.netlist['n1049'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1797", [self.port['vss'].netconn,self.netlist['n647'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1792", [self.port['vss'].netconn,self.port['db7'].netconn,self.netlist['n1501']], isweak=False, parent=self),
            NMOS("t1790", [self.netlist['n934'],self.netlist['pipeUNK27'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1791", [self.port['vss'].netconn,self.netlist['VEC0'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t1558", [self.netlist['notRdy0'],self.netlist['n1624'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t1559", [self.port['vss'].netconn,self.netlist['n616'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1554", [self.port['vss'].netconn,self.port['ab4'].netconn,self.netlist['n86']], isweak=False, parent=self),
            NMOS("t1550", [self.netlist['n914'],self.netlist['n484'],self.netlist['n1386']], isweak=False, parent=self),
            NMOS("t1551", [self.port['vss'].netconn,self.netlist['n307'],self.netlist['n31']], isweak=False, parent=self),
            NMOS("t1552", [self.port['vss'].netconn,self.netlist['n1580'],self.netlist['sb2']], isweak=False, parent=self),
            NMOS("t1150", [self.netlist['n1420'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1151", [self.netlist['n4'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1152", [self.netlist['n167'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1153", [self.netlist['n145'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1154", [self.netlist['n517'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1155", [self.netlist['n301'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1156", [self.netlist['n950'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1157", [self.port['vss'].netconn,self.netlist['n1710'],self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1158", [self.port['vss'].netconn,self.netlist['n1419'],self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1159", [self.netlist['n1164'],self.port['vss'].netconn,self.netlist['notir7']], isweak=False, parent=self),
            NMOS("t1968", [self.netlist['C23'],self.port['vss'].netconn,self.netlist['n1691']], isweak=False, parent=self),
            NMOS("t1389", [self.netlist['n471'],self.port['vss'].netconn,self.netlist['dor6']], isweak=False, parent=self),
            NMOS("t606", [self.port['vss'].netconn,self.netlist['n985'],self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1838", [self.port['vss'].netconn,self.netlist['n1460'],self.netlist['pd6']], isweak=False, parent=self),
            NMOS("t196", [self.netlist['n612'],self.port['vcc'].netconn,self.netlist['n1720']], isweak=False, parent=self),
            NMOS("t197", [self.port['vcc'].netconn,self.netlist['n1076'],self.netlist['dor4']], isweak=False, parent=self),
            NMOS("t194", [self.netlist['n1172'],self.netlist['n405'],self.netlist['BRtaken']], isweak=False, parent=self),
            NMOS("t58", [self.netlist['n480'],self.netlist['n1092'],self.netlist['n264']], isweak=False, parent=self),
            NMOS("t59", [self.port['vss'].netconn,self.netlist['n632'],self.netlist['n1582']], isweak=False, parent=self),
            NMOS("t195", [self.netlist['n373'],self.port['vss'].netconn,self.netlist['n1720']], isweak=False, parent=self),
            NMOS("t2055", [self.netlist['n1455'],self.port['vss'].netconn,self.netlist['n1243']], isweak=False, parent=self),
            NMOS("t50", [self.port['vss'].netconn,self.netlist['n794'],self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t61", [self.netlist['n136'],self.netlist['n274'],self.netlist['n1003']], isweak=False, parent=self),
            NMOS("t52", [self.netlist['dpc4_SSB'],self.port['vss'].netconn,self.netlist['n593']], isweak=False, parent=self),
            NMOS("t53", [self.netlist['dasb0'],self.netlist['alua0'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t54", [self.netlist['n1362'],self.netlist['n613'],self.netlist['n600']], isweak=False, parent=self),
            NMOS("t55", [self.netlist['sb5'],self.netlist['alua5'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t56", [self.netlist['sb6'],self.netlist['alua6'],self.netlist['dpc11_SBADD']], isweak=False, parent=self),
            NMOS("t193", [self.netlist['n368'],self.port['vss'].netconn,self.netlist['n309']], isweak=False, parent=self),
            NMOS("t190", [self.port['vss'].netconn,self.netlist['notir3'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t3239", [self.port['vss'].netconn,self.netlist['n1512'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3238", [self.port['vss'].netconn,self.netlist['n60'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3237", [self.port['vss'].netconn,self.netlist['n645'],self.netlist['NMIP']], isweak=False, parent=self),
            NMOS("t3236", [self.netlist['n420'],self.port['vss'].netconn,self.netlist['n865']], isweak=False, parent=self),
            NMOS("t3235", [self.netlist['n1251'],self.port['vss'].netconn,self.netlist['noty7']], isweak=False, parent=self),
            NMOS("t3234", [self.netlist['n1265'],self.port['vss'].netconn,self.netlist['pch2']], isweak=False, parent=self),
            NMOS("t3233", [self.netlist['n1344'],self.netlist['a4'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3232", [self.port['vss'].netconn,self.netlist['n388'],self.netlist['n936']], isweak=False, parent=self),
            NMOS("t3231", [self.port['vss'].netconn,self.netlist['n1707'],self.netlist['n936']], isweak=False, parent=self),
            NMOS("t702", [self.port['vcc'].netconn,self.netlist['n1152'],self.netlist['abl2']], isweak=False, parent=self),
            NMOS("t701", [self.port['vss'].netconn,self.netlist['n951'],self.netlist['abl2']], isweak=False, parent=self),
            NMOS("t700", [self.port['vss'].netconn,self.netlist['n642'],self.netlist['abl2']], isweak=False, parent=self),
            NMOS("t2425", [self.port['vss'].netconn,self.netlist['n1546'],self.netlist['n781']], isweak=False, parent=self),
            NMOS("t2421", [self.port['vss'].netconn,self.netlist['n607'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t2420", [self.port['vss'].netconn,self.netlist['n1665'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t3220", [self.port['vss'].netconn,self.netlist['n1211'],self.netlist['n1002']], isweak=False, parent=self),
            NMOS("t2423", [self.port['vss'].netconn,self.netlist['n1050'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t3221", [self.netlist['n299'],self.netlist['n1470'],self.netlist['n1416']], isweak=False, parent=self),
            NMOS("t2422", [self.port['vss'].netconn,self.netlist['n1419'],self.netlist['notir3']], isweak=False, parent=self),
            NMOS("t356", [self.port['vss'].netconn,self.netlist['n600'],self.netlist['n1341']], isweak=False, parent=self),
            NMOS("t1724", [self.netlist['n1389'],self.netlist['adl2'],self.netlist['dpc5_SADL']], isweak=False, parent=self),
            NMOS("t3309", [self.netlist['n871'],self.port['vss'].netconn,self.netlist['notx7']], isweak=False, parent=self),
            NMOS("t3223", [self.netlist['n272'],self.port['vss'].netconn,self.netlist['n862']], isweak=False, parent=self),
            NMOS("t299", [self.port['vcc'].netconn,self.netlist['adh0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t298", [self.port['vss'].netconn,self.netlist['n455'],self.netlist['n279']], isweak=False, parent=self),
            NMOS("t295", [self.netlist['n1187'],self.port['vss'].netconn,self.netlist['s6']], isweak=False, parent=self),
            NMOS("t294", [self.netlist['n1649'],self.port['vss'].netconn,self.netlist['n764']], isweak=False, parent=self),
            NMOS("t3301", [self.port['vss'].netconn,self.netlist['n1569'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t296", [self.netlist['idl0'],self.netlist['n719'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t291", [self.netlist['n347'],self.port['vss'].netconn,self.netlist['n281']], isweak=False, parent=self),
            NMOS("t2588", [self.port['vss'].netconn,self.netlist['n1392'],self.port['nmi'].netconn], isweak=False, parent=self),
            NMOS("t3305", [self.port['vss'].netconn,self.netlist['n1385'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t292", [self.port['vss'].netconn,self.netlist['n553'],self.netlist['n781']], isweak=False, parent=self),
            NMOS("t2589", [self.netlist['n1024'],self.netlist['n1699'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1902", [self.netlist['n1617'],self.netlist['n1327'],self.netlist['C67']], isweak=False, parent=self),
            NMOS("t3057", [self.port['vss'].netconn,self.netlist['cclk'],self.netlist['n1467']], isweak=False, parent=self),
            NMOS("t3508", [self.port['vss'].netconn,self.netlist['dpc35_PCHC'],self.netlist['n923']], isweak=False, parent=self),
            NMOS("t3493", [self.netlist['n1037'],self.netlist['n1280'],self.netlist['n145']], isweak=False, parent=self),
            NMOS("t3492", [self.port['vcc'].netconn,self.netlist['dpc6_SBS'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t3491", [self.netlist['n282'],self.port['vss'].netconn,self.netlist['n6']], isweak=False, parent=self),
            NMOS("t3490", [self.netlist['n669'],self.port['vss'].netconn,self.netlist['n1504']], isweak=False, parent=self),
            NMOS("t3497", [self.netlist['t3'],self.port['vss'].netconn,self.netlist['n678']], isweak=False, parent=self),
            NMOS("t3496", [self.port['vss'].netconn,self.netlist['notx6'],self.netlist['x6']], isweak=False, parent=self),
            NMOS("t3495", [self.netlist['n583'],self.port['vss'].netconn,self.netlist['idb1']], isweak=False, parent=self),
            NMOS("t3494", [self.port['vss'].netconn,self.netlist['n35'],self.netlist['n43']], isweak=False, parent=self),
            NMOS("t3499", [self.netlist['n93'],self.netlist['pd0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3498", [self.netlist['n1319'],self.netlist['pd1'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2788", [self.netlist['notaluvout'],self.port['vss'].netconn,self.netlist['n637']], isweak=False, parent=self),
            NMOS("t3505", [self.port['vss'].netconn,self.netlist['n1130'],self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t3504", [self.port['vcc'].netconn,self.netlist['idb4'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2780", [self.port['vss'].netconn,self.netlist['n1231'],self.netlist['n1409']], isweak=False, parent=self),
            NMOS("t2781", [self.port['vss'].netconn,self.netlist['n11'],self.netlist['n1228']], isweak=False, parent=self),
            NMOS("t2782", [self.port['vss'].netconn,self.netlist['n1135'],self.netlist['sb5']], isweak=False, parent=self),
            NMOS("t2783", [self.port['vss'].netconn,self.netlist['n1695'],self.netlist['alua7']], isweak=False, parent=self),
            NMOS("t2784", [self.netlist['n1398'],self.port['vss'].netconn,self.netlist['alua7']], isweak=False, parent=self),
            NMOS("t3507", [self.port['vss'].netconn,self.netlist['n356'],self.netlist['n923']], isweak=False, parent=self),
            NMOS("t2786", [self.port['vss'].netconn,self.netlist['n1117'],self.netlist['n70']], isweak=False, parent=self),
            NMOS("t2787", [self.port['vss'].netconn,self.netlist['n10'],self.netlist['n1211']], isweak=False, parent=self),
            NMOS("t2018", [self.netlist['nnT2BR'],self.port['vss'].netconn,self.netlist['n636']], isweak=False, parent=self),
            NMOS("t2019", [self.port['vcc'].netconn,self.port['ab0'].netconn,self.netlist['n855']], isweak=False, parent=self),
            NMOS("t3015", [self.netlist['n1545'],self.port['vss'].netconn,self.netlist['n1034']], isweak=False, parent=self),
            NMOS("t3014", [self.netlist['n1087'],self.port['vss'].netconn,self.netlist['n717']], isweak=False, parent=self),
            NMOS("t3013", [self.netlist['RESG'],self.port['vss'].netconn,self.netlist['n717']], isweak=False, parent=self),
            NMOS("t3012", [self.netlist['n1382'],self.netlist['n1291'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t3011", [self.port['vss'].netconn,self.netlist['n1425'],self.netlist['n988']], isweak=False, parent=self),
            NMOS("t3010", [self.netlist['n742'],self.netlist['n854'],self.netlist['n312']], isweak=False, parent=self),
            NMOS("t2010", [self.netlist['n916'],self.netlist['n1409'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2011", [self.netlist['n862'],self.port['vss'].netconn,self.netlist['n666']], isweak=False, parent=self),
            NMOS("t2544", [self.port['vcc'].netconn,self.netlist['n43'],self.netlist['n839']], isweak=False, parent=self),
            NMOS("t2013", [self.netlist['pchp7'],self.port['vss'].netconn,self.netlist['n535']], isweak=False, parent=self),
            NMOS("t747", [self.port['vss'].netconn,self.netlist['n712'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t2543", [self.netlist['n1507'],self.port['vss'].netconn,self.netlist['adl3']], isweak=False, parent=self),
            NMOS("t2016", [self.port['vss'].netconn,self.netlist['DBNeg'],self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t2017", [self.netlist['DBZ'],self.port['vss'].netconn,self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t3503", [self.netlist['nots2'],self.netlist['n1190'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2585", [self.netlist['n1608'],self.port['vss'].netconn,self.netlist['n1423']], isweak=False, parent=self),
            NMOS("t3300", [self.port['vss'].netconn,self.netlist['n1226'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t1544", [self.port['vss'].netconn,self.netlist['C67'],self.netlist['n1084']], isweak=False, parent=self),
            NMOS("t1949", [self.netlist['n1024'],self.port['vss'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t1948", [self.port['vss'].netconn,self.netlist['n1211'],self.netlist['n862']], isweak=False, parent=self),
            NMOS("t1947", [self.netlist['dpc33_PCHDB'],self.port['vss'].netconn,self.netlist['n849']], isweak=False, parent=self),
            NMOS("t1946", [self.port['vss'].netconn,self.netlist['n1079'],self.netlist['n1411']], isweak=False, parent=self),
            NMOS("t1945", [self.port['vss'].netconn,self.netlist['noty3'],self.netlist['y3']], isweak=False, parent=self),
            NMOS("t1944", [self.netlist['n1219'],self.port['vss'].netconn,self.netlist['n776']], isweak=False, parent=self),
            NMOS("t602", [self.netlist['n1543'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1942", [self.netlist['n519'],self.port['vss'].netconn,self.port['clk0'].netconn], isweak=False, parent=self),
            NMOS("t1941", [self.netlist['n428'],self.netlist['n644'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t601", [self.netlist['n1173'],self.port['vss'].netconn,self.netlist['clock1']], isweak=False, parent=self),
            NMOS("t1914", [self.netlist['n773'],self.port['vss'].netconn,self.netlist['n273']], isweak=False, parent=self),
            NMOS("t2305", [self.port['vss'].netconn,self.netlist['n0'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2306", [self.netlist['n594'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2307", [self.netlist['n1052'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2300", [self.port['vss'].netconn,self.netlist['n822'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2301", [self.port['vss'].netconn,self.netlist['n131'],self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2302", [self.netlist['n1086'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2303", [self.netlist['n1074'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2308", [self.netlist['n1589'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t2309", [self.netlist['n446'],self.port['vss'].netconn,self.netlist['notir6']], isweak=False, parent=self),
            NMOS("t3163", [self.netlist['n1140'],self.port['vss'].netconn,self.netlist['n617']], isweak=False, parent=self),
            NMOS("t3162", [self.netlist['AxB7'],self.port['vss'].netconn,self.netlist['n1398']], isweak=False, parent=self),
            NMOS("t3161", [self.port['vss'].netconn,self.netlist['n117'],self.netlist['n1398']], isweak=False, parent=self),
            NMOS("t3160", [self.netlist['n300'],self.port['vss'].netconn,self.netlist['n342']], isweak=False, parent=self),
            NMOS("t3167", [self.port['vss'].netconn,self.netlist['n1379'],self.netlist['n1476']], isweak=False, parent=self),
            NMOS("t3166", [self.netlist['n90'],self.port['vss'].netconn,self.netlist['n1625']], isweak=False, parent=self),
            NMOS("t3165", [self.port['vss'].netconn,self.netlist['n1515'],self.netlist['n125']], isweak=False, parent=self),
            NMOS("t3164", [self.port['vss'].netconn,self.netlist['n1295'],self.netlist['n1527']], isweak=False, parent=self),
            NMOS("t3306", [self.port['vss'].netconn,self.netlist['n1164'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t3169", [self.netlist['n595'],self.port['vss'].netconn,self.netlist['n1168']], isweak=False, parent=self),
            NMOS("t3168", [self.port['vss'].netconn,self.netlist['n275'],self.netlist['n1697']], isweak=False, parent=self),
            NMOS("t3500", [self.port['vss'].netconn,self.netlist['n1152'],self.netlist['n951']], isweak=False, parent=self),
            NMOS("t518", [self.port['vss'].netconn,self.netlist['notir6'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t519", [self.netlist['n1222'],self.port['vss'].netconn,self.netlist['n1225']], isweak=False, parent=self),
            NMOS("t2164", [self.port['vss'].netconn,self.netlist['n1211'],self.netlist['nnT2BR']], isweak=False, parent=self),
            NMOS("t2166", [self.port['vss'].netconn,self.netlist['n1211'],self.netlist['n1286']], isweak=False, parent=self),
            NMOS("t2167", [self.netlist['n1612'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t2168", [self.netlist['n804'],self.port['vss'].netconn,self.netlist['t4']], isweak=False, parent=self),
            NMOS("t513", [self.netlist['n754'],self.netlist['n1422'],self.netlist['pipeUNK06']], isweak=False, parent=self),
            NMOS("t510", [self.netlist['n383'],self.port['vss'].netconn,self.netlist['n712']], isweak=False, parent=self),
            NMOS("t511", [self.port['vss'].netconn,self.netlist['n1560'],self.netlist['n1337']], isweak=False, parent=self),
            NMOS("t516", [self.port['vss'].netconn,self.netlist['n225'],self.netlist['n1223']], isweak=False, parent=self),
            NMOS("t517", [self.netlist['dpc9_DBADD'],self.port['vcc'].netconn,self.netlist['n1223']], isweak=False, parent=self),
            NMOS("t514", [self.netlist['n755'],self.port['vss'].netconn,self.netlist['pipeUNK06']], isweak=False, parent=self),
            NMOS("t515", [self.netlist['nots5'],self.netlist['n496'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2942", [self.port['vcc'].netconn,self.netlist['n676'],self.netlist['n617']], isweak=False, parent=self),
            NMOS("t2943", [self.netlist['notdor1'],self.netlist['n1474'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2764", [self.port['vcc'].netconn,self.netlist['dpc31_PCHPCH'],self.netlist['n611']], isweak=False, parent=self),
            NMOS("t2765", [self.port['vss'].netconn,self.netlist['n917'],self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t2762", [self.netlist['idl3'],self.netlist['n1661'],self.netlist['cp1']], isweak=False, parent=self),
            NMOS("t2763", [self.port['vss'].netconn,self.netlist['n255'],self.netlist['n611']], isweak=False, parent=self),
            NMOS("t2760", [self.port['vss'].netconn,self.netlist['n227'],self.netlist['n540']], isweak=False, parent=self),
            NMOS("t2761", [self.port['vss'].netconn,self.netlist['dpc2_XSB'],self.netlist['n602']], isweak=False, parent=self),
            NMOS("t2948", [self.netlist['n382'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t2949", [self.netlist['n1173'],self.port['vss'].netconn,self.netlist['irline3']], isweak=False, parent=self),
            NMOS("t1894", [self.port['rw'].netconn,self.port['vcc'].netconn,self.netlist['n102']], isweak=False, parent=self),
            NMOS("t2768", [self.port['vcc'].netconn,self.netlist['n171'],self.netlist['n1026']], isweak=False, parent=self),
            NMOS("t2769", [self.netlist['n1082'],self.netlist['n455'],self.netlist['pipeUNK16']], isweak=False, parent=self),
            NMOS("t1419", [self.port['vss'].netconn,self.netlist['n60'],self.netlist['notir0']], isweak=False, parent=self),
            NMOS("t1418", [self.netlist['n224'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1415", [self.netlist['n300'],self.port['vss'].netconn,self.netlist['n857']], isweak=False, parent=self),
            NMOS("t1414", [self.netlist['n1614'],self.port['vss'].netconn,self.netlist['n1177']], isweak=False, parent=self),
            NMOS("t1386", [self.port['vss'].netconn,self.netlist['n637'],self.netlist['n1318']], isweak=False, parent=self),
            NMOS("t1416", [self.netlist['n520'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1411", [self.port['vss'].netconn,self.netlist['n384'],self.netlist['n1228']], isweak=False, parent=self),
            NMOS("t1410", [self.netlist['dpc33_PCHDB'],self.port['vcc'].netconn,self.netlist['n321']], isweak=False, parent=self),
            NMOS("t1413", [self.port['vss'].netconn,self.netlist['n385'],self.netlist['n1377']], isweak=False, parent=self),
            NMOS("t2047", [self.netlist['n20'],self.netlist['n993'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1097", [self.port['vss'].netconn,self.netlist['n36'],self.netlist['n8']], isweak=False, parent=self),
            NMOS("t1099", [self.netlist['DC78'],self.netlist['n1030'],self.netlist['n570']], isweak=False, parent=self),
            NMOS("t1098", [self.port['vss'].netconn,self.netlist['n150'],self.netlist['n8']], isweak=False, parent=self),
            NMOS("t996", [self.netlist['n1053'],self.netlist['n673'],self.netlist['n575']], isweak=False, parent=self),
            NMOS("t1300", [self.port['vss'].netconn,self.netlist['n660'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t1303", [self.port['vss'].netconn,self.netlist['n904'],self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t995", [self.netlist['n1382'],self.port['vss'].netconn,self.netlist['notRdy0']], isweak=False, parent=self),
            NMOS("t992", [self.port['vss'].netconn,self.netlist['n869'],self.netlist['abh5']], isweak=False, parent=self),
            NMOS("t1304", [self.netlist['n1419'],self.port['vss'].netconn,self.netlist['notir4']], isweak=False, parent=self),
            NMOS("t990", [self.netlist['n1608'],self.port['vcc'].netconn,self.netlist['abh5']], isweak=False, parent=self),
            NMOS("t991", [self.port['vss'].netconn,self.netlist['n1423'],self.netlist['abh5']], isweak=False, parent=self),
            NMOS("t1309", [self.netlist['pipeUNK42'],self.netlist['n889'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1308", [self.netlist['alub2'],self.netlist['adl2'],self.netlist['dpc10_ADLADD']], isweak=False, parent=self),
            NMOS("t998", [self.port['vss'].netconn,self.netlist['n931'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t999", [self.port['vss'].netconn,self.netlist['n1375'],self.netlist['n88']], isweak=False, parent=self),
            NMOS("t648", [self.port['vss'].netconn,self.netlist['n682'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t1529", [self.netlist['sb5'],self.netlist['x5'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t1528", [self.netlist['x6'],self.netlist['sb6'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t2633", [self.port['vss'].netconn,self.netlist['dpc3_SBX'],self.netlist['n1247']], isweak=False, parent=self),
            NMOS("t1521", [self.netlist['n999'],self.port['vcc'].netconn,self.netlist['n1677']], isweak=False, parent=self),
            NMOS("t1520", [self.netlist['n475'],self.port['vss'].netconn,self.netlist['n1677']], isweak=False, parent=self),
            NMOS("t1523", [self.netlist['x4'],self.netlist['dasb4'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t1522", [self.netlist['n958'],self.netlist['n865'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1525", [self.netlist['sb2'],self.netlist['x2'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t1524", [self.netlist['sb3'],self.netlist['x3'],self.netlist['dpc3_SBX']], isweak=False, parent=self),
            NMOS("t1527", [self.port['vcc'].netconn,self.netlist['n821'],self.netlist['n582']], isweak=False, parent=self),
            NMOS("t1526", [self.netlist['n1067'],self.port['vss'].netconn,self.netlist['n582']], isweak=False, parent=self),
            NMOS("t749", [self.port['vss'].netconn,self.netlist['n1381'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1903", [self.port['vss'].netconn,self.netlist['n302'],self.netlist['n1083']], isweak=False, parent=self),
            NMOS("t643", [self.netlist['n1562'],self.port['vss'].netconn,self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t1901", [self.netlist['n592'],self.port['vss'].netconn,self.netlist['C67']], isweak=False, parent=self),
            NMOS("t3099", [self.netlist['n1476'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t1907", [self.port['vss'].netconn,self.netlist['n1277'],self.netlist['n1020']], isweak=False, parent=self),
            NMOS("t106", [self.port['vss'].netconn,self.netlist['n972'],self.netlist['n1691']], isweak=False, parent=self),
            NMOS("t1906", [self.port['vss'].netconn,self.netlist['n548'],self.netlist['s7']], isweak=False, parent=self),
            NMOS("t1635", [self.port['vss'].netconn,self.netlist['n1470'],self.netlist['n1111']], isweak=False, parent=self),
            NMOS("t1634", [self.netlist['n628'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1637", [self.port['vss'].netconn,self.netlist['n313'],self.netlist['alua3']], isweak=False, parent=self),
            NMOS("t1636", [self.netlist['n1614'],self.port['vss'].netconn,self.netlist['n1111']], isweak=False, parent=self),
            NMOS("t1630", [self.netlist['n798'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1633", [self.netlist['n525'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t1632", [self.netlist['n288'],self.port['vss'].netconn,self.netlist['RnWstretched']], isweak=False, parent=self),
            NMOS("t1904", [self.port['vss'].netconn,self.netlist['n1019'],self.netlist['n1083']], isweak=False, parent=self),
            NMOS("t1639", [self.port['vss'].netconn,self.netlist['dpc12_0ADD'],self.netlist['n956']], isweak=False, parent=self),
            NMOS("t1638", [self.port['vss'].netconn,self.netlist['n649'],self.netlist['alua3']], isweak=False, parent=self),
            NMOS("t3094", [self.netlist['n259'],self.port['vss'].netconn,self.netlist['notir5']], isweak=False, parent=self),
            NMOS("t2329", [self.netlist['n919'],self.netlist['n856'],self.netlist['dpc34_PCLC']], isweak=False, parent=self),
            NMOS("t2222", [self.port['ab6'].netconn,self.port['vcc'].netconn,self.netlist['n1191']], isweak=False, parent=self),
            NMOS("t2733", [self.netlist['n994'],self.netlist['n768'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t2732", [self.port['vss'].netconn,self.netlist['n1586'],self.netlist['n682']], isweak=False, parent=self),
            NMOS("t2227", [self.netlist['n1201'],self.port['vcc'].netconn,self.netlist['n1499']], isweak=False, parent=self),
            NMOS("t2226", [self.netlist['n709'],self.port['vss'].netconn,self.netlist['n1499']], isweak=False, parent=self),
            NMOS("t198", [self.netlist['n773'],self.port['vss'].netconn,self.netlist['n646']], isweak=False, parent=self),
            NMOS("t199", [self.netlist['n1141'],self.port['vss'].netconn,self.netlist['n982']], isweak=False, parent=self),
            NMOS("t65", [self.port['vss'].netconn,self.port['db2'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t64", [self.netlist['alu6'],self.port['vss'].netconn,self.netlist['notalu6']], isweak=False, parent=self),
            NMOS("t67", [self.port['vss'].netconn,self.netlist['idl2'],self.netlist['notidl2']], isweak=False, parent=self),
            NMOS("t66", [self.netlist['n1495'],self.netlist['n1644'],self.netlist['n1457']], isweak=False, parent=self),
            NMOS("t192", [self.port['vss'].netconn,self.netlist['n453'],self.netlist['pch7']], isweak=False, parent=self),
            NMOS("t60", [self.netlist['n923'],self.port['vss'].netconn,self.netlist['pch3']], isweak=False, parent=self),
            NMOS("t63", [self.netlist['n1527'],self.netlist['n1347'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t191", [self.netlist['notir5'],self.netlist['n1609'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3228", [self.netlist['n1252'],self.netlist['NMIL'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3229", [self.port['vss'].netconn,self.netlist['n1483'],self.netlist['alua6']], isweak=False, parent=self),
            NMOS("t358", [self.netlist['n1224'],self.port['vss'].netconn,self.netlist['idb0']], isweak=False, parent=self),
            NMOS("t359", [self.netlist['n1397'],self.netlist['n1303'],self.netlist['n335']], isweak=False, parent=self),
            NMOS("t354", [self.netlist['dpc30_ADHPCH'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t355", [self.netlist['dpc31_PCHPCH'],self.port['vss'].netconn,self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3222", [self.port['vss'].netconn,self.netlist['n152'],self.netlist['n952']], isweak=False, parent=self),
            NMOS("t357", [self.netlist['n300'],self.port['vss'].netconn,self.netlist['n712']], isweak=False, parent=self),
            NMOS("t3224", [self.netlist['n1351'],self.netlist['n1717'],self.netlist['n258']], isweak=False, parent=self),
            NMOS("t3225", [self.netlist['sb1'],self.netlist['n1709'],self.netlist['dpc2_XSB']], isweak=False, parent=self),
            NMOS("t3226", [self.port['vss'].netconn,self.netlist['n1228'],self.netlist['n669']], isweak=False, parent=self),
            NMOS("t3227", [self.port['vss'].netconn,self.port['db4'].netconn,self.port['vss'].netconn], isweak=False, parent=self),
            NMOS("t1919", [self.port['vss'].netconn,self.netlist['n135'],self.netlist['n127']], isweak=False, parent=self),
            NMOS("t3314", [self.netlist['n1711'],self.port['vss'].netconn,self.netlist['s1']], isweak=False, parent=self),
            NMOS("t3315", [self.netlist['n1455'],self.port['vss'].netconn,self.netlist['n257']], isweak=False, parent=self),
            NMOS("t3316", [self.netlist['n564'],self.netlist['y0'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3317", [self.netlist['n429'],self.netlist['n659'],self.netlist['cclk']], isweak=False, parent=self),
            NMOS("t3310", [self.port['vss'].netconn,self.netlist['n726'],self.netlist['n1210']], isweak=False, parent=self),
            NMOS("t3311", [self.netlist['n256'],self.port['vss'].netconn,self.netlist['n1210']], isweak=False, parent=self),
            NMOS("t3312", [self.netlist['n1076'],self.port['vss'].netconn,self.netlist['n1463']], isweak=False, parent=self),
            NMOS("t3313", [self.netlist['n147'],self.port['vcc'].netconn,self.netlist['n1463']], isweak=False, parent=self),
            NMOS("t1342", [self.netlist['n1399'],self.port['vss'].netconn,self.netlist['n1715']], isweak=False, parent=self),
            NMOS("t3318", [self.port['vss'].netconn,self.netlist['n1209'],self.netlist['n1213']], isweak=False, parent=self),
            NMOS("t3319", [self.netlist['dpc30_ADHPCH'],self.port['vss'].netconn,self.netlist['n228']], isweak=False, parent=self),
        ])
