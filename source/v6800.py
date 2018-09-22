
import gate
import net
from primitive import NMOS

class v6800( gate.module ):
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict([
            ('reset', gate.IN),
            ('rw', gate.OUT),
            ('db0', gate.INOUT),
            ('db1', gate.INOUT),
            ('db3', gate.INOUT),
            ('db2', gate.INOUT),
            ('db5', gate.INOUT),
            ('db4', gate.INOUT),
            ('db7', gate.INOUT),
            ('db6', gate.INOUT),
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
            ('ab10', gate.OUT),
            ('ab11', gate.OUT),
            ('ab12', gate.OUT),
            ('ab13', gate.OUT),
            ('ab14', gate.OUT),
            ('ab15', gate.OUT),
            ('phi1', gate.IN),
            ('phi2', gate.IN),
            ('irq', gate.IN),
            ('nmi', gate.IN),
            ('halt', gate.IN),
            ('tsc', gate.IN),
            ('ba', gate.OUT),
            ('vma', gate.OUT),
            ('dbe', gate.IN),
            ('gnd', gate.IN),
            ('vcc', gate.IN),

        ])
        gate.module.__init__( self, name, portlist, mapping, parent)

        ## Net Declarations
        self.netlist['Ta0'] = net.net('Ta0', pullup_str=100,   parent=self)
        self.netlist['Ta1'] = net.net('Ta1', pullup_str=100,   parent=self)
        self.netlist['Ta2'] = net.net('Ta2',  charge_storage=True,  parent=self)
        self.netlist['Td0_0'] = net.net('Td0_0', pullup_str=100,   parent=self)
        self.netlist['Te1_0'] = net.net('Te1_0',  charge_storage=True,  parent=self)
        self.netlist['Tg0'] = net.net('Tg0', pullup_str=100,   parent=self)
        self.netlist['Tg1'] = net.net('Tg1', pullup_str=100,   parent=self)
        self.netlist['Tg2'] = net.net('Tg2', pullup_str=100,   parent=self)
        self.netlist['Tg3'] = net.net('Tg3', pullup_str=100,   parent=self)
        self.netlist['Tg4'] = net.net('Tg4', pullup_str=100,   parent=self)
        self.netlist['Tg5'] = net.net('Tg5', pullup_str=100,   parent=self)
        self.netlist['Tg6'] = net.net('Tg6', pullup_str=100,   parent=self)
        self.netlist['Tg7'] = net.net('Tg7', pullup_str=100,   parent=self)
        self.netlist['Tg8'] = net.net('Tg8', pullup_str=100,   parent=self)
        self.netlist['Tr3'] = net.net('Tr3', pullup_str=100,   parent=self)
        self.netlist['Tr4'] = net.net('Tr4', pullup_str=100,   parent=self)
        self.netlist['Tr5'] = net.net('Tr5', pullup_str=100,   parent=self)
        self.netlist['Tr6'] = net.net('Tr6', pullup_str=100,   parent=self)
        self.netlist['Tr7'] = net.net('Tr7', pullup_str=100,   parent=self)
        self.netlist['Tr8'] = net.net('Tr8', pullup_str=100,   parent=self)
        self.netlist['Ts'] = net.net('Ts', pullup_str=100,   parent=self)
        self.netlist['Tx0'] = net.net('Tx0', pullup_str=100,   parent=self)
        self.netlist['Tx1'] = net.net('Tx1', pullup_str=100,   parent=self)
        self.netlist['Tx2'] = net.net('Tx2', pullup_str=100,   parent=self)
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
        self.netlist['abl0'] = net.net('abl0',  charge_storage=True,  parent=self)
        self.netlist['abl1'] = net.net('abl1',  charge_storage=True,  parent=self)
        self.netlist['abl2'] = net.net('abl2',  charge_storage=True,  parent=self)
        self.netlist['abl3'] = net.net('abl3',  charge_storage=True,  parent=self)
        self.netlist['abl4'] = net.net('abl4',  charge_storage=True,  parent=self)
        self.netlist['abl5'] = net.net('abl5',  charge_storage=True,  parent=self)
        self.netlist['abl6'] = net.net('abl6',  charge_storage=True,  parent=self)
        self.netlist['abl7'] = net.net('abl7',  charge_storage=True,  parent=self)
        self.netlist['ablx0'] = net.net('ablx0', pullup_str=100,   parent=self)
        self.netlist['ablx1'] = net.net('ablx1', pullup_str=100,   parent=self)
        self.netlist['ablx2'] = net.net('ablx2', pullup_str=100,   parent=self)
        self.netlist['ablx3'] = net.net('ablx3', pullup_str=100,   parent=self)
        self.netlist['ablx4'] = net.net('ablx4', pullup_str=100,   parent=self)
        self.netlist['ablx5'] = net.net('ablx5', pullup_str=100,   parent=self)
        self.netlist['ablx6'] = net.net('ablx6', pullup_str=100,   parent=self)
        self.netlist['ablx7'] = net.net('ablx7', pullup_str=100,   parent=self)
        self.netlist['acca0'] = net.net('acca0', pullup_str=100,   parent=self)
        self.netlist['acca0_1'] = net.net('acca0_1',  charge_storage=True,  parent=self)
        self.netlist['acca1'] = net.net('acca1', pullup_str=100,   parent=self)
        self.netlist['acca1_1'] = net.net('acca1_1',  charge_storage=True,  parent=self)
        self.netlist['acca2'] = net.net('acca2', pullup_str=100,   parent=self)
        self.netlist['acca2_1'] = net.net('acca2_1',  charge_storage=True,  parent=self)
        self.netlist['acca3'] = net.net('acca3', pullup_str=100,   parent=self)
        self.netlist['acca3_1'] = net.net('acca3_1',  charge_storage=True,  parent=self)
        self.netlist['acca4'] = net.net('acca4', pullup_str=100,   parent=self)
        self.netlist['acca4_1'] = net.net('acca4_1',  charge_storage=True,  parent=self)
        self.netlist['acca5'] = net.net('acca5', pullup_str=100,   parent=self)
        self.netlist['acca5_1'] = net.net('acca5_1',  charge_storage=True,  parent=self)
        self.netlist['acca6'] = net.net('acca6', pullup_str=100,   parent=self)
        self.netlist['acca6_1'] = net.net('acca6_1',  charge_storage=True,  parent=self)
        self.netlist['acca7'] = net.net('acca7', pullup_str=100,   parent=self)
        self.netlist['acca7_1'] = net.net('acca7_1',  charge_storage=True,  parent=self)
        self.netlist['accb0'] = net.net('accb0', pullup_str=100,   parent=self)
        self.netlist['accb0_1'] = net.net('accb0_1',  charge_storage=True,  parent=self)
        self.netlist['accb1'] = net.net('accb1', pullup_str=100,   parent=self)
        self.netlist['accb1_1'] = net.net('accb1_1',  charge_storage=True,  parent=self)
        self.netlist['accb2'] = net.net('accb2', pullup_str=100,   parent=self)
        self.netlist['accb2_1'] = net.net('accb2_1',  charge_storage=True,  parent=self)
        self.netlist['accb3'] = net.net('accb3', pullup_str=100,   parent=self)
        self.netlist['accb3_1'] = net.net('accb3_1',  charge_storage=True,  parent=self)
        self.netlist['accb4'] = net.net('accb4', pullup_str=100,   parent=self)
        self.netlist['accb4_1'] = net.net('accb4_1',  charge_storage=True,  parent=self)
        self.netlist['accb5'] = net.net('accb5', pullup_str=100,   parent=self)
        self.netlist['accb5_1'] = net.net('accb5_1',  charge_storage=True,  parent=self)
        self.netlist['accb6'] = net.net('accb6', pullup_str=100,   parent=self)
        self.netlist['accb6_1'] = net.net('accb6_1',  charge_storage=True,  parent=self)
        self.netlist['accb7'] = net.net('accb7', pullup_str=100,   parent=self)
        self.netlist['accb7_1'] = net.net('accb7_1',  charge_storage=True,  parent=self)
        self.netlist['adda0'] = net.net('adda0',  charge_storage=True,  parent=self)
        self.netlist['adda0in'] = net.net('adda0in',  charge_storage=True,  parent=self)
        self.netlist['adda1'] = net.net('adda1',  charge_storage=True,  parent=self)
        self.netlist['adda1in'] = net.net('adda1in',  charge_storage=True,  parent=self)
        self.netlist['adda2'] = net.net('adda2',  charge_storage=True,  parent=self)
        self.netlist['adda2in'] = net.net('adda2in',  charge_storage=True,  parent=self)
        self.netlist['adda3'] = net.net('adda3',  charge_storage=True,  parent=self)
        self.netlist['adda3in'] = net.net('adda3in',  charge_storage=True,  parent=self)
        self.netlist['adda4'] = net.net('adda4',  charge_storage=True,  parent=self)
        self.netlist['adda4in'] = net.net('adda4in',  charge_storage=True,  parent=self)
        self.netlist['adda5'] = net.net('adda5',  charge_storage=True,  parent=self)
        self.netlist['adda5in'] = net.net('adda5in',  charge_storage=True,  parent=self)
        self.netlist['adda6'] = net.net('adda6',  charge_storage=True,  parent=self)
        self.netlist['adda6in'] = net.net('adda6in',  charge_storage=True,  parent=self)
        self.netlist['adda7'] = net.net('adda7',  charge_storage=True,  parent=self)
        self.netlist['adda7in'] = net.net('adda7in',  charge_storage=True,  parent=self)
        self.netlist['addb0'] = net.net('addb0', pullup_str=100,   parent=self)
        self.netlist['addb1'] = net.net('addb1', pullup_str=100,   parent=self)
        self.netlist['addb2'] = net.net('addb2', pullup_str=100,   parent=self)
        self.netlist['addb3'] = net.net('addb3', pullup_str=100,   parent=self)
        self.netlist['addb4'] = net.net('addb4', pullup_str=100,   parent=self)
        self.netlist['addb5'] = net.net('addb5', pullup_str=100,   parent=self)
        self.netlist['addb6'] = net.net('addb6', pullup_str=100,   parent=self)
        self.netlist['addb7'] = net.net('addb7', pullup_str=100,   parent=self)
        self.netlist['ahd0_0'] = net.net('ahd0_0', pullup_str=100,   parent=self)
        self.netlist['ahd1_0'] = net.net('ahd1_0', pullup_str=100,   parent=self)
        self.netlist['ahd2_0'] = net.net('ahd2_0', pullup_str=100,   parent=self)
        self.netlist['ahd3_0'] = net.net('ahd3_0', pullup_str=100,   parent=self)
        self.netlist['ahd4_0'] = net.net('ahd4_0', pullup_str=100,   parent=self)
        self.netlist['ahd5_0'] = net.net('ahd5_0', pullup_str=100,   parent=self)
        self.netlist['ahd6_0'] = net.net('ahd6_0', pullup_str=100,   parent=self)
        self.netlist['ahd7_0'] = net.net('ahd7_0', pullup_str=100,   parent=self)
        self.netlist['ald0_0'] = net.net('ald0_0', pullup_str=100,   parent=self)
        self.netlist['ald1_0'] = net.net('ald1_0', pullup_str=100,   parent=self)
        self.netlist['ald2_0'] = net.net('ald2_0', pullup_str=100,   parent=self)
        self.netlist['ald3_0'] = net.net('ald3_0', pullup_str=100,   parent=self)
        self.netlist['ald4_0'] = net.net('ald4_0', pullup_str=100,   parent=self)
        self.netlist['ald5_0'] = net.net('ald5_0', pullup_str=100,   parent=self)
        self.netlist['ald6_0'] = net.net('ald6_0', pullup_str=100,   parent=self)
        self.netlist['ald7_0'] = net.net('ald7_0', pullup_str=100,   parent=self)
        self.port['ba'].netconn.charge_storage=True
        self.netlist['ba_0'] = net.net('ba_0', pullup_str=100,   parent=self)
        self.port['db0'].netconn.charge_storage=True
        self.port['db1'].netconn.charge_storage=True
        self.port['db2'].netconn.charge_storage=True
        self.port['db3'].netconn.charge_storage=True
        self.port['db4'].netconn.charge_storage=True
        self.port['db5'].netconn.charge_storage=True
        self.port['db6'].netconn.charge_storage=True
        self.port['db7'].netconn.charge_storage=True
        self.port['dbe'].netconn.charge_storage=True
        self.netlist['dbi0'] = net.net('dbi0', pullup_str=100,   parent=self)
        self.netlist['dbi1'] = net.net('dbi1', pullup_str=100,   parent=self)
        self.netlist['dbi2'] = net.net('dbi2', pullup_str=100,   parent=self)
        self.netlist['dbi3'] = net.net('dbi3', pullup_str=100,   parent=self)
        self.netlist['dbi4'] = net.net('dbi4', pullup_str=100,   parent=self)
        self.netlist['dbi5'] = net.net('dbi5', pullup_str=100,   parent=self)
        self.netlist['dbi6'] = net.net('dbi6', pullup_str=100,   parent=self)
        self.netlist['dbi7'] = net.net('dbi7', pullup_str=100,   parent=self)
        self.netlist['dbo0'] = net.net('dbo0',  charge_storage=True,  parent=self)
        self.netlist['dbo1'] = net.net('dbo1',  charge_storage=True,  parent=self)
        self.netlist['dbo2'] = net.net('dbo2',  charge_storage=True,  parent=self)
        self.netlist['dbo3'] = net.net('dbo3',  charge_storage=True,  parent=self)
        self.netlist['dbo4'] = net.net('dbo4',  charge_storage=True,  parent=self)
        self.netlist['dbo5'] = net.net('dbo5',  charge_storage=True,  parent=self)
        self.netlist['dbo6'] = net.net('dbo6',  charge_storage=True,  parent=self)
        self.netlist['dbo7'] = net.net('dbo7',  charge_storage=True,  parent=self)
        self.netlist['decode'] = net.net('decode', pullup_str=100,   parent=self)
        self.netlist['decode_1'] = net.net('decode_1', pullup_str=100,   parent=self)
        self.netlist['enrwa'] = net.net('enrwa', pullup_str=100,   parent=self)
        self.netlist['flagc'] = net.net('flagc', pullup_str=100,   parent=self)
        self.netlist['flagh'] = net.net('flagh', pullup_str=100,   parent=self)
        self.netlist['flagi'] = net.net('flagi', pullup_str=100,   parent=self)
        self.netlist['flagn'] = net.net('flagn', pullup_str=100,   parent=self)
        self.netlist['flagv'] = net.net('flagv', pullup_str=100,   parent=self)
        self.netlist['flagz'] = net.net('flagz', pullup_str=100,   parent=self)
        self.netlist['gnd'] = net.supply0('gnd')
        self.port['halt'].netconn.charge_storage=True
        self.netlist['halt_0'] = net.net('halt_0', pullup_str=100,   parent=self)
        self.netlist['i0'] = net.net('i0', pullup_str=100,   parent=self)
        self.netlist['i1'] = net.net('i1', pullup_str=100,   parent=self)
        self.netlist['i2'] = net.net('i2', pullup_str=100,   parent=self)
        self.netlist['i3'] = net.net('i3', pullup_str=100,   parent=self)
        self.netlist['i4'] = net.net('i4', pullup_str=100,   parent=self)
        self.netlist['i5'] = net.net('i5', pullup_str=100,   parent=self)
        self.netlist['i6'] = net.net('i6', pullup_str=100,   parent=self)
        self.netlist['i7'] = net.net('i7', pullup_str=100,   parent=self)
        self.netlist['idb0'] = net.net('idb0', pullup_str=100,   parent=self)
        self.netlist['idb0_2'] = net.net('idb0_2', pullup_str=100,   parent=self)
        self.netlist['idb1'] = net.net('idb1', pullup_str=100,   parent=self)
        self.netlist['idb1_2'] = net.net('idb1_2', pullup_str=100,   parent=self)
        self.netlist['idb2'] = net.net('idb2', pullup_str=100,   parent=self)
        self.netlist['idb2_2'] = net.net('idb2_2', pullup_str=100,   parent=self)
        self.netlist['idb3'] = net.net('idb3', pullup_str=100,   parent=self)
        self.netlist['idb3_2'] = net.net('idb3_2', pullup_str=100,   parent=self)
        self.netlist['idb4'] = net.net('idb4', pullup_str=100,   parent=self)
        self.netlist['idb4_2'] = net.net('idb4_2', pullup_str=100,   parent=self)
        self.netlist['idb5'] = net.net('idb5', pullup_str=100,   parent=self)
        self.netlist['idb5_2'] = net.net('idb5_2', pullup_str=100,   parent=self)
        self.netlist['idb6'] = net.net('idb6', pullup_str=100,   parent=self)
        self.netlist['idb6_2'] = net.net('idb6_2', pullup_str=100,   parent=self)
        self.netlist['idb7'] = net.net('idb7', pullup_str=100,   parent=self)
        self.netlist['idb7_2'] = net.net('idb7_2', pullup_str=100,   parent=self)
        self.netlist['inch0'] = net.net('inch0', pullup_str=100,   parent=self)
        self.netlist['inch1'] = net.net('inch1', pullup_str=100,   parent=self)
        self.netlist['inch2'] = net.net('inch2', pullup_str=100,   parent=self)
        self.netlist['inch3'] = net.net('inch3', pullup_str=100,   parent=self)
        self.netlist['inch4'] = net.net('inch4', pullup_str=100,   parent=self)
        self.netlist['inch5'] = net.net('inch5', pullup_str=100,   parent=self)
        self.netlist['inch6'] = net.net('inch6', pullup_str=100,   parent=self)
        self.netlist['inch7'] = net.net('inch7', pullup_str=100,   parent=self)
        self.netlist['inchi0_0'] = net.net('inchi0_0', pullup_str=100,   parent=self)
        self.netlist['inchi1_0'] = net.net('inchi1_0', pullup_str=100,   parent=self)
        self.netlist['inchi2_0'] = net.net('inchi2_0', pullup_str=100,   parent=self)
        self.netlist['inchi4_0'] = net.net('inchi4_0', pullup_str=100,   parent=self)
        self.netlist['inchi5_0'] = net.net('inchi5_0', pullup_str=100,   parent=self)
        self.netlist['inchi6_0'] = net.net('inchi6_0', pullup_str=100,   parent=self)
        self.netlist['incl0'] = net.net('incl0', pullup_str=100,   parent=self)
        self.netlist['incl1'] = net.net('incl1', pullup_str=100,   parent=self)
        self.netlist['incl2'] = net.net('incl2', pullup_str=100,   parent=self)
        self.netlist['incl3'] = net.net('incl3', pullup_str=100,   parent=self)
        self.netlist['incl4'] = net.net('incl4', pullup_str=100,   parent=self)
        self.netlist['incl5'] = net.net('incl5', pullup_str=100,   parent=self)
        self.netlist['incl6'] = net.net('incl6', pullup_str=100,   parent=self)
        self.netlist['incl7'] = net.net('incl7', pullup_str=100,   parent=self)
        self.netlist['incli0_0'] = net.net('incli0_0', pullup_str=100,   parent=self)
        self.netlist['incli1_0'] = net.net('incli1_0', pullup_str=100,   parent=self)
        self.netlist['incli2_0'] = net.net('incli2_0', pullup_str=100,   parent=self)
        self.netlist['incli4_0'] = net.net('incli4_0', pullup_str=100,   parent=self)
        self.netlist['incli5_0'] = net.net('incli5_0', pullup_str=100,   parent=self)
        self.netlist['incli6_0'] = net.net('incli6_0', pullup_str=100,   parent=self)
        self.netlist['ir0'] = net.net('ir0',  charge_storage=True,  parent=self)
        self.netlist['ir0_1'] = net.net('ir0_1', pullup_str=100,   parent=self)
        self.netlist['ir1'] = net.net('ir1',  charge_storage=True,  parent=self)
        self.netlist['ir1_1'] = net.net('ir1_1', pullup_str=100,   parent=self)
        self.netlist['ir2'] = net.net('ir2',  charge_storage=True,  parent=self)
        self.netlist['ir2_1'] = net.net('ir2_1', pullup_str=100,   parent=self)
        self.netlist['ir3'] = net.net('ir3',  charge_storage=True,  parent=self)
        self.netlist['ir3_1'] = net.net('ir3_1', pullup_str=100,   parent=self)
        self.netlist['ir4'] = net.net('ir4',  charge_storage=True,  parent=self)
        self.netlist['ir4_1'] = net.net('ir4_1', pullup_str=100,   parent=self)
        self.netlist['ir5'] = net.net('ir5',  charge_storage=True,  parent=self)
        self.netlist['ir5_1'] = net.net('ir5_1', pullup_str=100,   parent=self)
        self.netlist['ir6'] = net.net('ir6',  charge_storage=True,  parent=self)
        self.netlist['ir6_1'] = net.net('ir6_1', pullup_str=100,   parent=self)
        self.netlist['ir7'] = net.net('ir7',  charge_storage=True,  parent=self)
        self.netlist['ir7_1'] = net.net('ir7_1', pullup_str=100,   parent=self)
        self.port['irq'].netconn.charge_storage=True
        self.netlist['ixh0'] = net.net('ixh0', pullup_str=100,   parent=self)
        self.netlist['ixh0_1'] = net.net('ixh0_1',  charge_storage=True,  parent=self)
        self.netlist['ixh1'] = net.net('ixh1', pullup_str=100,   parent=self)
        self.netlist['ixh1_1'] = net.net('ixh1_1',  charge_storage=True,  parent=self)
        self.netlist['ixh2'] = net.net('ixh2', pullup_str=100,   parent=self)
        self.netlist['ixh2_1'] = net.net('ixh2_1',  charge_storage=True,  parent=self)
        self.netlist['ixh3'] = net.net('ixh3', pullup_str=100,   parent=self)
        self.netlist['ixh3_1'] = net.net('ixh3_1',  charge_storage=True,  parent=self)
        self.netlist['ixh4'] = net.net('ixh4', pullup_str=100,   parent=self)
        self.netlist['ixh4_1'] = net.net('ixh4_1',  charge_storage=True,  parent=self)
        self.netlist['ixh5'] = net.net('ixh5', pullup_str=100,   parent=self)
        self.netlist['ixh5_1'] = net.net('ixh5_1',  charge_storage=True,  parent=self)
        self.netlist['ixh6'] = net.net('ixh6', pullup_str=100,   parent=self)
        self.netlist['ixh6_1'] = net.net('ixh6_1',  charge_storage=True,  parent=self)
        self.netlist['ixh7'] = net.net('ixh7', pullup_str=100,   parent=self)
        self.netlist['ixh7_1'] = net.net('ixh7_1',  charge_storage=True,  parent=self)
        self.netlist['ixl0'] = net.net('ixl0', pullup_str=100,   parent=self)
        self.netlist['ixl0_1'] = net.net('ixl0_1',  charge_storage=True,  parent=self)
        self.netlist['ixl1'] = net.net('ixl1', pullup_str=100,   parent=self)
        self.netlist['ixl1_1'] = net.net('ixl1_1',  charge_storage=True,  parent=self)
        self.netlist['ixl2'] = net.net('ixl2', pullup_str=100,   parent=self)
        self.netlist['ixl2_1'] = net.net('ixl2_1',  charge_storage=True,  parent=self)
        self.netlist['ixl3'] = net.net('ixl3', pullup_str=100,   parent=self)
        self.netlist['ixl3_1'] = net.net('ixl3_1',  charge_storage=True,  parent=self)
        self.netlist['ixl4'] = net.net('ixl4', pullup_str=100,   parent=self)
        self.netlist['ixl4_1'] = net.net('ixl4_1',  charge_storage=True,  parent=self)
        self.netlist['ixl5'] = net.net('ixl5', pullup_str=100,   parent=self)
        self.netlist['ixl5_1'] = net.net('ixl5_1',  charge_storage=True,  parent=self)
        self.netlist['ixl6'] = net.net('ixl6', pullup_str=100,   parent=self)
        self.netlist['ixl6_1'] = net.net('ixl6_1',  charge_storage=True,  parent=self)
        self.netlist['ixl7'] = net.net('ixl7', pullup_str=100,   parent=self)
        self.netlist['ixl7_1'] = net.net('ixl7_1',  charge_storage=True,  parent=self)
        self.netlist['n1'] = net.net('n1', pullup_str=100,   parent=self)
        self.netlist['n10'] = net.net('n10', pullup_str=100,   parent=self)
        self.netlist['n100'] = net.net('n100', pullup_str=100,   parent=self)
        self.netlist['n1000'] = net.net('n1000',  charge_storage=True,  parent=self)
        self.netlist['n1001'] = net.net('n1001',  charge_storage=True,  parent=self)
        self.netlist['n1002'] = net.net('n1002',  charge_storage=True,  parent=self)
        self.netlist['n1003'] = net.net('n1003', pullup_str=100,   parent=self)
        self.netlist['n1004'] = net.net('n1004', pullup_str=100,   parent=self)
        self.netlist['n1006'] = net.net('n1006', pullup_str=100,   parent=self)
        self.netlist['n1008'] = net.net('n1008', pullup_str=100,   parent=self)
        self.netlist['n1009'] = net.net('n1009',  charge_storage=True,  parent=self)
        self.netlist['n101'] = net.net('n101', pullup_str=100,   parent=self)
        self.netlist['n1010'] = net.net('n1010', pullup_str=100,   parent=self)
        self.netlist['n1011'] = net.net('n1011',  charge_storage=True,  parent=self)
        self.netlist['n1012'] = net.net('n1012', pullup_str=100,   parent=self)
        self.netlist['n1013'] = net.net('n1013', pullup_str=100,   parent=self)
        self.netlist['n1014'] = net.net('n1014', pullup_str=100,   parent=self)
        self.netlist['n1015'] = net.net('n1015', pullup_str=100,   parent=self)
        self.netlist['n1018'] = net.net('n1018', pullup_str=100,   parent=self)
        self.netlist['n1019'] = net.net('n1019', pullup_str=100,   parent=self)
        self.netlist['n102'] = net.net('n102', pullup_str=100,   parent=self)
        self.netlist['n1020'] = net.net('n1020', pullup_str=100,   parent=self)
        self.netlist['n1022'] = net.net('n1022', pullup_str=100,   parent=self)
        self.netlist['n1024'] = net.net('n1024', pullup_str=100,   parent=self)
        self.netlist['n1025'] = net.net('n1025',  charge_storage=True,  parent=self)
        self.netlist['n1027'] = net.net('n1027',  charge_storage=True,  parent=self)
        self.netlist['n1028'] = net.net('n1028',  charge_storage=True,  parent=self)
        self.netlist['n1029'] = net.net('n1029', pullup_str=100,   parent=self)
        self.netlist['n103'] = net.net('n103', pullup_str=100,   parent=self)
        self.netlist['n1030'] = net.net('n1030', pullup_str=100,   parent=self)
        self.netlist['n1031'] = net.net('n1031',  charge_storage=True,  parent=self)
        self.netlist['n1032'] = net.net('n1032',  charge_storage=True,  parent=self)
        self.netlist['n1033'] = net.net('n1033', pullup_str=100,   parent=self)
        self.netlist['n1034'] = net.net('n1034', pullup_str=100,   parent=self)
        self.netlist['n1035'] = net.net('n1035', pullup_str=100,   parent=self)
        self.netlist['n1037'] = net.net('n1037',  charge_storage=True,  parent=self)
        self.netlist['n1038'] = net.net('n1038',  charge_storage=True,  parent=self)
        self.netlist['n1039'] = net.net('n1039', pullup_str=100,   parent=self)
        self.netlist['n104'] = net.net('n104', pullup_str=100,   parent=self)
        self.netlist['n1040'] = net.net('n1040', pullup_str=100,   parent=self)
        self.netlist['n1041'] = net.net('n1041', pullup_str=100,   parent=self)
        self.netlist['n1042'] = net.net('n1042', pullup_str=100,   parent=self)
        self.netlist['n1043'] = net.net('n1043', pullup_str=100,   parent=self)
        self.netlist['n1044'] = net.net('n1044', pullup_str=100,   parent=self)
        self.netlist['n1045'] = net.net('n1045',  charge_storage=True,  parent=self)
        self.netlist['n1046'] = net.net('n1046', pullup_str=100,   parent=self)
        self.netlist['n1047'] = net.net('n1047',  charge_storage=True,  parent=self)
        self.netlist['n1048'] = net.net('n1048', pullup_str=100,   parent=self)
        self.netlist['n1049'] = net.net('n1049', pullup_str=100,   parent=self)
        self.netlist['n105'] = net.net('n105', pullup_str=100,   parent=self)
        self.netlist['n1050'] = net.net('n1050',  charge_storage=True,  parent=self)
        self.netlist['n1051'] = net.net('n1051', pullup_str=100,   parent=self)
        self.netlist['n1052'] = net.net('n1052', pullup_str=100,   parent=self)
        self.netlist['n1053'] = net.net('n1053', pullup_str=100,   parent=self)
        self.netlist['n1054'] = net.net('n1054', pullup_str=100,   parent=self)
        self.netlist['n1056'] = net.net('n1056', pullup_str=100,   parent=self)
        self.netlist['n1057'] = net.net('n1057', pullup_str=100,   parent=self)
        self.netlist['n1058'] = net.net('n1058',  charge_storage=True,  parent=self)
        self.netlist['n1059'] = net.net('n1059', pullup_str=100,   parent=self)
        self.netlist['n106'] = net.net('n106', pullup_str=100,   parent=self)
        self.netlist['n1061'] = net.net('n1061', pullup_str=100,   parent=self)
        self.netlist['n1062'] = net.net('n1062',  charge_storage=True,  parent=self)
        self.netlist['n1063'] = net.net('n1063', pullup_str=100,   parent=self)
        self.netlist['n1065'] = net.net('n1065', pullup_str=100,   parent=self)
        self.netlist['n1067'] = net.net('n1067', pullup_str=100,   parent=self)
        self.netlist['n1068'] = net.net('n1068', pullup_str=100,   parent=self)
        self.netlist['n1069'] = net.net('n1069', pullup_str=100,   parent=self)
        self.netlist['n107'] = net.net('n107', pullup_str=100,   parent=self)
        self.netlist['n1070'] = net.net('n1070', pullup_str=100,   parent=self)
        self.netlist['n1071'] = net.net('n1071',  charge_storage=True,  parent=self)
        self.netlist['n1072'] = net.net('n1072', pullup_str=100,   parent=self)
        self.netlist['n1074'] = net.net('n1074', pullup_str=100,   parent=self)
        self.netlist['n1075'] = net.net('n1075', pullup_str=100,   parent=self)
        self.netlist['n1076'] = net.net('n1076',  charge_storage=True,  parent=self)
        self.netlist['n1077'] = net.net('n1077',  charge_storage=True,  parent=self)
        self.netlist['n1078'] = net.net('n1078',  charge_storage=True,  parent=self)
        self.netlist['n1079'] = net.net('n1079', pullup_str=100,   parent=self)
        self.netlist['n108'] = net.net('n108', pullup_str=100,   parent=self)
        self.netlist['n1080'] = net.net('n1080',  charge_storage=True,  parent=self)
        self.netlist['n1082'] = net.net('n1082',  charge_storage=True,  parent=self)
        self.netlist['n1083'] = net.net('n1083', pullup_str=100,   parent=self)
        self.netlist['n1084'] = net.net('n1084',  charge_storage=True,  parent=self)
        self.netlist['n1085'] = net.net('n1085', pullup_str=100,   parent=self)
        self.netlist['n1086'] = net.net('n1086', pullup_str=100,   parent=self)
        self.netlist['n1087'] = net.net('n1087', pullup_str=100,   parent=self)
        self.netlist['n1088'] = net.net('n1088',  charge_storage=True,  parent=self)
        self.netlist['n1089'] = net.net('n1089',  charge_storage=True,  parent=self)
        self.netlist['n109'] = net.net('n109', pullup_str=100,   parent=self)
        self.netlist['n1090'] = net.net('n1090', pullup_str=100,   parent=self)
        self.netlist['n1092'] = net.net('n1092', pullup_str=100,   parent=self)
        self.netlist['n1093'] = net.net('n1093', pullup_str=100,   parent=self)
        self.netlist['n1094'] = net.net('n1094',  charge_storage=True,  parent=self)
        self.netlist['n1095'] = net.net('n1095', pullup_str=100,   parent=self)
        self.netlist['n1096'] = net.net('n1096', pullup_str=100,   parent=self)
        self.netlist['n1097'] = net.net('n1097', pullup_str=100,   parent=self)
        self.netlist['n1099'] = net.net('n1099',  charge_storage=True,  parent=self)
        self.netlist['n11'] = net.net('n11', pullup_str=100,   parent=self)
        self.netlist['n110'] = net.net('n110', pullup_str=100,   parent=self)
        self.netlist['n1101'] = net.net('n1101',  charge_storage=True,  parent=self)
        self.netlist['n1103'] = net.net('n1103',  charge_storage=True,  parent=self)
        self.netlist['n1104'] = net.net('n1104',  charge_storage=True,  parent=self)
        self.netlist['n1105'] = net.net('n1105',  charge_storage=True,  parent=self)
        self.netlist['n1107'] = net.net('n1107', pullup_str=100,   parent=self)
        self.netlist['n1108'] = net.net('n1108', pullup_str=100,   parent=self)
        self.netlist['n1109'] = net.net('n1109', pullup_str=100,   parent=self)
        self.netlist['n111'] = net.net('n111', pullup_str=100,   parent=self)
        self.netlist['n1110'] = net.net('n1110', pullup_str=100,   parent=self)
        self.netlist['n1111'] = net.net('n1111', pullup_str=100,   parent=self)
        self.netlist['n1112'] = net.net('n1112', pullup_str=100,   parent=self)
        self.netlist['n1113'] = net.net('n1113', pullup_str=100,   parent=self)
        self.netlist['n1114'] = net.net('n1114',  charge_storage=True,  parent=self)
        self.netlist['n1115'] = net.net('n1115', pullup_str=100,   parent=self)
        self.netlist['n1116'] = net.net('n1116', pullup_str=100,   parent=self)
        self.netlist['n1117'] = net.net('n1117',  charge_storage=True,  parent=self)
        self.netlist['n1118'] = net.net('n1118',  charge_storage=True,  parent=self)
        self.netlist['n1119'] = net.net('n1119', pullup_str=100,   parent=self)
        self.netlist['n112'] = net.net('n112', pullup_str=100,   parent=self)
        self.netlist['n1120'] = net.net('n1120', pullup_str=100,   parent=self)
        self.netlist['n1121'] = net.net('n1121', pullup_str=100,   parent=self)
        self.netlist['n1122'] = net.net('n1122', pullup_str=100,   parent=self)
        self.netlist['n1123'] = net.net('n1123',  charge_storage=True,  parent=self)
        self.netlist['n1125'] = net.net('n1125', pullup_str=100,   parent=self)
        self.netlist['n1126'] = net.net('n1126', pullup_str=100,   parent=self)
        self.netlist['n1127'] = net.net('n1127',  charge_storage=True,  parent=self)
        self.netlist['n1128'] = net.net('n1128', pullup_str=100,   parent=self)
        self.netlist['n1129'] = net.net('n1129',  charge_storage=True,  parent=self)
        self.netlist['n113'] = net.net('n113',  charge_storage=True,  parent=self)
        self.netlist['n1130'] = net.net('n1130',  charge_storage=True,  parent=self)
        self.netlist['n1131'] = net.net('n1131',  charge_storage=True,  parent=self)
        self.netlist['n1134'] = net.net('n1134',  charge_storage=True,  parent=self)
        self.netlist['n1136'] = net.net('n1136',  charge_storage=True,  parent=self)
        self.netlist['n1138'] = net.net('n1138', pullup_str=100,   parent=self)
        self.netlist['n1139'] = net.net('n1139', pullup_str=100,   parent=self)
        self.netlist['n114'] = net.net('n114',  charge_storage=True,  parent=self)
        self.netlist['n1140'] = net.net('n1140', pullup_str=100,   parent=self)
        self.netlist['n1141'] = net.net('n1141',  charge_storage=True,  parent=self)
        self.netlist['n1143'] = net.net('n1143',  charge_storage=True,  parent=self)
        self.netlist['n1144'] = net.net('n1144',  charge_storage=True,  parent=self)
        self.netlist['n1147'] = net.net('n1147',  charge_storage=True,  parent=self)
        self.netlist['n1148'] = net.net('n1148', pullup_str=100,   parent=self)
        self.netlist['n1149'] = net.net('n1149', pullup_str=100,   parent=self)
        self.netlist['n115'] = net.net('n115',  charge_storage=True,  parent=self)
        self.netlist['n1150'] = net.net('n1150', pullup_str=100,   parent=self)
        self.netlist['n1151'] = net.net('n1151', pullup_str=100,   parent=self)
        self.netlist['n1152'] = net.net('n1152', pullup_str=100,   parent=self)
        self.netlist['n1153'] = net.net('n1153', pullup_str=100,   parent=self)
        self.netlist['n1154'] = net.net('n1154', pullup_str=100,   parent=self)
        self.netlist['n1155'] = net.net('n1155', pullup_str=100,   parent=self)
        self.netlist['n1156'] = net.net('n1156', pullup_str=100,   parent=self)
        self.netlist['n1157'] = net.net('n1157', pullup_str=100,   parent=self)
        self.netlist['n1158'] = net.net('n1158', pullup_str=100,   parent=self)
        self.netlist['n116'] = net.net('n116',  charge_storage=True,  parent=self)
        self.netlist['n1161'] = net.net('n1161',  charge_storage=True,  parent=self)
        self.netlist['n1162'] = net.net('n1162',  charge_storage=True,  parent=self)
        self.netlist['n1163'] = net.net('n1163',  charge_storage=True,  parent=self)
        self.netlist['n1164'] = net.net('n1164',  charge_storage=True,  parent=self)
        self.netlist['n1165'] = net.net('n1165',  charge_storage=True,  parent=self)
        self.netlist['n1168'] = net.net('n1168', pullup_str=100,   parent=self)
        self.netlist['n1169'] = net.net('n1169', pullup_str=100,   parent=self)
        self.netlist['n117'] = net.net('n117',  charge_storage=True,  parent=self)
        self.netlist['n1170'] = net.net('n1170',  charge_storage=True,  parent=self)
        self.netlist['n1171'] = net.net('n1171', pullup_str=100,   parent=self)
        self.netlist['n1172'] = net.net('n1172',  charge_storage=True,  parent=self)
        self.netlist['n1173'] = net.net('n1173', pullup_str=100,   parent=self)
        self.netlist['n1174'] = net.net('n1174',  charge_storage=True,  parent=self)
        self.netlist['n1175'] = net.net('n1175', pullup_str=100,   parent=self)
        self.netlist['n1176'] = net.net('n1176', pullup_str=100,   parent=self)
        self.netlist['n1177'] = net.net('n1177',  charge_storage=True,  parent=self)
        self.netlist['n1178'] = net.net('n1178', pullup_str=100,   parent=self)
        self.netlist['n1179'] = net.net('n1179',  charge_storage=True,  parent=self)
        self.netlist['n118'] = net.net('n118',  charge_storage=True,  parent=self)
        self.netlist['n1180'] = net.net('n1180', pullup_str=100,   parent=self)
        self.netlist['n1181'] = net.net('n1181', pullup_str=100,   parent=self)
        self.netlist['n1182'] = net.net('n1182', pullup_str=100,   parent=self)
        self.netlist['n1183'] = net.net('n1183', pullup_str=100,   parent=self)
        self.netlist['n1184'] = net.net('n1184',  charge_storage=True,  parent=self)
        self.netlist['n1185'] = net.net('n1185', pullup_str=100,   parent=self)
        self.netlist['n1186'] = net.net('n1186', pullup_str=100,   parent=self)
        self.netlist['n1187'] = net.net('n1187',  charge_storage=True,  parent=self)
        self.netlist['n1188'] = net.net('n1188', pullup_str=100,   parent=self)
        self.netlist['n1189'] = net.net('n1189', pullup_str=100,   parent=self)
        self.netlist['n119'] = net.net('n119',  charge_storage=True,  parent=self)
        self.netlist['n1190'] = net.net('n1190',  charge_storage=True,  parent=self)
        self.netlist['n1191'] = net.net('n1191',  charge_storage=True,  parent=self)
        self.netlist['n1192'] = net.net('n1192', pullup_str=100,   parent=self)
        self.netlist['n1193'] = net.net('n1193', pullup_str=100,   parent=self)
        self.netlist['n1195'] = net.net('n1195', pullup_str=100,   parent=self)
        self.netlist['n1197'] = net.net('n1197', pullup_str=100,   parent=self)
        self.netlist['n1198'] = net.net('n1198', pullup_str=100,   parent=self)
        self.netlist['n1199'] = net.net('n1199', pullup_str=100,   parent=self)
        self.netlist['n120'] = net.net('n120',  charge_storage=True,  parent=self)
        self.netlist['n1200'] = net.net('n1200', pullup_str=100,   parent=self)
        self.netlist['n1201'] = net.net('n1201',  charge_storage=True,  parent=self)
        self.netlist['n1203'] = net.net('n1203',  charge_storage=True,  parent=self)
        self.netlist['n1204'] = net.net('n1204', pullup_str=100,   parent=self)
        self.netlist['n1205'] = net.net('n1205', pullup_str=100,   parent=self)
        self.netlist['n1209'] = net.net('n1209',  charge_storage=True,  parent=self)
        self.netlist['n121'] = net.net('n121', pullup_str=100,   parent=self)
        self.netlist['n1210'] = net.net('n1210',  charge_storage=True,  parent=self)
        self.netlist['n1211'] = net.net('n1211', pullup_str=100,   parent=self)
        self.netlist['n1212'] = net.net('n1212', pullup_str=100,   parent=self)
        self.netlist['n1213'] = net.net('n1213', pullup_str=100,   parent=self)
        self.netlist['n1214'] = net.net('n1214',  charge_storage=True,  parent=self)
        self.netlist['n1215'] = net.net('n1215', pullup_str=100,   parent=self)
        self.netlist['n1216'] = net.net('n1216', pullup_str=100,   parent=self)
        self.netlist['n1217'] = net.net('n1217', pullup_str=100,   parent=self)
        self.netlist['n1218'] = net.net('n1218',  charge_storage=True,  parent=self)
        self.netlist['n122'] = net.net('n122',  charge_storage=True,  parent=self)
        self.netlist['n1220'] = net.net('n1220',  charge_storage=True,  parent=self)
        self.netlist['n1222'] = net.net('n1222',  charge_storage=True,  parent=self)
        self.netlist['n1223'] = net.net('n1223', pullup_str=100,   parent=self)
        self.netlist['n1224'] = net.net('n1224', pullup_str=100,   parent=self)
        self.netlist['n1226'] = net.net('n1226', pullup_str=100,   parent=self)
        self.netlist['n1227'] = net.net('n1227', pullup_str=100,   parent=self)
        self.netlist['n1229'] = net.net('n1229',  charge_storage=True,  parent=self)
        self.netlist['n123'] = net.net('n123', pullup_str=100,   parent=self)
        self.netlist['n1230'] = net.net('n1230',  charge_storage=True,  parent=self)
        self.netlist['n1231'] = net.net('n1231', pullup_str=100,   parent=self)
        self.netlist['n1232'] = net.net('n1232',  charge_storage=True,  parent=self)
        self.netlist['n1233'] = net.net('n1233', pullup_str=100,   parent=self)
        self.netlist['n1234'] = net.net('n1234', pullup_str=100,   parent=self)
        self.netlist['n1235'] = net.net('n1235', pullup_str=100,   parent=self)
        self.netlist['n1236'] = net.net('n1236', pullup_str=100,   parent=self)
        self.netlist['n1237'] = net.net('n1237', pullup_str=100,   parent=self)
        self.netlist['n1238'] = net.net('n1238', pullup_str=100,   parent=self)
        self.netlist['n124'] = net.net('n124',  charge_storage=True,  parent=self)
        self.netlist['n1240'] = net.net('n1240', pullup_str=100,   parent=self)
        self.netlist['n1241'] = net.net('n1241',  charge_storage=True,  parent=self)
        self.netlist['n1242'] = net.net('n1242',  charge_storage=True,  parent=self)
        self.netlist['n1243'] = net.net('n1243', pullup_str=100,   parent=self)
        self.netlist['n1244'] = net.net('n1244', pullup_str=100,   parent=self)
        self.netlist['n1245'] = net.net('n1245',  charge_storage=True,  parent=self)
        self.netlist['n1247'] = net.net('n1247', pullup_str=100,   parent=self)
        self.netlist['n1248'] = net.net('n1248',  charge_storage=True,  parent=self)
        self.netlist['n1249'] = net.net('n1249',  charge_storage=True,  parent=self)
        self.netlist['n125'] = net.net('n125', pullup_str=100,   parent=self)
        self.netlist['n1250'] = net.net('n1250', pullup_str=100,   parent=self)
        self.netlist['n1251'] = net.net('n1251', pullup_str=100,   parent=self)
        self.netlist['n1252'] = net.net('n1252', pullup_str=100,   parent=self)
        self.netlist['n1253'] = net.net('n1253', pullup_str=100,   parent=self)
        self.netlist['n1254'] = net.net('n1254', pullup_str=100,   parent=self)
        self.netlist['n1255'] = net.net('n1255',  charge_storage=True,  parent=self)
        self.netlist['n1256'] = net.net('n1256',  charge_storage=True,  parent=self)
        self.netlist['n1257'] = net.net('n1257',  charge_storage=True,  parent=self)
        self.netlist['n1258'] = net.net('n1258',  charge_storage=True,  parent=self)
        self.netlist['n1259'] = net.net('n1259', pullup_str=100,   parent=self)
        self.netlist['n126'] = net.net('n126',  charge_storage=True,  parent=self)
        self.netlist['n1260'] = net.net('n1260', pullup_str=100,   parent=self)
        self.netlist['n1262'] = net.net('n1262', pullup_str=100,   parent=self)
        self.netlist['n1266'] = net.net('n1266', pullup_str=100,   parent=self)
        self.netlist['n127'] = net.net('n127', pullup_str=100,   parent=self)
        self.netlist['n1270'] = net.net('n1270', pullup_str=100,   parent=self)
        self.netlist['n1275'] = net.net('n1275', pullup_str=100,   parent=self)
        self.netlist['n1276'] = net.net('n1276', pullup_str=100,   parent=self)
        self.netlist['n1278'] = net.net('n1278', pullup_str=100,   parent=self)
        self.netlist['n1279'] = net.net('n1279', pullup_str=100,   parent=self)
        self.netlist['n128'] = net.net('n128',  charge_storage=True,  parent=self)
        self.netlist['n129'] = net.net('n129', pullup_str=100,   parent=self)
        self.netlist['n1290'] = net.net('n1290', pullup_str=100,   parent=self)
        self.netlist['n1291'] = net.net('n1291', pullup_str=100,   parent=self)
        self.netlist['n1292'] = net.net('n1292', pullup_str=100,   parent=self)
        self.netlist['n1293'] = net.net('n1293', pullup_str=100,   parent=self)
        self.netlist['n1294'] = net.net('n1294', pullup_str=100,   parent=self)
        self.netlist['n1295'] = net.net('n1295', pullup_str=100,   parent=self)
        self.netlist['n1296'] = net.net('n1296', pullup_str=100,   parent=self)
        self.netlist['n1297'] = net.net('n1297', pullup_str=100,   parent=self)
        self.netlist['n1298'] = net.net('n1298', pullup_str=100,   parent=self)
        self.netlist['n1299'] = net.net('n1299', pullup_str=100,   parent=self)
        self.netlist['n13'] = net.net('n13', pullup_str=100,   parent=self)
        self.netlist['n130'] = net.net('n130',  charge_storage=True,  parent=self)
        self.netlist['n1302'] = net.net('n1302', pullup_str=100,   parent=self)
        self.netlist['n1303'] = net.net('n1303', pullup_str=100,   parent=self)
        self.netlist['n1305'] = net.net('n1305', pullup_str=100,   parent=self)
        self.netlist['n1306'] = net.net('n1306', pullup_str=100,   parent=self)
        self.netlist['n1307'] = net.net('n1307', pullup_str=100,   parent=self)
        self.netlist['n131'] = net.net('n131',  charge_storage=True,  parent=self)
        self.netlist['n1310'] = net.net('n1310',  charge_storage=True,  parent=self)
        self.netlist['n1311'] = net.net('n1311', pullup_str=100,   parent=self)
        self.netlist['n1312'] = net.net('n1312',  charge_storage=True,  parent=self)
        self.netlist['n1313'] = net.net('n1313', pullup_str=100,   parent=self)
        self.netlist['n1314'] = net.net('n1314',  charge_storage=True,  parent=self)
        self.netlist['n1319'] = net.net('n1319',  charge_storage=True,  parent=self)
        self.netlist['n132'] = net.net('n132', pullup_str=100,   parent=self)
        self.netlist['n1320'] = net.net('n1320',  charge_storage=True,  parent=self)
        self.netlist['n1321'] = net.net('n1321',  charge_storage=True,  parent=self)
        self.netlist['n1322'] = net.net('n1322',  charge_storage=True,  parent=self)
        self.netlist['n1323'] = net.net('n1323',  charge_storage=True,  parent=self)
        self.netlist['n1324'] = net.net('n1324',  charge_storage=True,  parent=self)
        self.netlist['n1325'] = net.net('n1325',  charge_storage=True,  parent=self)
        self.netlist['n1326'] = net.net('n1326',  charge_storage=True,  parent=self)
        self.netlist['n1327'] = net.net('n1327',  charge_storage=True,  parent=self)
        self.netlist['n1328'] = net.net('n1328',  charge_storage=True,  parent=self)
        self.netlist['n1329'] = net.net('n1329',  charge_storage=True,  parent=self)
        self.netlist['n133'] = net.net('n133', pullup_str=100,   parent=self)
        self.netlist['n1330'] = net.net('n1330',  charge_storage=True,  parent=self)
        self.netlist['n1331'] = net.net('n1331',  charge_storage=True,  parent=self)
        self.netlist['n1332'] = net.net('n1332',  charge_storage=True,  parent=self)
        self.netlist['n1333'] = net.net('n1333',  charge_storage=True,  parent=self)
        self.netlist['n1334'] = net.net('n1334',  charge_storage=True,  parent=self)
        self.netlist['n1335'] = net.net('n1335',  charge_storage=True,  parent=self)
        self.netlist['n1336'] = net.net('n1336',  charge_storage=True,  parent=self)
        self.netlist['n1337'] = net.net('n1337',  charge_storage=True,  parent=self)
        self.netlist['n1338'] = net.net('n1338',  charge_storage=True,  parent=self)
        self.netlist['n1339'] = net.net('n1339',  charge_storage=True,  parent=self)
        self.netlist['n134'] = net.net('n134', pullup_str=100,   parent=self)
        self.netlist['n1340'] = net.net('n1340',  charge_storage=True,  parent=self)
        self.netlist['n1341'] = net.net('n1341',  charge_storage=True,  parent=self)
        self.netlist['n1342'] = net.net('n1342',  charge_storage=True,  parent=self)
        self.netlist['n1343'] = net.net('n1343',  charge_storage=True,  parent=self)
        self.netlist['n1344'] = net.net('n1344',  charge_storage=True,  parent=self)
        self.netlist['n1345'] = net.net('n1345',  charge_storage=True,  parent=self)
        self.netlist['n1346'] = net.net('n1346',  charge_storage=True,  parent=self)
        self.netlist['n1347'] = net.net('n1347',  charge_storage=True,  parent=self)
        self.netlist['n1348'] = net.net('n1348',  charge_storage=True,  parent=self)
        self.netlist['n1349'] = net.net('n1349',  charge_storage=True,  parent=self)
        self.netlist['n135'] = net.net('n135', pullup_str=100,   parent=self)
        self.netlist['n1350'] = net.net('n1350',  charge_storage=True,  parent=self)
        self.netlist['n1351'] = net.net('n1351',  charge_storage=True,  parent=self)
        self.netlist['n1352'] = net.net('n1352',  charge_storage=True,  parent=self)
        self.netlist['n1353'] = net.net('n1353',  charge_storage=True,  parent=self)
        self.netlist['n1354'] = net.net('n1354',  charge_storage=True,  parent=self)
        self.netlist['n1355'] = net.net('n1355',  charge_storage=True,  parent=self)
        self.netlist['n1356'] = net.net('n1356',  charge_storage=True,  parent=self)
        self.netlist['n1357'] = net.net('n1357',  charge_storage=True,  parent=self)
        self.netlist['n1358'] = net.net('n1358',  charge_storage=True,  parent=self)
        self.netlist['n1359'] = net.net('n1359',  charge_storage=True,  parent=self)
        self.netlist['n136'] = net.net('n136', pullup_str=100,   parent=self)
        self.netlist['n1360'] = net.net('n1360',  charge_storage=True,  parent=self)
        self.netlist['n1361'] = net.net('n1361',  charge_storage=True,  parent=self)
        self.netlist['n1362'] = net.net('n1362',  charge_storage=True,  parent=self)
        self.netlist['n1363'] = net.net('n1363',  charge_storage=True,  parent=self)
        self.netlist['n1364'] = net.net('n1364',  charge_storage=True,  parent=self)
        self.netlist['n1365'] = net.net('n1365',  charge_storage=True,  parent=self)
        self.netlist['n1366'] = net.net('n1366',  charge_storage=True,  parent=self)
        self.netlist['n1367'] = net.net('n1367',  charge_storage=True,  parent=self)
        self.netlist['n1368'] = net.net('n1368',  charge_storage=True,  parent=self)
        self.netlist['n1369'] = net.net('n1369',  charge_storage=True,  parent=self)
        self.netlist['n137'] = net.net('n137', pullup_str=100,   parent=self)
        self.netlist['n1370'] = net.net('n1370',  charge_storage=True,  parent=self)
        self.netlist['n1371'] = net.net('n1371',  charge_storage=True,  parent=self)
        self.netlist['n1372'] = net.net('n1372',  charge_storage=True,  parent=self)
        self.netlist['n1373'] = net.net('n1373',  charge_storage=True,  parent=self)
        self.netlist['n1374'] = net.net('n1374',  charge_storage=True,  parent=self)
        self.netlist['n1375'] = net.net('n1375',  charge_storage=True,  parent=self)
        self.netlist['n1376'] = net.net('n1376',  charge_storage=True,  parent=self)
        self.netlist['n1377'] = net.net('n1377',  charge_storage=True,  parent=self)
        self.netlist['n1378'] = net.net('n1378',  charge_storage=True,  parent=self)
        self.netlist['n1379'] = net.net('n1379',  charge_storage=True,  parent=self)
        self.netlist['n138'] = net.net('n138', pullup_str=100,   parent=self)
        self.netlist['n1380'] = net.net('n1380',  charge_storage=True,  parent=self)
        self.netlist['n1381'] = net.net('n1381',  charge_storage=True,  parent=self)
        self.netlist['n1382'] = net.net('n1382',  charge_storage=True,  parent=self)
        self.netlist['n1383'] = net.net('n1383',  charge_storage=True,  parent=self)
        self.netlist['n1384'] = net.net('n1384',  charge_storage=True,  parent=self)
        self.netlist['n1385'] = net.net('n1385',  charge_storage=True,  parent=self)
        self.netlist['n1386'] = net.net('n1386',  charge_storage=True,  parent=self)
        self.netlist['n1387'] = net.net('n1387',  charge_storage=True,  parent=self)
        self.netlist['n1388'] = net.net('n1388',  charge_storage=True,  parent=self)
        self.netlist['n1389'] = net.net('n1389',  charge_storage=True,  parent=self)
        self.netlist['n139'] = net.net('n139', pullup_str=100,   parent=self)
        self.netlist['n1390'] = net.net('n1390',  charge_storage=True,  parent=self)
        self.netlist['n1391'] = net.net('n1391',  charge_storage=True,  parent=self)
        self.netlist['n1392'] = net.net('n1392',  charge_storage=True,  parent=self)
        self.netlist['n1393'] = net.net('n1393',  charge_storage=True,  parent=self)
        self.netlist['n1394'] = net.net('n1394',  charge_storage=True,  parent=self)
        self.netlist['n1395'] = net.net('n1395',  charge_storage=True,  parent=self)
        self.netlist['n1396'] = net.net('n1396',  charge_storage=True,  parent=self)
        self.netlist['n1397'] = net.net('n1397',  charge_storage=True,  parent=self)
        self.netlist['n1398'] = net.net('n1398',  charge_storage=True,  parent=self)
        self.netlist['n1399'] = net.net('n1399',  charge_storage=True,  parent=self)
        self.netlist['n14'] = net.net('n14', pullup_str=100,   parent=self)
        self.netlist['n140'] = net.net('n140', pullup_str=100,   parent=self)
        self.netlist['n1400'] = net.net('n1400',  charge_storage=True,  parent=self)
        self.netlist['n1401'] = net.net('n1401',  charge_storage=True,  parent=self)
        self.netlist['n1402'] = net.net('n1402',  charge_storage=True,  parent=self)
        self.netlist['n1403'] = net.net('n1403',  charge_storage=True,  parent=self)
        self.netlist['n1404'] = net.net('n1404',  charge_storage=True,  parent=self)
        self.netlist['n1405'] = net.net('n1405',  charge_storage=True,  parent=self)
        self.netlist['n1407'] = net.net('n1407',  charge_storage=True,  parent=self)
        self.netlist['n1408'] = net.net('n1408',  charge_storage=True,  parent=self)
        self.netlist['n1409'] = net.net('n1409',  charge_storage=True,  parent=self)
        self.netlist['n1410'] = net.net('n1410',  charge_storage=True,  parent=self)
        self.netlist['n1411'] = net.net('n1411',  charge_storage=True,  parent=self)
        self.netlist['n1412'] = net.net('n1412',  charge_storage=True,  parent=self)
        self.netlist['n1413'] = net.net('n1413',  charge_storage=True,  parent=self)
        self.netlist['n1414'] = net.net('n1414',  charge_storage=True,  parent=self)
        self.netlist['n1415'] = net.net('n1415',  charge_storage=True,  parent=self)
        self.netlist['n1416'] = net.net('n1416',  charge_storage=True,  parent=self)
        self.netlist['n1417'] = net.net('n1417',  charge_storage=True,  parent=self)
        self.netlist['n1418'] = net.net('n1418',  charge_storage=True,  parent=self)
        self.netlist['n1419'] = net.net('n1419',  charge_storage=True,  parent=self)
        self.netlist['n1420'] = net.net('n1420',  charge_storage=True,  parent=self)
        self.netlist['n1421'] = net.net('n1421',  charge_storage=True,  parent=self)
        self.netlist['n1422'] = net.net('n1422',  charge_storage=True,  parent=self)
        self.netlist['n1423'] = net.net('n1423',  charge_storage=True,  parent=self)
        self.netlist['n1424'] = net.net('n1424',  charge_storage=True,  parent=self)
        self.netlist['n1425'] = net.net('n1425',  charge_storage=True,  parent=self)
        self.netlist['n1426'] = net.net('n1426',  charge_storage=True,  parent=self)
        self.netlist['n1427'] = net.net('n1427',  charge_storage=True,  parent=self)
        self.netlist['n1428'] = net.net('n1428',  charge_storage=True,  parent=self)
        self.netlist['n1429'] = net.net('n1429',  charge_storage=True,  parent=self)
        self.netlist['n1430'] = net.net('n1430',  charge_storage=True,  parent=self)
        self.netlist['n1431'] = net.net('n1431',  charge_storage=True,  parent=self)
        self.netlist['n1432'] = net.net('n1432',  charge_storage=True,  parent=self)
        self.netlist['n1433'] = net.net('n1433',  charge_storage=True,  parent=self)
        self.netlist['n1434'] = net.net('n1434',  charge_storage=True,  parent=self)
        self.netlist['n1435'] = net.net('n1435',  charge_storage=True,  parent=self)
        self.netlist['n1436'] = net.net('n1436',  charge_storage=True,  parent=self)
        self.netlist['n1437'] = net.net('n1437',  charge_storage=True,  parent=self)
        self.netlist['n1438'] = net.net('n1438',  charge_storage=True,  parent=self)
        self.netlist['n1439'] = net.net('n1439',  charge_storage=True,  parent=self)
        self.netlist['n1440'] = net.net('n1440',  charge_storage=True,  parent=self)
        self.netlist['n1441'] = net.net('n1441',  charge_storage=True,  parent=self)
        self.netlist['n1442'] = net.net('n1442',  charge_storage=True,  parent=self)
        self.netlist['n1443'] = net.net('n1443',  charge_storage=True,  parent=self)
        self.netlist['n1444'] = net.net('n1444',  charge_storage=True,  parent=self)
        self.netlist['n1446'] = net.net('n1446',  charge_storage=True,  parent=self)
        self.netlist['n1448'] = net.net('n1448',  charge_storage=True,  parent=self)
        self.netlist['n1449'] = net.net('n1449', pullup_str=100,   parent=self)
        self.netlist['n1450'] = net.net('n1450',  charge_storage=True,  parent=self)
        self.netlist['n1451'] = net.net('n1451',  charge_storage=True,  parent=self)
        self.netlist['n1452'] = net.net('n1452', pullup_str=100,   parent=self)
        self.netlist['n1453'] = net.net('n1453', pullup_str=100,   parent=self)
        self.netlist['n1454'] = net.net('n1454', pullup_str=100,   parent=self)
        self.netlist['n1460'] = net.net('n1460', pullup_str=100,   parent=self)
        self.netlist['n1463'] = net.net('n1463', pullup_str=100,   parent=self)
        self.netlist['n1464'] = net.net('n1464',  charge_storage=True,  parent=self)
        self.netlist['n1465'] = net.net('n1465', pullup_str=100,   parent=self)
        self.netlist['n1466'] = net.net('n1466', pullup_str=100,   parent=self)
        self.netlist['n1467'] = net.net('n1467', pullup_str=100,   parent=self)
        self.netlist['n1468'] = net.net('n1468',  charge_storage=True,  parent=self)
        self.netlist['n1470'] = net.net('n1470', pullup_str=100,   parent=self)
        self.netlist['n1471'] = net.net('n1471',  charge_storage=True,  parent=self)
        self.netlist['n1472'] = net.net('n1472', pullup_str=100,   parent=self)
        self.netlist['n1473'] = net.net('n1473', pullup_str=100,   parent=self)
        self.netlist['n1474'] = net.net('n1474', pullup_str=100,   parent=self)
        self.netlist['n1476'] = net.net('n1476', pullup_str=100,   parent=self)
        self.netlist['n1477'] = net.net('n1477', pullup_str=100,   parent=self)
        self.netlist['n1478'] = net.net('n1478', pullup_str=100,   parent=self)
        self.netlist['n1479'] = net.net('n1479', pullup_str=100,   parent=self)
        self.netlist['n1480'] = net.net('n1480', pullup_str=100,   parent=self)
        self.netlist['n1481'] = net.net('n1481', pullup_str=100,   parent=self)
        self.netlist['n1483'] = net.net('n1483',  charge_storage=True,  parent=self)
        self.netlist['n1484'] = net.net('n1484', pullup_str=100,   parent=self)
        self.netlist['n1485'] = net.net('n1485', pullup_str=100,   parent=self)
        self.netlist['n1486'] = net.net('n1486',  charge_storage=True,  parent=self)
        self.netlist['n1487'] = net.net('n1487', pullup_str=100,   parent=self)
        self.netlist['n1489'] = net.net('n1489',  charge_storage=True,  parent=self)
        self.netlist['n1493'] = net.net('n1493',  charge_storage=True,  parent=self)
        self.netlist['n1499'] = net.net('n1499', pullup_str=100,   parent=self)
        self.netlist['n15'] = net.net('n15', pullup_str=100,   parent=self)
        self.netlist['n1500'] = net.net('n1500', pullup_str=100,   parent=self)
        self.netlist['n1502'] = net.net('n1502',  charge_storage=True,  parent=self)
        self.netlist['n1505'] = net.net('n1505', pullup_str=100,   parent=self)
        self.netlist['n1506'] = net.net('n1506', pullup_str=100,   parent=self)
        self.netlist['n1508'] = net.net('n1508',  charge_storage=True,  parent=self)
        self.netlist['n1509'] = net.net('n1509', pullup_str=100,   parent=self)
        self.netlist['n1510'] = net.net('n1510', pullup_str=100,   parent=self)
        self.netlist['n1513'] = net.net('n1513', pullup_str=100,   parent=self)
        self.netlist['n1514'] = net.net('n1514', pullup_str=100,   parent=self)
        self.netlist['n1515'] = net.net('n1515', pullup_str=100,   parent=self)
        self.netlist['n1516'] = net.net('n1516', pullup_str=100,   parent=self)
        self.netlist['n1517'] = net.net('n1517', pullup_str=100,   parent=self)
        self.netlist['n1518'] = net.net('n1518', pullup_str=100,   parent=self)
        self.netlist['n1519'] = net.net('n1519', pullup_str=100,   parent=self)
        self.netlist['n1520'] = net.net('n1520', pullup_str=100,   parent=self)
        self.netlist['n1521'] = net.net('n1521', pullup_str=100,   parent=self)
        self.netlist['n1522'] = net.net('n1522', pullup_str=100,   parent=self)
        self.netlist['n1523'] = net.net('n1523', pullup_str=100,   parent=self)
        self.netlist['n1524'] = net.net('n1524', pullup_str=100,   parent=self)
        self.netlist['n1525'] = net.net('n1525', pullup_str=100,   parent=self)
        self.netlist['n1526'] = net.net('n1526', pullup_str=100,   parent=self)
        self.netlist['n1527'] = net.net('n1527', pullup_str=100,   parent=self)
        self.netlist['n1529'] = net.net('n1529', pullup_str=100,   parent=self)
        self.netlist['n1530'] = net.net('n1530', pullup_str=100,   parent=self)
        self.netlist['n1531'] = net.net('n1531', pullup_str=100,   parent=self)
        self.netlist['n1532'] = net.net('n1532', pullup_str=100,   parent=self)
        self.netlist['n1533'] = net.net('n1533', pullup_str=100,   parent=self)
        self.netlist['n1534'] = net.net('n1534', pullup_str=100,   parent=self)
        self.netlist['n1535'] = net.net('n1535', pullup_str=100,   parent=self)
        self.netlist['n1536'] = net.net('n1536', pullup_str=100,   parent=self)
        self.netlist['n1537'] = net.net('n1537', pullup_str=100,   parent=self)
        self.netlist['n1538'] = net.net('n1538', pullup_str=100,   parent=self)
        self.netlist['n1566'] = net.net('n1566', pullup_str=100,   parent=self)
        self.netlist['n1567'] = net.net('n1567',  charge_storage=True,  parent=self)
        self.netlist['n1568'] = net.net('n1568',  charge_storage=True,  parent=self)
        self.netlist['n1569'] = net.net('n1569',  charge_storage=True,  parent=self)
        self.netlist['n157'] = net.net('n157', pullup_str=100,   parent=self)
        self.netlist['n1570'] = net.net('n1570',  charge_storage=True,  parent=self)
        self.netlist['n1574'] = net.net('n1574',  charge_storage=True,  parent=self)
        self.netlist['n1576'] = net.net('n1576',  charge_storage=True,  parent=self)
        self.netlist['n1578'] = net.net('n1578',  charge_storage=True,  parent=self)
        self.netlist['n1579'] = net.net('n1579',  charge_storage=True,  parent=self)
        self.netlist['n158'] = net.net('n158',  charge_storage=True,  parent=self)
        self.netlist['n1582'] = net.net('n1582',  charge_storage=True,  parent=self)
        self.netlist['n1583'] = net.net('n1583',  charge_storage=True,  parent=self)
        self.netlist['n159'] = net.net('n159',  charge_storage=True,  parent=self)
        self.netlist['n1598'] = net.net('n1598', pullup_str=100,   parent=self)
        self.netlist['n1599'] = net.net('n1599', pullup_str=100,   parent=self)
        self.netlist['n16'] = net.net('n16', pullup_str=100,   parent=self)
        self.netlist['n1600'] = net.net('n1600', pullup_str=100,   parent=self)
        self.netlist['n1601'] = net.net('n1601', pullup_str=100,   parent=self)
        self.netlist['n1602'] = net.net('n1602', pullup_str=100,   parent=self)
        self.netlist['n1603'] = net.net('n1603', pullup_str=100,   parent=self)
        self.netlist['n1604'] = net.net('n1604', pullup_str=100,   parent=self)
        self.netlist['n1605'] = net.net('n1605', pullup_str=100,   parent=self)
        self.netlist['n1606'] = net.net('n1606',  charge_storage=True,  parent=self)
        self.netlist['n1607'] = net.net('n1607', pullup_str=100,   parent=self)
        self.netlist['n1608'] = net.net('n1608', pullup_str=100,   parent=self)
        self.netlist['n1609'] = net.net('n1609', pullup_str=100,   parent=self)
        self.netlist['n161'] = net.net('n161', pullup_str=100,   parent=self)
        self.netlist['n1610'] = net.net('n1610', pullup_str=100,   parent=self)
        self.netlist['n1611'] = net.net('n1611', pullup_str=100,   parent=self)
        self.netlist['n1612'] = net.net('n1612', pullup_str=100,   parent=self)
        self.netlist['n1613'] = net.net('n1613', pullup_str=100,   parent=self)
        self.netlist['n1614'] = net.net('n1614', pullup_str=100,   parent=self)
        self.netlist['n1615'] = net.net('n1615', pullup_str=100,   parent=self)
        self.netlist['n1616'] = net.net('n1616', pullup_str=100,   parent=self)
        self.netlist['n1617'] = net.net('n1617', pullup_str=100,   parent=self)
        self.netlist['n1618'] = net.net('n1618', pullup_str=100,   parent=self)
        self.netlist['n1619'] = net.net('n1619', pullup_str=100,   parent=self)
        self.netlist['n162'] = net.net('n162', pullup_str=100,   parent=self)
        self.netlist['n1620'] = net.net('n1620', pullup_str=100,   parent=self)
        self.netlist['n1621'] = net.net('n1621', pullup_str=100,   parent=self)
        self.netlist['n1622'] = net.net('n1622', pullup_str=100,   parent=self)
        self.netlist['n1623'] = net.net('n1623', pullup_str=100,   parent=self)
        self.netlist['n1624'] = net.net('n1624', pullup_str=100,   parent=self)
        self.netlist['n1625'] = net.net('n1625', pullup_str=100,   parent=self)
        self.netlist['n1626'] = net.net('n1626', pullup_str=100,   parent=self)
        self.netlist['n1627'] = net.net('n1627', pullup_str=100,   parent=self)
        self.netlist['n1628'] = net.net('n1628', pullup_str=100,   parent=self)
        self.netlist['n1629'] = net.net('n1629', pullup_str=100,   parent=self)
        self.netlist['n163'] = net.net('n163', pullup_str=100,   parent=self)
        self.netlist['n1630'] = net.net('n1630', pullup_str=100,   parent=self)
        self.netlist['n1632'] = net.net('n1632', pullup_str=100,   parent=self)
        self.netlist['n1638'] = net.net('n1638', pullup_str=100,   parent=self)
        self.netlist['n1639'] = net.net('n1639', pullup_str=100,   parent=self)
        self.netlist['n164'] = net.net('n164', pullup_str=100,   parent=self)
        self.netlist['n1640'] = net.net('n1640', pullup_str=100,   parent=self)
        self.netlist['n1646'] = net.net('n1646',  charge_storage=True,  parent=self)
        self.netlist['n1647'] = net.net('n1647',  charge_storage=True,  parent=self)
        self.netlist['n165'] = net.net('n165', pullup_str=100,   parent=self)
        self.netlist['n1652'] = net.net('n1652',  charge_storage=True,  parent=self)
        self.netlist['n1654'] = net.net('n1654',  charge_storage=True,  parent=self)
        self.netlist['n1659'] = net.net('n1659',  charge_storage=True,  parent=self)
        self.netlist['n166'] = net.net('n166',  charge_storage=True,  parent=self)
        self.netlist['n1660'] = net.net('n1660',  charge_storage=True,  parent=self)
        self.netlist['n1661'] = net.net('n1661',  charge_storage=True,  parent=self)
        self.netlist['n1662'] = net.net('n1662',  charge_storage=True,  parent=self)
        self.netlist['n1663'] = net.net('n1663',  charge_storage=True,  parent=self)
        self.netlist['n1664'] = net.net('n1664',  charge_storage=True,  parent=self)
        self.netlist['n1665'] = net.net('n1665',  charge_storage=True,  parent=self)
        self.netlist['n1666'] = net.net('n1666',  charge_storage=True,  parent=self)
        self.netlist['n1668'] = net.net('n1668',  charge_storage=True,  parent=self)
        self.netlist['n167'] = net.net('n167', pullup_str=100,   parent=self)
        self.netlist['n1672'] = net.net('n1672',  charge_storage=True,  parent=self)
        self.netlist['n1673'] = net.net('n1673',  charge_storage=True,  parent=self)
        self.netlist['n1674'] = net.net('n1674',  charge_storage=True,  parent=self)
        self.netlist['n1675'] = net.net('n1675',  charge_storage=True,  parent=self)
        self.netlist['n1676'] = net.net('n1676',  charge_storage=True,  parent=self)
        self.netlist['n168'] = net.net('n168',  charge_storage=True,  parent=self)
        self.netlist['n169'] = net.net('n169', pullup_str=100,   parent=self)
        self.netlist['n1690'] = net.net('n1690',  charge_storage=True,  parent=self)
        self.netlist['n17'] = net.net('n17', pullup_str=100,   parent=self)
        self.netlist['n170'] = net.net('n170',  charge_storage=True,  parent=self)
        self.netlist['n1704'] = net.net('n1704', pullup_str=100,   parent=self)
        self.netlist['n1705'] = net.net('n1705', pullup_str=100,   parent=self)
        self.netlist['n1706'] = net.net('n1706', pullup_str=100,   parent=self)
        self.netlist['n1707'] = net.net('n1707', pullup_str=100,   parent=self)
        self.netlist['n1708'] = net.net('n1708', pullup_str=100,   parent=self)
        self.netlist['n1709'] = net.net('n1709', pullup_str=100,   parent=self)
        self.netlist['n171'] = net.net('n171', pullup_str=100,   parent=self)
        self.netlist['n1710'] = net.net('n1710', pullup_str=100,   parent=self)
        self.netlist['n1711'] = net.net('n1711', pullup_str=100,   parent=self)
        self.netlist['n1712'] = net.net('n1712', pullup_str=100,   parent=self)
        self.netlist['n1713'] = net.net('n1713', pullup_str=100,   parent=self)
        self.netlist['n1714'] = net.net('n1714', pullup_str=100,   parent=self)
        self.netlist['n1715'] = net.net('n1715', pullup_str=100,   parent=self)
        self.netlist['n1716'] = net.net('n1716', pullup_str=100,   parent=self)
        self.netlist['n1717'] = net.net('n1717', pullup_str=100,   parent=self)
        self.netlist['n1718'] = net.net('n1718', pullup_str=100,   parent=self)
        self.netlist['n1719'] = net.net('n1719', pullup_str=100,   parent=self)
        self.netlist['n172'] = net.net('n172', pullup_str=100,   parent=self)
        self.netlist['n1720'] = net.net('n1720', pullup_str=100,   parent=self)
        self.netlist['n1721'] = net.net('n1721', pullup_str=100,   parent=self)
        self.netlist['n1722'] = net.net('n1722', pullup_str=100,   parent=self)
        self.netlist['n1723'] = net.net('n1723', pullup_str=100,   parent=self)
        self.netlist['n1724'] = net.net('n1724', pullup_str=100,   parent=self)
        self.netlist['n1725'] = net.net('n1725', pullup_str=100,   parent=self)
        self.netlist['n1726'] = net.net('n1726', pullup_str=100,   parent=self)
        self.netlist['n1727'] = net.net('n1727', pullup_str=100,   parent=self)
        self.netlist['n1728'] = net.net('n1728', pullup_str=100,   parent=self)
        self.netlist['n1729'] = net.net('n1729', pullup_str=100,   parent=self)
        self.netlist['n173'] = net.net('n173', pullup_str=100,   parent=self)
        self.netlist['n1730'] = net.net('n1730', pullup_str=100,   parent=self)
        self.netlist['n1731'] = net.net('n1731', pullup_str=100,   parent=self)
        self.netlist['n1732'] = net.net('n1732', pullup_str=100,   parent=self)
        self.netlist['n1733'] = net.net('n1733', pullup_str=100,   parent=self)
        self.netlist['n1734'] = net.net('n1734', pullup_str=100,   parent=self)
        self.netlist['n1735'] = net.net('n1735', pullup_str=100,   parent=self)
        self.netlist['n1736'] = net.net('n1736', pullup_str=100,   parent=self)
        self.netlist['n1737'] = net.net('n1737', pullup_str=100,   parent=self)
        self.netlist['n1738'] = net.net('n1738', pullup_str=100,   parent=self)
        self.netlist['n1739'] = net.net('n1739', pullup_str=100,   parent=self)
        self.netlist['n174'] = net.net('n174', pullup_str=100,   parent=self)
        self.netlist['n1740'] = net.net('n1740', pullup_str=100,   parent=self)
        self.netlist['n1741'] = net.net('n1741', pullup_str=100,   parent=self)
        self.netlist['n1742'] = net.net('n1742', pullup_str=100,   parent=self)
        self.netlist['n1743'] = net.net('n1743', pullup_str=100,   parent=self)
        self.netlist['n1744'] = net.net('n1744', pullup_str=100,   parent=self)
        self.netlist['n1745'] = net.net('n1745', pullup_str=100,   parent=self)
        self.netlist['n1746'] = net.net('n1746', pullup_str=100,   parent=self)
        self.netlist['n1747'] = net.net('n1747', pullup_str=100,   parent=self)
        self.netlist['n1748'] = net.net('n1748', pullup_str=100,   parent=self)
        self.netlist['n1749'] = net.net('n1749', pullup_str=100,   parent=self)
        self.netlist['n175'] = net.net('n175', pullup_str=100,   parent=self)
        self.netlist['n1750'] = net.net('n1750', pullup_str=100,   parent=self)
        self.netlist['n1751'] = net.net('n1751', pullup_str=100,   parent=self)
        self.netlist['n1752'] = net.net('n1752', pullup_str=100,   parent=self)
        self.netlist['n1753'] = net.net('n1753', pullup_str=100,   parent=self)
        self.netlist['n1754'] = net.net('n1754', pullup_str=100,   parent=self)
        self.netlist['n1755'] = net.net('n1755', pullup_str=100,   parent=self)
        self.netlist['n1756'] = net.net('n1756', pullup_str=100,   parent=self)
        self.netlist['n1757'] = net.net('n1757', pullup_str=100,   parent=self)
        self.netlist['n1758'] = net.net('n1758',  charge_storage=True,  parent=self)
        self.netlist['n1759'] = net.net('n1759',  charge_storage=True,  parent=self)
        self.netlist['n176'] = net.net('n176', pullup_str=100,   parent=self)
        self.netlist['n1760'] = net.net('n1760', pullup_str=100,   parent=self)
        self.netlist['n1761'] = net.net('n1761', pullup_str=100,   parent=self)
        self.netlist['n1762'] = net.net('n1762', pullup_str=100,   parent=self)
        self.netlist['n1763'] = net.net('n1763',  charge_storage=True,  parent=self)
        self.netlist['n1764'] = net.net('n1764',  charge_storage=True,  parent=self)
        self.netlist['n1765'] = net.net('n1765', pullup_str=100,   parent=self)
        self.netlist['n1766'] = net.net('n1766', pullup_str=100,   parent=self)
        self.netlist['n1767'] = net.net('n1767',  charge_storage=True,  parent=self)
        self.netlist['n1768'] = net.net('n1768',  charge_storage=True,  parent=self)
        self.netlist['n1769'] = net.net('n1769', pullup_str=100,   parent=self)
        self.netlist['n177'] = net.net('n177', pullup_str=100,   parent=self)
        self.netlist['n1770'] = net.net('n1770', pullup_str=100,   parent=self)
        self.netlist['n1771'] = net.net('n1771', pullup_str=100,   parent=self)
        self.netlist['n1772'] = net.net('n1772', pullup_str=100,   parent=self)
        self.netlist['n1773'] = net.net('n1773', pullup_str=100,   parent=self)
        self.netlist['n1774'] = net.net('n1774', pullup_str=100,   parent=self)
        self.netlist['n1775'] = net.net('n1775', pullup_str=100,   parent=self)
        self.netlist['n1776'] = net.net('n1776', pullup_str=100,   parent=self)
        self.netlist['n1777'] = net.net('n1777', pullup_str=100,   parent=self)
        self.netlist['n1778'] = net.net('n1778', pullup_str=100,   parent=self)
        self.netlist['n1779'] = net.net('n1779',  charge_storage=True,  parent=self)
        self.netlist['n178'] = net.net('n178', pullup_str=100,   parent=self)
        self.netlist['n1780'] = net.net('n1780',  charge_storage=True,  parent=self)
        self.netlist['n1781'] = net.net('n1781', pullup_str=100,   parent=self)
        self.netlist['n1782'] = net.net('n1782', pullup_str=100,   parent=self)
        self.netlist['n1783'] = net.net('n1783', pullup_str=100,   parent=self)
        self.netlist['n1785'] = net.net('n1785', pullup_str=100,   parent=self)
        self.netlist['n1788'] = net.net('n1788',  charge_storage=True,  parent=self)
        self.netlist['n1789'] = net.net('n1789', pullup_str=100,   parent=self)
        self.netlist['n179'] = net.net('n179', pullup_str=100,   parent=self)
        self.netlist['n1790'] = net.net('n1790', pullup_str=100,   parent=self)
        self.netlist['n1791'] = net.net('n1791', pullup_str=100,   parent=self)
        self.netlist['n1792'] = net.net('n1792', pullup_str=100,   parent=self)
        self.netlist['n1793'] = net.net('n1793', pullup_str=100,   parent=self)
        self.netlist['n1794'] = net.net('n1794', pullup_str=100,   parent=self)
        self.netlist['n1795'] = net.net('n1795', pullup_str=100,   parent=self)
        self.netlist['n1796'] = net.net('n1796', pullup_str=100,   parent=self)
        self.netlist['n1797'] = net.net('n1797', pullup_str=100,   parent=self)
        self.netlist['n1798'] = net.net('n1798', pullup_str=100,   parent=self)
        self.netlist['n1799'] = net.net('n1799', pullup_str=100,   parent=self)
        self.netlist['n18'] = net.net('n18', pullup_str=100,   parent=self)
        self.netlist['n180'] = net.net('n180', pullup_str=100,   parent=self)
        self.netlist['n1800'] = net.net('n1800', pullup_str=100,   parent=self)
        self.netlist['n1801'] = net.net('n1801', pullup_str=100,   parent=self)
        self.netlist['n1802'] = net.net('n1802', pullup_str=100,   parent=self)
        self.netlist['n1803'] = net.net('n1803', pullup_str=100,   parent=self)
        self.netlist['n1804'] = net.net('n1804', pullup_str=100,   parent=self)
        self.netlist['n1805'] = net.net('n1805', pullup_str=100,   parent=self)
        self.netlist['n1806'] = net.net('n1806', pullup_str=100,   parent=self)
        self.netlist['n1807'] = net.net('n1807', pullup_str=100,   parent=self)
        self.netlist['n1808'] = net.net('n1808', pullup_str=100,   parent=self)
        self.netlist['n1809'] = net.net('n1809', pullup_str=100,   parent=self)
        self.netlist['n181'] = net.net('n181', pullup_str=100,   parent=self)
        self.netlist['n1810'] = net.net('n1810', pullup_str=100,   parent=self)
        self.netlist['n1811'] = net.net('n1811', pullup_str=100,   parent=self)
        self.netlist['n1812'] = net.net('n1812', pullup_str=100,   parent=self)
        self.netlist['n1813'] = net.net('n1813', pullup_str=100,   parent=self)
        self.netlist['n1814'] = net.net('n1814', pullup_str=100,   parent=self)
        self.netlist['n1815'] = net.net('n1815', pullup_str=100,   parent=self)
        self.netlist['n1816'] = net.net('n1816', pullup_str=100,   parent=self)
        self.netlist['n1817'] = net.net('n1817', pullup_str=100,   parent=self)
        self.netlist['n1818'] = net.net('n1818', pullup_str=100,   parent=self)
        self.netlist['n1819'] = net.net('n1819', pullup_str=100,   parent=self)
        self.netlist['n1820'] = net.net('n1820', pullup_str=100,   parent=self)
        self.netlist['n1821'] = net.net('n1821', pullup_str=100,   parent=self)
        self.netlist['n1822'] = net.net('n1822', pullup_str=100,   parent=self)
        self.netlist['n1823'] = net.net('n1823', pullup_str=100,   parent=self)
        self.netlist['n1824'] = net.net('n1824', pullup_str=100,   parent=self)
        self.netlist['n1825'] = net.net('n1825', pullup_str=100,   parent=self)
        self.netlist['n1826'] = net.net('n1826', pullup_str=100,   parent=self)
        self.netlist['n1827'] = net.net('n1827', pullup_str=100,   parent=self)
        self.netlist['n1828'] = net.net('n1828', pullup_str=100,   parent=self)
        self.netlist['n1829'] = net.net('n1829', pullup_str=100,   parent=self)
        self.netlist['n1830'] = net.net('n1830', pullup_str=100,   parent=self)
        self.netlist['n1831'] = net.net('n1831', pullup_str=100,   parent=self)
        self.netlist['n1832'] = net.net('n1832', pullup_str=100,   parent=self)
        self.netlist['n1833'] = net.net('n1833', pullup_str=100,   parent=self)
        self.netlist['n1834'] = net.net('n1834', pullup_str=100,   parent=self)
        self.netlist['n1835'] = net.net('n1835', pullup_str=100,   parent=self)
        self.netlist['n1836'] = net.net('n1836', pullup_str=100,   parent=self)
        self.netlist['n1837'] = net.net('n1837', pullup_str=100,   parent=self)
        self.netlist['n1838'] = net.net('n1838', pullup_str=100,   parent=self)
        self.netlist['n1839'] = net.net('n1839', pullup_str=100,   parent=self)
        self.netlist['n184'] = net.net('n184', pullup_str=100,   parent=self)
        self.netlist['n1840'] = net.net('n1840', pullup_str=100,   parent=self)
        self.netlist['n1841'] = net.net('n1841', pullup_str=100,   parent=self)
        self.netlist['n1842'] = net.net('n1842', pullup_str=100,   parent=self)
        self.netlist['n1843'] = net.net('n1843', pullup_str=100,   parent=self)
        self.netlist['n1844'] = net.net('n1844', pullup_str=100,   parent=self)
        self.netlist['n1845'] = net.net('n1845', pullup_str=100,   parent=self)
        self.netlist['n1846'] = net.net('n1846', pullup_str=100,   parent=self)
        self.netlist['n1847'] = net.net('n1847', pullup_str=100,   parent=self)
        self.netlist['n1848'] = net.net('n1848', pullup_str=100,   parent=self)
        self.netlist['n1849'] = net.net('n1849', pullup_str=100,   parent=self)
        self.netlist['n185'] = net.net('n185', pullup_str=100,   parent=self)
        self.netlist['n1850'] = net.net('n1850', pullup_str=100,   parent=self)
        self.netlist['n1851'] = net.net('n1851', pullup_str=100,   parent=self)
        self.netlist['n1852'] = net.net('n1852', pullup_str=100,   parent=self)
        self.netlist['n1853'] = net.net('n1853', pullup_str=100,   parent=self)
        self.netlist['n186'] = net.net('n186',  charge_storage=True,  parent=self)
        self.netlist['n19'] = net.net('n19', pullup_str=100,   parent=self)
        self.netlist['n1951'] = net.net('n1951',  charge_storage=True,  parent=self)
        self.netlist['n1952'] = net.net('n1952',  charge_storage=True,  parent=self)
        self.netlist['n1956'] = net.net('n1956',  charge_storage=True,  parent=self)
        self.netlist['n1968'] = net.net('n1968',  charge_storage=True,  parent=self)
        self.netlist['n2'] = net.net('n2', pullup_str=100,   parent=self)
        self.netlist['n20'] = net.net('n20', pullup_str=100,   parent=self)
        self.netlist['n21'] = net.net('n21', pullup_str=100,   parent=self)
        self.netlist['n210'] = net.net('n210', pullup_str=100,   parent=self)
        self.netlist['n211'] = net.net('n211',  charge_storage=True,  parent=self)
        self.netlist['n212'] = net.net('n212',  charge_storage=True,  parent=self)
        self.netlist['n213'] = net.net('n213',  charge_storage=True,  parent=self)
        self.netlist['n214'] = net.net('n214',  charge_storage=True,  parent=self)
        self.netlist['n215'] = net.net('n215',  charge_storage=True,  parent=self)
        self.netlist['n216'] = net.net('n216',  charge_storage=True,  parent=self)
        self.netlist['n217'] = net.net('n217',  charge_storage=True,  parent=self)
        self.netlist['n218'] = net.net('n218',  charge_storage=True,  parent=self)
        self.netlist['n219'] = net.net('n219', pullup_str=100,   parent=self)
        self.netlist['n22'] = net.net('n22', pullup_str=100,   parent=self)
        self.netlist['n220'] = net.net('n220', pullup_str=100,   parent=self)
        self.netlist['n221'] = net.net('n221', pullup_str=100,   parent=self)
        self.netlist['n222'] = net.net('n222', pullup_str=100,   parent=self)
        self.netlist['n223'] = net.net('n223', pullup_str=100,   parent=self)
        self.netlist['n224'] = net.net('n224', pullup_str=100,   parent=self)
        self.netlist['n225'] = net.net('n225', pullup_str=100,   parent=self)
        self.netlist['n226'] = net.net('n226', pullup_str=100,   parent=self)
        self.netlist['n227'] = net.net('n227', pullup_str=100,   parent=self)
        self.netlist['n228'] = net.net('n228', pullup_str=100,   parent=self)
        self.netlist['n229'] = net.net('n229', pullup_str=100,   parent=self)
        self.netlist['n23'] = net.net('n23', pullup_str=100,   parent=self)
        self.netlist['n230'] = net.net('n230', pullup_str=100,   parent=self)
        self.netlist['n231'] = net.net('n231', pullup_str=100,   parent=self)
        self.netlist['n232'] = net.net('n232', pullup_str=100,   parent=self)
        self.netlist['n233'] = net.net('n233', pullup_str=100,   parent=self)
        self.netlist['n24'] = net.net('n24', pullup_str=100,   parent=self)
        self.netlist['n241'] = net.net('n241', pullup_str=100,   parent=self)
        self.netlist['n244'] = net.net('n244', pullup_str=100,   parent=self)
        self.netlist['n246'] = net.net('n246', pullup_str=100,   parent=self)
        self.netlist['n247'] = net.net('n247', pullup_str=100,   parent=self)
        self.netlist['n248'] = net.net('n248', pullup_str=100,   parent=self)
        self.netlist['n249'] = net.net('n249', pullup_str=100,   parent=self)
        self.netlist['n25'] = net.net('n25', pullup_str=100,   parent=self)
        self.netlist['n250'] = net.net('n250', pullup_str=100,   parent=self)
        self.netlist['n251'] = net.net('n251', pullup_str=100,   parent=self)
        self.netlist['n26'] = net.net('n26', pullup_str=100,   parent=self)
        self.netlist['n260'] = net.net('n260',  charge_storage=True,  parent=self)
        self.netlist['n261'] = net.net('n261',  charge_storage=True,  parent=self)
        self.netlist['n262'] = net.net('n262',  charge_storage=True,  parent=self)
        self.netlist['n263'] = net.net('n263',  charge_storage=True,  parent=self)
        self.netlist['n264'] = net.net('n264',  charge_storage=True,  parent=self)
        self.netlist['n2675'] = net.net('n2675',  charge_storage=True,  parent=self)
        self.netlist['n2676'] = net.net('n2676',  charge_storage=True,  parent=self)
        self.netlist['n2677'] = net.net('n2677',  charge_storage=True,  parent=self)
        self.netlist['n2678'] = net.net('n2678',  charge_storage=True,  parent=self)
        self.netlist['n2679'] = net.net('n2679',  charge_storage=True,  parent=self)
        self.netlist['n268'] = net.net('n268', pullup_str=100,   parent=self)
        self.netlist['n2680'] = net.net('n2680',  charge_storage=True,  parent=self)
        self.netlist['n2681'] = net.net('n2681',  charge_storage=True,  parent=self)
        self.netlist['n2682'] = net.net('n2682',  charge_storage=True,  parent=self)
        self.netlist['n2683'] = net.net('n2683',  charge_storage=True,  parent=self)
        self.netlist['n2684'] = net.net('n2684',  charge_storage=True,  parent=self)
        self.netlist['n2685'] = net.net('n2685',  charge_storage=True,  parent=self)
        self.netlist['n2686'] = net.net('n2686',  charge_storage=True,  parent=self)
        self.netlist['n2687'] = net.net('n2687',  charge_storage=True,  parent=self)
        self.netlist['n2688'] = net.net('n2688',  charge_storage=True,  parent=self)
        self.netlist['n2689'] = net.net('n2689',  charge_storage=True,  parent=self)
        self.netlist['n269'] = net.net('n269', pullup_str=100,   parent=self)
        self.netlist['n2690'] = net.net('n2690',  charge_storage=True,  parent=self)
        self.netlist['n2691'] = net.net('n2691',  charge_storage=True,  parent=self)
        self.netlist['n2692'] = net.net('n2692',  charge_storage=True,  parent=self)
        self.netlist['n2693'] = net.net('n2693',  charge_storage=True,  parent=self)
        self.netlist['n2694'] = net.net('n2694',  charge_storage=True,  parent=self)
        self.netlist['n2695'] = net.net('n2695',  charge_storage=True,  parent=self)
        self.netlist['n2696'] = net.net('n2696',  charge_storage=True,  parent=self)
        self.netlist['n2697'] = net.net('n2697',  charge_storage=True,  parent=self)
        self.netlist['n2698'] = net.net('n2698',  charge_storage=True,  parent=self)
        self.netlist['n2699'] = net.net('n2699',  charge_storage=True,  parent=self)
        self.netlist['n270'] = net.net('n270', pullup_str=100,   parent=self)
        self.netlist['n2700'] = net.net('n2700',  charge_storage=True,  parent=self)
        self.netlist['n2701'] = net.net('n2701',  charge_storage=True,  parent=self)
        self.netlist['n2702'] = net.net('n2702',  charge_storage=True,  parent=self)
        self.netlist['n2703'] = net.net('n2703',  charge_storage=True,  parent=self)
        self.netlist['n2704'] = net.net('n2704',  charge_storage=True,  parent=self)
        self.netlist['n2705'] = net.net('n2705',  charge_storage=True,  parent=self)
        self.netlist['n2706'] = net.net('n2706',  charge_storage=True,  parent=self)
        self.netlist['n2707'] = net.net('n2707',  charge_storage=True,  parent=self)
        self.netlist['n2708'] = net.net('n2708',  charge_storage=True,  parent=self)
        self.netlist['n2709'] = net.net('n2709',  charge_storage=True,  parent=self)
        self.netlist['n271'] = net.net('n271', pullup_str=100,   parent=self)
        self.netlist['n2710'] = net.net('n2710',  charge_storage=True,  parent=self)
        self.netlist['n2711'] = net.net('n2711',  charge_storage=True,  parent=self)
        self.netlist['n2712'] = net.net('n2712',  charge_storage=True,  parent=self)
        self.netlist['n2713'] = net.net('n2713',  charge_storage=True,  parent=self)
        self.netlist['n2714'] = net.net('n2714',  charge_storage=True,  parent=self)
        self.netlist['n2715'] = net.net('n2715',  charge_storage=True,  parent=self)
        self.netlist['n2716'] = net.net('n2716',  charge_storage=True,  parent=self)
        self.netlist['n2717'] = net.net('n2717',  charge_storage=True,  parent=self)
        self.netlist['n2718'] = net.net('n2718',  charge_storage=True,  parent=self)
        self.netlist['n2719'] = net.net('n2719',  charge_storage=True,  parent=self)
        self.netlist['n272'] = net.net('n272', pullup_str=100,   parent=self)
        self.netlist['n2720'] = net.net('n2720',  charge_storage=True,  parent=self)
        self.netlist['n2721'] = net.net('n2721',  charge_storage=True,  parent=self)
        self.netlist['n2722'] = net.net('n2722',  charge_storage=True,  parent=self)
        self.netlist['n2723'] = net.net('n2723',  charge_storage=True,  parent=self)
        self.netlist['n2724'] = net.net('n2724',  charge_storage=True,  parent=self)
        self.netlist['n2725'] = net.net('n2725',  charge_storage=True,  parent=self)
        self.netlist['n2726'] = net.net('n2726',  charge_storage=True,  parent=self)
        self.netlist['n2727'] = net.net('n2727',  charge_storage=True,  parent=self)
        self.netlist['n2728'] = net.net('n2728',  charge_storage=True,  parent=self)
        self.netlist['n2729'] = net.net('n2729',  charge_storage=True,  parent=self)
        self.netlist['n273'] = net.net('n273',  charge_storage=True,  parent=self)
        self.netlist['n2730'] = net.net('n2730',  charge_storage=True,  parent=self)
        self.netlist['n2731'] = net.net('n2731',  charge_storage=True,  parent=self)
        self.netlist['n2732'] = net.net('n2732',  charge_storage=True,  parent=self)
        self.netlist['n2733'] = net.net('n2733',  charge_storage=True,  parent=self)
        self.netlist['n2734'] = net.net('n2734',  charge_storage=True,  parent=self)
        self.netlist['n2735'] = net.net('n2735',  charge_storage=True,  parent=self)
        self.netlist['n2736'] = net.net('n2736',  charge_storage=True,  parent=self)
        self.netlist['n2737'] = net.net('n2737',  charge_storage=True,  parent=self)
        self.netlist['n2738'] = net.net('n2738',  charge_storage=True,  parent=self)
        self.netlist['n2739'] = net.net('n2739',  charge_storage=True,  parent=self)
        self.netlist['n274'] = net.net('n274',  charge_storage=True,  parent=self)
        self.netlist['n2740'] = net.net('n2740',  charge_storage=True,  parent=self)
        self.netlist['n2741'] = net.net('n2741',  charge_storage=True,  parent=self)
        self.netlist['n2742'] = net.net('n2742',  charge_storage=True,  parent=self)
        self.netlist['n2743'] = net.net('n2743',  charge_storage=True,  parent=self)
        self.netlist['n2744'] = net.net('n2744',  charge_storage=True,  parent=self)
        self.netlist['n2745'] = net.net('n2745',  charge_storage=True,  parent=self)
        self.netlist['n2746'] = net.net('n2746',  charge_storage=True,  parent=self)
        self.netlist['n2747'] = net.net('n2747',  charge_storage=True,  parent=self)
        self.netlist['n2748'] = net.net('n2748',  charge_storage=True,  parent=self)
        self.netlist['n2749'] = net.net('n2749',  charge_storage=True,  parent=self)
        self.netlist['n275'] = net.net('n275', pullup_str=100,   parent=self)
        self.netlist['n2750'] = net.net('n2750',  charge_storage=True,  parent=self)
        self.netlist['n2751'] = net.net('n2751',  charge_storage=True,  parent=self)
        self.netlist['n2752'] = net.net('n2752',  charge_storage=True,  parent=self)
        self.netlist['n2753'] = net.net('n2753',  charge_storage=True,  parent=self)
        self.netlist['n2754'] = net.net('n2754',  charge_storage=True,  parent=self)
        self.netlist['n2755'] = net.net('n2755',  charge_storage=True,  parent=self)
        self.netlist['n2756'] = net.net('n2756',  charge_storage=True,  parent=self)
        self.netlist['n2757'] = net.net('n2757',  charge_storage=True,  parent=self)
        self.netlist['n2758'] = net.net('n2758',  charge_storage=True,  parent=self)
        self.netlist['n2759'] = net.net('n2759',  charge_storage=True,  parent=self)
        self.netlist['n276'] = net.net('n276', pullup_str=100,   parent=self)
        self.netlist['n2760'] = net.net('n2760',  charge_storage=True,  parent=self)
        self.netlist['n2761'] = net.net('n2761',  charge_storage=True,  parent=self)
        self.netlist['n2762'] = net.net('n2762',  charge_storage=True,  parent=self)
        self.netlist['n2763'] = net.net('n2763',  charge_storage=True,  parent=self)
        self.netlist['n2764'] = net.net('n2764',  charge_storage=True,  parent=self)
        self.netlist['n2765'] = net.net('n2765',  charge_storage=True,  parent=self)
        self.netlist['n2766'] = net.net('n2766',  charge_storage=True,  parent=self)
        self.netlist['n2767'] = net.net('n2767',  charge_storage=True,  parent=self)
        self.netlist['n2768'] = net.net('n2768',  charge_storage=True,  parent=self)
        self.netlist['n2769'] = net.net('n2769',  charge_storage=True,  parent=self)
        self.netlist['n277'] = net.net('n277', pullup_str=100,   parent=self)
        self.netlist['n2770'] = net.net('n2770',  charge_storage=True,  parent=self)
        self.netlist['n2771'] = net.net('n2771',  charge_storage=True,  parent=self)
        self.netlist['n2772'] = net.net('n2772',  charge_storage=True,  parent=self)
        self.netlist['n2773'] = net.net('n2773',  charge_storage=True,  parent=self)
        self.netlist['n2774'] = net.net('n2774',  charge_storage=True,  parent=self)
        self.netlist['n2775'] = net.net('n2775',  charge_storage=True,  parent=self)
        self.netlist['n2776'] = net.net('n2776',  charge_storage=True,  parent=self)
        self.netlist['n2777'] = net.net('n2777',  charge_storage=True,  parent=self)
        self.netlist['n2778'] = net.net('n2778',  charge_storage=True,  parent=self)
        self.netlist['n2779'] = net.net('n2779',  charge_storage=True,  parent=self)
        self.netlist['n2780'] = net.net('n2780',  charge_storage=True,  parent=self)
        self.netlist['n2781'] = net.net('n2781',  charge_storage=True,  parent=self)
        self.netlist['n2782'] = net.net('n2782',  charge_storage=True,  parent=self)
        self.netlist['n2783'] = net.net('n2783',  charge_storage=True,  parent=self)
        self.netlist['n2784'] = net.net('n2784',  charge_storage=True,  parent=self)
        self.netlist['n2785'] = net.net('n2785',  charge_storage=True,  parent=self)
        self.netlist['n2786'] = net.net('n2786',  charge_storage=True,  parent=self)
        self.netlist['n2787'] = net.net('n2787',  charge_storage=True,  parent=self)
        self.netlist['n2788'] = net.net('n2788',  charge_storage=True,  parent=self)
        self.netlist['n2789'] = net.net('n2789',  charge_storage=True,  parent=self)
        self.netlist['n2790'] = net.net('n2790',  charge_storage=True,  parent=self)
        self.netlist['n2791'] = net.net('n2791',  charge_storage=True,  parent=self)
        self.netlist['n2792'] = net.net('n2792',  charge_storage=True,  parent=self)
        self.netlist['n2793'] = net.net('n2793',  charge_storage=True,  parent=self)
        self.netlist['n2794'] = net.net('n2794',  charge_storage=True,  parent=self)
        self.netlist['n2795'] = net.net('n2795',  charge_storage=True,  parent=self)
        self.netlist['n2796'] = net.net('n2796',  charge_storage=True,  parent=self)
        self.netlist['n2797'] = net.net('n2797',  charge_storage=True,  parent=self)
        self.netlist['n2798'] = net.net('n2798',  charge_storage=True,  parent=self)
        self.netlist['n2799'] = net.net('n2799',  charge_storage=True,  parent=self)
        self.netlist['n2800'] = net.net('n2800',  charge_storage=True,  parent=self)
        self.netlist['n2801'] = net.net('n2801',  charge_storage=True,  parent=self)
        self.netlist['n2802'] = net.net('n2802',  charge_storage=True,  parent=self)
        self.netlist['n2803'] = net.net('n2803',  charge_storage=True,  parent=self)
        self.netlist['n2804'] = net.net('n2804',  charge_storage=True,  parent=self)
        self.netlist['n2805'] = net.net('n2805',  charge_storage=True,  parent=self)
        self.netlist['n2806'] = net.net('n2806',  charge_storage=True,  parent=self)
        self.netlist['n2807'] = net.net('n2807',  charge_storage=True,  parent=self)
        self.netlist['n2808'] = net.net('n2808',  charge_storage=True,  parent=self)
        self.netlist['n2809'] = net.net('n2809',  charge_storage=True,  parent=self)
        self.netlist['n2810'] = net.net('n2810',  charge_storage=True,  parent=self)
        self.netlist['n2811'] = net.net('n2811',  charge_storage=True,  parent=self)
        self.netlist['n2812'] = net.net('n2812',  charge_storage=True,  parent=self)
        self.netlist['n2813'] = net.net('n2813',  charge_storage=True,  parent=self)
        self.netlist['n2814'] = net.net('n2814',  charge_storage=True,  parent=self)
        self.netlist['n2815'] = net.net('n2815',  charge_storage=True,  parent=self)
        self.netlist['n2816'] = net.net('n2816',  charge_storage=True,  parent=self)
        self.netlist['n2817'] = net.net('n2817',  charge_storage=True,  parent=self)
        self.netlist['n2818'] = net.net('n2818',  charge_storage=True,  parent=self)
        self.netlist['n2819'] = net.net('n2819',  charge_storage=True,  parent=self)
        self.netlist['n2820'] = net.net('n2820',  charge_storage=True,  parent=self)
        self.netlist['n2821'] = net.net('n2821',  charge_storage=True,  parent=self)
        self.netlist['n2822'] = net.net('n2822',  charge_storage=True,  parent=self)
        self.netlist['n2823'] = net.net('n2823',  charge_storage=True,  parent=self)
        self.netlist['n2824'] = net.net('n2824',  charge_storage=True,  parent=self)
        self.netlist['n2825'] = net.net('n2825',  charge_storage=True,  parent=self)
        self.netlist['n2826'] = net.net('n2826',  charge_storage=True,  parent=self)
        self.netlist['n2827'] = net.net('n2827',  charge_storage=True,  parent=self)
        self.netlist['n2828'] = net.net('n2828',  charge_storage=True,  parent=self)
        self.netlist['n2829'] = net.net('n2829',  charge_storage=True,  parent=self)
        self.netlist['n2830'] = net.net('n2830',  charge_storage=True,  parent=self)
        self.netlist['n2831'] = net.net('n2831',  charge_storage=True,  parent=self)
        self.netlist['n2832'] = net.net('n2832',  charge_storage=True,  parent=self)
        self.netlist['n2833'] = net.net('n2833',  charge_storage=True,  parent=self)
        self.netlist['n2834'] = net.net('n2834',  charge_storage=True,  parent=self)
        self.netlist['n2835'] = net.net('n2835',  charge_storage=True,  parent=self)
        self.netlist['n2836'] = net.net('n2836',  charge_storage=True,  parent=self)
        self.netlist['n2837'] = net.net('n2837',  charge_storage=True,  parent=self)
        self.netlist['n2838'] = net.net('n2838',  charge_storage=True,  parent=self)
        self.netlist['n2839'] = net.net('n2839',  charge_storage=True,  parent=self)
        self.netlist['n2840'] = net.net('n2840',  charge_storage=True,  parent=self)
        self.netlist['n2841'] = net.net('n2841',  charge_storage=True,  parent=self)
        self.netlist['n2842'] = net.net('n2842',  charge_storage=True,  parent=self)
        self.netlist['n2843'] = net.net('n2843',  charge_storage=True,  parent=self)
        self.netlist['n2844'] = net.net('n2844',  charge_storage=True,  parent=self)
        self.netlist['n2845'] = net.net('n2845',  charge_storage=True,  parent=self)
        self.netlist['n2846'] = net.net('n2846',  charge_storage=True,  parent=self)
        self.netlist['n2847'] = net.net('n2847',  charge_storage=True,  parent=self)
        self.netlist['n2848'] = net.net('n2848',  charge_storage=True,  parent=self)
        self.netlist['n2849'] = net.net('n2849',  charge_storage=True,  parent=self)
        self.netlist['n285'] = net.net('n285', pullup_str=100,   parent=self)
        self.netlist['n2850'] = net.net('n2850',  charge_storage=True,  parent=self)
        self.netlist['n2851'] = net.net('n2851',  charge_storage=True,  parent=self)
        self.netlist['n2852'] = net.net('n2852',  charge_storage=True,  parent=self)
        self.netlist['n2853'] = net.net('n2853',  charge_storage=True,  parent=self)
        self.netlist['n2854'] = net.net('n2854',  charge_storage=True,  parent=self)
        self.netlist['n2855'] = net.net('n2855',  charge_storage=True,  parent=self)
        self.netlist['n2856'] = net.net('n2856',  charge_storage=True,  parent=self)
        self.netlist['n2857'] = net.net('n2857',  charge_storage=True,  parent=self)
        self.netlist['n2858'] = net.net('n2858',  charge_storage=True,  parent=self)
        self.netlist['n2859'] = net.net('n2859',  charge_storage=True,  parent=self)
        self.netlist['n286'] = net.net('n286', pullup_str=100,   parent=self)
        self.netlist['n2860'] = net.net('n2860',  charge_storage=True,  parent=self)
        self.netlist['n2861'] = net.net('n2861',  charge_storage=True,  parent=self)
        self.netlist['n2862'] = net.net('n2862',  charge_storage=True,  parent=self)
        self.netlist['n2863'] = net.net('n2863',  charge_storage=True,  parent=self)
        self.netlist['n2864'] = net.net('n2864',  charge_storage=True,  parent=self)
        self.netlist['n2865'] = net.net('n2865',  charge_storage=True,  parent=self)
        self.netlist['n2866'] = net.net('n2866',  charge_storage=True,  parent=self)
        self.netlist['n2867'] = net.net('n2867',  charge_storage=True,  parent=self)
        self.netlist['n2868'] = net.net('n2868',  charge_storage=True,  parent=self)
        self.netlist['n2869'] = net.net('n2869',  charge_storage=True,  parent=self)
        self.netlist['n287'] = net.net('n287', pullup_str=100,   parent=self)
        self.netlist['n2870'] = net.net('n2870',  charge_storage=True,  parent=self)
        self.netlist['n2871'] = net.net('n2871',  charge_storage=True,  parent=self)
        self.netlist['n2872'] = net.net('n2872',  charge_storage=True,  parent=self)
        self.netlist['n2873'] = net.net('n2873',  charge_storage=True,  parent=self)
        self.netlist['n2874'] = net.net('n2874',  charge_storage=True,  parent=self)
        self.netlist['n2875'] = net.net('n2875',  charge_storage=True,  parent=self)
        self.netlist['n2876'] = net.net('n2876',  charge_storage=True,  parent=self)
        self.netlist['n2877'] = net.net('n2877',  charge_storage=True,  parent=self)
        self.netlist['n2878'] = net.net('n2878',  charge_storage=True,  parent=self)
        self.netlist['n2879'] = net.net('n2879',  charge_storage=True,  parent=self)
        self.netlist['n2880'] = net.net('n2880',  charge_storage=True,  parent=self)
        self.netlist['n2881'] = net.net('n2881',  charge_storage=True,  parent=self)
        self.netlist['n2882'] = net.net('n2882',  charge_storage=True,  parent=self)
        self.netlist['n2883'] = net.net('n2883',  charge_storage=True,  parent=self)
        self.netlist['n2884'] = net.net('n2884',  charge_storage=True,  parent=self)
        self.netlist['n2885'] = net.net('n2885',  charge_storage=True,  parent=self)
        self.netlist['n2886'] = net.net('n2886',  charge_storage=True,  parent=self)
        self.netlist['n2887'] = net.net('n2887',  charge_storage=True,  parent=self)
        self.netlist['n2888'] = net.net('n2888',  charge_storage=True,  parent=self)
        self.netlist['n2889'] = net.net('n2889',  charge_storage=True,  parent=self)
        self.netlist['n2890'] = net.net('n2890',  charge_storage=True,  parent=self)
        self.netlist['n2891'] = net.net('n2891',  charge_storage=True,  parent=self)
        self.netlist['n2892'] = net.net('n2892',  charge_storage=True,  parent=self)
        self.netlist['n2893'] = net.net('n2893',  charge_storage=True,  parent=self)
        self.netlist['n2894'] = net.net('n2894',  charge_storage=True,  parent=self)
        self.netlist['n2895'] = net.net('n2895',  charge_storage=True,  parent=self)
        self.netlist['n2896'] = net.net('n2896',  charge_storage=True,  parent=self)
        self.netlist['n2897'] = net.net('n2897',  charge_storage=True,  parent=self)
        self.netlist['n2898'] = net.net('n2898',  charge_storage=True,  parent=self)
        self.netlist['n2899'] = net.net('n2899',  charge_storage=True,  parent=self)
        self.netlist['n2900'] = net.net('n2900',  charge_storage=True,  parent=self)
        self.netlist['n2901'] = net.net('n2901',  charge_storage=True,  parent=self)
        self.netlist['n2902'] = net.net('n2902',  charge_storage=True,  parent=self)
        self.netlist['n2903'] = net.net('n2903',  charge_storage=True,  parent=self)
        self.netlist['n2904'] = net.net('n2904',  charge_storage=True,  parent=self)
        self.netlist['n2905'] = net.net('n2905',  charge_storage=True,  parent=self)
        self.netlist['n2906'] = net.net('n2906',  charge_storage=True,  parent=self)
        self.netlist['n2907'] = net.net('n2907',  charge_storage=True,  parent=self)
        self.netlist['n2908'] = net.net('n2908',  charge_storage=True,  parent=self)
        self.netlist['n2909'] = net.net('n2909',  charge_storage=True,  parent=self)
        self.netlist['n2910'] = net.net('n2910',  charge_storage=True,  parent=self)
        self.netlist['n2911'] = net.net('n2911',  charge_storage=True,  parent=self)
        self.netlist['n2912'] = net.net('n2912',  charge_storage=True,  parent=self)
        self.netlist['n2913'] = net.net('n2913',  charge_storage=True,  parent=self)
        self.netlist['n2914'] = net.net('n2914',  charge_storage=True,  parent=self)
        self.netlist['n2915'] = net.net('n2915',  charge_storage=True,  parent=self)
        self.netlist['n2916'] = net.net('n2916',  charge_storage=True,  parent=self)
        self.netlist['n2917'] = net.net('n2917',  charge_storage=True,  parent=self)
        self.netlist['n2918'] = net.net('n2918',  charge_storage=True,  parent=self)
        self.netlist['n2919'] = net.net('n2919',  charge_storage=True,  parent=self)
        self.netlist['n2920'] = net.net('n2920',  charge_storage=True,  parent=self)
        self.netlist['n2921'] = net.net('n2921',  charge_storage=True,  parent=self)
        self.netlist['n2922'] = net.net('n2922',  charge_storage=True,  parent=self)
        self.netlist['n2923'] = net.net('n2923',  charge_storage=True,  parent=self)
        self.netlist['n2924'] = net.net('n2924',  charge_storage=True,  parent=self)
        self.netlist['n2925'] = net.net('n2925',  charge_storage=True,  parent=self)
        self.netlist['n2926'] = net.net('n2926',  charge_storage=True,  parent=self)
        self.netlist['n2927'] = net.net('n2927',  charge_storage=True,  parent=self)
        self.netlist['n2928'] = net.net('n2928',  charge_storage=True,  parent=self)
        self.netlist['n2929'] = net.net('n2929',  charge_storage=True,  parent=self)
        self.netlist['n2930'] = net.net('n2930',  charge_storage=True,  parent=self)
        self.netlist['n2931'] = net.net('n2931',  charge_storage=True,  parent=self)
        self.netlist['n2932'] = net.net('n2932',  charge_storage=True,  parent=self)
        self.netlist['n2933'] = net.net('n2933',  charge_storage=True,  parent=self)
        self.netlist['n2934'] = net.net('n2934',  charge_storage=True,  parent=self)
        self.netlist['n2935'] = net.net('n2935',  charge_storage=True,  parent=self)
        self.netlist['n2936'] = net.net('n2936',  charge_storage=True,  parent=self)
        self.netlist['n2937'] = net.net('n2937',  charge_storage=True,  parent=self)
        self.netlist['n2938'] = net.net('n2938',  charge_storage=True,  parent=self)
        self.netlist['n2939'] = net.net('n2939',  charge_storage=True,  parent=self)
        self.netlist['n2940'] = net.net('n2940',  charge_storage=True,  parent=self)
        self.netlist['n2941'] = net.net('n2941',  charge_storage=True,  parent=self)
        self.netlist['n2942'] = net.net('n2942',  charge_storage=True,  parent=self)
        self.netlist['n2943'] = net.net('n2943',  charge_storage=True,  parent=self)
        self.netlist['n3'] = net.net('n3', pullup_str=100,   parent=self)
        self.netlist['n308'] = net.net('n308', pullup_str=100,   parent=self)
        self.netlist['n309'] = net.net('n309', pullup_str=100,   parent=self)
        self.netlist['n314'] = net.net('n314', pullup_str=100,   parent=self)
        self.netlist['n315'] = net.net('n315', pullup_str=100,   parent=self)
        self.netlist['n316'] = net.net('n316', pullup_str=100,   parent=self)
        self.netlist['n317'] = net.net('n317', pullup_str=100,   parent=self)
        self.netlist['n318'] = net.net('n318', pullup_str=100,   parent=self)
        self.netlist['n319'] = net.net('n319', pullup_str=100,   parent=self)
        self.netlist['n320'] = net.net('n320', pullup_str=100,   parent=self)
        self.netlist['n321'] = net.net('n321', pullup_str=100,   parent=self)
        self.netlist['n322'] = net.net('n322', pullup_str=100,   parent=self)
        self.netlist['n323'] = net.net('n323', pullup_str=100,   parent=self)
        self.netlist['n324'] = net.net('n324', pullup_str=100,   parent=self)
        self.netlist['n325'] = net.net('n325', pullup_str=100,   parent=self)
        self.netlist['n326'] = net.net('n326', pullup_str=100,   parent=self)
        self.netlist['n327'] = net.net('n327', pullup_str=100,   parent=self)
        self.netlist['n328'] = net.net('n328', pullup_str=100,   parent=self)
        self.netlist['n329'] = net.net('n329', pullup_str=100,   parent=self)
        self.netlist['n36'] = net.net('n36', pullup_str=100,   parent=self)
        self.netlist['n37'] = net.net('n37', pullup_str=100,   parent=self)
        self.netlist['n374'] = net.net('n374', pullup_str=100,   parent=self)
        self.netlist['n375'] = net.net('n375', pullup_str=100,   parent=self)
        self.netlist['n376'] = net.net('n376', pullup_str=100,   parent=self)
        self.netlist['n379'] = net.net('n379', pullup_str=100,   parent=self)
        self.netlist['n38'] = net.net('n38', pullup_str=100,   parent=self)
        self.netlist['n380'] = net.net('n380', pullup_str=100,   parent=self)
        self.netlist['n381'] = net.net('n381', pullup_str=100,   parent=self)
        self.netlist['n382'] = net.net('n382', pullup_str=100,   parent=self)
        self.netlist['n383'] = net.net('n383', pullup_str=100,   parent=self)
        self.netlist['n384'] = net.net('n384', pullup_str=100,   parent=self)
        self.netlist['n385'] = net.net('n385', pullup_str=100,   parent=self)
        self.netlist['n388'] = net.net('n388', pullup_str=100,   parent=self)
        self.netlist['n39'] = net.net('n39', pullup_str=100,   parent=self)
        self.netlist['n391'] = net.net('n391',  charge_storage=True,  parent=self)
        self.netlist['n392'] = net.net('n392', pullup_str=100,   parent=self)
        self.netlist['n394'] = net.net('n394', pullup_str=100,   parent=self)
        self.netlist['n396'] = net.net('n396', pullup_str=100,   parent=self)
        self.netlist['n398'] = net.net('n398',  charge_storage=True,  parent=self)
        self.netlist['n399'] = net.net('n399', pullup_str=100,   parent=self)
        self.netlist['n4'] = net.net('n4', pullup_str=100,   parent=self)
        self.netlist['n40'] = net.net('n40', pullup_str=100,   parent=self)
        self.netlist['n401'] = net.net('n401', pullup_str=100,   parent=self)
        self.netlist['n403'] = net.net('n403',  charge_storage=True,  parent=self)
        self.netlist['n404'] = net.net('n404', pullup_str=100,   parent=self)
        self.netlist['n407'] = net.net('n407',  charge_storage=True,  parent=self)
        self.netlist['n408'] = net.net('n408', pullup_str=100,   parent=self)
        self.netlist['n41'] = net.net('n41', pullup_str=100,   parent=self)
        self.netlist['n411'] = net.net('n411', pullup_str=100,   parent=self)
        self.netlist['n413'] = net.net('n413', pullup_str=100,   parent=self)
        self.netlist['n414'] = net.net('n414', pullup_str=100,   parent=self)
        self.netlist['n415'] = net.net('n415', pullup_str=100,   parent=self)
        self.netlist['n416'] = net.net('n416', pullup_str=100,   parent=self)
        self.netlist['n417'] = net.net('n417', pullup_str=100,   parent=self)
        self.netlist['n418'] = net.net('n418', pullup_str=100,   parent=self)
        self.netlist['n419'] = net.net('n419',  charge_storage=True,  parent=self)
        self.netlist['n42'] = net.net('n42', pullup_str=100,   parent=self)
        self.netlist['n420'] = net.net('n420',  charge_storage=True,  parent=self)
        self.netlist['n421'] = net.net('n421', pullup_str=100,   parent=self)
        self.netlist['n422'] = net.net('n422',  charge_storage=True,  parent=self)
        self.netlist['n423'] = net.net('n423',  charge_storage=True,  parent=self)
        self.netlist['n424'] = net.net('n424', pullup_str=100,   parent=self)
        self.netlist['n425'] = net.net('n425',  charge_storage=True,  parent=self)
        self.netlist['n426'] = net.net('n426', pullup_str=100,   parent=self)
        self.netlist['n427'] = net.net('n427',  charge_storage=True,  parent=self)
        self.netlist['n428'] = net.net('n428', pullup_str=100,   parent=self)
        self.netlist['n429'] = net.net('n429',  charge_storage=True,  parent=self)
        self.netlist['n43'] = net.net('n43', pullup_str=100,   parent=self)
        self.netlist['n430'] = net.net('n430', pullup_str=100,   parent=self)
        self.netlist['n431'] = net.net('n431',  charge_storage=True,  parent=self)
        self.netlist['n432'] = net.net('n432', pullup_str=100,   parent=self)
        self.netlist['n433'] = net.net('n433',  charge_storage=True,  parent=self)
        self.netlist['n434'] = net.net('n434', pullup_str=100,   parent=self)
        self.netlist['n435'] = net.net('n435',  charge_storage=True,  parent=self)
        self.netlist['n436'] = net.net('n436', pullup_str=100,   parent=self)
        self.netlist['n437'] = net.net('n437',  charge_storage=True,  parent=self)
        self.netlist['n438'] = net.net('n438', pullup_str=100,   parent=self)
        self.netlist['n439'] = net.net('n439',  charge_storage=True,  parent=self)
        self.netlist['n44'] = net.net('n44', pullup_str=100,   parent=self)
        self.netlist['n440'] = net.net('n440',  charge_storage=True,  parent=self)
        self.netlist['n441'] = net.net('n441',  charge_storage=True,  parent=self)
        self.netlist['n442'] = net.net('n442',  charge_storage=True,  parent=self)
        self.netlist['n443'] = net.net('n443', pullup_str=100,   parent=self)
        self.netlist['n444'] = net.net('n444',  charge_storage=True,  parent=self)
        self.netlist['n445'] = net.net('n445', pullup_str=100,   parent=self)
        self.netlist['n446'] = net.net('n446',  charge_storage=True,  parent=self)
        self.netlist['n447'] = net.net('n447',  charge_storage=True,  parent=self)
        self.netlist['n448'] = net.net('n448', pullup_str=100,   parent=self)
        self.netlist['n449'] = net.net('n449',  charge_storage=True,  parent=self)
        self.netlist['n45'] = net.net('n45', pullup_str=100,   parent=self)
        self.netlist['n450'] = net.net('n450', pullup_str=100,   parent=self)
        self.netlist['n451'] = net.net('n451',  charge_storage=True,  parent=self)
        self.netlist['n452'] = net.net('n452', pullup_str=100,   parent=self)
        self.netlist['n453'] = net.net('n453',  charge_storage=True,  parent=self)
        self.netlist['n454'] = net.net('n454', pullup_str=100,   parent=self)
        self.netlist['n455'] = net.net('n455',  charge_storage=True,  parent=self)
        self.netlist['n456'] = net.net('n456', pullup_str=100,   parent=self)
        self.netlist['n457'] = net.net('n457',  charge_storage=True,  parent=self)
        self.netlist['n458'] = net.net('n458', pullup_str=100,   parent=self)
        self.netlist['n459'] = net.net('n459',  charge_storage=True,  parent=self)
        self.netlist['n46'] = net.net('n46', pullup_str=100,   parent=self)
        self.netlist['n460'] = net.net('n460', pullup_str=100,   parent=self)
        self.netlist['n461'] = net.net('n461',  charge_storage=True,  parent=self)
        self.netlist['n462'] = net.net('n462', pullup_str=100,   parent=self)
        self.netlist['n463'] = net.net('n463',  charge_storage=True,  parent=self)
        self.netlist['n464'] = net.net('n464', pullup_str=100,   parent=self)
        self.netlist['n465'] = net.net('n465',  charge_storage=True,  parent=self)
        self.netlist['n466'] = net.net('n466', pullup_str=100,   parent=self)
        self.netlist['n467'] = net.net('n467',  charge_storage=True,  parent=self)
        self.netlist['n468'] = net.net('n468', pullup_str=100,   parent=self)
        self.netlist['n469'] = net.net('n469',  charge_storage=True,  parent=self)
        self.netlist['n47'] = net.net('n47', pullup_str=100,   parent=self)
        self.netlist['n470'] = net.net('n470',  charge_storage=True,  parent=self)
        self.netlist['n471'] = net.net('n471', pullup_str=100,   parent=self)
        self.netlist['n472'] = net.net('n472', pullup_str=100,   parent=self)
        self.netlist['n473'] = net.net('n473', pullup_str=100,   parent=self)
        self.netlist['n474'] = net.net('n474', pullup_str=100,   parent=self)
        self.netlist['n475'] = net.net('n475', pullup_str=100,   parent=self)
        self.netlist['n476'] = net.net('n476', pullup_str=100,   parent=self)
        self.netlist['n477'] = net.net('n477', pullup_str=100,   parent=self)
        self.netlist['n479'] = net.net('n479', pullup_str=100,   parent=self)
        self.netlist['n48'] = net.net('n48', pullup_str=100,   parent=self)
        self.netlist['n480'] = net.net('n480',  charge_storage=True,  parent=self)
        self.netlist['n481'] = net.net('n481',  charge_storage=True,  parent=self)
        self.netlist['n482'] = net.net('n482',  charge_storage=True,  parent=self)
        self.netlist['n483'] = net.net('n483', pullup_str=100,   parent=self)
        self.netlist['n484'] = net.net('n484',  charge_storage=True,  parent=self)
        self.netlist['n485'] = net.net('n485',  charge_storage=True,  parent=self)
        self.netlist['n486'] = net.net('n486', pullup_str=100,   parent=self)
        self.netlist['n49'] = net.net('n49', pullup_str=100,   parent=self)
        self.netlist['n492'] = net.net('n492',  charge_storage=True,  parent=self)
        self.netlist['n493'] = net.net('n493',  charge_storage=True,  parent=self)
        self.netlist['n494'] = net.net('n494', pullup_str=100,   parent=self)
        self.netlist['n495'] = net.net('n495', pullup_str=100,   parent=self)
        self.netlist['n496'] = net.net('n496', pullup_str=100,   parent=self)
        self.netlist['n497'] = net.net('n497', pullup_str=100,   parent=self)
        self.netlist['n498'] = net.net('n498', pullup_str=100,   parent=self)
        self.netlist['n499'] = net.net('n499', pullup_str=100,   parent=self)
        self.netlist['n5'] = net.net('n5', pullup_str=100,   parent=self)
        self.netlist['n50'] = net.net('n50', pullup_str=100,   parent=self)
        self.netlist['n500'] = net.net('n500', pullup_str=100,   parent=self)
        self.netlist['n501'] = net.net('n501', pullup_str=100,   parent=self)
        self.netlist['n502'] = net.net('n502',  charge_storage=True,  parent=self)
        self.netlist['n503'] = net.net('n503',  charge_storage=True,  parent=self)
        self.netlist['n504'] = net.net('n504',  charge_storage=True,  parent=self)
        self.netlist['n505'] = net.net('n505',  charge_storage=True,  parent=self)
        self.netlist['n506'] = net.net('n506', pullup_str=100,   parent=self)
        self.netlist['n507'] = net.net('n507', pullup_str=100,   parent=self)
        self.netlist['n510'] = net.net('n510', pullup_str=100,   parent=self)
        self.netlist['n511'] = net.net('n511', pullup_str=100,   parent=self)
        self.netlist['n514'] = net.net('n514', pullup_str=100,   parent=self)
        self.netlist['n515'] = net.net('n515', pullup_str=100,   parent=self)
        self.netlist['n518'] = net.net('n518', pullup_str=100,   parent=self)
        self.netlist['n519'] = net.net('n519', pullup_str=100,   parent=self)
        self.netlist['n522'] = net.net('n522',  charge_storage=True,  parent=self)
        self.netlist['n523'] = net.net('n523',  charge_storage=True,  parent=self)
        self.netlist['n524'] = net.net('n524',  charge_storage=True,  parent=self)
        self.netlist['n525'] = net.net('n525', pullup_str=100,   parent=self)
        self.netlist['n526'] = net.net('n526',  charge_storage=True,  parent=self)
        self.netlist['n527'] = net.net('n527', pullup_str=100,   parent=self)
        self.netlist['n528'] = net.net('n528', pullup_str=100,   parent=self)
        self.netlist['n529'] = net.net('n529',  charge_storage=True,  parent=self)
        self.netlist['n530'] = net.net('n530',  charge_storage=True,  parent=self)
        self.netlist['n531'] = net.net('n531', pullup_str=100,   parent=self)
        self.netlist['n532'] = net.net('n532', pullup_str=100,   parent=self)
        self.netlist['n533'] = net.net('n533', pullup_str=100,   parent=self)
        self.netlist['n534'] = net.net('n534',  charge_storage=True,  parent=self)
        self.netlist['n535'] = net.net('n535', pullup_str=100,   parent=self)
        self.netlist['n536'] = net.net('n536', pullup_str=100,   parent=self)
        self.netlist['n537'] = net.net('n537',  charge_storage=True,  parent=self)
        self.netlist['n538'] = net.net('n538', pullup_str=100,   parent=self)
        self.netlist['n539'] = net.net('n539', pullup_str=100,   parent=self)
        self.netlist['n54'] = net.net('n54', pullup_str=100,   parent=self)
        self.netlist['n540'] = net.net('n540', pullup_str=100,   parent=self)
        self.netlist['n542'] = net.net('n542', pullup_str=100,   parent=self)
        self.netlist['n546'] = net.net('n546', pullup_str=100,   parent=self)
        self.netlist['n547'] = net.net('n547', pullup_str=100,   parent=self)
        self.netlist['n549'] = net.net('n549', pullup_str=100,   parent=self)
        self.netlist['n55'] = net.net('n55', pullup_str=100,   parent=self)
        self.netlist['n551'] = net.net('n551', pullup_str=100,   parent=self)
        self.netlist['n554'] = net.net('n554', pullup_str=100,   parent=self)
        self.netlist['n555'] = net.net('n555', pullup_str=100,   parent=self)
        self.netlist['n557'] = net.net('n557', pullup_str=100,   parent=self)
        self.netlist['n559'] = net.net('n559', pullup_str=100,   parent=self)
        self.netlist['n562'] = net.net('n562', pullup_str=100,   parent=self)
        self.netlist['n563'] = net.net('n563', pullup_str=100,   parent=self)
        self.netlist['n565'] = net.net('n565', pullup_str=100,   parent=self)
        self.netlist['n567'] = net.net('n567', pullup_str=100,   parent=self)
        self.netlist['n57'] = net.net('n57', pullup_str=100,   parent=self)
        self.netlist['n570'] = net.net('n570', pullup_str=100,   parent=self)
        self.netlist['n571'] = net.net('n571', pullup_str=100,   parent=self)
        self.netlist['n572'] = net.net('n572', pullup_str=100,   parent=self)
        self.netlist['n573'] = net.net('n573', pullup_str=100,   parent=self)
        self.netlist['n574'] = net.net('n574',  charge_storage=True,  parent=self)
        self.netlist['n575'] = net.net('n575', pullup_str=100,   parent=self)
        self.netlist['n576'] = net.net('n576', pullup_str=100,   parent=self)
        self.netlist['n577'] = net.net('n577', pullup_str=100,   parent=self)
        self.netlist['n578'] = net.net('n578', pullup_str=100,   parent=self)
        self.netlist['n579'] = net.net('n579',  charge_storage=True,  parent=self)
        self.netlist['n58'] = net.net('n58', pullup_str=100,   parent=self)
        self.netlist['n580'] = net.net('n580',  charge_storage=True,  parent=self)
        self.netlist['n581'] = net.net('n581', pullup_str=100,   parent=self)
        self.netlist['n582'] = net.net('n582', pullup_str=100,   parent=self)
        self.netlist['n583'] = net.net('n583',  charge_storage=True,  parent=self)
        self.netlist['n584'] = net.net('n584', pullup_str=100,   parent=self)
        self.netlist['n585'] = net.net('n585', pullup_str=100,   parent=self)
        self.netlist['n586'] = net.net('n586', pullup_str=100,   parent=self)
        self.netlist['n587'] = net.net('n587',  charge_storage=True,  parent=self)
        self.netlist['n588'] = net.net('n588',  charge_storage=True,  parent=self)
        self.netlist['n589'] = net.net('n589', pullup_str=100,   parent=self)
        self.netlist['n590'] = net.net('n590', pullup_str=100,   parent=self)
        self.netlist['n591'] = net.net('n591',  charge_storage=True,  parent=self)
        self.netlist['n592'] = net.net('n592',  charge_storage=True,  parent=self)
        self.netlist['n594'] = net.net('n594', pullup_str=100,   parent=self)
        self.netlist['n595'] = net.net('n595',  charge_storage=True,  parent=self)
        self.netlist['n596'] = net.net('n596', pullup_str=100,   parent=self)
        self.netlist['n597'] = net.net('n597', pullup_str=100,   parent=self)
        self.netlist['n6'] = net.net('n6', pullup_str=100,   parent=self)
        self.netlist['n60'] = net.net('n60', pullup_str=100,   parent=self)
        self.netlist['n600'] = net.net('n600', pullup_str=100,   parent=self)
        self.netlist['n603'] = net.net('n603',  charge_storage=True,  parent=self)
        self.netlist['n605'] = net.net('n605',  charge_storage=True,  parent=self)
        self.netlist['n606'] = net.net('n606', pullup_str=100,   parent=self)
        self.netlist['n607'] = net.net('n607', pullup_str=100,   parent=self)
        self.netlist['n61'] = net.net('n61', pullup_str=100,   parent=self)
        self.netlist['n611'] = net.net('n611',  charge_storage=True,  parent=self)
        self.netlist['n612'] = net.net('n612', pullup_str=100,   parent=self)
        self.netlist['n613'] = net.net('n613',  charge_storage=True,  parent=self)
        self.netlist['n614'] = net.net('n614',  charge_storage=True,  parent=self)
        self.netlist['n615'] = net.net('n615',  charge_storage=True,  parent=self)
        self.netlist['n616'] = net.net('n616',  charge_storage=True,  parent=self)
        self.netlist['n617'] = net.net('n617',  charge_storage=True,  parent=self)
        self.netlist['n618'] = net.net('n618', pullup_str=100,   parent=self)
        self.netlist['n619'] = net.net('n619', pullup_str=100,   parent=self)
        self.netlist['n620'] = net.net('n620', pullup_str=100,   parent=self)
        self.netlist['n621'] = net.net('n621', pullup_str=100,   parent=self)
        self.netlist['n622'] = net.net('n622',  charge_storage=True,  parent=self)
        self.netlist['n623'] = net.net('n623', pullup_str=100,   parent=self)
        self.netlist['n624'] = net.net('n624', pullup_str=100,   parent=self)
        self.netlist['n625'] = net.net('n625', pullup_str=100,   parent=self)
        self.netlist['n626'] = net.net('n626', pullup_str=100,   parent=self)
        self.netlist['n627'] = net.net('n627',  charge_storage=True,  parent=self)
        self.netlist['n628'] = net.net('n628', pullup_str=100,   parent=self)
        self.netlist['n629'] = net.net('n629', pullup_str=100,   parent=self)
        self.netlist['n63'] = net.net('n63', pullup_str=100,   parent=self)
        self.netlist['n630'] = net.net('n630', pullup_str=100,   parent=self)
        self.netlist['n631'] = net.net('n631', pullup_str=100,   parent=self)
        self.netlist['n632'] = net.net('n632',  charge_storage=True,  parent=self)
        self.netlist['n633'] = net.net('n633', pullup_str=100,   parent=self)
        self.netlist['n634'] = net.net('n634', pullup_str=100,   parent=self)
        self.netlist['n635'] = net.net('n635', pullup_str=100,   parent=self)
        self.netlist['n636'] = net.net('n636', pullup_str=100,   parent=self)
        self.netlist['n64'] = net.net('n64', pullup_str=100,   parent=self)
        self.netlist['n645'] = net.net('n645', pullup_str=100,   parent=self)
        self.netlist['n646'] = net.net('n646', pullup_str=100,   parent=self)
        self.netlist['n651'] = net.net('n651', pullup_str=100,   parent=self)
        self.netlist['n652'] = net.net('n652', pullup_str=100,   parent=self)
        self.netlist['n653'] = net.net('n653', pullup_str=100,   parent=self)
        self.netlist['n654'] = net.net('n654',  charge_storage=True,  parent=self)
        self.netlist['n658'] = net.net('n658', pullup_str=100,   parent=self)
        self.netlist['n659'] = net.net('n659', pullup_str=100,   parent=self)
        self.netlist['n66'] = net.net('n66', pullup_str=100,   parent=self)
        self.netlist['n661'] = net.net('n661', pullup_str=100,   parent=self)
        self.netlist['n662'] = net.net('n662', pullup_str=100,   parent=self)
        self.netlist['n665'] = net.net('n665', pullup_str=100,   parent=self)
        self.netlist['n666'] = net.net('n666', pullup_str=100,   parent=self)
        self.netlist['n667'] = net.net('n667', pullup_str=100,   parent=self)
        self.netlist['n67'] = net.net('n67', pullup_str=100,   parent=self)
        self.netlist['n671'] = net.net('n671', pullup_str=100,   parent=self)
        self.netlist['n672'] = net.net('n672', pullup_str=100,   parent=self)
        self.netlist['n674'] = net.net('n674', pullup_str=100,   parent=self)
        self.netlist['n675'] = net.net('n675', pullup_str=100,   parent=self)
        self.netlist['n679'] = net.net('n679', pullup_str=100,   parent=self)
        self.netlist['n680'] = net.net('n680', pullup_str=100,   parent=self)
        self.netlist['n681'] = net.net('n681', pullup_str=100,   parent=self)
        self.netlist['n682'] = net.net('n682', pullup_str=100,   parent=self)
        self.netlist['n684'] = net.net('n684', pullup_str=100,   parent=self)
        self.netlist['n685'] = net.net('n685', pullup_str=100,   parent=self)
        self.netlist['n687'] = net.net('n687', pullup_str=100,   parent=self)
        self.netlist['n688'] = net.net('n688', pullup_str=100,   parent=self)
        self.netlist['n689'] = net.net('n689', pullup_str=100,   parent=self)
        self.netlist['n69'] = net.net('n69', pullup_str=100,   parent=self)
        self.netlist['n690'] = net.net('n690', pullup_str=100,   parent=self)
        self.netlist['n693'] = net.net('n693',  charge_storage=True,  parent=self)
        self.netlist['n695'] = net.net('n695',  charge_storage=True,  parent=self)
        self.netlist['n698'] = net.net('n698',  charge_storage=True,  parent=self)
        self.netlist['n699'] = net.net('n699', pullup_str=100,   parent=self)
        self.netlist['n7'] = net.net('n7', pullup_str=100,   parent=self)
        self.netlist['n70'] = net.net('n70', pullup_str=100,   parent=self)
        self.netlist['n700'] = net.net('n700', pullup_str=100,   parent=self)
        self.netlist['n701'] = net.net('n701', pullup_str=100,   parent=self)
        self.netlist['n702'] = net.net('n702', pullup_str=100,   parent=self)
        self.netlist['n703'] = net.net('n703',  charge_storage=True,  parent=self)
        self.netlist['n704'] = net.net('n704', pullup_str=100,   parent=self)
        self.netlist['n705'] = net.net('n705',  charge_storage=True,  parent=self)
        self.netlist['n706'] = net.net('n706',  charge_storage=True,  parent=self)
        self.netlist['n707'] = net.net('n707',  charge_storage=True,  parent=self)
        self.netlist['n708'] = net.net('n708',  charge_storage=True,  parent=self)
        self.netlist['n709'] = net.net('n709', pullup_str=100,   parent=self)
        self.netlist['n710'] = net.net('n710', pullup_str=100,   parent=self)
        self.netlist['n711'] = net.net('n711', pullup_str=100,   parent=self)
        self.netlist['n712'] = net.net('n712', pullup_str=100,   parent=self)
        self.netlist['n713'] = net.net('n713', pullup_str=100,   parent=self)
        self.netlist['n714'] = net.net('n714',  charge_storage=True,  parent=self)
        self.netlist['n715'] = net.net('n715',  charge_storage=True,  parent=self)
        self.netlist['n717'] = net.net('n717', pullup_str=100,   parent=self)
        self.netlist['n718'] = net.net('n718', pullup_str=100,   parent=self)
        self.netlist['n719'] = net.net('n719', pullup_str=100,   parent=self)
        self.netlist['n72'] = net.net('n72', pullup_str=100,   parent=self)
        self.netlist['n720'] = net.net('n720',  charge_storage=True,  parent=self)
        self.netlist['n721'] = net.net('n721',  charge_storage=True,  parent=self)
        self.netlist['n722'] = net.net('n722', pullup_str=100,   parent=self)
        self.netlist['n723'] = net.net('n723',  charge_storage=True,  parent=self)
        self.netlist['n724'] = net.net('n724',  charge_storage=True,  parent=self)
        self.netlist['n725'] = net.net('n725',  charge_storage=True,  parent=self)
        self.netlist['n726'] = net.net('n726', pullup_str=100,   parent=self)
        self.netlist['n727'] = net.net('n727', pullup_str=100,   parent=self)
        self.netlist['n728'] = net.net('n728', pullup_str=100,   parent=self)
        self.netlist['n73'] = net.net('n73', pullup_str=100,   parent=self)
        self.netlist['n730'] = net.net('n730',  charge_storage=True,  parent=self)
        self.netlist['n731'] = net.net('n731',  charge_storage=True,  parent=self)
        self.netlist['n732'] = net.net('n732', pullup_str=100,   parent=self)
        self.netlist['n733'] = net.net('n733', pullup_str=100,   parent=self)
        self.netlist['n734'] = net.net('n734',  charge_storage=True,  parent=self)
        self.netlist['n736'] = net.net('n736', pullup_str=100,   parent=self)
        self.netlist['n737'] = net.net('n737',  charge_storage=True,  parent=self)
        self.netlist['n738'] = net.net('n738', pullup_str=100,   parent=self)
        self.netlist['n739'] = net.net('n739', pullup_str=100,   parent=self)
        self.netlist['n740'] = net.net('n740',  charge_storage=True,  parent=self)
        self.netlist['n741'] = net.net('n741', pullup_str=100,   parent=self)
        self.netlist['n742'] = net.net('n742',  charge_storage=True,  parent=self)
        self.netlist['n743'] = net.net('n743',  charge_storage=True,  parent=self)
        self.netlist['n745'] = net.net('n745', pullup_str=100,   parent=self)
        self.netlist['n746'] = net.net('n746', pullup_str=100,   parent=self)
        self.netlist['n747'] = net.net('n747', pullup_str=100,   parent=self)
        self.netlist['n748'] = net.net('n748',  charge_storage=True,  parent=self)
        self.netlist['n749'] = net.net('n749', pullup_str=100,   parent=self)
        self.netlist['n75'] = net.net('n75', pullup_str=100,   parent=self)
        self.netlist['n750'] = net.net('n750',  charge_storage=True,  parent=self)
        self.netlist['n751'] = net.net('n751', pullup_str=100,   parent=self)
        self.netlist['n753'] = net.net('n753',  charge_storage=True,  parent=self)
        self.netlist['n754'] = net.net('n754',  charge_storage=True,  parent=self)
        self.netlist['n755'] = net.net('n755', pullup_str=100,   parent=self)
        self.netlist['n756'] = net.net('n756',  charge_storage=True,  parent=self)
        self.netlist['n757'] = net.net('n757', pullup_str=100,   parent=self)
        self.netlist['n759'] = net.net('n759',  charge_storage=True,  parent=self)
        self.netlist['n76'] = net.net('n76', pullup_str=100,   parent=self)
        self.netlist['n760'] = net.net('n760', pullup_str=100,   parent=self)
        self.netlist['n761'] = net.net('n761', pullup_str=100,   parent=self)
        self.netlist['n762'] = net.net('n762',  charge_storage=True,  parent=self)
        self.netlist['n763'] = net.net('n763', pullup_str=100,   parent=self)
        self.netlist['n764'] = net.net('n764', pullup_str=100,   parent=self)
        self.netlist['n765'] = net.net('n765', pullup_str=100,   parent=self)
        self.netlist['n766'] = net.net('n766',  charge_storage=True,  parent=self)
        self.netlist['n767'] = net.net('n767', pullup_str=100,   parent=self)
        self.netlist['n768'] = net.net('n768', pullup_str=100,   parent=self)
        self.netlist['n77'] = net.net('n77', pullup_str=100,   parent=self)
        self.netlist['n770'] = net.net('n770',  charge_storage=True,  parent=self)
        self.netlist['n771'] = net.net('n771',  charge_storage=True,  parent=self)
        self.netlist['n774'] = net.net('n774', pullup_str=100,   parent=self)
        self.netlist['n775'] = net.net('n775', pullup_str=100,   parent=self)
        self.netlist['n776'] = net.net('n776',  charge_storage=True,  parent=self)
        self.netlist['n778'] = net.net('n778',  charge_storage=True,  parent=self)
        self.netlist['n779'] = net.net('n779', pullup_str=100,   parent=self)
        self.netlist['n78'] = net.net('n78', pullup_str=100,   parent=self)
        self.netlist['n780'] = net.net('n780',  charge_storage=True,  parent=self)
        self.netlist['n781'] = net.net('n781', pullup_str=100,   parent=self)
        self.netlist['n782'] = net.net('n782', pullup_str=100,   parent=self)
        self.netlist['n783'] = net.net('n783',  charge_storage=True,  parent=self)
        self.netlist['n784'] = net.net('n784',  charge_storage=True,  parent=self)
        self.netlist['n787'] = net.net('n787',  charge_storage=True,  parent=self)
        self.netlist['n788'] = net.net('n788', pullup_str=100,   parent=self)
        self.netlist['n789'] = net.net('n789', pullup_str=100,   parent=self)
        self.netlist['n79'] = net.net('n79', pullup_str=100,   parent=self)
        self.netlist['n791'] = net.net('n791', pullup_str=100,   parent=self)
        self.netlist['n792'] = net.net('n792', pullup_str=100,   parent=self)
        self.netlist['n793'] = net.net('n793', pullup_str=100,   parent=self)
        self.netlist['n795'] = net.net('n795', pullup_str=100,   parent=self)
        self.netlist['n796'] = net.net('n796', pullup_str=100,   parent=self)
        self.netlist['n797'] = net.net('n797', pullup_str=100,   parent=self)
        self.netlist['n798'] = net.net('n798', pullup_str=100,   parent=self)
        self.netlist['n799'] = net.net('n799',  charge_storage=True,  parent=self)
        self.netlist['n8'] = net.net('n8', pullup_str=100,   parent=self)
        self.netlist['n80'] = net.net('n80', pullup_str=100,   parent=self)
        self.netlist['n800'] = net.net('n800',  charge_storage=True,  parent=self)
        self.netlist['n801'] = net.net('n801', pullup_str=100,   parent=self)
        self.netlist['n802'] = net.net('n802', pullup_str=100,   parent=self)
        self.netlist['n803'] = net.net('n803', pullup_str=100,   parent=self)
        self.netlist['n804'] = net.net('n804', pullup_str=100,   parent=self)
        self.netlist['n805'] = net.net('n805', pullup_str=100,   parent=self)
        self.netlist['n806'] = net.net('n806', pullup_str=100,   parent=self)
        self.netlist['n807'] = net.net('n807', pullup_str=100,   parent=self)
        self.netlist['n808'] = net.net('n808', pullup_str=100,   parent=self)
        self.netlist['n809'] = net.net('n809',  charge_storage=True,  parent=self)
        self.netlist['n81'] = net.net('n81',  charge_storage=True,  parent=self)
        self.netlist['n810'] = net.net('n810', pullup_str=100,   parent=self)
        self.netlist['n811'] = net.net('n811',  charge_storage=True,  parent=self)
        self.netlist['n812'] = net.net('n812', pullup_str=100,   parent=self)
        self.netlist['n813'] = net.net('n813',  charge_storage=True,  parent=self)
        self.netlist['n814'] = net.net('n814', pullup_str=100,   parent=self)
        self.netlist['n815'] = net.net('n815',  charge_storage=True,  parent=self)
        self.netlist['n816'] = net.net('n816', pullup_str=100,   parent=self)
        self.netlist['n817'] = net.net('n817',  charge_storage=True,  parent=self)
        self.netlist['n818'] = net.net('n818', pullup_str=100,   parent=self)
        self.netlist['n819'] = net.net('n819',  charge_storage=True,  parent=self)
        self.netlist['n82'] = net.net('n82', pullup_str=100,   parent=self)
        self.netlist['n820'] = net.net('n820', pullup_str=100,   parent=self)
        self.netlist['n821'] = net.net('n821', pullup_str=100,   parent=self)
        self.netlist['n822'] = net.net('n822', pullup_str=100,   parent=self)
        self.netlist['n824'] = net.net('n824',  charge_storage=True,  parent=self)
        self.netlist['n826'] = net.net('n826', pullup_str=100,   parent=self)
        self.netlist['n827'] = net.net('n827',  charge_storage=True,  parent=self)
        self.netlist['n829'] = net.net('n829',  charge_storage=True,  parent=self)
        self.netlist['n83'] = net.net('n83',  charge_storage=True,  parent=self)
        self.netlist['n830'] = net.net('n830',  charge_storage=True,  parent=self)
        self.netlist['n831'] = net.net('n831', pullup_str=100,   parent=self)
        self.netlist['n833'] = net.net('n833', pullup_str=100,   parent=self)
        self.netlist['n834'] = net.net('n834',  charge_storage=True,  parent=self)
        self.netlist['n836'] = net.net('n836', pullup_str=100,   parent=self)
        self.netlist['n837'] = net.net('n837', pullup_str=100,   parent=self)
        self.netlist['n839'] = net.net('n839', pullup_str=100,   parent=self)
        self.netlist['n84'] = net.net('n84', pullup_str=100,   parent=self)
        self.netlist['n840'] = net.net('n840', pullup_str=100,   parent=self)
        self.netlist['n841'] = net.net('n841', pullup_str=100,   parent=self)
        self.netlist['n842'] = net.net('n842', pullup_str=100,   parent=self)
        self.netlist['n846'] = net.net('n846', pullup_str=100,   parent=self)
        self.netlist['n847'] = net.net('n847', pullup_str=100,   parent=self)
        self.netlist['n848'] = net.net('n848', pullup_str=100,   parent=self)
        self.netlist['n849'] = net.net('n849', pullup_str=100,   parent=self)
        self.netlist['n85'] = net.net('n85',  charge_storage=True,  parent=self)
        self.netlist['n852'] = net.net('n852',  charge_storage=True,  parent=self)
        self.netlist['n854'] = net.net('n854',  charge_storage=True,  parent=self)
        self.netlist['n855'] = net.net('n855', pullup_str=100,   parent=self)
        self.netlist['n856'] = net.net('n856',  charge_storage=True,  parent=self)
        self.netlist['n857'] = net.net('n857',  charge_storage=True,  parent=self)
        self.netlist['n858'] = net.net('n858',  charge_storage=True,  parent=self)
        self.netlist['n859'] = net.net('n859', pullup_str=100,   parent=self)
        self.netlist['n86'] = net.net('n86', pullup_str=100,   parent=self)
        self.netlist['n861'] = net.net('n861', pullup_str=100,   parent=self)
        self.netlist['n862'] = net.net('n862',  charge_storage=True,  parent=self)
        self.netlist['n864'] = net.net('n864', pullup_str=100,   parent=self)
        self.netlist['n865'] = net.net('n865',  charge_storage=True,  parent=self)
        self.netlist['n866'] = net.net('n866', pullup_str=100,   parent=self)
        self.netlist['n867'] = net.net('n867',  charge_storage=True,  parent=self)
        self.netlist['n868'] = net.net('n868', pullup_str=100,   parent=self)
        self.netlist['n869'] = net.net('n869', pullup_str=100,   parent=self)
        self.netlist['n870'] = net.net('n870',  charge_storage=True,  parent=self)
        self.netlist['n872'] = net.net('n872',  charge_storage=True,  parent=self)
        self.netlist['n873'] = net.net('n873', pullup_str=100,   parent=self)
        self.netlist['n874'] = net.net('n874', pullup_str=100,   parent=self)
        self.netlist['n875'] = net.net('n875', pullup_str=100,   parent=self)
        self.netlist['n876'] = net.net('n876',  charge_storage=True,  parent=self)
        self.netlist['n877'] = net.net('n877', pullup_str=100,   parent=self)
        self.netlist['n878'] = net.net('n878',  charge_storage=True,  parent=self)
        self.netlist['n880'] = net.net('n880', pullup_str=100,   parent=self)
        self.netlist['n881'] = net.net('n881', pullup_str=100,   parent=self)
        self.netlist['n882'] = net.net('n882',  charge_storage=True,  parent=self)
        self.netlist['n883'] = net.net('n883', pullup_str=100,   parent=self)
        self.netlist['n884'] = net.net('n884',  charge_storage=True,  parent=self)
        self.netlist['n885'] = net.net('n885', pullup_str=100,   parent=self)
        self.netlist['n886'] = net.net('n886', pullup_str=100,   parent=self)
        self.netlist['n888'] = net.net('n888',  charge_storage=True,  parent=self)
        self.netlist['n889'] = net.net('n889', pullup_str=100,   parent=self)
        self.netlist['n892'] = net.net('n892',  charge_storage=True,  parent=self)
        self.netlist['n893'] = net.net('n893', pullup_str=100,   parent=self)
        self.netlist['n895'] = net.net('n895',  charge_storage=True,  parent=self)
        self.netlist['n896'] = net.net('n896',  charge_storage=True,  parent=self)
        self.netlist['n897'] = net.net('n897', pullup_str=100,   parent=self)
        self.netlist['n898'] = net.net('n898',  charge_storage=True,  parent=self)
        self.netlist['n9'] = net.net('n9', pullup_str=100,   parent=self)
        self.netlist['n900'] = net.net('n900',  charge_storage=True,  parent=self)
        self.netlist['n902'] = net.net('n902',  charge_storage=True,  parent=self)
        self.netlist['n903'] = net.net('n903',  charge_storage=True,  parent=self)
        self.netlist['n904'] = net.net('n904', pullup_str=100,   parent=self)
        self.netlist['n906'] = net.net('n906',  charge_storage=True,  parent=self)
        self.netlist['n907'] = net.net('n907', pullup_str=100,   parent=self)
        self.netlist['n909'] = net.net('n909',  charge_storage=True,  parent=self)
        self.netlist['n910'] = net.net('n910',  charge_storage=True,  parent=self)
        self.netlist['n912'] = net.net('n912', pullup_str=100,   parent=self)
        self.netlist['n913'] = net.net('n913',  charge_storage=True,  parent=self)
        self.netlist['n915'] = net.net('n915', pullup_str=100,   parent=self)
        self.netlist['n917'] = net.net('n917',  charge_storage=True,  parent=self)
        self.netlist['n918'] = net.net('n918', pullup_str=100,   parent=self)
        self.netlist['n919'] = net.net('n919', pullup_str=100,   parent=self)
        self.netlist['n920'] = net.net('n920',  charge_storage=True,  parent=self)
        self.netlist['n921'] = net.net('n921',  charge_storage=True,  parent=self)
        self.netlist['n922'] = net.net('n922',  charge_storage=True,  parent=self)
        self.netlist['n923'] = net.net('n923', pullup_str=100,   parent=self)
        self.netlist['n924'] = net.net('n924', pullup_str=100,   parent=self)
        self.netlist['n925'] = net.net('n925', pullup_str=100,   parent=self)
        self.netlist['n926'] = net.net('n926', pullup_str=100,   parent=self)
        self.netlist['n928'] = net.net('n928', pullup_str=100,   parent=self)
        self.netlist['n929'] = net.net('n929', pullup_str=100,   parent=self)
        self.netlist['n930'] = net.net('n930', pullup_str=100,   parent=self)
        self.netlist['n931'] = net.net('n931',  charge_storage=True,  parent=self)
        self.netlist['n932'] = net.net('n932', pullup_str=100,   parent=self)
        self.netlist['n933'] = net.net('n933',  charge_storage=True,  parent=self)
        self.netlist['n934'] = net.net('n934',  charge_storage=True,  parent=self)
        self.netlist['n935'] = net.net('n935', pullup_str=100,   parent=self)
        self.netlist['n936'] = net.net('n936',  charge_storage=True,  parent=self)
        self.netlist['n937'] = net.net('n937', pullup_str=100,   parent=self)
        self.netlist['n938'] = net.net('n938',  charge_storage=True,  parent=self)
        self.netlist['n939'] = net.net('n939', pullup_str=100,   parent=self)
        self.netlist['n94'] = net.net('n94', pullup_str=100,   parent=self)
        self.netlist['n940'] = net.net('n940',  charge_storage=True,  parent=self)
        self.netlist['n941'] = net.net('n941', pullup_str=100,   parent=self)
        self.netlist['n942'] = net.net('n942', pullup_str=100,   parent=self)
        self.netlist['n943'] = net.net('n943', pullup_str=100,   parent=self)
        self.netlist['n944'] = net.net('n944', pullup_str=100,   parent=self)
        self.netlist['n945'] = net.net('n945', pullup_str=100,   parent=self)
        self.netlist['n946'] = net.net('n946', pullup_str=100,   parent=self)
        self.netlist['n947'] = net.net('n947', pullup_str=100,   parent=self)
        self.netlist['n948'] = net.net('n948',  charge_storage=True,  parent=self)
        self.netlist['n95'] = net.net('n95', pullup_str=100,   parent=self)
        self.netlist['n950'] = net.net('n950',  charge_storage=True,  parent=self)
        self.netlist['n951'] = net.net('n951', pullup_str=100,   parent=self)
        self.netlist['n952'] = net.net('n952',  charge_storage=True,  parent=self)
        self.netlist['n953'] = net.net('n953', pullup_str=100,   parent=self)
        self.netlist['n954'] = net.net('n954', pullup_str=100,   parent=self)
        self.netlist['n956'] = net.net('n956', pullup_str=100,   parent=self)
        self.netlist['n957'] = net.net('n957', pullup_str=100,   parent=self)
        self.netlist['n958'] = net.net('n958', pullup_str=100,   parent=self)
        self.netlist['n959'] = net.net('n959', pullup_str=100,   parent=self)
        self.netlist['n96'] = net.net('n96',  charge_storage=True,  parent=self)
        self.netlist['n960'] = net.net('n960', pullup_str=100,   parent=self)
        self.netlist['n962'] = net.net('n962',  charge_storage=True,  parent=self)
        self.netlist['n963'] = net.net('n963', pullup_str=100,   parent=self)
        self.netlist['n965'] = net.net('n965', pullup_str=100,   parent=self)
        self.netlist['n966'] = net.net('n966', pullup_str=100,   parent=self)
        self.netlist['n967'] = net.net('n967',  charge_storage=True,  parent=self)
        self.netlist['n969'] = net.net('n969', pullup_str=100,   parent=self)
        self.netlist['n97'] = net.net('n97', pullup_str=100,   parent=self)
        self.netlist['n970'] = net.net('n970', pullup_str=100,   parent=self)
        self.netlist['n971'] = net.net('n971', pullup_str=100,   parent=self)
        self.netlist['n973'] = net.net('n973',  charge_storage=True,  parent=self)
        self.netlist['n976'] = net.net('n976', pullup_str=100,   parent=self)
        self.netlist['n977'] = net.net('n977', pullup_str=100,   parent=self)
        self.netlist['n978'] = net.net('n978',  charge_storage=True,  parent=self)
        self.netlist['n979'] = net.net('n979', pullup_str=100,   parent=self)
        self.netlist['n98'] = net.net('n98', pullup_str=100,   parent=self)
        self.netlist['n980'] = net.net('n980', pullup_str=100,   parent=self)
        self.netlist['n982'] = net.net('n982', pullup_str=100,   parent=self)
        self.netlist['n983'] = net.net('n983', pullup_str=100,   parent=self)
        self.netlist['n984'] = net.net('n984', pullup_str=100,   parent=self)
        self.netlist['n985'] = net.net('n985', pullup_str=100,   parent=self)
        self.netlist['n986'] = net.net('n986', pullup_str=100,   parent=self)
        self.netlist['n987'] = net.net('n987', pullup_str=100,   parent=self)
        self.netlist['n988'] = net.net('n988', pullup_str=100,   parent=self)
        self.netlist['n989'] = net.net('n989', pullup_str=100,   parent=self)
        self.netlist['n99'] = net.net('n99', pullup_str=100,   parent=self)
        self.netlist['n990'] = net.net('n990', pullup_str=100,   parent=self)
        self.netlist['n991'] = net.net('n991',  charge_storage=True,  parent=self)
        self.netlist['n992'] = net.net('n992', pullup_str=100,   parent=self)
        self.netlist['n993'] = net.net('n993',  charge_storage=True,  parent=self)
        self.netlist['n994'] = net.net('n994',  charge_storage=True,  parent=self)
        self.netlist['n996'] = net.net('n996', pullup_str=100,   parent=self)
        self.netlist['n997'] = net.net('n997',  charge_storage=True,  parent=self)
        self.netlist['n998'] = net.net('n998',  charge_storage=True,  parent=self)
        self.port['nmi'].netconn.pullup_str=100
        self.netlist['ob'] = net.net('ob',  charge_storage=True,  parent=self)
        self.netlist['obl0'] = net.net('obl0',  charge_storage=True,  parent=self)
        self.netlist['obl1'] = net.net('obl1',  charge_storage=True,  parent=self)
        self.netlist['obl2'] = net.net('obl2',  charge_storage=True,  parent=self)
        self.netlist['obl3'] = net.net('obl3',  charge_storage=True,  parent=self)
        self.netlist['obl4'] = net.net('obl4',  charge_storage=True,  parent=self)
        self.netlist['obl5'] = net.net('obl5',  charge_storage=True,  parent=self)
        self.netlist['obl6'] = net.net('obl6',  charge_storage=True,  parent=self)
        self.netlist['obl7'] = net.net('obl7',  charge_storage=True,  parent=self)
        self.netlist['pch0'] = net.net('pch0', pullup_str=100,   parent=self)
        self.netlist['pch0_1'] = net.net('pch0_1',  charge_storage=True,  parent=self)
        self.netlist['pch1'] = net.net('pch1', pullup_str=100,   parent=self)
        self.netlist['pch1_1'] = net.net('pch1_1',  charge_storage=True,  parent=self)
        self.netlist['pch2'] = net.net('pch2', pullup_str=100,   parent=self)
        self.netlist['pch2_1'] = net.net('pch2_1',  charge_storage=True,  parent=self)
        self.netlist['pch3'] = net.net('pch3', pullup_str=100,   parent=self)
        self.netlist['pch3_1'] = net.net('pch3_1',  charge_storage=True,  parent=self)
        self.netlist['pch4'] = net.net('pch4', pullup_str=100,   parent=self)
        self.netlist['pch4_1'] = net.net('pch4_1',  charge_storage=True,  parent=self)
        self.netlist['pch5'] = net.net('pch5', pullup_str=100,   parent=self)
        self.netlist['pch5_1'] = net.net('pch5_1',  charge_storage=True,  parent=self)
        self.netlist['pch6'] = net.net('pch6', pullup_str=100,   parent=self)
        self.netlist['pch6_1'] = net.net('pch6_1',  charge_storage=True,  parent=self)
        self.netlist['pch7'] = net.net('pch7', pullup_str=100,   parent=self)
        self.netlist['pch7_1'] = net.net('pch7_1',  charge_storage=True,  parent=self)
        self.netlist['pcl0'] = net.net('pcl0', pullup_str=100,   parent=self)
        self.netlist['pcl0_1'] = net.net('pcl0_1',  charge_storage=True,  parent=self)
        self.netlist['pcl1'] = net.net('pcl1', pullup_str=100,   parent=self)
        self.netlist['pcl1_1'] = net.net('pcl1_1',  charge_storage=True,  parent=self)
        self.netlist['pcl2'] = net.net('pcl2', pullup_str=100,   parent=self)
        self.netlist['pcl2_1'] = net.net('pcl2_1',  charge_storage=True,  parent=self)
        self.netlist['pcl3'] = net.net('pcl3', pullup_str=100,   parent=self)
        self.netlist['pcl3_1'] = net.net('pcl3_1',  charge_storage=True,  parent=self)
        self.netlist['pcl4'] = net.net('pcl4', pullup_str=100,   parent=self)
        self.netlist['pcl4_1'] = net.net('pcl4_1',  charge_storage=True,  parent=self)
        self.netlist['pcl5'] = net.net('pcl5', pullup_str=100,   parent=self)
        self.netlist['pcl5_1'] = net.net('pcl5_1',  charge_storage=True,  parent=self)
        self.netlist['pcl6'] = net.net('pcl6', pullup_str=100,   parent=self)
        self.netlist['pcl6_1'] = net.net('pcl6_1',  charge_storage=True,  parent=self)
        self.netlist['pcl7'] = net.net('pcl7', pullup_str=100,   parent=self)
        self.netlist['pcl7_1'] = net.net('pcl7_1',  charge_storage=True,  parent=self)
        self.port['phi1'].netconn.charge_storage=True
        self.port['phi2'].netconn.charge_storage=True
        self.netlist['phi2_1'] = net.net('phi2_1', pullup_str=100,   parent=self)
        self.netlist['qaddgen0'] = net.net('qaddgen0', pullup_str=100,   parent=self)
        self.netlist['res'] = net.net('res',  charge_storage=True,  parent=self)
        self.port['reset'].netconn.pullup_str=100
        self.netlist['reset_0'] = net.net('reset_0', pullup_str=100,   parent=self)
        self.port['rw'].netconn.charge_storage=True
        self.netlist['sph0'] = net.net('sph0', pullup_str=100,   parent=self)
        self.netlist['sph0_1'] = net.net('sph0_1',  charge_storage=True,  parent=self)
        self.netlist['sph1'] = net.net('sph1', pullup_str=100,   parent=self)
        self.netlist['sph1_1'] = net.net('sph1_1',  charge_storage=True,  parent=self)
        self.netlist['sph2'] = net.net('sph2', pullup_str=100,   parent=self)
        self.netlist['sph2_1'] = net.net('sph2_1',  charge_storage=True,  parent=self)
        self.netlist['sph3'] = net.net('sph3', pullup_str=100,   parent=self)
        self.netlist['sph3_1'] = net.net('sph3_1',  charge_storage=True,  parent=self)
        self.netlist['sph4'] = net.net('sph4', pullup_str=100,   parent=self)
        self.netlist['sph4_1'] = net.net('sph4_1',  charge_storage=True,  parent=self)
        self.netlist['sph5'] = net.net('sph5', pullup_str=100,   parent=self)
        self.netlist['sph5_1'] = net.net('sph5_1',  charge_storage=True,  parent=self)
        self.netlist['sph6'] = net.net('sph6', pullup_str=100,   parent=self)
        self.netlist['sph6_1'] = net.net('sph6_1',  charge_storage=True,  parent=self)
        self.netlist['sph7'] = net.net('sph7', pullup_str=100,   parent=self)
        self.netlist['sph7_1'] = net.net('sph7_1',  charge_storage=True,  parent=self)
        self.netlist['spl0'] = net.net('spl0', pullup_str=100,   parent=self)
        self.netlist['spl0_1'] = net.net('spl0_1',  charge_storage=True,  parent=self)
        self.netlist['spl1'] = net.net('spl1', pullup_str=100,   parent=self)
        self.netlist['spl1_1'] = net.net('spl1_1',  charge_storage=True,  parent=self)
        self.netlist['spl2'] = net.net('spl2', pullup_str=100,   parent=self)
        self.netlist['spl2_1'] = net.net('spl2_1',  charge_storage=True,  parent=self)
        self.netlist['spl3'] = net.net('spl3', pullup_str=100,   parent=self)
        self.netlist['spl3_1'] = net.net('spl3_1',  charge_storage=True,  parent=self)
        self.netlist['spl4'] = net.net('spl4', pullup_str=100,   parent=self)
        self.netlist['spl4_1'] = net.net('spl4_1',  charge_storage=True,  parent=self)
        self.netlist['spl5'] = net.net('spl5', pullup_str=100,   parent=self)
        self.netlist['spl5_1'] = net.net('spl5_1',  charge_storage=True,  parent=self)
        self.netlist['spl6'] = net.net('spl6', pullup_str=100,   parent=self)
        self.netlist['spl6_1'] = net.net('spl6_1',  charge_storage=True,  parent=self)
        self.netlist['spl7'] = net.net('spl7', pullup_str=100,   parent=self)
        self.netlist['spl7_1'] = net.net('spl7_1',  charge_storage=True,  parent=self)
        self.netlist['sum0'] = net.net('sum0', pullup_str=100,   parent=self)
        self.netlist['sum1'] = net.net('sum1', pullup_str=100,   parent=self)
        self.netlist['sum2'] = net.net('sum2', pullup_str=100,   parent=self)
        self.netlist['sum3'] = net.net('sum3', pullup_str=100,   parent=self)
        self.netlist['sum4'] = net.net('sum4', pullup_str=100,   parent=self)
        self.netlist['sum5'] = net.net('sum5', pullup_str=100,   parent=self)
        self.netlist['sum6'] = net.net('sum6', pullup_str=100,   parent=self)
        self.netlist['sum7'] = net.net('sum7', pullup_str=100,   parent=self)
        self.netlist['sumab0'] = net.net('sumab0', pullup_str=100,   parent=self)
        self.netlist['sumab1'] = net.net('sumab1', pullup_str=100,   parent=self)
        self.netlist['sumab2'] = net.net('sumab2', pullup_str=100,   parent=self)
        self.netlist['sumab3'] = net.net('sumab3', pullup_str=100,   parent=self)
        self.netlist['sumab4'] = net.net('sumab4', pullup_str=100,   parent=self)
        self.netlist['sumab5'] = net.net('sumab5', pullup_str=100,   parent=self)
        self.netlist['sumab6'] = net.net('sumab6', pullup_str=100,   parent=self)
        self.netlist['sumab7'] = net.net('sumab7', pullup_str=100,   parent=self)
        self.netlist['sync'] = net.net('sync',  charge_storage=True,  parent=self)
        self.netlist['tmp0'] = net.net('tmp0', pullup_str=100,   parent=self)
        self.netlist['tmp0_1'] = net.net('tmp0_1',  charge_storage=True,  parent=self)
        self.netlist['tmp1'] = net.net('tmp1', pullup_str=100,   parent=self)
        self.netlist['tmp1_1'] = net.net('tmp1_1',  charge_storage=True,  parent=self)
        self.netlist['tmp2'] = net.net('tmp2', pullup_str=100,   parent=self)
        self.netlist['tmp2_1'] = net.net('tmp2_1',  charge_storage=True,  parent=self)
        self.netlist['tmp3'] = net.net('tmp3', pullup_str=100,   parent=self)
        self.netlist['tmp3_1'] = net.net('tmp3_1',  charge_storage=True,  parent=self)
        self.netlist['tmp4'] = net.net('tmp4', pullup_str=100,   parent=self)
        self.netlist['tmp4_1'] = net.net('tmp4_1',  charge_storage=True,  parent=self)
        self.netlist['tmp5'] = net.net('tmp5', pullup_str=100,   parent=self)
        self.netlist['tmp5_1'] = net.net('tmp5_1',  charge_storage=True,  parent=self)
        self.netlist['tmp6'] = net.net('tmp6', pullup_str=100,   parent=self)
        self.netlist['tmp6_1'] = net.net('tmp6_1',  charge_storage=True,  parent=self)
        self.netlist['tmp7'] = net.net('tmp7', pullup_str=100,   parent=self)
        self.netlist['tmp7_1'] = net.net('tmp7_1',  charge_storage=True,  parent=self)
        self.port['tsc'].netconn.charge_storage=True
        self.netlist['vcc'] = net.supply1('vcc')
        self.port['vma'].netconn.charge_storage=True
        self.netlist['vma_0'] = net.net('vma_0', pullup_str=100,   parent=self)
        ## Component declarations
        self.gatelist.extend([
            NMOS("t3488", [self.netlist['n1097'],self.port['gnd'].netconn,self.netlist['n1444']], isweak=False, parent=self),
            NMOS("t3489", [self.netlist['n1096'],self.port['gnd'].netconn,self.netlist['n1369']], isweak=False, parent=self),
            NMOS("t3958", [self.port['gnd'].netconn,self.netlist['n1628'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3959", [self.port['gnd'].netconn,self.netlist['n1847'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3956", [self.port['gnd'].netconn,self.netlist['n1837'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3957", [self.port['gnd'].netconn,self.netlist['n1810'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3954", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3955", [self.port['gnd'].netconn,self.netlist['n1618'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3480", [self.port['gnd'].netconn,self.netlist['Tg7'],self.netlist['n1078']], isweak=False, parent=self),
            NMOS("t3953", [self.port['gnd'].netconn,self.netlist['n1828'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3950", [self.port['gnd'].netconn,self.netlist['n1834'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3951", [self.port['gnd'].netconn,self.netlist['n1515'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t776", [self.port['gnd'].netconn,self.netlist['inch1'],self.netlist['n214']], isweak=False, parent=self),
            NMOS("t777", [self.port['gnd'].netconn,self.netlist['inch0'],self.netlist['n218']], isweak=False, parent=self),
            NMOS("t774", [self.netlist['inch7'],self.netlist['pch7_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t773", [self.netlist['inch7'],self.netlist['abh7'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t770", [self.netlist['inch5'],self.netlist['pch5_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t2541", [self.netlist['n866'],self.netlist['n715'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t778", [self.port['gnd'].netconn,self.netlist['inch3'],self.netlist['n213']], isweak=False, parent=self),
            NMOS("t779", [self.port['gnd'].netconn,self.netlist['inch2'],self.netlist['n217']], isweak=False, parent=self),
            NMOS("t3552", [self.netlist['n2914'],self.netlist['n1566'],self.netlist['n1058']], isweak=False, parent=self),
            NMOS("t175", [self.port['ab11'].netconn,self.port['gnd'].netconn,self.netlist['n41']], isweak=False, parent=self),
            NMOS("t2579", [self.netlist['n728'],self.port['gnd'].netconn,self.netlist['n730']], isweak=False, parent=self),
            NMOS("t177", [self.port['ab8'].netconn,self.port['gnd'].netconn,self.netlist['n38']], isweak=False, parent=self),
            NMOS("t3004", [self.netlist['n2837'],self.netlist['n915'],self.netlist['n797']], isweak=False, parent=self),
            NMOS("t3557", [self.netlist['n1119'],self.port['gnd'].netconn,self.netlist['n1105']], isweak=False, parent=self),
            NMOS("t3554", [self.netlist['n1119'],self.netlist['n1118'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3555", [self.netlist['n1120'],self.port['gnd'].netconn,self.netlist['n1118']], isweak=False, parent=self),
            NMOS("t2573", [self.netlist['n727'],self.port['gnd'].netconn,self.netlist['Tx1']], isweak=False, parent=self),
            NMOS("t2572", [self.netlist['n2798'],self.netlist['n722'],self.netlist['n958']], isweak=False, parent=self),
            NMOS("t3558", [self.port['gnd'].netconn,self.netlist['n1113'],self.netlist['n1101']], isweak=False, parent=self),
            NMOS("t2570", [self.netlist['n2798'],self.port['gnd'].netconn,self.netlist['n959']], isweak=False, parent=self),
            NMOS("t2577", [self.netlist['n86'],self.port['gnd'].netconn,self.netlist['n733']], isweak=False, parent=self),
            NMOS("t3790", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3791", [self.port['gnd'].netconn,self.netlist['n1610'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3792", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3793", [self.port['gnd'].netconn,self.netlist['n1843'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3794", [self.port['gnd'].netconn,self.netlist['n1816'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3795", [self.port['gnd'].netconn,self.netlist['n1629'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3796", [self.port['gnd'].netconn,self.netlist['n1848'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3797", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3798", [self.port['gnd'].netconn,self.netlist['n1526'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3799", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3828", [self.port['gnd'].netconn,self.netlist['n1213'],self.netlist['n1788']], isweak=False, parent=self),
            NMOS("t3829", [self.port['gnd'].netconn,self.netlist['n1211'],self.netlist['n3']], isweak=False, parent=self),
            NMOS("t3487", [self.netlist['n1097'],self.port['gnd'].netconn,self.netlist['n1346']], isweak=False, parent=self),
            NMOS("t3764", [self.port['gnd'].netconn,self.netlist['n1629'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3952", [self.port['gnd'].netconn,self.netlist['n1609'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3481", [self.netlist['n1092'],self.port['gnd'].netconn,self.netlist['n1368']], isweak=False, parent=self),
            NMOS("t619", [self.netlist['pcl0'],self.netlist['pcl0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2680", [self.netlist['n2808'],self.netlist['n763'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t2682", [self.port['gnd'].netconn,self.netlist['n2808'],self.netlist['n791']], isweak=False, parent=self),
            NMOS("t2684", [self.netlist['n2809'],self.netlist['n763'],self.netlist['n764']], isweak=False, parent=self),
            NMOS("t2686", [self.netlist['n764'],self.port['gnd'].netconn,self.netlist['n718']], isweak=False, parent=self),
            NMOS("t1950", [self.port['gnd'].netconn,self.netlist['n2747'],self.netlist['adda6']], isweak=False, parent=self),
            NMOS("t2688", [self.netlist['n436'],self.netlist['n2810'],self.netlist['n471']], isweak=False, parent=self),
            NMOS("t612", [self.netlist['pcl1'],self.netlist['pcl1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t615", [self.netlist['pcl2'],self.netlist['pcl2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1956", [self.netlist['n2764'],self.netlist['n2763'],self.netlist['addb6']], isweak=False, parent=self),
            NMOS("t2371", [self.netlist['n674'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2373", [self.netlist['n674'],self.port['gnd'].netconn,self.netlist['n679']], isweak=False, parent=self),
            NMOS("t2372", [self.netlist['n675'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2374", [self.netlist['n675'],self.port['gnd'].netconn,self.netlist['n680']], isweak=False, parent=self),
            NMOS("t2376", [self.port['db2'].netconn,self.port['gnd'].netconn,self.netlist['n679']], isweak=False, parent=self),
            NMOS("t4648", [self.netlist['n1603'],self.netlist['n1419'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4647", [self.netlist['n1823'],self.netlist['n1405'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3178", [self.port['gnd'].netconn,self.netlist['n977'],self.netlist['n1341']], isweak=False, parent=self),
            NMOS("t3179", [self.netlist['n978'],self.netlist['n861'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4646", [self.netlist['n1520'],self.netlist['n1421'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3174", [self.netlist['n4'],self.port['gnd'].netconn,self.netlist['Tr8']], isweak=False, parent=self),
            NMOS("t3175", [self.netlist['n977'],self.port['gnd'].netconn,self.netlist['n1363']], isweak=False, parent=self),
            NMOS("t3176", [self.netlist['n977'],self.port['gnd'].netconn,self.netlist['n1434']], isweak=False, parent=self),
            NMOS("t3177", [self.netlist['n4'],self.port['gnd'].netconn,self.netlist['n965']], isweak=False, parent=self),
            NMOS("t3170", [self.netlist['n767'],self.netlist['n2861'],self.netlist['n1388']], isweak=False, parent=self),
            NMOS("t3171", [self.netlist['n976'],self.port['gnd'].netconn,self.netlist['n977']], isweak=False, parent=self),
            NMOS("t3539", [self.netlist['n1120'],self.netlist['n1117'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5050", [self.netlist['n1483'],self.netlist['n1484'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2879", [self.netlist['n709'],self.netlist['n2826'],self.netlist['n969']], isweak=False, parent=self),
            NMOS("t505", [self.netlist['n701'],self.netlist['n122'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t504", [self.netlist['n121'],self.netlist['n120'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t507", [self.netlist['n126'],self.netlist['n125'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t506", [self.netlist['n124'],self.netlist['n123'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t501", [self.netlist['n110'],self.port['gnd'].netconn,self.netlist['n1663']], isweak=False, parent=self),
            NMOS("t500", [self.netlist['n109'],self.port['gnd'].netconn,self.netlist['n1664']], isweak=False, parent=self),
            NMOS("t503", [self.port['gnd'].netconn,self.netlist['n112'],self.netlist['n1674']], isweak=False, parent=self),
            NMOS("t502", [self.netlist['n111'],self.port['gnd'].netconn,self.netlist['n1652']], isweak=False, parent=self),
            NMOS("t509", [self.netlist['n129'],self.netlist['n130'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t508", [self.netlist['n128'],self.netlist['n127'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3499", [self.netlist['n1101'],self.netlist['n479'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1338", [self.netlist['ixh2'],self.netlist['idb2'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t2199", [self.netlist['n620'],self.port['gnd'].netconn,self.netlist['sumab6']], isweak=False, parent=self),
            NMOS("t5053", [self.netlist['n1486'],self.netlist['n1487'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2195", [self.port['gnd'].netconn,self.netlist['n2786'],self.netlist['n580']], isweak=False, parent=self),
            NMOS("t2197", [self.port['gnd'].netconn,self.netlist['n619'],self.netlist['n620']], isweak=False, parent=self),
            NMOS("t2191", [self.port['gnd'].netconn,self.netlist['n621'],self.netlist['sumab7']], isweak=False, parent=self),
            NMOS("t2193", [self.netlist['n619'],self.netlist['n2786'],self.netlist['sumab6']], isweak=False, parent=self),
            NMOS("t2192", [self.port['gnd'].netconn,self.netlist['n621'],self.netlist['n579']], isweak=False, parent=self),
            NMOS("t2753", [self.netlist['n792'],self.port['gnd'].netconn,self.netlist['n1022']], isweak=False, parent=self),
            NMOS("t2752", [self.port['gnd'].netconn,self.netlist['n793'],self.netlist['n1063']], isweak=False, parent=self),
            NMOS("t2751", [self.netlist['n792'],self.port['gnd'].netconn,self.netlist['n1355']], isweak=False, parent=self),
            NMOS("t1889", [self.port['gnd'].netconn,self.netlist['n533'],self.netlist['n287']], isweak=False, parent=self),
            NMOS("t2209", [self.netlist['n624'],self.netlist['n2788'],self.netlist['sumab4']], isweak=False, parent=self),
            NMOS("t2208", [self.port['gnd'].netconn,self.netlist['n626'],self.netlist['n583']], isweak=False, parent=self),
            NMOS("t2979", [self.netlist['n897'],self.netlist['n896'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2754", [self.netlist['n793'],self.port['gnd'].netconn,self.netlist['n1430']], isweak=False, parent=self),
            NMOS("t2205", [self.port['gnd'].netconn,self.netlist['n623'],self.netlist['n626']], isweak=False, parent=self),
            NMOS("t2976", [self.port['gnd'].netconn,self.netlist['n893'],self.netlist['n898']], isweak=False, parent=self),
            NMOS("t2207", [self.port['gnd'].netconn,self.netlist['n626'],self.netlist['sumab5']], isweak=False, parent=self),
            NMOS("t1881", [self.netlist['n531'],self.port['gnd'].netconn,self.netlist['n537']], isweak=False, parent=self),
            NMOS("t2201", [self.netlist['n623'],self.netlist['n2787'],self.netlist['sumab5']], isweak=False, parent=self),
            NMOS("t2200", [self.netlist['n620'],self.port['gnd'].netconn,self.netlist['n580']], isweak=False, parent=self),
            NMOS("t2203", [self.port['gnd'].netconn,self.netlist['n2787'],self.netlist['n583']], isweak=False, parent=self),
            NMOS("t1234", [self.netlist['idb4'],self.port['gnd'].netconn,self.netlist['n309']], isweak=False, parent=self),
            NMOS("t308", [self.port['gnd'].netconn,self.netlist['n73'],self.netlist['abl1']], isweak=False, parent=self),
            NMOS("t1112", [self.port['gnd'].netconn,self.netlist['spl3'],self.netlist['n1743']], isweak=False, parent=self),
            NMOS("t3330", [self.netlist['n1041'],self.port['gnd'].netconn,self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t1408", [self.netlist['ixh6'],self.netlist['ixh6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3001", [self.port['gnd'].netconn,self.netlist['n2837'],self.netlist['n917']], isweak=False, parent=self),
            NMOS("t1404", [self.port['gnd'].netconn,self.netlist['ixh7'],self.netlist['n1781']], isweak=False, parent=self),
            NMOS("t1405", [self.port['gnd'].netconn,self.netlist['n1781'],self.netlist['ixh7_1']], isweak=False, parent=self),
            NMOS("t1402", [self.netlist['ixh7'],self.netlist['ixh7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3550", [self.port['gnd'].netconn,self.netlist['n2914'],self.netlist['n1112']], isweak=False, parent=self),
            NMOS("t1400", [self.netlist['idb7'],self.netlist['accb7_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t2995", [self.netlist['Tg2'],self.netlist['n909'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1330", [self.netlist['ixl0_1'],self.netlist['abl0'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t2997", [self.netlist['n912'],self.netlist['n910'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3003", [self.netlist['Tg5'],self.port['gnd'].netconn,self.netlist['n913']], isweak=False, parent=self),
            NMOS("t2991", [self.netlist['n2835'],self.netlist['n125'],self.netlist['n1329']], isweak=False, parent=self),
            NMOS("t2990", [self.netlist['n2836'],self.port['gnd'].netconn,self.netlist['n1329']], isweak=False, parent=self),
            NMOS("t2993", [self.netlist['n907'],self.netlist['n2836'],self.netlist['n909']], isweak=False, parent=self),
            NMOS("t1331", [self.netlist['abl0'],self.netlist['ablx0'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t2999", [self.port['gnd'].netconn,self.netlist['n912'],self.netlist['n800']], isweak=False, parent=self),
            NMOS("t1332", [self.netlist['ablx0'],self.netlist['ixh0'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t4588", [self.port['gnd'].netconn,self.netlist['n1518'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4589", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1080", [self.netlist['idb7'],self.netlist['tmp7'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t1081", [self.netlist['spl7'],self.netlist['spl7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1086", [self.netlist['spl5'],self.netlist['abl5'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t1087", [self.netlist['spl4'],self.netlist['abl4'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t1084", [self.netlist['spl7'],self.netlist['abl7'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t1085", [self.netlist['spl6'],self.netlist['abl6'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t4580", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1334", [self.netlist['idb2'],self.netlist['ixl2_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1088", [self.netlist['spl3'],self.netlist['abl3'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t1089", [self.netlist['spl2'],self.netlist['abl2'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t4584", [self.port['gnd'].netconn,self.netlist['n1535'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4585", [self.port['gnd'].netconn,self.netlist['n1846'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4586", [self.port['gnd'].netconn,self.netlist['n1505'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t962", [self.port['vcc'].netconn,self.netlist['abh0'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t981", [self.port['vcc'].netconn,self.netlist['abh7'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t980", [self.port['vcc'].netconn,self.netlist['abh6'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t983", [self.port['vcc'].netconn,self.netlist['idb7'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t982", [self.port['vcc'].netconn,self.netlist['abl7'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t985", [self.port['gnd'].netconn,self.netlist['n269'],self.netlist['abh5']], isweak=False, parent=self),
            NMOS("t984", [self.port['gnd'].netconn,self.netlist['n268'],self.netlist['abh7']], isweak=False, parent=self),
            NMOS("t987", [self.port['gnd'].netconn,self.netlist['n271'],self.netlist['abh1']], isweak=False, parent=self),
            NMOS("t986", [self.port['gnd'].netconn,self.netlist['n270'],self.netlist['abh3']], isweak=False, parent=self),
            NMOS("t989", [self.netlist['n275'],self.port['gnd'].netconn,self.netlist['abh4']], isweak=False, parent=self),
            NMOS("t988", [self.netlist['n272'],self.port['gnd'].netconn,self.netlist['abh6']], isweak=False, parent=self),
            NMOS("t4212", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t960", [self.port['vcc'].netconn,self.netlist['idb0'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t4214", [self.port['gnd'].netconn,self.netlist['n1603'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4215", [self.port['gnd'].netconn,self.netlist['n1790'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4216", [self.port['gnd'].netconn,self.netlist['n1612'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4217", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4566", [self.netlist['n1810'],self.netlist['n1389'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1510", [self.netlist['accb5'],self.netlist['accb5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4564", [self.netlist['n1808'],self.netlist['n1387'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4565", [self.netlist['n1809'],self.netlist['n1388'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4562", [self.netlist['n1806'],self.netlist['n1385'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4563", [self.netlist['n1807'],self.netlist['n1386'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4560", [self.netlist['n1804'],self.netlist['n1383'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4561", [self.netlist['n1805'],self.netlist['n1384'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t5017", [self.port['vcc'].netconn,self.netlist['n1839'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4568", [self.netlist['n1812'],self.netlist['n1391'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4569", [self.netlist['n1813'],self.netlist['n1392'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1538", [self.port['gnd'].netconn,self.netlist['n1712'],self.netlist['accb1_1']], isweak=False, parent=self),
            NMOS("t5016", [self.port['vcc'].netconn,self.netlist['n1620'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5011", [self.port['vcc'].netconn,self.netlist['n1797'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1530", [self.netlist['accb1'],self.netlist['accb1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1531", [self.netlist['accb2'],self.netlist['accb2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1536", [self.port['gnd'].netconn,self.netlist['n1705'],self.netlist['accb2_1']], isweak=False, parent=self),
            NMOS("t1537", [self.port['gnd'].netconn,self.netlist['accb2'],self.netlist['n1705']], isweak=False, parent=self),
            NMOS("t5057", [self.port['gnd'].netconn,self.netlist['n1487'],self.netlist['n1470']], isweak=False, parent=self),
            NMOS("t4549", [self.netlist['n1790'],self.netlist['n1372'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3822", [self.netlist['n2938'],self.netlist['n1212'],self.netlist['n1215']], isweak=False, parent=self),
            NMOS("t4018", [self.port['gnd'].netconn,self.netlist['n1520'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4019", [self.port['gnd'].netconn,self.netlist['n1614'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t3820", [self.netlist['n1209'],self.netlist['n1183'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4104", [self.netlist['n1236'],self.netlist['n1229'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4016", [self.port['gnd'].netconn,self.netlist['n1612'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t3821", [self.port['gnd'].netconn,self.netlist['n2938'],self.netlist['n1210']], isweak=False, parent=self),
            NMOS("t4100", [self.port['gnd'].netconn,self.netlist['n1238'],self.netlist['n849']], isweak=False, parent=self),
            NMOS("t4101", [self.netlist['ba_0'],self.port['gnd'].netconn,self.netlist['n1230']], isweak=False, parent=self),
            NMOS("t4102", [self.port['gnd'].netconn,self.netlist['n1236'],self.netlist['n1231']], isweak=False, parent=self),
            NMOS("t4545", [self.netlist['n1638'],self.netlist['n1369'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4108", [self.netlist['n1233'],self.netlist['n1230'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1163", [self.netlist['sph5'],self.netlist['abh5'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1690", [self.netlist['n404'],self.port['gnd'].netconn,self.port['db4'].netconn], isweak=False, parent=self),
            NMOS("t1165", [self.netlist['sph3'],self.netlist['abh3'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t3825", [self.netlist['n1213'],self.netlist['n1210'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1164", [self.netlist['sph4'],self.netlist['abh4'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1626", [self.port['gnd'].netconn,self.netlist['idb2'],self.netlist['n375']], isweak=False, parent=self),
            NMOS("t1627", [self.netlist['n2742'],self.port['gnd'].netconn,self.netlist['acca4']], isweak=False, parent=self),
            NMOS("t1624", [self.port['gnd'].netconn,self.netlist['n383'],self.netlist['flagh']], isweak=False, parent=self),
            NMOS("t1625", [self.port['gnd'].netconn,self.netlist['idb3'],self.netlist['n376']], isweak=False, parent=self),
            NMOS("t4010", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t1620", [self.netlist['n385'],self.port['gnd'].netconn,self.netlist['n382']], isweak=False, parent=self),
            NMOS("t1621", [self.netlist['n2743'],self.port['gnd'].netconn,self.netlist['n382']], isweak=False, parent=self),
            NMOS("t4011", [self.port['gnd'].netconn,self.netlist['n1827'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t1628", [self.port['gnd'].netconn,self.netlist['n2744'],self.netlist['acca2']], isweak=False, parent=self),
            NMOS("t1629", [self.netlist['n2744'],self.port['gnd'].netconn,self.netlist['acca1']], isweak=False, parent=self),
            NMOS("t3410", [self.netlist['n2899'],self.port['gnd'].netconn,self.netlist['n1339']], isweak=False, parent=self),
            NMOS("t192", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n44']], isweak=False, parent=self),
            NMOS("t4360", [self.netlist['n1293'],self.port['gnd'].netconn,self.netlist['n1248']], isweak=False, parent=self),
            NMOS("t4362", [self.port['gnd'].netconn,self.netlist['n1305'],self.netlist['n1448']], isweak=False, parent=self),
            NMOS("t4363", [self.netlist['n1306'],self.port['gnd'].netconn,self.netlist['n1168']], isweak=False, parent=self),
            NMOS("t4365", [self.netlist['n1306'],self.port['gnd'].netconn,self.netlist['n1307']], isweak=False, parent=self),
            NMOS("t4367", [self.port['rw'].netconn,self.port['gnd'].netconn,self.netlist['n1307']], isweak=False, parent=self),
            NMOS("t4369", [self.port['gnd'].netconn,self.netlist['n1307'],self.netlist['n1168']], isweak=False, parent=self),
            NMOS("t2026", [self.netlist['n567'],self.port['gnd'].netconn,self.netlist['adda1']], isweak=False, parent=self),
            NMOS("t4968", [self.port['vcc'].netconn,self.netlist['n1614'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4969", [self.port['vcc'].netconn,self.netlist['n1833'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4962", [self.port['vcc'].netconn,self.netlist['n1509'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4963", [self.port['vcc'].netconn,self.netlist['n1791'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4960", [self.port['vcc'].netconn,self.netlist['n1613'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4961", [self.port['vcc'].netconn,self.netlist['n1832'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4966", [self.port['vcc'].netconn,self.netlist['n1520'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4967", [self.port['vcc'].netconn,self.netlist['n1800'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4964", [self.port['vcc'].netconn,self.netlist['n1604'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4965", [self.port['vcc'].netconn,self.netlist['n1824'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1060", [self.port['gnd'].netconn,self.netlist['tmp0'],self.netlist['n1733']], isweak=False, parent=self),
            NMOS("t183", [self.port['gnd'].netconn,self.port['ab9'].netconn,self.netlist['n40']], isweak=False, parent=self),
            NMOS("t182", [self.port['ab10'].netconn,self.port['gnd'].netconn,self.netlist['n39']], isweak=False, parent=self),
            NMOS("t349", [self.netlist['n5'],self.port['gnd'].netconn,self.netlist['enrwa']], isweak=False, parent=self),
            NMOS("t348", [self.netlist['ald0_0'],self.netlist['obl0'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t1190", [self.netlist['sph5'],self.port['gnd'].netconn,self.netlist['n1750']], isweak=False, parent=self),
            NMOS("t345", [self.port['gnd'].netconn,self.netlist['n6'],self.netlist['n81']], isweak=False, parent=self),
            NMOS("t342", [self.netlist['n7'],self.port['gnd'].netconn,self.netlist['n83']], isweak=False, parent=self),
            NMOS("t341", [self.netlist['n1672'],self.netlist['n76'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t340", [self.netlist['n73'],self.netlist['n1673'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t2681", [self.port['gnd'].netconn,self.netlist['n2809'],self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t1192", [self.port['gnd'].netconn,self.netlist['sph4'],self.netlist['n1747']], isweak=False, parent=self),
            NMOS("t4495", [self.netlist['n1505'],self.netlist['n1320'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t5000", [self.port['vcc'].netconn,self.netlist['n1619'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3360", [self.port['gnd'].netconn,self.netlist['n1035'],self.netlist['n989']], isweak=False, parent=self),
            NMOS("t3363", [self.netlist['n1030'],self.port['gnd'].netconn,self.netlist['n1032']], isweak=False, parent=self),
            NMOS("t3365", [self.netlist['n1030'],self.netlist['n1031'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3364", [self.netlist['n1033'],self.port['gnd'].netconn,self.netlist['n1031']], isweak=False, parent=self),
            NMOS("t3366", [self.netlist['n1033'],self.netlist['n1037'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3368", [self.port['gnd'].netconn,self.netlist['n1048'],self.netlist['n1050']], isweak=False, parent=self),
            NMOS("t1424", [self.netlist['ixh3'],self.port['gnd'].netconn,self.netlist['n1715']], isweak=False, parent=self),
            NMOS("t1953", [self.port['gnd'].netconn,self.netlist['n542'],self.netlist['addb6']], isweak=False, parent=self),
            NMOS("t4163", [self.port['gnd'].netconn,self.netlist['n1605'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1954", [self.netlist['n2763'],self.netlist['n547'],self.netlist['adda6']], isweak=False, parent=self),
            NMOS("t72", [self.port['gnd'].netconn,self.netlist['n23'],self.netlist['obl4']], isweak=False, parent=self),
            NMOS("t73", [self.port['gnd'].netconn,self.netlist['n24'],self.netlist['obl1']], isweak=False, parent=self),
            NMOS("t70", [self.port['gnd'].netconn,self.netlist['n21'],self.netlist['obl0']], isweak=False, parent=self),
            NMOS("t71", [self.port['gnd'].netconn,self.netlist['n22'],self.netlist['obl2']], isweak=False, parent=self),
            NMOS("t76", [self.port['gnd'].netconn,self.netlist['n21'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t77", [self.port['gnd'].netconn,self.netlist['n22'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t74", [self.port['gnd'].netconn,self.netlist['n25'],self.netlist['obl3']], isweak=False, parent=self),
            NMOS("t75", [self.port['gnd'].netconn,self.netlist['n26'],self.netlist['obl5']], isweak=False, parent=self),
            NMOS("t4166", [self.port['gnd'].netconn,self.netlist['n1531'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t78", [self.port['gnd'].netconn,self.netlist['n23'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t79", [self.port['gnd'].netconn,self.netlist['n24'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t3677", [self.netlist['n1176'],self.port['gnd'].netconn,self.netlist['n1177']], isweak=False, parent=self),
            NMOS("t3969", [self.port['gnd'].netconn,self.netlist['n1807'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3968", [self.port['gnd'].netconn,self.netlist['n1527'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t1422", [self.port['gnd'].netconn,self.netlist['ixh4'],self.netlist['n1721']], isweak=False, parent=self),
            NMOS("t3676", [self.netlist['n1175'],self.netlist['n1174'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3963", [self.port['gnd'].netconn,self.netlist['n1816'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3962", [self.port['gnd'].netconn,self.netlist['n1838'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3961", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t4165", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t3967", [self.port['gnd'].netconn,self.netlist['n1849'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3966", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3965", [self.port['gnd'].netconn,self.netlist['n1797'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3964", [self.port['gnd'].netconn,self.netlist['n1629'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t2564", [self.netlist['n726'],self.netlist['n2797'],self.netlist['n646']], isweak=False, parent=self),
            NMOS("t4905", [self.netlist['n1477'],self.port['gnd'].netconn,self.port['nmi'].netconn], isweak=False, parent=self),
            NMOS("t763", [self.netlist['inch4'],self.netlist['pch4_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t762", [self.netlist['inch3'],self.netlist['abh3'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t2560", [self.netlist['n165'],self.port['gnd'].netconn,self.netlist['n719']], isweak=False, parent=self),
            NMOS("t764", [self.netlist['inch3'],self.netlist['pch3_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t767", [self.netlist['inch6'],self.netlist['abh6'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t5069", [self.port['gnd'].netconn,self.netlist['n1484'],self.netlist['n1493']], isweak=False, parent=self),
            NMOS("t769", [self.netlist['inch6'],self.netlist['pch6_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t768", [self.netlist['inch5'],self.netlist['abh5'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t2568", [self.port['gnd'].netconn,self.netlist['n2798'],self.netlist['n724']], isweak=False, parent=self),
            NMOS("t2569", [self.netlist['n2798'],self.port['gnd'].netconn,self.netlist['n727']], isweak=False, parent=self),
            NMOS("t5028", [self.port['vcc'].netconn,self.netlist['n1621'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t163", [self.netlist['n41'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t3671", [self.netlist['n2934'],self.port['gnd'].netconn,self.netlist['n1192']], isweak=False, parent=self),
            NMOS("t3569", [self.port['gnd'].netconn,self.netlist['n2916'],self.netlist['n1136']], isweak=False, parent=self),
            NMOS("t3567", [self.port['gnd'].netconn,self.netlist['n2915'],self.netlist['n1404']], isweak=False, parent=self),
            NMOS("t3566", [self.netlist['n2915'],self.netlist['n868'],self.netlist['n945']], isweak=False, parent=self),
            NMOS("t3564", [self.netlist['n1130'],self.netlist['n1131'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3563", [self.netlist['n1122'],self.port['gnd'].netconn,self.netlist['n1110']], isweak=False, parent=self),
            NMOS("t3562", [self.netlist['n1122'],self.port['gnd'].netconn,self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3561", [self.port['gnd'].netconn,self.netlist['n1122'],self.netlist['n1131']], isweak=False, parent=self),
            NMOS("t3560", [self.netlist['n1128'],self.netlist['n1129'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3769", [self.port['gnd'].netconn,self.netlist['n1519'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3768", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3819", [self.netlist['n990'],self.netlist['n1788'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3818", [self.netlist['n2937'],self.netlist['n1205'],self.netlist['n846']], isweak=False, parent=self),
            NMOS("t3817", [self.port['gnd'].netconn,self.netlist['n2937'],self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t3816", [self.netlist['n1204'],self.port['gnd'].netconn,self.netlist['n1201']], isweak=False, parent=self),
            NMOS("t3767", [self.port['gnd'].netconn,self.netlist['n1847'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3814", [self.port['gnd'].netconn,self.netlist['n2937'],self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t3761", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3760", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3811", [self.netlist['n1'],self.port['gnd'].netconn,self.netlist['n1148']], isweak=False, parent=self),
            NMOS("t3762", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3585", [self.netlist['n2919'],self.netlist['n937'],self.netlist['n1324']], isweak=False, parent=self),
            NMOS("t3584", [self.netlist['n2919'],self.port['gnd'].netconn,self.netlist['Tg0']], isweak=False, parent=self),
            NMOS("t3587", [self.port['gnd'].netconn,self.netlist['n1140'],self.netlist['n1352']], isweak=False, parent=self),
            NMOS("t3581", [self.netlist['n2918'],self.netlist['n939'],self.netlist['n1387']], isweak=False, parent=self),
            NMOS("t3583", [self.port['gnd'].netconn,self.netlist['n2918'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3582", [self.port['gnd'].netconn,self.netlist['n2919'],self.netlist['Tg1']], isweak=False, parent=self),
            NMOS("t2", [self.port['gnd'].netconn,self.netlist['n14'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2994", [self.netlist['n907'],self.netlist['n906'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3589", [self.port['gnd'].netconn,self.netlist['n2920'],self.netlist['n1375']], isweak=False, parent=self),
            NMOS("t3588", [self.netlist['n2920'],self.netlist['n935'],self.netlist['Tg1']], isweak=False, parent=self),
            NMOS("t3", [self.netlist['n15'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2692", [self.port['gnd'].netconn,self.netlist['n765'],self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t2693", [self.netlist['n765'],self.port['gnd'].netconn,self.netlist['n763']], isweak=False, parent=self),
            NMOS("t2690", [self.netlist['n2810'],self.netlist['n2811'],self.netlist['n468']], isweak=False, parent=self),
            NMOS("t2691", [self.netlist['n2811'],self.port['gnd'].netconn,self.netlist['n434']], isweak=False, parent=self),
            NMOS("t2696", [self.netlist['Tg0'],self.netlist['n770'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3679", [self.netlist['n1175'],self.port['gnd'].netconn,self.netlist['n1176']], isweak=False, parent=self),
            NMOS("t2694", [self.netlist['n767'],self.netlist['n766'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2699", [self.port['gnd'].netconn,self.netlist['Tg1'],self.netlist['n771']], isweak=False, parent=self),
            NMOS("t2362", [self.port['db2'].netconn,self.port['vcc'].netconn,self.netlist['n674']], isweak=False, parent=self),
            NMOS("t2360", [self.port['db5'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2367", [self.port['db3'].netconn,self.port['vcc'].netconn,self.netlist['n675']], isweak=False, parent=self),
            NMOS("t1909", [self.netlist['n2756'],self.netlist['n2755'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t3109", [self.netlist['n956'],self.port['gnd'].netconn,self.netlist['n1381']], isweak=False, parent=self),
            NMOS("t3108", [self.port['gnd'].netconn,self.netlist['n2855'],self.netlist['n1428']], isweak=False, parent=self),
            NMOS("t3484", [self.netlist['n1093'],self.port['gnd'].netconn,self.netlist['n1345']], isweak=False, parent=self),
            NMOS("t3101", [self.netlist['n2854'],self.netlist['n904'],self.netlist['n950']], isweak=False, parent=self),
            NMOS("t3103", [self.netlist['n953'],self.port['gnd'].netconn,self.netlist['n952']], isweak=False, parent=self),
            NMOS("t3102", [self.netlist['n951'],self.netlist['n952'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3106", [self.netlist['n2855'],self.netlist['n951'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3073", [self.netlist['n2849'],self.netlist['n2848'],self.netlist['n1326']], isweak=False, parent=self),
            NMOS("t3072", [self.netlist['n2848'],self.port['gnd'].netconn,self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t573", [self.netlist['pcl7'],self.netlist['abl7'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t574", [self.netlist['pcl6'],self.netlist['abl6'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t575", [self.netlist['pcl5'],self.netlist['abl5'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t576", [self.netlist['pcl4'],self.netlist['abl4'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t577", [self.netlist['pcl3'],self.netlist['abl3'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t578", [self.netlist['pcl2'],self.netlist['abl2'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t579", [self.netlist['pcl1'],self.netlist['abl1'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t1565", [self.port['gnd'].netconn,self.netlist['acca6'],self.netlist['n1731']], isweak=False, parent=self),
            NMOS("t2189", [self.port['gnd'].netconn,self.netlist['n618'],self.netlist['n621']], isweak=False, parent=self),
            NMOS("t2187", [self.port['gnd'].netconn,self.netlist['n2785'],self.netlist['n579']], isweak=False, parent=self),
            NMOS("t2184", [self.netlist['n618'],self.netlist['n2784'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2185", [self.netlist['n618'],self.netlist['n2785'],self.netlist['sumab7']], isweak=False, parent=self),
            NMOS("t2182", [self.netlist['n623'],self.netlist['n2782'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2183", [self.netlist['n619'],self.netlist['n2783'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2180", [self.netlist['n628'],self.netlist['n2780'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2181", [self.netlist['n624'],self.netlist['n2781'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2968", [self.netlist['n888'],self.netlist['n889'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3614", [self.netlist['n2924'],self.netlist['n1152'],self.netlist['n1351']], isweak=False, parent=self),
            NMOS("t3617", [self.netlist['n1151'],self.port['gnd'].netconn,self.netlist['n1330']], isweak=False, parent=self),
            NMOS("t3616", [self.port['gnd'].netconn,self.netlist['n1150'],self.netlist['n1401']], isweak=False, parent=self),
            NMOS("t2748", [self.netlist['n464'],self.port['gnd'].netconn,self.netlist['n924']], isweak=False, parent=self),
            NMOS("t3610", [self.netlist['n2922'],self.port['gnd'].netconn,self.netlist['n960']], isweak=False, parent=self),
            NMOS("t3613", [self.port['gnd'].netconn,self.netlist['n1148'],self.netlist['n928']], isweak=False, parent=self),
            NMOS("t2219", [self.port['gnd'].netconn,self.netlist['n2789'],self.netlist['n587']], isweak=False, parent=self),
            NMOS("t2216", [self.netlist['n625'],self.port['gnd'].netconn,self.netlist['n584']], isweak=False, parent=self),
            NMOS("t2217", [self.netlist['n628'],self.netlist['n2789'],self.netlist['sumab3']], isweak=False, parent=self),
            NMOS("t2746", [self.netlist['n464'],self.port['gnd'].netconn,self.netlist['Tr4']], isweak=False, parent=self),
            NMOS("t2963", [self.netlist['n2834'],self.port['gnd'].netconn,self.netlist['Tg1']], isweak=False, parent=self),
            NMOS("t2740", [self.netlist['n535'],self.port['gnd'].netconn,self.netlist['n789']], isweak=False, parent=self),
            NMOS("t2213", [self.port['gnd'].netconn,self.netlist['n624'],self.netlist['n625']], isweak=False, parent=self),
            NMOS("t2966", [self.netlist['n886'],self.netlist['n2834'],self.netlist['n1358']], isweak=False, parent=self),
            NMOS("t2211", [self.port['gnd'].netconn,self.netlist['n2788'],self.netlist['n584']], isweak=False, parent=self),
            NMOS("t888", [self.netlist['n225'],self.netlist['n2716'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t889", [self.netlist['n94'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1439", [self.port['gnd'].netconn,self.netlist['ixh0'],self.netlist['n1706']], isweak=False, parent=self),
            NMOS("t3002", [self.netlist['Tg5'],self.netlist['n800'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t880", [self.port['gnd'].netconn,self.netlist['n2724'],self.netlist['n186']], isweak=False, parent=self),
            NMOS("t881", [self.netlist['n210'],self.netlist['n2709'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t882", [self.netlist['n222'],self.netlist['n2710'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1430", [self.netlist['ixh2'],self.netlist['ixh2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1437", [self.netlist['ixh0'],self.netlist['ixh0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t885", [self.netlist['n220'],self.netlist['n2713'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1435", [self.port['gnd'].netconn,self.netlist['n1714'],self.netlist['ixh1_1']], isweak=False, parent=self),
            NMOS("t887", [self.netlist['n221'],self.netlist['n2715'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2986", [self.netlist['Tr3'],self.netlist['n902'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2987", [self.netlist['n903'],self.netlist['n904'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2984", [self.netlist['n827'],self.netlist['Tr4'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2985", [self.netlist['Tr5'],self.netlist['n900'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2982", [self.netlist['Tr6'],self.netlist['n895'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2983", [self.netlist['n886'],self.netlist['n898'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2980", [self.netlist['Tr6'],self.port['gnd'].netconn,self.netlist['n896']], isweak=False, parent=self),
            NMOS("t2988", [self.port['gnd'].netconn,self.netlist['n2835'],self.netlist['Tg0']], isweak=False, parent=self),
            NMOS("t4923", [self.port['vcc'].netconn,self.netlist['n1826'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t408", [self.netlist['n77'],self.port['gnd'].netconn,self.netlist['n49']], isweak=False, parent=self),
            NMOS("t409", [self.port['gnd'].netconn,self.netlist['incli0_0'],self.netlist['n50']], isweak=False, parent=self),
            NMOS("t404", [self.port['gnd'].netconn,self.netlist['n1663'],self.netlist['n77']], isweak=False, parent=self),
            NMOS("t405", [self.netlist['n77'],self.port['gnd'].netconn,self.netlist['n45']], isweak=False, parent=self),
            NMOS("t407", [self.netlist['incli2_0'],self.port['gnd'].netconn,self.netlist['n49']], isweak=False, parent=self),
            NMOS("t401", [self.netlist['n1664'],self.netlist['n1666'],self.netlist['incli6_0']], isweak=False, parent=self),
            NMOS("t402", [self.netlist['n1665'],self.netlist['n1664'],self.netlist['incli5_0']], isweak=False, parent=self),
            NMOS("t403", [self.netlist['n1665'],self.netlist['n1663'],self.netlist['incli4_0']], isweak=False, parent=self),
            NMOS("t1983", [self.port['gnd'].netconn,self.netlist['n549'],self.netlist['addb4']], isweak=False, parent=self),
            NMOS("t5027", [self.port['vcc'].netconn,self.netlist['n1807'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1980", [self.port['gnd'].netconn,self.netlist['n2752'],self.netlist['adda4']], isweak=False, parent=self),
            NMOS("t978", [self.port['vcc'].netconn,self.netlist['idb6'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t979", [self.port['vcc'].netconn,self.netlist['abl6'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t1329", [self.netlist['idb0'],self.netlist['ixl0_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1984", [self.netlist['n2767'],self.netlist['n555'],self.netlist['adda4']], isweak=False, parent=self),
            NMOS("t974", [self.port['vcc'].netconn,self.netlist['abh4'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t975", [self.port['vcc'].netconn,self.netlist['abh5'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t976", [self.port['vcc'].netconn,self.netlist['abl5'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t977", [self.port['vcc'].netconn,self.netlist['idb5'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t970", [self.port['vcc'].netconn,self.netlist['abl3'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t971", [self.port['vcc'].netconn,self.netlist['idb3'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t1321", [self.netlist['ixh6_1'],self.netlist['idb6'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t973", [self.port['vcc'].netconn,self.netlist['abl4'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t4553", [self.netlist['n1795'],self.netlist['n1376'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1506", [self.netlist['accb7'],self.netlist['accb7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4551", [self.netlist['n1793'],self.netlist['n1374'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1056", [self.netlist['tmp1'],self.netlist['tmp1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1051", [self.port['gnd'].netconn,self.netlist['n1739'],self.netlist['tmp2_1']], isweak=False, parent=self),
            NMOS("t1502", [self.netlist['accb5'],self.netlist['ablx5'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t1053", [self.netlist['tmp2'],self.netlist['tmp2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1500", [self.netlist['accb3'],self.netlist['ablx3'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t4005", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4004", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4559", [self.netlist['n1802'],self.netlist['n1382'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4558", [self.netlist['n1801'],self.netlist['n1381'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1059", [self.netlist['n1736'],self.port['gnd'].netconn,self.netlist['tmp1_1']], isweak=False, parent=self),
            NMOS("t4000", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4003", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t1508", [self.netlist['n1732'],self.port['gnd'].netconn,self.netlist['accb7_1']], isweak=False, parent=self),
            NMOS("t2298", [self.netlist['n651'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2299", [self.netlist['n651'],self.port['gnd'].netconn,self.netlist['dbi7']], isweak=False, parent=self),
            NMOS("t4484", [self.netlist['enrwa'],self.port['gnd'].netconn,self.netlist['n2']], isweak=False, parent=self),
            NMOS("t4489", [self.port['gnd'].netconn,self.netlist['enrwa'],self.netlist['n1508']], isweak=False, parent=self),
            NMOS("t5021", [self.port['vcc'].netconn,self.netlist['n1844'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4171", [self.port['gnd'].netconn,self.netlist['n1535'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4170", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4173", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4172", [self.port['gnd'].netconn,self.netlist['n1505'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4175", [self.port['gnd'].netconn,self.netlist['n1509'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4174", [self.port['gnd'].netconn,self.netlist['n1519'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4177", [self.port['gnd'].netconn,self.netlist['n1531'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4176", [self.port['gnd'].netconn,self.netlist['n1834'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t1183", [self.netlist['n1753'],self.port['gnd'].netconn,self.netlist['sph6_1']], isweak=False, parent=self),
            NMOS("t4178", [self.port['gnd'].netconn,self.netlist['n1532'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t1181", [self.port['gnd'].netconn,self.netlist['n1756'],self.netlist['sph7_1']], isweak=False, parent=self),
            NMOS("t1180", [self.port['gnd'].netconn,self.netlist['sph7'],self.netlist['n1756']], isweak=False, parent=self),
            NMOS("t1187", [self.netlist['sph5'],self.netlist['sph5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1902", [self.port['gnd'].netconn,self.netlist['sumab0'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t1184", [self.netlist['sph6'],self.netlist['sph6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t5024", [self.port['vcc'].netconn,self.netlist['n1630'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4520", [self.netlist['n1598'],self.netlist['n1094'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t5022", [self.port['vcc'].netconn,self.netlist['n1538'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1611", [self.port['gnd'].netconn,self.netlist['n2741'],self.netlist['acca5']], isweak=False, parent=self),
            NMOS("t1610", [self.port['gnd'].netconn,self.netlist['n2741'],self.netlist['acca6']], isweak=False, parent=self),
            NMOS("t1616", [self.netlist['n2741'],self.netlist['n2742'],self.netlist['n385']], isweak=False, parent=self),
            NMOS("t1614", [self.netlist['n2741'],self.netlist['n380'],self.netlist['acca7']], isweak=False, parent=self),
            NMOS("t3007", [self.netlist['n915'],self.netlist['n913'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1618", [self.netlist['n381'],self.netlist['n2743'],self.netlist['n383']], isweak=False, parent=self),
            NMOS("t5023", [self.port['vcc'].netconn,self.netlist['n1817'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4399", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4398", [self.port['gnd'].netconn,self.netlist['n1841'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t3008", [self.netlist['Tg4'],self.netlist['n917'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4395", [self.port['gnd'].netconn,self.netlist['n1617'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4394", [self.port['gnd'].netconn,self.netlist['n1608'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4397", [self.port['gnd'].netconn,self.netlist['n1809'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4396", [self.port['gnd'].netconn,self.netlist['n1836'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4391", [self.port['gnd'].netconn,self.netlist['n1851'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4390", [self.port['gnd'].netconn,self.netlist['n1845'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4393", [self.port['gnd'].netconn,self.netlist['n1793'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4392", [self.port['gnd'].netconn,self.netlist['n1513'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4957", [self.port['vcc'].netconn,self.netlist['n1823'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4956", [self.port['vcc'].netconn,self.netlist['n1603'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4955", [self.port['vcc'].netconn,self.netlist['n1790'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4954", [self.port['vcc'].netconn,self.netlist['n1506'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4953", [self.port['vcc'].netconn,self.netlist['n1831'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3009", [self.port['gnd'].netconn,self.netlist['n2838'],self.netlist['n1327']], isweak=False, parent=self),
            NMOS("t4951", [self.port['vcc'].netconn,self.netlist['n1798'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4950", [self.port['vcc'].netconn,self.netlist['n1518'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4959", [self.port['vcc'].netconn,self.netlist['n1799'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4958", [self.port['vcc'].netconn,self.netlist['n1519'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1879", [self.port['gnd'].netconn,self.netlist['n533'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t4385", [self.netlist['n1303'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t4970", [self.port['vcc'].netconn,self.netlist['n1510'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4383", [self.netlist['n1303'],self.netlist['ir0'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1925", [self.netlist['n571'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t5094", [self.port['gnd'].netconn,self.netlist['n1500'],self.netlist['n1499']], isweak=False, parent=self),
            NMOS("t5075", [self.netlist['n2943'],self.netlist['n1502'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1924", [self.netlist['n570'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t666", [self.netlist['n175'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1926", [self.netlist['n565'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t3069", [self.netlist['n941'],self.netlist['n940'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1921", [self.netlist['n563'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t161", [self.netlist['n40'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t1920", [self.netlist['n562'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t378", [self.netlist['n79'],self.port['gnd'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t1923", [self.netlist['n567'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t370", [self.port['gnd'].netconn,self.netlist['n2691'],self.netlist['n766']], isweak=False, parent=self),
            NMOS("t1922", [self.netlist['n557'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t376", [self.port['gnd'].netconn,self.netlist['n79'],self.netlist['n712']], isweak=False, parent=self),
            NMOS("t377", [self.port['gnd'].netconn,self.netlist['n1674'],self.netlist['n79']], isweak=False, parent=self),
            NMOS("t374", [self.netlist['n80'],self.port['gnd'].netconn,self.netlist['n712']], isweak=False, parent=self),
            NMOS("t375", [self.port['gnd'].netconn,self.netlist['n77'],self.netlist['n712']], isweak=False, parent=self),
            NMOS("t2546", [self.netlist['n2795'],self.netlist['n132'],self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t2750", [self.netlist['n793'],self.port['gnd'].netconn,self.netlist['n1385']], isweak=False, parent=self),
            NMOS("t2757", [self.port['gnd'].netconn,self.netlist['n2817'],self.netlist['n1378']], isweak=False, parent=self),
            NMOS("t282", [self.port['gnd'].netconn,self.netlist['n2687'],self.netlist['n1668']], isweak=False, parent=self),
            NMOS("t2977", [self.netlist['n897'],self.port['gnd'].netconn,self.netlist['n900']], isweak=False, parent=self),
            NMOS("t3370", [self.netlist['n1048'],self.netlist['n1045'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3371", [self.netlist['n1046'],self.port['gnd'].netconn,self.netlist['n1045']], isweak=False, parent=self),
            NMOS("t3376", [self.netlist['n2895'],self.port['gnd'].netconn,self.netlist['n1153']], isweak=False, parent=self),
            NMOS("t3377", [self.netlist['n1052'],self.netlist['n2896'],self.netlist['n1154']], isweak=False, parent=self),
            NMOS("t3374", [self.netlist['n1046'],self.netlist['n1047'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3375", [self.netlist['n1051'],self.netlist['n1050'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3378", [self.netlist['n1054'],self.netlist['n2895'],self.netlist['n1052']], isweak=False, parent=self),
            NMOS("t2291", [self.port['gnd'].netconn,self.netlist['n653'],self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t1880", [self.port['gnd'].netconn,self.netlist['idb0'],self.netlist['n533']], isweak=False, parent=self),
            NMOS("t2758", [self.netlist['n757'],self.netlist['n2817'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t1887", [self.netlist['n532'],self.port['gnd'].netconn,self.netlist['n534']], isweak=False, parent=self),
            NMOS("t3440", [self.port['gnd'].netconn,self.netlist['n1069'],self.netlist['n1334']], isweak=False, parent=self),
            NMOS("t1132", [self.netlist['idb2'],self.netlist['spl2_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t2971", [self.port['gnd'].netconn,self.netlist['n889'],self.netlist['n895']], isweak=False, parent=self),
            NMOS("t1885", [self.netlist['n531'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3442", [self.netlist['n1070'],self.netlist['n1071'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t4945", [self.port['vcc'].netconn,self.netlist['n1846'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t289", [self.port['gnd'].netconn,self.netlist['n66'],self.netlist['idb3']], isweak=False, parent=self),
            NMOS("t2510", [self.netlist['n84'],self.port['gnd'].netconn,self.netlist['Tx1']], isweak=False, parent=self),
            NMOS("t2513", [self.port['gnd'].netconn,self.netlist['n701'],self.netlist['n706']], isweak=False, parent=self),
            NMOS("t2512", [self.port['gnd'].netconn,self.netlist['n84'],self.netlist['n705']], isweak=False, parent=self),
            NMOS("t798", [self.netlist['n184'],self.port['gnd'].netconn,self.netlist['n250']], isweak=False, parent=self),
            NMOS("t799", [self.netlist['n1759'],self.netlist['n1758'],self.netlist['inchi1_0']], isweak=False, parent=self),
            NMOS("t2517", [self.netlist['n701'],self.port['gnd'].netconn,self.netlist['n849']], isweak=False, parent=self),
            NMOS("t2516", [self.netlist['n701'],self.port['gnd'].netconn,self.netlist['Tx0']], isweak=False, parent=self),
            NMOS("t794", [self.port['gnd'].netconn,self.netlist['inchi0_0'],self.netlist['n247']], isweak=False, parent=self),
            NMOS("t795", [self.netlist['n184'],self.port['gnd'].netconn,self.netlist['n247']], isweak=False, parent=self),
            NMOS("t796", [self.netlist['n1763'],self.netlist['n1759'],self.netlist['inchi2_0']], isweak=False, parent=self),
            NMOS("t797", [self.port['gnd'].netconn,self.netlist['inchi1_0'],self.netlist['n250']], isweak=False, parent=self),
            NMOS("t790", [self.port['gnd'].netconn,self.netlist['n184'],self.netlist['n249']], isweak=False, parent=self),
            NMOS("t791", [self.netlist['n1764'],self.port['gnd'].netconn,self.netlist['n184']], isweak=False, parent=self),
            NMOS("t792", [self.port['gnd'].netconn,self.netlist['inchi2_0'],self.netlist['n246']], isweak=False, parent=self),
            NMOS("t793", [self.port['gnd'].netconn,self.netlist['n184'],self.netlist['n246']], isweak=False, parent=self),
            NMOS("t4574", [self.netlist['n1821'],self.netlist['n1397'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t151", [self.netlist['n40'],self.port['gnd'].netconn,self.netlist['n807']], isweak=False, parent=self),
            NMOS("t157", [self.netlist['n38'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t154", [self.netlist['n41'],self.port['gnd'].netconn,self.netlist['n804']], isweak=False, parent=self),
            NMOS("t155", [self.port['ab11'].netconn,self.port['vcc'].netconn,self.netlist['n804']], isweak=False, parent=self),
            NMOS("t3570", [self.netlist['n2916'],self.netlist['n855'],self.netlist['n1352']], isweak=False, parent=self),
            NMOS("t3571", [self.netlist['n855'],self.netlist['n2917'],self.netlist['n1140']], isweak=False, parent=self),
            NMOS("t3572", [self.netlist['n2917'],self.port['gnd'].netconn,self.netlist['n1134']], isweak=False, parent=self),
            NMOS("t3573", [self.netlist['Tx0'],self.netlist['n1134'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3574", [self.netlist['n1136'],self.netlist['Tg3'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3576", [self.port['gnd'].netconn,self.netlist['n1138'],self.netlist['n1331']], isweak=False, parent=self),
            NMOS("t3577", [self.netlist['n1139'],self.port['gnd'].netconn,self.netlist['n1409']], isweak=False, parent=self),
            NMOS("t3808", [self.port['gnd'].netconn,self.netlist['n1853'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3809", [self.netlist['n1201'],self.netlist['n1205'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3778", [self.port['gnd'].netconn,self.netlist['n1602'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3779", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3800", [self.port['gnd'].netconn,self.netlist['n1533'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3777", [self.port['gnd'].netconn,self.netlist['n1535'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3774", [self.port['gnd'].netconn,self.netlist['n1522'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3775", [self.port['gnd'].netconn,self.netlist['n1529'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3804", [self.port['gnd'].netconn,self.netlist['n1632'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3773", [self.port['gnd'].netconn,self.netlist['n1513'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3806", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3807", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3596", [self.netlist['n1068'],self.netlist['n1147'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3594", [self.netlist['idb0'],self.netlist['n1143'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3595", [self.netlist['n1067'],self.netlist['n1144'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3592", [self.netlist['n1122'],self.port['gnd'].netconn,self.netlist['n1147']], isweak=False, parent=self),
            NMOS("t3593", [self.netlist['n1122'],self.port['gnd'].netconn,self.netlist['n1144']], isweak=False, parent=self),
            NMOS("t3591", [self.netlist['n1141'],self.netlist['n1570'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5037", [self.port['vcc'].netconn,self.netlist['n1850'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3598", [self.netlist['n2921'],self.netlist['n941'],self.netlist['Tg0']], isweak=False, parent=self),
            NMOS("t3599", [self.netlist['n2921'],self.port['gnd'].netconn,self.netlist['n1429']], isweak=False, parent=self),
            NMOS("t5044", [self.port['vcc'].netconn,self.netlist['n1639'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2540", [self.netlist['n710'],self.netlist['n714'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t5045", [self.port['vcc'].netconn,self.netlist['n1852'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2359", [self.port['db4'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2358", [self.netlist['n672'],self.port['gnd'].netconn,self.netlist['dbo5']], isweak=False, parent=self),
            NMOS("t2357", [self.netlist['n671'],self.port['gnd'].netconn,self.netlist['dbo4']], isweak=False, parent=self),
            NMOS("t2424", [self.port['ab13'].netconn,self.port['vcc'].netconn,self.netlist['n802']], isweak=False, parent=self),
            NMOS("t2427", [self.port['vcc'].netconn,self.port['ab15'].netconn,self.netlist['n801']], isweak=False, parent=self),
            NMOS("t5036", [self.port['vcc'].netconn,self.netlist['n1632'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2420", [self.netlist['n685'],self.port['gnd'].netconn,self.netlist['dbo1']], isweak=False, parent=self),
            NMOS("t2423", [self.port['vcc'].netconn,self.port['db7'].netconn,self.netlist['n653']], isweak=False, parent=self),
            NMOS("t2350", [self.port['db5'].netconn,self.port['gnd'].netconn,self.netlist['n672']], isweak=False, parent=self),
            NMOS("t3974", [self.port['gnd'].netconn,self.netlist['n1632'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3975", [self.port['gnd'].netconn,self.netlist['n1599'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3118", [self.netlist['n2858'],self.port['gnd'].netconn,self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t3977", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3970", [self.port['gnd'].netconn,self.netlist['n1534'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3971", [self.port['gnd'].netconn,self.netlist['n1813'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3972", [self.port['gnd'].netconn,self.netlist['n1845'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3973", [self.port['gnd'].netconn,self.netlist['n1598'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3112", [self.netlist['n2856'],self.port['gnd'].netconn,self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t3111", [self.netlist['n957'],self.netlist['n2856'],self.netlist['n1350']], isweak=False, parent=self),
            NMOS("t3116", [self.netlist['n957'],self.netlist['n2857'],self.netlist['n945']], isweak=False, parent=self),
            NMOS("t3979", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3114", [self.port['gnd'].netconn,self.netlist['n957'],self.netlist['n1411']], isweak=False, parent=self),
            NMOS("t3115", [self.netlist['n957'],self.port['gnd'].netconn,self.netlist['n1423']], isweak=False, parent=self),
            NMOS("t562", [self.netlist['incl5'],self.netlist['abl5'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t561", [self.netlist['incl6'],self.netlist['abl6'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t560", [self.netlist['incl5'],self.netlist['pcl5_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t566", [self.netlist['incl0'],self.netlist['abl0'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t565", [self.netlist['incl0'],self.netlist['pcl0_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t569", [self.netlist['incl7'],self.netlist['abl7'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t568", [self.netlist['incl7'],self.netlist['pcl7_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t2998", [self.netlist['Tg6'],self.port['gnd'].netconn,self.netlist['n910']], isweak=False, parent=self),
            NMOS("t2739", [self.netlist['n535'],self.port['gnd'].netconn,self.netlist['Tx1']], isweak=False, parent=self),
            NMOS("t3607", [self.netlist['n2923'],self.netlist['n1149'],self.netlist['n1152']], isweak=False, parent=self),
            NMOS("t2229", [self.port['gnd'].netconn,self.netlist['n629'],self.netlist['n630']], isweak=False, parent=self),
            NMOS("t3605", [self.netlist['n2922'],self.port['gnd'].netconn,self.netlist['n1169']], isweak=False, parent=self),
            NMOS("t3602", [self.netlist['n1148'],self.port['gnd'].netconn,self.netlist['n1203']], isweak=False, parent=self),
            NMOS("t3603", [self.netlist['n2923'],self.netlist['n2922'],self.netlist['n1374']], isweak=False, parent=self),
            NMOS("t3600", [self.netlist['n2921'],self.port['gnd'].netconn,self.netlist['n1335']], isweak=False, parent=self),
            NMOS("t3601", [self.netlist['n1148'],self.port['gnd'].netconn,self.netlist['n1204']], isweak=False, parent=self),
            NMOS("t2223", [self.port['gnd'].netconn,self.netlist['n631'],self.netlist['sumab3']], isweak=False, parent=self),
            NMOS("t2730", [self.port['gnd'].netconn,self.netlist['flagh'],self.netlist['n787']], isweak=False, parent=self),
            NMOS("t2221", [self.port['gnd'].netconn,self.netlist['n628'],self.netlist['n631']], isweak=False, parent=self),
            NMOS("t2227", [self.port['gnd'].netconn,self.netlist['n2790'],self.netlist['n588']], isweak=False, parent=self),
            NMOS("t2734", [self.netlist['n2815'],self.netlist['n788'],self.netlist['n944']], isweak=False, parent=self),
            NMOS("t2737", [self.port['gnd'].netconn,self.netlist['n2815'],self.netlist['n125']], isweak=False, parent=self),
            NMOS("t2224", [self.port['gnd'].netconn,self.netlist['n631'],self.netlist['n587']], isweak=False, parent=self),
            NMOS("t899", [self.netlist['ahd2_0'],self.port['gnd'].netconn,self.netlist['n263']], isweak=False, parent=self),
            NMOS("t898", [self.netlist['n2727'],self.port['gnd'].netconn,self.netlist['n263']], isweak=False, parent=self),
            NMOS("t893", [self.port['gnd'].netconn,self.netlist['ahd7_0'],self.netlist['n1780']], isweak=False, parent=self),
            NMOS("t1495", [self.port['gnd'].netconn,self.netlist['ixl0'],self.netlist['n1708']], isweak=False, parent=self),
            NMOS("t890", [self.netlist['n251'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t897", [self.netlist['ahd4_0'],self.port['gnd'].netconn,self.netlist['n262']], isweak=False, parent=self),
            NMOS("t896", [self.netlist['n2726'],self.port['gnd'].netconn,self.netlist['n262']], isweak=False, parent=self),
            NMOS("t895", [self.port['gnd'].netconn,self.netlist['ahd6_0'],self.netlist['n260']], isweak=False, parent=self),
            NMOS("t894", [self.port['gnd'].netconn,self.netlist['n2725'],self.netlist['n260']], isweak=False, parent=self),
            NMOS("t829", [self.netlist['n230'],self.port['gnd'].netconn,self.netlist['n1768']], isweak=False, parent=self),
            NMOS("t419", [self.port['gnd'].netconn,self.netlist['incli5_0'],self.netlist['n44']], isweak=False, parent=self),
            NMOS("t416", [self.netlist['incli6_0'],self.port['gnd'].netconn,self.netlist['n47']], isweak=False, parent=self),
            NMOS("t412", [self.netlist['n77'],self.port['gnd'].netconn,self.netlist['n46']], isweak=False, parent=self),
            NMOS("t411", [self.port['gnd'].netconn,self.netlist['incli1_0'],self.netlist['n46']], isweak=False, parent=self),
            NMOS("t410", [self.netlist['n77'],self.port['gnd'].netconn,self.netlist['n50']], isweak=False, parent=self),
            NMOS("t2645", [self.netlist['n751'],self.port['gnd'].netconn,self.netlist['n753']], isweak=False, parent=self),
            NMOS("t1339", [self.netlist['idb4'],self.netlist['ixl4_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t2647", [self.netlist['n751'],self.netlist['n750'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2646", [self.netlist['n458'],self.port['gnd'].netconn,self.netlist['n750']], isweak=False, parent=self),
            NMOS("t1998", [self.netlist['n559'],self.port['gnd'].netconn,self.netlist['addb3']], isweak=False, parent=self),
            NMOS("t2640", [self.netlist['n2806'],self.netlist['n424'],self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t969", [self.port['vcc'].netconn,self.netlist['abh3'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t968", [self.port['vcc'].netconn,self.netlist['abh2'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t967", [self.port['vcc'].netconn,self.netlist['abl2'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t966", [self.port['vcc'].netconn,self.netlist['idb2'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t965", [self.port['vcc'].netconn,self.netlist['idb1'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t1333", [self.netlist['ixh0'],self.netlist['idb0'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t1990", [self.port['gnd'].netconn,self.netlist['addb4'],self.netlist['n504']], isweak=False, parent=self),
            NMOS("t1335", [self.netlist['ixl2_1'],self.netlist['abl2'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t961", [self.port['vcc'].netconn,self.netlist['abl0'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t1993", [self.netlist['n2753'],self.netlist['sumab3'],self.netlist['addb3']], isweak=False, parent=self),
            NMOS("t1046", [self.netlist['tmp3'],self.netlist['tmp3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1511", [self.netlist['accb6'],self.netlist['accb6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t5039", [self.port['vcc'].netconn,self.netlist['n1819'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4583", [self.port['gnd'].netconn,self.netlist['n1622'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4548", [self.netlist['n1789'],self.netlist['n1371'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1043", [self.netlist['tmp4'],self.netlist['tmp4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1516", [self.port['gnd'].netconn,self.netlist['n1728'],self.netlist['accb6_1']], isweak=False, parent=self),
            NMOS("t1041", [self.port['gnd'].netconn,self.netlist['n1745'],self.netlist['tmp4_1']], isweak=False, parent=self),
            NMOS("t1518", [self.port['gnd'].netconn,self.netlist['n1724'],self.netlist['accb5_1']], isweak=False, parent=self),
            NMOS("t4017", [self.port['gnd'].netconn,self.netlist['n1506'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4014", [self.port['gnd'].netconn,self.netlist['n1836'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4015", [self.port['gnd'].netconn,self.netlist['n1530'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4012", [self.port['gnd'].netconn,self.netlist['n1803'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4013", [self.port['gnd'].netconn,self.netlist['n1617'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4542", [self.netlist['n1629'],self.netlist['n1366'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1049", [self.netlist['n1742'],self.port['gnd'].netconn,self.netlist['tmp3_1']], isweak=False, parent=self),
            NMOS("t4587", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4492", [self.netlist['enrwa'],self.port['gnd'].netconn,self.netlist['n1314']], isweak=False, parent=self),
            NMOS("t1195", [self.netlist['sph4'],self.netlist['sph4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4496", [self.netlist['n1506'],self.netlist['n1321'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1191", [self.port['gnd'].netconn,self.netlist['n1750'],self.netlist['sph5_1']], isweak=False, parent=self),
            NMOS("t4494", [self.netlist['n1481'],self.netlist['n1319'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1193", [self.port['gnd'].netconn,self.netlist['n1747'],self.netlist['sph4_1']], isweak=False, parent=self),
            NMOS("t4498", [self.netlist['n1513'],self.netlist['n1323'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4499", [self.netlist['n1514'],self.netlist['n1324'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1198", [self.netlist['sph3'],self.netlist['sph3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1310", [self.netlist['abh1'],self.netlist['ixh1_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t4162", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1425", [self.port['gnd'].netconn,self.netlist['n1715'],self.netlist['ixh3_1']], isweak=False, parent=self),
            NMOS("t4160", [self.port['gnd'].netconn,self.netlist['n1614'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1311", [self.netlist['abh2'],self.netlist['ixh2_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1420", [self.netlist['ixh4'],self.netlist['ixh4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4167", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4164", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1423", [self.port['gnd'].netconn,self.netlist['n1721'],self.netlist['ixh4_1']], isweak=False, parent=self),
            NMOS("t1316", [self.netlist['abh4'],self.netlist['ixh4_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t4168", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4169", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1317", [self.netlist['abh3'],self.netlist['ixh3_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t2771", [self.port['gnd'].netconn,self.netlist['n749'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t1314", [self.netlist['ixh4_1'],self.netlist['idb4'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t1315", [self.netlist['ixh3_1'],self.netlist['idb3'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t1936", [self.netlist['n2761'],self.netlist['n546'],self.netlist['adda7']], isweak=False, parent=self),
            NMOS("t4210", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1609", [self.port['gnd'].netconn,self.netlist['n384'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t4211", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1605", [self.netlist['n379'],self.netlist['n2740'],self.netlist['n384']], isweak=False, parent=self),
            NMOS("t1607", [self.netlist['n2740'],self.port['gnd'].netconn,self.netlist['n380']], isweak=False, parent=self),
            NMOS("t1600", [self.netlist['n376'],self.port['gnd'].netconn,self.netlist['flagn']], isweak=False, parent=self),
            NMOS("t4213", [self.port['gnd'].netconn,self.netlist['n1823'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1040", [self.port['gnd'].netconn,self.netlist['tmp4'],self.netlist['n1745']], isweak=False, parent=self),
            NMOS("t3533", [self.netlist['n2911'],self.port['gnd'].netconn,self.netlist['n1568']], isweak=False, parent=self),
            NMOS("t4533", [self.netlist['n1614'],self.netlist['n1357'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2555", [self.netlist['n719'],self.port['gnd'].netconn,self.netlist['n721']], isweak=False, parent=self),
            NMOS("t4388", [self.port['gnd'].netconn,self.netlist['n1534'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4389", [self.port['gnd'].netconn,self.netlist['n1813'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4386", [self.netlist['n1303'],self.port['gnd'].netconn,self.netlist['n1249']], isweak=False, parent=self),
            NMOS("t4387", [self.netlist['n1305'],self.netlist['ob'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2109", [self.port['gnd'].netconn,self.netlist['n589'],self.netlist['n563']], isweak=False, parent=self),
            NMOS("t2005", [self.netlist['addb3'],self.port['gnd'].netconn,self.netlist['n503']], isweak=False, parent=self),
            NMOS("t4380", [self.netlist['decode_1'],self.port['gnd'].netconn,self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4381", [self.netlist['ir0'],self.netlist['ir0_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t4409", [self.port['gnd'].netconn,self.netlist['n1605'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t2556", [self.port['gnd'].netconn,self.netlist['n157'],self.netlist['n720']], isweak=False, parent=self),
            NMOS("t4567", [self.netlist['n1811'],self.netlist['n1390'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2044", [self.netlist['n2775'],self.netlist['n571'],self.netlist['adda0']], isweak=False, parent=self),
            NMOS("t4532", [self.netlist['n1613'],self.netlist['n1356'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2550", [self.port['gnd'].netconn,self.netlist['n717'],self.netlist['n1192']], isweak=False, parent=self),
            NMOS("t4940", [self.port['vcc'].netconn,self.netlist['n1622'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4941", [self.port['vcc'].netconn,self.netlist['n1841'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4942", [self.port['vcc'].netconn,self.netlist['n1535'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4943", [self.port['vcc'].netconn,self.netlist['n1814'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4944", [self.port['vcc'].netconn,self.netlist['n1627'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t756", [self.netlist['inch1'],self.netlist['abh1'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t4946", [self.port['vcc'].netconn,self.netlist['n1505'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4947", [self.port['vcc'].netconn,self.netlist['n1789'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4948", [self.port['vcc'].netconn,self.netlist['n1602'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4949", [self.port['vcc'].netconn,self.netlist['n1822'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2552", [self.netlist['n720'],self.netlist['n719'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4535", [self.netlist['n1618'],self.netlist['n1359'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4605", [self.port['gnd'].netconn,self.netlist['n1531'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t3029", [self.netlist['n468'],self.netlist['n2842'],self.netlist['n1396']], isweak=False, parent=self),
            NMOS("t3439", [self.port['gnd'].netconn,self.netlist['n1069'],self.netlist['n1386']], isweak=False, parent=self),
            NMOS("t3482", [self.netlist['n1092'],self.port['gnd'].netconn,self.netlist['n1395']], isweak=False, parent=self),
            NMOS("t4206", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1519", [self.netlist['accb5'],self.port['gnd'].netconn,self.netlist['n1724']], isweak=False, parent=self),
            NMOS("t3438", [self.netlist['n1068'],self.port['gnd'].netconn,self.netlist['n1362']], isweak=False, parent=self),
            NMOS("t367", [self.port['gnd'].netconn,self.netlist['n11'],self.netlist['n1138']], isweak=False, parent=self),
            NMOS("t366", [self.netlist['n9'],self.port['gnd'].netconn,self.netlist['n849']], isweak=False, parent=self),
            NMOS("t361", [self.netlist['n8'],self.port['gnd'].netconn,self.netlist['n10']], isweak=False, parent=self),
            NMOS("t1932", [self.netlist['n538'],self.port['gnd'].netconn,self.netlist['adda7']], isweak=False, parent=self),
            NMOS("t362", [self.port['gnd'].netconn,self.netlist['n8'],self.netlist['n9']], isweak=False, parent=self),
            NMOS("t4534", [self.netlist['n1615'],self.netlist['n1358'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3384", [self.port['gnd'].netconn,self.netlist['n2896'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t369", [self.netlist['n2691'],self.netlist['Tg0'],self.netlist['n1139']], isweak=False, parent=self),
            NMOS("t368", [self.netlist['Tg0'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t3927", [self.port['gnd'].netconn,self.netlist['n1793'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3926", [self.port['gnd'].netconn,self.netlist['n1640'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2706", [self.netlist['n775'],self.port['gnd'].netconn,self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t3389", [self.netlist['n1054'],self.netlist['n2895'],self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t4930", [self.port['vcc'].netconn,self.netlist['n1514'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3924", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t4537", [self.netlist['n1620'],self.netlist['n1361'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3923", [self.port['gnd'].netconn,self.netlist['n1819'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3849", [self.port['gnd'].netconn,self.netlist['n1797'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t1539", [self.netlist['accb1'],self.port['gnd'].netconn,self.netlist['n1712']], isweak=False, parent=self),
            NMOS("t4478", [self.port['gnd'].netconn,self.netlist['n1178'],self.netlist['n1319']], isweak=False, parent=self),
            NMOS("t2768", [self.netlist['n2819'],self.port['gnd'].netconn,self.netlist['n1393']], isweak=False, parent=self),
            NMOS("t3920", [self.port['gnd'].netconn,self.netlist['n1818'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2641", [self.port['gnd'].netconn,self.netlist['n2806'],self.netlist['n1359']], isweak=False, parent=self),
            NMOS("t4479", [self.port['gnd'].netconn,self.netlist['n1168'],self.netlist['enrwa']], isweak=False, parent=self),
            NMOS("t3349", [self.netlist['n2891'],self.port['gnd'].netconn,self.netlist['n1049']], isweak=False, parent=self),
            NMOS("t3348", [self.port['gnd'].netconn,self.netlist['n1035'],self.netlist['n1049']], isweak=False, parent=self),
            NMOS("t3347", [self.port['gnd'].netconn,self.netlist['n2892'],self.netlist['n1027']], isweak=False, parent=self),
            NMOS("t3346", [self.port['gnd'].netconn,self.netlist['flagz'],self.netlist['n1579']], isweak=False, parent=self),
            NMOS("t3345", [self.netlist['flagz'],self.netlist['n1038'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3343", [self.netlist['n2892'],self.netlist['n1024'],self.netlist['n645']], isweak=False, parent=self),
            NMOS("t3342", [self.netlist['n2892'],self.netlist['n2891'],self.netlist['n1025']], isweak=False, parent=self),
            NMOS("t3341", [self.port['gnd'].netconn,self.netlist['n2890'],self.netlist['n989']], isweak=False, parent=self),
            NMOS("t3340", [self.netlist['n2890'],self.netlist['n2889'],self.netlist['n1158']], isweak=False, parent=self),
            NMOS("t3335", [self.netlist['n1044'],self.port['gnd'].netconn,self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t14", [self.netlist['n17'],self.port['gnd'].netconn,self.netlist['n25']], isweak=False, parent=self),
            NMOS("t10", [self.netlist['n15'],self.port['gnd'].netconn,self.netlist['n23']], isweak=False, parent=self),
            NMOS("t12", [self.netlist['n16'],self.port['gnd'].netconn,self.netlist['n24']], isweak=False, parent=self),
            NMOS("t5006", [self.port['vcc'].netconn,self.netlist['n1537'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2557", [self.netlist['n721'],self.netlist['n125'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2146", [self.netlist['n606'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2500", [self.netlist['n699'],self.netlist['n698'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2507", [self.netlist['n84'],self.port['gnd'].netconn,self.netlist['Tr8']], isweak=False, parent=self),
            NMOS("t789", [self.netlist['n1767'],self.netlist['n1764'],self.netlist['inchi4_0']], isweak=False, parent=self),
            NMOS("t788", [self.netlist['n1768'],self.netlist['n1767'],self.netlist['inchi5_0']], isweak=False, parent=self),
            NMOS("t787", [self.netlist['n1779'],self.netlist['n1768'],self.netlist['inchi6_0']], isweak=False, parent=self),
            NMOS("t2508", [self.netlist['n84'],self.port['gnd'].netconn,self.netlist['n700']], isweak=False, parent=self),
            NMOS("t2509", [self.netlist['n84'],self.port['gnd'].netconn,self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t783", [self.port['gnd'].netconn,self.netlist['inch6'],self.netlist['n215']], isweak=False, parent=self),
            NMOS("t782", [self.port['gnd'].netconn,self.netlist['inch7'],self.netlist['n211']], isweak=False, parent=self),
            NMOS("t781", [self.port['gnd'].netconn,self.netlist['inch4'],self.netlist['n216']], isweak=False, parent=self),
            NMOS("t780", [self.port['gnd'].netconn,self.netlist['inch5'],self.netlist['n212']], isweak=False, parent=self),
            NMOS("t633", [self.netlist['n159'],self.netlist['n123'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5007", [self.port['vcc'].netconn,self.netlist['n1816'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t148", [self.netlist['n39'],self.port['gnd'].netconn,self.netlist['n803']], isweak=False, parent=self),
            NMOS("t145", [self.netlist['n38'],self.port['gnd'].netconn,self.netlist['n1072']], isweak=False, parent=self),
            NMOS("t142", [self.port['ab10'].netconn,self.port['vcc'].netconn,self.netlist['n803']], isweak=False, parent=self),
            NMOS("t3298", [self.netlist['n2883'],self.netlist['n798'],self.netlist['n1332']], isweak=False, parent=self),
            NMOS("t3749", [self.port['gnd'].netconn,self.netlist['n1843'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t1971", [self.netlist['n2766'],self.netlist['n2765'],self.netlist['addb5']], isweak=False, parent=self),
            NMOS("t3743", [self.port['gnd'].netconn,self.netlist['n1810'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3290", [self.netlist['n2880'],self.netlist['n2881'],self.netlist['n1020']], isweak=False, parent=self),
            NMOS("t3741", [self.port['gnd'].netconn,self.netlist['n1834'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3740", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3747", [self.port['gnd'].netconn,self.netlist['n1516'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3746", [self.port['gnd'].netconn,self.netlist['n1628'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3297", [self.port['gnd'].netconn,self.netlist['n2883'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3296", [self.netlist['n943'],self.netlist['n2882'],self.netlist['n942']], isweak=False, parent=self),
            NMOS("t5004", [self.port['vcc'].netconn,self.netlist['n1624'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1030", [self.netlist['tmp6'],self.port['gnd'].netconn,self.netlist['n1751']], isweak=False, parent=self),
            NMOS("t873", [self.port['gnd'].netconn,self.netlist['n2717'],self.netlist['n1779']], isweak=False, parent=self),
            NMOS("t1975", [self.netlist['addb5'],self.port['gnd'].netconn,self.netlist['n505']], isweak=False, parent=self),
            NMOS("t5005", [self.port['vcc'].netconn,self.netlist['n1843'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3127", [self.port['gnd'].netconn,self.netlist['n883'],self.netlist['n1373']], isweak=False, parent=self),
            NMOS("t3125", [self.netlist['n959'],self.port['gnd'].netconn,self.netlist['n1349']], isweak=False, parent=self),
            NMOS("t3124", [self.port['gnd'].netconn,self.netlist['n959'],self.netlist['n1399']], isweak=False, parent=self),
            NMOS("t3122", [self.netlist['n958'],self.port['gnd'].netconn,self.netlist['n1421']], isweak=False, parent=self),
            NMOS("t3121", [self.netlist['n958'],self.port['gnd'].netconn,self.netlist['n1410']], isweak=False, parent=self),
            NMOS("t3120", [self.netlist['n958'],self.port['gnd'].netconn,self.netlist['n880']], isweak=False, parent=self),
            NMOS("t2341", [self.netlist['n666'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2342", [self.netlist['n667'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2435", [self.port['ab14'].netconn,self.port['vcc'].netconn,self.netlist['n805']], isweak=False, parent=self),
            NMOS("t2344", [self.netlist['n667'],self.port['gnd'].netconn,self.netlist['n672']], isweak=False, parent=self),
            NMOS("t2346", [self.port['db4'].netconn,self.port['gnd'].netconn,self.netlist['n671']], isweak=False, parent=self),
            NMOS("t3128", [self.netlist['n883'],self.port['gnd'].netconn,self.netlist['n1322']], isweak=False, parent=self),
            NMOS("t3901", [self.port['gnd'].netconn,self.netlist['n1842'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3900", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3903", [self.port['gnd'].netconn,self.netlist['n1847'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3902", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3905", [self.port['gnd'].netconn,self.netlist['n1532'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3904", [self.port['gnd'].netconn,self.netlist['n1838'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3907", [self.port['gnd'].netconn,self.netlist['n1843'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3906", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3909", [self.port['gnd'].netconn,self.netlist['n1629'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3908", [self.port['gnd'].netconn,self.netlist['n1816'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t5002", [self.port['vcc'].netconn,self.netlist['n1532'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t481", [self.port['gnd'].netconn,self.netlist['n101'],self.netlist['n109']], isweak=False, parent=self),
            NMOS("t2700", [self.netlist['n775'],self.port['gnd'].netconn,self.netlist['n1364']], isweak=False, parent=self),
            NMOS("t4069", [self.port['vcc'].netconn,self.netlist['sync'],self.netlist['n1240']], isweak=False, parent=self),
            NMOS("t3501", [self.netlist['n1103'],self.netlist['n1566'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4103", [self.netlist['ba_0'],self.port['gnd'].netconn,self.netlist['n1231']], isweak=False, parent=self),
            NMOS("t2702", [self.port['gnd'].netconn,self.netlist['n536'],self.netlist['Tr8']], isweak=False, parent=self),
            NMOS("t4332", [self.port['gnd'].netconn,self.netlist['n1296'],self.netlist['ir2']], isweak=False, parent=self),
            NMOS("t1878", [self.netlist['n530'],self.netlist['n414'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t559", [self.netlist['incl6'],self.netlist['pcl6_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t556", [self.netlist['incl3'],self.netlist['abl3'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t554", [self.netlist['incl3'],self.netlist['pcl3_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t555", [self.netlist['incl4'],self.netlist['abl4'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t553", [self.netlist['incl4'],self.netlist['pcl4_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t550", [self.netlist['incl1'],self.netlist['abl1'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t2235", [self.port['gnd'].netconn,self.netlist['n2791'],self.netlist['n591']], isweak=False, parent=self),
            NMOS("t2237", [self.port['gnd'].netconn,self.netlist['n633'],self.netlist['n636']], isweak=False, parent=self),
            NMOS("t2231", [self.netlist['n630'],self.port['gnd'].netconn,self.netlist['sumab2']], isweak=False, parent=self),
            NMOS("t2232", [self.netlist['n630'],self.port['gnd'].netconn,self.netlist['n588']], isweak=False, parent=self),
            NMOS("t2233", [self.netlist['n633'],self.netlist['n2791'],self.netlist['sumab1']], isweak=False, parent=self),
            NMOS("t2178", [self.netlist['n633'],self.netlist['n2778'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1857", [self.netlist['idb3_2'],self.port['gnd'].netconn,self.netlist['n514']], isweak=False, parent=self),
            NMOS("t2707", [self.netlist['n775'],self.port['gnd'].netconn,self.netlist['n788']], isweak=False, parent=self),
            NMOS("t2239", [self.port['gnd'].netconn,self.netlist['n636'],self.netlist['sumab1']], isweak=False, parent=self),
            NMOS("t1853", [self.port['gnd'].netconn,self.netlist['idb4_2'],self.netlist['n511']], isweak=False, parent=self),
            NMOS("t1852", [self.port['gnd'].netconn,self.netlist['n511'],self.netlist['idb4']], isweak=False, parent=self),
            NMOS("t3632", [self.port['gnd'].netconn,self.netlist['n1154'],self.netlist['n1156']], isweak=False, parent=self),
            NMOS("t2728", [self.netlist['n2814'],self.port['gnd'].netconn,self.netlist['n783']], isweak=False, parent=self),
            NMOS("t3630", [self.port['gnd'].netconn,self.netlist['n1154'],self.netlist['flagz']], isweak=False, parent=self),
            NMOS("t3636", [self.netlist['n2928'],self.netlist['n1155'],self.netlist['n1126']], isweak=False, parent=self),
            NMOS("t3635", [self.port['gnd'].netconn,self.netlist['n2928'],self.netlist['flagn']], isweak=False, parent=self),
            NMOS("t3634", [self.port['gnd'].netconn,self.netlist['n2928'],self.netlist['flagv']], isweak=False, parent=self),
            NMOS("t2722", [self.netlist['n781'],self.netlist['n2812'],self.netlist['n987']], isweak=False, parent=self),
            NMOS("t2723", [self.netlist['n781'],self.netlist['n2813'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t2720", [self.netlist['n778'],self.netlist['n483'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2721", [self.netlist['n779'],self.netlist['n780'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2726", [self.netlist['n781'],self.netlist['n2814'],self.netlist['n530']], isweak=False, parent=self),
            NMOS("t2258", [self.netlist['n645'],self.port['gnd'].netconn,self.netlist['sum4']], isweak=False, parent=self),
            NMOS("t2724", [self.netlist['n2812'],self.port['gnd'].netconn,self.netlist['n784']], isweak=False, parent=self),
            NMOS("t4314", [self.netlist['ir7'],self.netlist['ir7_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t1876", [self.netlist['n527'],self.netlist['n526'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2621", [self.netlist['n452'],self.netlist['n740'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4711", [self.netlist['n1450'],self.netlist['n1453'],self.netlist['n1449']], isweak=False, parent=self),
            NMOS("t580", [self.netlist['pcl0'],self.netlist['abl0'],self.netlist['n139']], isweak=False, parent=self),
            NMOS("t428", [self.netlist['n2697'],self.netlist['n114'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t429", [self.netlist['n2698'],self.netlist['n118'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t4715", [self.netlist['n1451'],self.netlist['n2940'],self.netlist['n1454']], isweak=False, parent=self),
            NMOS("t4717", [self.netlist['n1452'],self.port['gnd'].netconn,self.port['dbe'].netconn], isweak=False, parent=self),
            NMOS("t4716", [self.netlist['n2940'],self.netlist['n1305'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4718", [self.netlist['n1453'],self.port['gnd'].netconn,self.netlist['n1452']], isweak=False, parent=self),
            NMOS("t420", [self.netlist['incli4_0'],self.port['gnd'].netconn,self.netlist['n48']], isweak=False, parent=self),
            NMOS("t4312", [self.netlist['n1276'],self.netlist['ir7'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t426", [self.netlist['n2695'],self.netlist['n113'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t427", [self.netlist['n2696'],self.netlist['n117'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t424", [self.netlist['n2693'],self.netlist['n96'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t425", [self.netlist['n2694'],self.netlist['n116'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t2656", [self.port['gnd'].netconn,self.netlist['n460'],self.netlist['n954']], isweak=False, parent=self),
            NMOS("t958", [self.netlist['idb6'],self.netlist['tmp6_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t2655", [self.port['gnd'].netconn,self.netlist['n428'],self.netlist['n795']], isweak=False, parent=self),
            NMOS("t2710", [self.netlist['n775'],self.port['gnd'].netconn,self.netlist['n774']], isweak=False, parent=self),
            NMOS("t2653", [self.netlist['n426'],self.port['gnd'].netconn,self.netlist['n833']], isweak=False, parent=self),
            NMOS("t2650", [self.netlist['n426'],self.port['gnd'].netconn,self.netlist['Tx0']], isweak=False, parent=self),
            NMOS("t952", [self.netlist['idb0'],self.netlist['tmp0_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t953", [self.netlist['idb1'],self.netlist['tmp1_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t950", [self.netlist['n95'],self.port['gnd'].netconn,self.netlist['n251']], isweak=False, parent=self),
            NMOS("t956", [self.netlist['idb4'],self.netlist['tmp4_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t957", [self.netlist['idb5'],self.netlist['tmp5_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t954", [self.netlist['idb2'],self.netlist['tmp2_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t955", [self.netlist['idb3'],self.netlist['tmp3_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t1073", [self.netlist['idb1'],self.netlist['spl1'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t1072", [self.netlist['idb6'],self.netlist['tmp6'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t1071", [self.netlist['idb6'],self.netlist['spl6'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t1070", [self.netlist['idb4'],self.netlist['tmp4'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t1077", [self.netlist['idb5'],self.netlist['spl5'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t1076", [self.netlist['idb3'],self.netlist['tmp3'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t1075", [self.netlist['idb3'],self.netlist['spl3'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t1074", [self.netlist['idb1'],self.netlist['tmp1'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t4023", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4022", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t1079", [self.netlist['idb7'],self.netlist['spl7'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t1078", [self.netlist['idb5'],self.netlist['tmp5'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t4027", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4026", [self.port['gnd'].netconn,self.netlist['n1537'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4025", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4024", [self.port['gnd'].netconn,self.netlist['n1619'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t3651", [self.netlist['n1128'],self.netlist['n2932'],self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t3650", [self.netlist['n2931'],self.netlist['n1128'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t1451", [self.netlist['ixl5'],self.netlist['ablx5'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t1450", [self.netlist['ixl6'],self.netlist['ablx6'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t1453", [self.netlist['ixl3'],self.netlist['ablx3'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t1452", [self.netlist['ixl4'],self.netlist['ablx4'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t1455", [self.netlist['ixl1'],self.netlist['ablx1'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t1454", [self.netlist['ixl2'],self.netlist['ablx2'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t4159", [self.port['gnd'].netconn,self.netlist['n1520'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1456", [self.netlist['ixl0'],self.netlist['ablx0'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t4157", [self.port['gnd'].netconn,self.netlist['n1509'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1458", [self.netlist['ixl7'],self.netlist['ixl7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4155", [self.port['gnd'].netconn,self.netlist['n1506'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t3159", [self.port['gnd'].netconn,self.netlist['n2859'],self.netlist['n973']], isweak=False, parent=self),
            NMOS("t4153", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4152", [self.port['gnd'].netconn,self.netlist['n1505'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4151", [self.port['gnd'].netconn,self.netlist['n1814'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4150", [self.port['gnd'].netconn,self.netlist['n1622'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4445", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4444", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4447", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4446", [self.port['gnd'].netconn,self.netlist['n1828'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4441", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4440", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4443", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4442", [self.port['gnd'].netconn,self.netlist['n1536'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4449", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4448", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t1679", [self.netlist['n408'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1671", [self.netlist['n407'],self.netlist['n404'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1673", [self.netlist['n408'],self.port['gnd'].netconn,self.netlist['dbi4']], isweak=False, parent=self),
            NMOS("t5074", [self.netlist['n2942'],self.netlist['n2943'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1674", [self.netlist['n401'],self.port['gnd'].netconn,self.netlist['dbi3']], isweak=False, parent=self),
            NMOS("t1677", [self.netlist['n403'],self.port['vcc'].netconn,self.netlist['n401']], isweak=False, parent=self),
            NMOS("t1676", [self.port['vcc'].netconn,self.netlist['n407'],self.netlist['n408']], isweak=False, parent=self),
            NMOS("t4544", [self.netlist['n1632'],self.netlist['n1368'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1048", [self.port['gnd'].netconn,self.netlist['tmp3'],self.netlist['n1742']], isweak=False, parent=self),
            NMOS("t1745", [self.netlist['n468'],self.netlist['n469'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1744", [self.netlist['n466'],self.netlist['n467'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1050", [self.port['gnd'].netconn,self.netlist['tmp2'],self.netlist['n1739']], isweak=False, parent=self),
            NMOS("t5073", [self.port['irq'].netconn,self.netlist['n2942'],self.port['irq'].netconn], isweak=False, parent=self),
            NMOS("t3640", [self.netlist['n1157'],self.port['gnd'].netconn,self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t2715", [self.netlist['n776'],self.netlist['n479'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1705", [self.netlist['n415'],self.port['gnd'].netconn,self.netlist['n470']], isweak=False, parent=self),
            NMOS("t1704", [self.port['vcc'].netconn,self.netlist['ablx0'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1707", [self.netlist['n417'],self.port['gnd'].netconn,self.netlist['n437']], isweak=False, parent=self),
            NMOS("t1706", [self.port['gnd'].netconn,self.netlist['n416'],self.netlist['n469']], isweak=False, parent=self),
            NMOS("t1701", [self.port['vcc'].netconn,self.netlist['ablx3'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1700", [self.port['vcc'].netconn,self.netlist['ablx4'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1703", [self.port['vcc'].netconn,self.netlist['ablx1'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1702", [self.port['vcc'].netconn,self.netlist['ablx2'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1709", [self.netlist['n415'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1708", [self.netlist['n418'],self.port['gnd'].netconn,self.netlist['n435']], isweak=False, parent=self),
            NMOS("t4546", [self.netlist['n1639'],self.netlist['n1141'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3641", [self.netlist['n1157'],self.port['gnd'].netconn,self.netlist['n1155']], isweak=False, parent=self),
            NMOS("t5008", [self.port['vcc'].netconn,self.netlist['n1629'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4463", [self.port['gnd'].netconn,self.netlist['Ts'],self.netlist['n2']], isweak=False, parent=self),
            NMOS("t5071", [self.netlist['halt_0'],self.port['gnd'].netconn,self.port['halt'].netconn], isweak=False, parent=self),
            NMOS("t4547", [self.netlist['n1640'],self.netlist['n1370'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t314", [self.port['gnd'].netconn,self.netlist['ald0_0'],self.netlist['n1672']], isweak=False, parent=self),
            NMOS("t446", [self.port['gnd'].netconn,self.netlist['n2707'],self.netlist['n1652']], isweak=False, parent=self),
            NMOS("t316", [self.port['gnd'].netconn,self.netlist['n75'],self.netlist['idb0']], isweak=False, parent=self),
            NMOS("t317", [self.netlist['n76'],self.port['gnd'].netconn,self.netlist['abl0']], isweak=False, parent=self),
            NMOS("t2940", [self.port['gnd'].netconn,self.netlist['n873'],self.netlist['n878']], isweak=False, parent=self),
            NMOS("t4540", [self.netlist['n1626'],self.netlist['n1364'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4461", [self.port['gnd'].netconn,self.netlist['Ts'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t3119", [self.netlist['n958'],self.netlist['n2858'],self.netlist['n1357']], isweak=False, parent=self),
            NMOS("t4541", [self.netlist['n1628'],self.netlist['n1365'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3644", [self.netlist['n1158'],self.port['gnd'].netconn,self.netlist['n1165']], isweak=False, parent=self),
            NMOS("t686", [self.netlist['n185'],self.port['gnd'].netconn,self.netlist['n78']], isweak=False, parent=self),
            NMOS("t838", [self.netlist['n231'],self.port['gnd'].netconn,self.netlist['ahd4_0']], isweak=False, parent=self),
            NMOS("t4609", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t3358", [self.netlist['n1029'],self.netlist['n1032'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t228", [self.netlist['n46'],self.netlist['n2681'],self.netlist['ald1_0']], isweak=False, parent=self),
            NMOS("t224", [self.netlist['n44'],self.netlist['n2677'],self.netlist['ald5_0']], isweak=False, parent=self),
            NMOS("t3351", [self.port['gnd'].netconn,self.netlist['n1035'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t226", [self.netlist['n45'],self.netlist['n2679'],self.netlist['ald3_0']], isweak=False, parent=self),
            NMOS("t3353", [self.netlist['n1024'],self.netlist['n2894'],self.netlist['n1035']], isweak=False, parent=self),
            NMOS("t3354", [self.netlist['n2894'],self.port['gnd'].netconn,self.netlist['n1038']], isweak=False, parent=self),
            NMOS("t3355", [self.port['gnd'].netconn,self.netlist['n1035'],self.netlist['n1027']], isweak=False, parent=self),
            NMOS("t222", [self.netlist['n43'],self.netlist['n2675'],self.netlist['ald7_0']], isweak=False, parent=self),
            NMOS("t5038", [self.port['vcc'].netconn,self.netlist['n1599'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t529", [self.netlist['n135'],self.port['gnd'].netconn,self.netlist['n130']], isweak=False, parent=self),
            NMOS("t2170", [self.netlist['n2778'],self.netlist['n632'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t3744", [self.port['gnd'].netconn,self.netlist['n1842'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t831", [self.netlist['n232'],self.port['gnd'].netconn,self.netlist['n1759']], isweak=False, parent=self),
            NMOS("t4543", [self.netlist['n1630'],self.netlist['n1367'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t20", [self.port['ab0'].netconn,self.port['vcc'].netconn,self.netlist['n13']], isweak=False, parent=self),
            NMOS("t25", [self.port['vcc'].netconn,self.port['ab2'].netconn,self.netlist['n14']], isweak=False, parent=self),
            NMOS("t3934", [self.port['gnd'].netconn,self.netlist['n1841'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t4466", [self.netlist['n2939'],self.port['gnd'].netconn,self.netlist['n1222']], isweak=False, parent=self),
            NMOS("t596", [self.port['gnd'].netconn,self.netlist['pcl6'],self.netlist['n1773']], isweak=False, parent=self),
            NMOS("t2504", [self.netlist['n82'],self.port['gnd'].netconn,self.netlist['n84']], isweak=False, parent=self),
            NMOS("t523", [self.netlist['n134'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t522", [self.netlist['n135'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2891", [self.netlist['n2830'],self.port['gnd'].netconn,self.netlist['n1371']], isweak=False, parent=self),
            NMOS("t2539", [self.port['gnd'].netconn,self.netlist['n2794'],self.netlist['n9']], isweak=False, parent=self),
            NMOS("t2538", [self.netlist['n2794'],self.port['gnd'].netconn,self.netlist['n10']], isweak=False, parent=self),
            NMOS("t2537", [self.netlist['n2794'],self.netlist['n712'],self.netlist['n713']], isweak=False, parent=self),
            NMOS("t2535", [self.netlist['n713'],self.port['gnd'].netconn,self.netlist['n707']], isweak=False, parent=self),
            NMOS("t2534", [self.port['gnd'].netconn,self.netlist['n713'],self.netlist['n2']], isweak=False, parent=self),
            NMOS("t2533", [self.netlist['n710'],self.port['gnd'].netconn,self.netlist['n708']], isweak=False, parent=self),
            NMOS("t2532", [self.port['gnd'].netconn,self.netlist['n713'],self.netlist['n714']], isweak=False, parent=self),
            NMOS("t4465", [self.port['gnd'].netconn,self.netlist['Ts'],self.netlist['n1310']], isweak=False, parent=self),
            NMOS("t3754", [self.port['gnd'].netconn,self.netlist['n1807'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t139", [self.port['ab9'].netconn,self.port['vcc'].netconn,self.netlist['n807']], isweak=False, parent=self),
            NMOS("t3756", [self.port['gnd'].netconn,self.netlist['n1601'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3757", [self.port['gnd'].netconn,self.netlist['n1845'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3750", [self.port['gnd'].netconn,self.netlist['n1816'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3751", [self.port['gnd'].netconn,self.netlist['n1526'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3752", [self.port['gnd'].netconn,self.netlist['n1806'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3753", [self.port['gnd'].netconn,self.netlist['n1533'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3758", [self.port['gnd'].netconn,self.netlist['n1849'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3759", [self.port['gnd'].netconn,self.netlist['n1538'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t137", [self.port['ab8'].netconn,self.port['vcc'].netconn,self.netlist['n1072']], isweak=False, parent=self),
            NMOS("t5015", [self.port['vcc'].netconn,self.netlist['n1806'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3289", [self.netlist['n1019'],self.netlist['n2880'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3282", [self.port['gnd'].netconn,self.netlist['n1018'],self.netlist['n1424']], isweak=False, parent=self),
            NMOS("t3936", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3281", [self.netlist['n456'],self.netlist['n2879'],self.netlist['Tg1']], isweak=False, parent=self),
            NMOS("t3286", [self.netlist['n1956'],self.port['gnd'].netconn,self.netlist['n1338']], isweak=False, parent=self),
            NMOS("t3287", [self.port['gnd'].netconn,self.netlist['n1020'],self.netlist['n1431']], isweak=False, parent=self),
            NMOS("t3285", [self.netlist['n1956'],self.port['gnd'].netconn,self.netlist['n1390']], isweak=False, parent=self),
            NMOS("t1965", [self.port['gnd'].netconn,self.netlist['n2750'],self.netlist['adda5']], isweak=False, parent=self),
            NMOS("t2932", [self.netlist['n2832'],self.port['gnd'].netconn,self.netlist['n1336']], isweak=False, parent=self),
            NMOS("t5014", [self.port['vcc'].netconn,self.netlist['n1526'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1200", [self.port['gnd'].netconn,self.netlist['sph3'],self.netlist['n1744']], isweak=False, parent=self),
            NMOS("t2958", [self.netlist['n1952'],self.port['gnd'].netconn,self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t595", [self.netlist['pcl1'],self.port['gnd'].netconn,self.netlist['n1775']], isweak=False, parent=self),
            NMOS("t3015", [self.netlist['n924'],self.port['gnd'].netconn,self.netlist['n1385']], isweak=False, parent=self),
            NMOS("t3132", [self.netlist['n960'],self.port['gnd'].netconn,self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t2408", [self.port['db0'].netconn,self.port['gnd'].netconn,self.netlist['n684']], isweak=False, parent=self),
            NMOS("t3134", [self.netlist['Ta0'],self.port['gnd'].netconn,self.netlist['n1356']], isweak=False, parent=self),
            NMOS("t3135", [self.port['gnd'].netconn,self.netlist['Ta0'],self.netlist['n1380']], isweak=False, parent=self),
            NMOS("t3136", [self.netlist['Ta0'],self.port['gnd'].netconn,self.netlist['n1328']], isweak=False, parent=self),
            NMOS("t3137", [self.port['gnd'].netconn,self.netlist['Ta0'],self.netlist['n963']], isweak=False, parent=self),
            NMOS("t2403", [self.netlist['n681'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2894", [self.netlist['n2829'],self.port['gnd'].netconn,self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t2400", [self.port['db1'].netconn,self.port['vcc'].netconn,self.netlist['n682']], isweak=False, parent=self),
            NMOS("t2406", [self.netlist['n682'],self.port['gnd'].netconn,self.netlist['n685']], isweak=False, parent=self),
            NMOS("t2405", [self.netlist['n681'],self.port['gnd'].netconn,self.netlist['n684']], isweak=False, parent=self),
            NMOS("t2895", [self.port['gnd'].netconn,self.netlist['n846'],self.netlist['n1439']], isweak=False, parent=self),
            NMOS("t3912", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3913", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3910", [self.port['gnd'].netconn,self.netlist['n1848'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3911", [self.port['gnd'].netconn,self.netlist['n1797'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3916", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2896", [self.port['gnd'].netconn,self.netlist['n849'],self.netlist['n856']], isweak=False, parent=self),
            NMOS("t3914", [self.port['gnd'].netconn,self.netlist['n1533'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3915", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3918", [self.port['gnd'].netconn,self.netlist['n1534'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3919", [self.port['gnd'].netconn,self.netlist['n1813'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3468", [self.netlist['n1087'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t2393", [self.port['db0'].netconn,self.port['vcc'].netconn,self.netlist['n681']], isweak=False, parent=self),
            NMOS("t2392", [self.port['db0'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2391", [self.port['db1'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2390", [self.port['db3'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t4286", [self.port['gnd'].netconn,self.netlist['i2'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t549", [self.netlist['incl2'],self.netlist['abl2'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t548", [self.netlist['incl1'],self.netlist['pcl1_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t541", [self.netlist['incl5'],self.port['gnd'].netconn,self.netlist['n113']], isweak=False, parent=self),
            NMOS("t540", [self.port['gnd'].netconn,self.netlist['incl2'],self.netlist['n118']], isweak=False, parent=self),
            NMOS("t543", [self.netlist['incl7'],self.port['gnd'].netconn,self.netlist['n96']], isweak=False, parent=self),
            NMOS("t542", [self.port['gnd'].netconn,self.netlist['incl4'],self.netlist['n117']], isweak=False, parent=self),
            NMOS("t545", [self.port['gnd'].netconn,self.netlist['n140'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t544", [self.port['gnd'].netconn,self.netlist['incl6'],self.netlist['n116']], isweak=False, parent=self),
            NMOS("t547", [self.netlist['incl2'],self.netlist['pcl2_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t4282", [self.netlist['n1266'],self.port['gnd'].netconn,self.netlist['ir3_1']], isweak=False, parent=self),
            NMOS("t2241", [self.netlist['n634'],self.netlist['n2792'],self.netlist['sumab0']], isweak=False, parent=self),
            NMOS("t2240", [self.port['gnd'].netconn,self.netlist['n636'],self.netlist['n591']], isweak=False, parent=self),
            NMOS("t2243", [self.port['gnd'].netconn,self.netlist['n2792'],self.netlist['n592']], isweak=False, parent=self),
            NMOS("t2714", [self.port['gnd'].netconn,self.netlist['n486'],self.netlist['n776']], isweak=False, parent=self),
            NMOS("t2245", [self.port['gnd'].netconn,self.netlist['n634'],self.netlist['n635']], isweak=False, parent=self),
            NMOS("t2712", [self.port['gnd'].netconn,self.netlist['n486'],self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t2711", [self.port['gnd'].netconn,self.netlist['n774'],self.netlist['n535']], isweak=False, parent=self),
            NMOS("t1849", [self.netlist['idb5_2'],self.port['gnd'].netconn,self.netlist['n510']], isweak=False, parent=self),
            NMOS("t2248", [self.netlist['n635'],self.port['gnd'].netconn,self.netlist['n592']], isweak=False, parent=self),
            NMOS("t1844", [self.port['gnd'].netconn,self.netlist['n507'],self.netlist['idb6']], isweak=False, parent=self),
            NMOS("t1845", [self.port['gnd'].netconn,self.netlist['idb6_2'],self.netlist['n507']], isweak=False, parent=self),
            NMOS("t2719", [self.netlist['n1582'],self.netlist['idb5'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1841", [self.port['gnd'].netconn,self.netlist['idb7_2'],self.netlist['n506']], isweak=False, parent=self),
            NMOS("t2087", [self.netlist['n581'],self.port['gnd'].netconn,self.netlist['n547']], isweak=False, parent=self),
            NMOS("t4126", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t2085", [self.port['gnd'].netconn,self.netlist['n582'],self.netlist['n546']], isweak=False, parent=self),
            NMOS("t3748", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t2083", [self.port['gnd'].netconn,self.netlist['n595'],self.netlist['n582']], isweak=False, parent=self),
            NMOS("t598", [self.port['gnd'].netconn,self.netlist['pcl2'],self.netlist['n1771']], isweak=False, parent=self),
            NMOS("t2081", [self.netlist['n579'],self.netlist['n595'],self.netlist['sumab7']], isweak=False, parent=self),
            NMOS("t4127", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t3625", [self.port['gnd'].netconn,self.netlist['n1153'],self.netlist['n1157']], isweak=False, parent=self),
            NMOS("t3627", [self.netlist['n1153'],self.netlist['n2927'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t3620", [self.netlist['n2925'],self.port['gnd'].netconn,self.netlist['n1150']], isweak=False, parent=self),
            NMOS("t3621", [self.netlist['n1152'],self.netlist['n2926'],self.netlist['n1151']], isweak=False, parent=self),
            NMOS("t2089", [self.netlist['n579'],self.port['gnd'].netconn,self.netlist['n581']], isweak=False, parent=self),
            NMOS("t2088", [self.netlist['n580'],self.netlist['n579'],self.netlist['sumab6']], isweak=False, parent=self),
            NMOS("t4433", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4125", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t5010", [self.port['vcc'].netconn,self.netlist['n1517'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1289", [self.netlist['n321'],self.port['gnd'].netconn,self.netlist['n287']], isweak=False, parent=self),
            NMOS("t1856", [self.port['gnd'].netconn,self.netlist['n514'],self.netlist['idb3']], isweak=False, parent=self),
            NMOS("t4123", [self.port['gnd'].netconn,self.netlist['n1621'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t435", [self.netlist['n102'],self.netlist['n2696'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t434", [self.netlist['n98'],self.netlist['n2695'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t437", [self.netlist['n103'],self.netlist['n2698'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3117", [self.netlist['n2857'],self.port['gnd'].netconn,self.netlist['n1403']], isweak=False, parent=self),
            NMOS("t431", [self.netlist['n2700'],self.netlist['n119'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t430", [self.netlist['n2699'],self.netlist['n115'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t433", [self.netlist['n101'],self.netlist['n2694'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3742", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t4693", [self.netlist['n1844'],self.netlist['n1437'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t439", [self.netlist['n104'],self.netlist['n2700'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3293", [self.netlist['n2881'],self.port['gnd'].netconn,self.netlist['n1384']], isweak=False, parent=self),
            NMOS("t496", [self.netlist['n105'],self.port['gnd'].netconn,self.netlist['n1666']], isweak=False, parent=self),
            NMOS("t4702", [self.netlist['n1853'],self.netlist['n1446'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4703", [self.netlist['n788'],self.netlist['n1448'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4700", [self.netlist['n1851'],self.netlist['n1444'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4701", [self.netlist['n1852'],self.netlist['n1130'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4707", [self.port['gnd'].netconn,self.netlist['n1574'],self.netlist['n1450']], isweak=False, parent=self),
            NMOS("t5013", [self.port['vcc'].netconn,self.netlist['n1830'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2877", [self.port['gnd'].netconn,self.netlist['n123'],self.netlist['n840']], isweak=False, parent=self),
            NMOS("t3295", [self.port['gnd'].netconn,self.netlist['n943'],self.netlist['n1377']], isweak=False, parent=self),
            NMOS("t4709", [self.port['gnd'].netconn,self.netlist['n1449'],self.netlist['n1451']], isweak=False, parent=self),
            NMOS("t3294", [self.netlist['n2882'],self.port['gnd'].netconn,self.netlist['n1354']], isweak=False, parent=self),
            NMOS("t2663", [self.port['gnd'].netconn,self.netlist['n462'],self.netlist['n833']], isweak=False, parent=self),
            NMOS("t2661", [self.netlist['n755'],self.port['gnd'].netconn,self.netlist['n756']], isweak=False, parent=self),
            NMOS("t2660", [self.netlist['n754'],self.netlist['n755'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2667", [self.netlist['n759'],self.netlist['n749'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3745", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t2665", [self.netlist['n462'],self.port['gnd'].netconn,self.netlist['n759']], isweak=False, parent=self),
            NMOS("t2664", [self.netlist['n462'],self.port['gnd'].netconn,self.netlist['n754']], isweak=False, parent=self),
            NMOS("t2887", [self.netlist['n704'],self.port['gnd'].netconn,self.netlist['Tx0']], isweak=False, parent=self),
            NMOS("t2886", [self.port['gnd'].netconn,self.netlist['n2828'],self.netlist['n874']], isweak=False, parent=self),
            NMOS("t4550", [self.netlist['n1791'],self.netlist['n1373'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2884", [self.netlist['n704'],self.port['gnd'].netconn,self.netlist['Tg7']], isweak=False, parent=self),
            NMOS("t2883", [self.netlist['Ta2'],self.netlist['n881'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2882", [self.netlist['n2827'],self.port['gnd'].netconn,self.netlist['n874']], isweak=False, parent=self),
            NMOS("t2880", [self.netlist['n2826'],self.netlist['n2827'],self.netlist['n1320']], isweak=False, parent=self),
            NMOS("t5033", [self.port['vcc'].netconn,self.netlist['n1845'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5032", [self.port['vcc'].netconn,self.netlist['n1626'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4528", [self.netlist['n1608'],self.netlist['n1352'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4529", [self.netlist['n1609'],self.netlist['n1353'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1068", [self.netlist['idb2'],self.netlist['tmp2'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t1069", [self.netlist['idb4'],self.netlist['spl4'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t5035", [self.port['vcc'].netconn,self.netlist['n1818'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5034", [self.port['vcc'].netconn,self.netlist['n1598'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4522", [self.netlist['n1600'],self.netlist['n1346'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1065", [self.netlist['idb0'],self.netlist['spl0'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t1066", [self.netlist['idb0'],self.netlist['tmp0'],self.netlist['n173']], isweak=False, parent=self),
            NMOS("t1067", [self.netlist['idb2'],self.netlist['spl2'],self.netlist['n175']], isweak=False, parent=self),
            NMOS("t4526", [self.netlist['n1605'],self.netlist['n1350'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1061", [self.port['gnd'].netconn,self.netlist['n1733'],self.netlist['tmp0_1']], isweak=False, parent=self),
            NMOS("t4524", [self.netlist['n1602'],self.netlist['n1348'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1063", [self.netlist['tmp0'],self.netlist['tmp0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2865", [self.netlist['n1951'],self.port['gnd'].netconn,self.netlist['n1321']], isweak=False, parent=self),
            NMOS("t2864", [self.netlist['n2822'],self.port['gnd'].netconn,self.netlist['n965']], isweak=False, parent=self),
            NMOS("t2867", [self.netlist['n841'],self.netlist['n2823'],self.netlist['n1039']], isweak=False, parent=self),
            NMOS("t2866", [self.netlist['n841'],self.netlist['n1951'],self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t2860", [self.netlist['n840'],self.port['gnd'].netconn,self.netlist['n841']], isweak=False, parent=self),
            NMOS("t2863", [self.port['gnd'].netconn,self.netlist['n2822'],self.netlist['n1149']], isweak=False, parent=self),
            NMOS("t4557", [self.netlist['n1799'],self.netlist['n1380'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2869", [self.netlist['n2824'],self.port['gnd'].netconn,self.netlist['Tx2']], isweak=False, parent=self),
            NMOS("t2868", [self.netlist['n2823'],self.netlist['n2824'],self.netlist['n1426']], isweak=False, parent=self),
            NMOS("t4098", [self.port['gnd'].netconn,self.netlist['n1226'],self.netlist['n1238']], isweak=False, parent=self),
            NMOS("t4289", [self.port['gnd'].netconn,self.netlist['i2'],self.netlist['n1296']], isweak=False, parent=self),
            NMOS("t1442", [self.netlist['ixh6'],self.netlist['abh6'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1443", [self.netlist['ixh5'],self.netlist['abh5'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1440", [self.port['gnd'].netconn,self.netlist['n1706'],self.netlist['ixh0_1']], isweak=False, parent=self),
            NMOS("t1441", [self.netlist['ixh7'],self.netlist['abh7'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1446", [self.netlist['ixh2'],self.netlist['abh2'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1447", [self.netlist['ixh1'],self.netlist['abh1'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1444", [self.netlist['ixh4'],self.netlist['abh4'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1445", [self.netlist['ixh3'],self.netlist['abh3'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t4636", [self.netlist['n1518'],self.netlist['n1422'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4637", [self.netlist['n1627'],self.netlist['n1412'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1448", [self.netlist['ixh0'],self.netlist['abh0'],self.netlist['n327']], isweak=False, parent=self),
            NMOS("t1449", [self.netlist['ixl7'],self.netlist['ablx7'],self.netlist['n317']], isweak=False, parent=self),
            NMOS("t4632", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4633", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4630", [self.port['gnd'].netconn,self.netlist['n1638'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4147", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4456", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4457", [self.port['gnd'].netconn,self.netlist['n1622'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4454", [self.port['gnd'].netconn,self.netlist['n1799'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4455", [self.port['gnd'].netconn,self.netlist['n1831'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4452", [self.port['gnd'].netconn,self.netlist['n1824'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4453", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4450", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4451", [self.port['gnd'].netconn,self.netlist['n1520'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4301", [self.netlist['n1270'],self.port['gnd'].netconn,self.netlist['ir0_1']], isweak=False, parent=self),
            NMOS("t4458", [self.port['gnd'].netconn,self.netlist['n1803'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4459", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t1668", [self.netlist['n394'],self.port['gnd'].netconn,self.port['db5'].netconn], isweak=False, parent=self),
            NMOS("t4555", [self.netlist['n1797'],self.netlist['n1378'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1662", [self.netlist['n396'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1660", [self.port['vcc'].netconn,self.netlist['n398'],self.netlist['n396']], isweak=False, parent=self),
            NMOS("t1666", [self.netlist['n398'],self.netlist['n394'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1667", [self.netlist['idb5'],self.netlist['dbo5'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t1664", [self.netlist['dbi5'],self.port['gnd'].netconn,self.netlist['n398']], isweak=False, parent=self),
            NMOS("t1665", [self.netlist['idb5'],self.netlist['dbi5'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t4034", [self.port['gnd'].netconn,self.netlist['n1818'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4035", [self.port['gnd'].netconn,self.netlist['n1840'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4036", [self.port['gnd'].netconn,self.netlist['n1630'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4624", [self.port['gnd'].netconn,self.netlist['n1621'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4030", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4031", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4032", [self.port['gnd'].netconn,self.netlist['n1819'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4033", [self.port['gnd'].netconn,self.netlist['n1850'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4038", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4039", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4627", [self.port['gnd'].netconn,self.netlist['n1850'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1710", [self.netlist['n417'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3993", [self.port['gnd'].netconn,self.netlist['n1526'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t3079", [self.netlist['n944'],self.netlist['n2850'],self.netlist['n1435']], isweak=False, parent=self),
            NMOS("t3990", [self.port['gnd'].netconn,self.netlist['n1630'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t1718", [self.netlist['n760'],self.netlist['n420'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1719", [self.netlist['n421'],self.netlist['n422'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1374", [self.netlist['ixl4'],self.netlist['idb4'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t3991", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4233", [self.netlist['n1247'],self.netlist['n1248'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3996", [self.port['gnd'].netconn,self.netlist['n1610'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4230", [self.netlist['n1247'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t4626", [self.port['gnd'].netconn,self.netlist['n1598'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4608", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t3994", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t269", [self.port['gnd'].netconn,self.netlist['ald5_0'],self.netlist['n1661']], isweak=False, parent=self),
            NMOS("t5018", [self.port['vcc'].netconn,self.netlist['n1533'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4236", [self.netlist['n1252'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t3995", [self.port['gnd'].netconn,self.netlist['n1829'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4288", [self.netlist['n1198'],self.port['gnd'].netconn,self.netlist['ir2_1']], isweak=False, parent=self),
            NMOS("t4237", [self.netlist['n1251'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t2965", [self.port['gnd'].netconn,self.netlist['Tr7'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t307", [self.port['gnd'].netconn,self.netlist['n72'],self.netlist['idb1']], isweak=False, parent=self),
            NMOS("t4234", [self.netlist['n1254'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t305", [self.port['gnd'].netconn,self.netlist['ald1_0'],self.netlist['n1673']], isweak=False, parent=self),
            NMOS("t309", [self.port['gnd'].netconn,self.netlist['n2690'],self.netlist['n1672']], isweak=False, parent=self),
            NMOS("t4235", [self.netlist['n1253'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t730", [self.netlist['pch0'],self.port['gnd'].netconn,self.netlist['n1760']], isweak=False, parent=self),
            NMOS("t4603", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t731", [self.netlist['pch6'],self.netlist['pch6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4602", [self.port['gnd'].netconn,self.netlist['n1834'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1", [self.port['gnd'].netconn,self.netlist['n13'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t4601", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4859", [self.port['vcc'].netconn,self.netlist['n1508'],self.netlist['n1460']], isweak=False, parent=self),
            NMOS("t1473", [self.netlist['ixl3'],self.netlist['ixl3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4620", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4856", [self.port['gnd'].netconn,self.port['tsc'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t4857", [self.netlist['n1476'],self.port['gnd'].netconn,self.port['tsc'].netconn], isweak=False, parent=self),
            NMOS("t2029", [self.netlist['n2773'],self.netlist['n570'],self.netlist['adda1']], isweak=False, parent=self),
            NMOS("t842", [self.port['gnd'].netconn,self.netlist['n210'],self.netlist['n226']], isweak=False, parent=self),
            NMOS("t1470", [self.port['gnd'].netconn,self.netlist['ixl5'],self.netlist['n1726']], isweak=False, parent=self),
            NMOS("t3684", [self.port['gnd'].netconn,self.netlist['n1181'],self.netlist['n849']], isweak=False, parent=self),
            NMOS("t1125", [self.port['gnd'].netconn,self.netlist['n1734'],self.netlist['spl0_1']], isweak=False, parent=self),
            NMOS("t2343", [self.netlist['n666'],self.port['gnd'].netconn,self.netlist['n671']], isweak=False, parent=self),
            NMOS("t1124", [self.port['gnd'].netconn,self.netlist['spl0'],self.netlist['n1734']], isweak=False, parent=self),
            NMOS("t1594", [self.netlist['n374'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1127", [self.netlist['spl0'],self.netlist['spl0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3129", [self.netlist['n883'],self.port['gnd'].netconn,self.netlist['n1427']], isweak=False, parent=self),
            NMOS("t239", [self.netlist['n2684'],self.netlist['n47'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t238", [self.netlist['n2683'],self.netlist['n43'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t5009", [self.port['vcc'].netconn,self.netlist['n1848'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t236", [self.netlist['n50'],self.netlist['n2682'],self.netlist['ald0_0']], isweak=False, parent=self),
            NMOS("t234", [self.netlist['n49'],self.netlist['n2680'],self.netlist['ald2_0']], isweak=False, parent=self),
            NMOS("t232", [self.netlist['n48'],self.netlist['n2678'],self.netlist['ald4_0']], isweak=False, parent=self),
            NMOS("t230", [self.netlist['n47'],self.netlist['n2676'],self.netlist['ald6_0']], isweak=False, parent=self),
            NMOS("t1123", [self.netlist['n1737'],self.port['gnd'].netconn,self.netlist['spl1_1']], isweak=False, parent=self),
            NMOS("t1122", [self.port['gnd'].netconn,self.netlist['spl1'],self.netlist['n1737']], isweak=False, parent=self),
            NMOS("t38", [self.port['ab3'].netconn,self.port['vcc'].netconn,self.netlist['n17']], isweak=False, parent=self),
            NMOS("t1797", [self.netlist['n494'],self.port['gnd'].netconn,self.netlist['ablx6']], isweak=False, parent=self),
            NMOS("t35", [self.port['ab1'].netconn,self.port['vcc'].netconn,self.netlist['n16']], isweak=False, parent=self),
            NMOS("t30", [self.port['ab4'].netconn,self.port['vcc'].netconn,self.netlist['n15']], isweak=False, parent=self),
            NMOS("t1795", [self.port['gnd'].netconn,self.netlist['n495'],self.netlist['ablx7']], isweak=False, parent=self),
            NMOS("t3656", [self.netlist['flagc'],self.netlist['n1161'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4346", [self.netlist['ir1'],self.netlist['ir1_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t3519", [self.netlist['n1121'],self.netlist['n1568'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4347", [self.netlist['ir2'],self.netlist['ir2_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t2528", [self.netlist['n711'],self.port['gnd'].netconn,self.netlist['Tg0']], isweak=False, parent=self),
            NMOS("t2529", [self.netlist['n711'],self.port['gnd'].netconn,self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t4344", [self.netlist['n1295'],self.netlist['ir4'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3517", [self.netlist['n1121'],self.port['gnd'].netconn,self.netlist['n1093']], isweak=False, parent=self),
            NMOS("t2520", [self.netlist['n706'],self.netlist['n866'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2521", [self.netlist['n702'],self.netlist['n707'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2522", [self.netlist['n708'],self.netlist['n709'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4345", [self.netlist['n1293'],self.netlist['ir5'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2524", [self.netlist['n711'],self.port['gnd'].netconn,self.netlist['n715']], isweak=False, parent=self),
            NMOS("t2525", [self.netlist['n711'],self.port['gnd'].netconn,self.netlist['Tr8']], isweak=False, parent=self),
            NMOS("t2526", [self.netlist['n711'],self.port['gnd'].netconn,self.netlist['n700']], isweak=False, parent=self),
            NMOS("t2527", [self.netlist['n711'],self.port['gnd'].netconn,self.netlist['n833']], isweak=False, parent=self),
            NMOS("t3720", [self.netlist['n1193'],self.port['gnd'].netconn,self.netlist['n1174']], isweak=False, parent=self),
            NMOS("t3722", [self.netlist['n1192'],self.port['gnd'].netconn,self.netlist['n1193']], isweak=False, parent=self),
            NMOS("t3724", [self.port['gnd'].netconn,self.netlist['n1183'],self.netlist['n990']], isweak=False, parent=self),
            NMOS("t3727", [self.port['gnd'].netconn,self.netlist['n1513'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3726", [self.netlist['n1183'],self.port['gnd'].netconn,self.netlist['n1212']], isweak=False, parent=self),
            NMOS("t3729", [self.port['gnd'].netconn,self.netlist['n1835'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3728", [self.port['gnd'].netconn,self.netlist['n1522'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t4191", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4190", [self.port['gnd'].netconn,self.netlist['n1819'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t3042", [self.port['gnd'].netconn,self.netlist['n483'],self.netlist['n1396']], isweak=False, parent=self),
            NMOS("t4197", [self.port['gnd'].netconn,self.netlist['n1621'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t3511", [self.netlist['n1109'],self.netlist['n1123'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1490", [self.netlist['ixl1'],self.port['gnd'].netconn,self.netlist['n1716']], isweak=False, parent=self),
            NMOS("t498", [self.netlist['n107'],self.port['gnd'].netconn,self.netlist['n1676']], isweak=False, parent=self),
            NMOS("t4195", [self.port['gnd'].netconn,self.netlist['n1638'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t2415", [self.port['db1'].netconn,self.port['gnd'].netconn,self.netlist['n685']], isweak=False, parent=self),
            NMOS("t2417", [self.netlist['n684'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t5078", [self.port['gnd'].netconn,self.netlist['n3'],self.port['irq'].netconn], isweak=False, parent=self),
            NMOS("t877", [self.port['gnd'].netconn,self.netlist['n2721'],self.netlist['n1768']], isweak=False, parent=self),
            NMOS("t2418", [self.netlist['n685'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2419", [self.netlist['n684'],self.port['gnd'].netconn,self.netlist['dbo0']], isweak=False, parent=self),
            NMOS("t2885", [self.netlist['n704'],self.netlist['n2828'],self.netlist['n1348']], isweak=False, parent=self),
            NMOS("t3383", [self.port['gnd'].netconn,self.netlist['n1053'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t3382", [self.port['gnd'].netconn,self.netlist['n1053'],self.netlist['n1156']], isweak=False, parent=self),
            NMOS("t3380", [self.netlist['n1052'],self.port['gnd'].netconn,self.netlist['n1053']], isweak=False, parent=self),
            NMOS("t3387", [self.port['gnd'].netconn,self.netlist['n1054'],self.netlist['n1040']], isweak=False, parent=self),
            NMOS("t3386", [self.netlist['n1054'],self.port['gnd'].netconn,self.netlist['n1125']], isweak=False, parent=self),
            NMOS("t3929", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3928", [self.port['gnd'].netconn,self.netlist['n1802'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3435", [self.netlist['n1068'],self.port['gnd'].netconn,self.netlist['n1095']], isweak=False, parent=self),
            NMOS("t3434", [self.netlist['n1068'],self.port['gnd'].netconn,self.netlist['n1069']], isweak=False, parent=self),
            NMOS("t3925", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3388", [self.port['gnd'].netconn,self.netlist['n1039'],self.netlist['n1054']], isweak=False, parent=self),
            NMOS("t3431", [self.port['gnd'].netconn,self.netlist['n2903'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3922", [self.port['gnd'].netconn,self.netlist['n1850'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3921", [self.port['gnd'].netconn,self.netlist['n1632'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3432", [self.port['gnd'].netconn,self.netlist['n1067'],self.netlist['n1095']], isweak=False, parent=self),
            NMOS("t2930", [self.netlist['n867'],self.netlist['n868'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2388", [self.netlist['n680'],self.port['gnd'].netconn,self.netlist['dbo3']], isweak=False, parent=self),
            NMOS("t2389", [self.port['db2'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2384", [self.port['gnd'].netconn,self.port['db3'].netconn,self.netlist['n680']], isweak=False, parent=self),
            NMOS("t2385", [self.netlist['n679'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2386", [self.netlist['n680'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2387", [self.netlist['n679'],self.port['gnd'].netconn,self.netlist['dbo2']], isweak=False, parent=self),
            NMOS("t636", [self.netlist['n161'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2252", [self.netlist['n645'],self.port['gnd'].netconn,self.netlist['sum6']], isweak=False, parent=self),
            NMOS("t2701", [self.netlist['n536'],self.port['gnd'].netconn,self.netlist['Tr7']], isweak=False, parent=self),
            NMOS("t2250", [self.netlist['n645'],self.port['gnd'].netconn,self.netlist['sum7']], isweak=False, parent=self),
            NMOS("t2251", [self.port['gnd'].netconn,self.netlist['sum7'],self.netlist['n617']], isweak=False, parent=self),
            NMOS("t2704", [self.port['gnd'].netconn,self.netlist['n536'],self.netlist['n775']], isweak=False, parent=self),
            NMOS("t2257", [self.port['gnd'].netconn,self.netlist['sum5'],self.netlist['n622']], isweak=False, parent=self),
            NMOS("t2254", [self.netlist['sum6'],self.port['gnd'].netconn,self.netlist['n613']], isweak=False, parent=self),
            NMOS("t2255", [self.netlist['n645'],self.port['gnd'].netconn,self.netlist['sum5']], isweak=False, parent=self),
            NMOS("t2708", [self.netlist['n775'],self.port['gnd'].netconn,self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t1871", [self.netlist['n523'],self.netlist['n495'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1870", [self.netlist['n522'],self.netlist['n494'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1877", [self.netlist['n528'],self.netlist['n529'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t657", [self.netlist['n177'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1875", [self.netlist['n524'],self.netlist['n525'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3659", [self.netlist['flagc'],self.port['gnd'].netconn,self.netlist['n1129']], isweak=False, parent=self),
            NMOS("t2092", [self.netlist['n583'],self.netlist['n580'],self.netlist['sumab5']], isweak=False, parent=self),
            NMOS("t656", [self.port['gnd'].netconn,self.netlist['n181'],self.netlist['n442']], isweak=False, parent=self),
            NMOS("t2094", [self.port['gnd'].netconn,self.netlist['n580'],self.netlist['n586']], isweak=False, parent=self),
            NMOS("t2096", [self.port['gnd'].netconn,self.netlist['n586'],self.netlist['n554']], isweak=False, parent=self),
            NMOS("t2098", [self.netlist['n585'],self.port['gnd'].netconn,self.netlist['n555']], isweak=False, parent=self),
            NMOS("t2099", [self.netlist['n583'],self.netlist['n584'],self.netlist['sumab4']], isweak=False, parent=self),
            NMOS("t3653", [self.port['gnd'].netconn,self.netlist['n1128'],self.netlist['n1108']], isweak=False, parent=self),
            NMOS("t3652", [self.netlist['n2932'],self.port['gnd'].netconn,self.netlist['n1162']], isweak=False, parent=self),
            NMOS("t3655", [self.netlist['n1128'],self.netlist['n2933'],self.netlist['n1122']], isweak=False, parent=self),
            NMOS("t3657", [self.netlist['n2933'],self.port['gnd'].netconn,self.netlist['n1161']], isweak=False, parent=self),
            NMOS("t650", [self.netlist['n174'],self.port['gnd'].netconn,self.netlist['n449']], isweak=False, parent=self),
            NMOS("t653", [self.port['gnd'].netconn,self.netlist['n178'],self.netlist['n440']], isweak=False, parent=self),
            NMOS("t1913", [self.netlist['n547'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t1271", [self.netlist['n328'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1270", [self.netlist['n319'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1272", [self.netlist['n320'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t440", [self.port['gnd'].netconn,self.netlist['n2701'],self.netlist['n1666']], isweak=False, parent=self),
            NMOS("t441", [self.port['gnd'].netconn,self.netlist['n2702'],self.netlist['n1665']], isweak=False, parent=self),
            NMOS("t442", [self.port['gnd'].netconn,self.netlist['n2703'],self.netlist['n1676']], isweak=False, parent=self),
            NMOS("t443", [self.port['gnd'].netconn,self.netlist['n2704'],self.netlist['n1675']], isweak=False, parent=self),
            NMOS("t444", [self.port['gnd'].netconn,self.netlist['n2705'],self.netlist['n1664']], isweak=False, parent=self),
            NMOS("t445", [self.port['gnd'].netconn,self.netlist['n2706'],self.netlist['n1663']], isweak=False, parent=self),
            NMOS("t3663", [self.netlist['n646'],self.netlist['n1165'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t447", [self.port['gnd'].netconn,self.netlist['n2708'],self.netlist['n1674']], isweak=False, parent=self),
            NMOS("t448", [self.netlist['n97'],self.netlist['n2701'],self.netlist['ald7_0']], isweak=False, parent=self),
            NMOS("t930", [self.netlist['n250'],self.netlist['n2738'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t931", [self.netlist['n2735'],self.netlist['n247'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t685", [self.netlist['n184'],self.port['gnd'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t4040", [self.port['gnd'].netconn,self.netlist['n1533'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t659", [self.netlist['n178'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4043", [self.port['gnd'].netconn,self.netlist['n1526'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t688", [self.netlist['n185'],self.port['gnd'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t658", [self.netlist['n171'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2899", [self.netlist['n848'],self.port['gnd'].netconn,self.netlist['n1186']], isweak=False, parent=self),
            NMOS("t4042", [self.port['gnd'].netconn,self.netlist['n1806'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2678", [self.netlist['n761'],self.netlist['n1583'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2679", [self.netlist['n796'],self.netlist['n762'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2890", [self.netlist['n704'],self.netlist['n2830'],self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t4045", [self.port['gnd'].netconn,self.netlist['n1843'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2676", [self.netlist['n432'],self.port['gnd'].netconn,self.netlist['n1583']], isweak=False, parent=self),
            NMOS("t2677", [self.port['gnd'].netconn,self.netlist['n761'],self.netlist['n762']], isweak=False, parent=self),
            NMOS("t2670", [self.netlist['n430'],self.port['gnd'].netconn,self.netlist['n793']], isweak=False, parent=self),
            NMOS("t2671", [self.port['gnd'].netconn,self.netlist['n760'],self.netlist['n792']], isweak=False, parent=self),
            NMOS("t2672", [self.port['gnd'].netconn,self.netlist['n2807'],self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t4044", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t1019", [self.netlist['tmp5'],self.netlist['abh5'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t1018", [self.netlist['tmp6'],self.netlist['abh6'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t4029", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4283", [self.port['gnd'].netconn,self.netlist['i3'],self.netlist['n1297']], isweak=False, parent=self),
            NMOS("t4047", [self.port['gnd'].netconn,self.netlist['n1811'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4281", [self.netlist['n1266'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4280", [self.port['gnd'].netconn,self.netlist['i3'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t1011", [self.netlist['n286'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1010", [self.netlist['n285'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5026", [self.port['vcc'].netconn,self.netlist['n1527'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4046", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t5020", [self.port['vcc'].netconn,self.netlist['n1625'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1014", [self.port['gnd'].netconn,self.netlist['n2739'],self.netlist['n170']], isweak=False, parent=self),
            NMOS("t1017", [self.netlist['tmp7'],self.netlist['abh7'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t1016", [self.netlist['n2739'],self.netlist['n287'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t1389", [self.netlist['acca4_1'],self.netlist['idb4'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t1388", [self.netlist['idb2'],self.netlist['accb2_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t2875", [self.port['gnd'].netconn,self.netlist['n2825'],self.netlist['n123']], isweak=False, parent=self),
            NMOS("t2872", [self.netlist['n842'],self.port['gnd'].netconn,self.netlist['Ta2']], isweak=False, parent=self),
            NMOS("t3243", [self.netlist['n2872'],self.port['gnd'].netconn,self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t2871", [self.port['gnd'].netconn,self.netlist['n127'],self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t1381", [self.netlist['idb5'],self.netlist['accb5'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t1380", [self.netlist['ixl3'],self.netlist['idb3'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1383", [self.netlist['idb7'],self.netlist['accb7'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t1382", [self.netlist['ixl5'],self.netlist['idb5'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1385", [self.netlist['acca0_1'],self.netlist['idb0'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t1384", [self.netlist['ixl7'],self.netlist['idb7'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t2878", [self.netlist['n2825'],self.netlist['n121'],self.netlist['n711']], isweak=False, parent=self),
            NMOS("t1386", [self.netlist['idb0'],self.netlist['accb0_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t3628", [self.netlist['n2927'],self.port['gnd'].netconn,self.netlist['n1156']], isweak=False, parent=self),
            NMOS("t592", [self.port['gnd'].netconn,self.netlist['pcl7'],self.netlist['n1774']], isweak=False, parent=self),
            NMOS("t593", [self.netlist['pcl5'],self.port['gnd'].netconn,self.netlist['n1777']], isweak=False, parent=self),
            NMOS("t590", [self.port['gnd'].netconn,self.netlist['n1771'],self.netlist['pcl2_1']], isweak=False, parent=self),
            NMOS("t591", [self.port['gnd'].netconn,self.netlist['n1770'],self.netlist['pcl0_1']], isweak=False, parent=self),
            NMOS("t848", [self.port['gnd'].netconn,self.netlist['n221'],self.netlist['n229']], isweak=False, parent=self),
            NMOS("t597", [self.port['gnd'].netconn,self.netlist['pcl4'],self.netlist['n1772']], isweak=False, parent=self),
            NMOS("t1479", [self.port['gnd'].netconn,self.netlist['n1722'],self.netlist['ixl4_1']], isweak=False, parent=self),
            NMOS("t1478", [self.port['gnd'].netconn,self.netlist['ixl4'],self.netlist['n1722']], isweak=False, parent=self),
            NMOS("t844", [self.port['gnd'].netconn,self.netlist['n219'],self.netlist['n227']], isweak=False, parent=self),
            NMOS("t1476", [self.netlist['ixl4'],self.netlist['ixl4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t846", [self.port['gnd'].netconn,self.netlist['n220'],self.netlist['n228']], isweak=False, parent=self),
            NMOS("t4600", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t840", [self.netlist['n233'],self.port['gnd'].netconn,self.netlist['ahd0_0']], isweak=False, parent=self),
            NMOS("t4606", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1471", [self.port['gnd'].netconn,self.netlist['n1726'],self.netlist['ixl5_1']], isweak=False, parent=self),
            NMOS("t4604", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1657", [self.netlist['n388'],self.port['gnd'].netconn,self.port['db6'].netconn], isweak=False, parent=self),
            NMOS("t1656", [self.netlist['idb6'],self.netlist['dbo6'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t1655", [self.netlist['dbi6'],self.netlist['idb6'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t1654", [self.netlist['dbi6'],self.port['gnd'].netconn,self.netlist['n391']], isweak=False, parent=self),
            NMOS("t4467", [self.netlist['n2939'],self.netlist['n1311'],self.netlist['n1312']], isweak=False, parent=self),
            NMOS("t1120", [self.netlist['spl2'],self.netlist['spl2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1651", [self.port['vcc'].netconn,self.netlist['n391'],self.netlist['n392']], isweak=False, parent=self),
            NMOS("t4464", [self.netlist['n1311'],self.netlist['n1310'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4469", [self.netlist['n1312'],self.netlist['n849'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1129", [self.netlist['spl0_1'],self.netlist['abl0'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1659", [self.netlist['n396'],self.port['gnd'].netconn,self.netlist['dbi5']], isweak=False, parent=self),
            NMOS("t4193", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4192", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1497", [self.netlist['accb0'],self.netlist['ablx0'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t1496", [self.port['gnd'].netconn,self.netlist['n1708'],self.netlist['ixl0_1']], isweak=False, parent=self),
            NMOS("t1491", [self.port['gnd'].netconn,self.netlist['n1716'],self.netlist['ixl1_1']], isweak=False, parent=self),
            NMOS("t4196", [self.port['gnd'].netconn,self.netlist['n1626'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1493", [self.netlist['ixl0'],self.netlist['ixl0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4194", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4199", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4198", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t1499", [self.netlist['accb2'],self.netlist['ablx2'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t1498", [self.netlist['accb1'],self.netlist['ablx1'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t84", [self.netlist['ald4_0'],self.netlist['obl4'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t83", [self.netlist['ald2_0'],self.netlist['obl2'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t3631", [self.netlist['n2927'],self.port['gnd'].netconn,self.netlist['flagz']], isweak=False, parent=self),
            NMOS("t82", [self.netlist['ald1_0'],self.netlist['obl1'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t4517", [self.netlist['n1536'],self.netlist['n1342'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4516", [self.netlist['n1535'],self.netlist['n1341'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4515", [self.netlist['n1534'],self.netlist['n1340'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4514", [self.netlist['n1533'],self.netlist['n1339'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4513", [self.netlist['n1532'],self.netlist['n1338'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4512", [self.netlist['n1531'],self.netlist['n1337'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4511", [self.netlist['n1530'],self.netlist['n1336'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4510", [self.netlist['n1529'],self.netlist['n1335'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4049", [self.port['gnd'].netconn,self.netlist['n1610'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4048", [self.port['gnd'].netconn,self.netlist['n1829'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2729", [self.netlist['n783'],self.netlist['n782'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4519", [self.netlist['n1538'],self.netlist['n1344'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4518", [self.netlist['n1537'],self.netlist['n1343'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t5088", [self.port['vma'].netconn,self.port['gnd'].netconn,self.netlist['n1499']], isweak=False, parent=self),
            NMOS("t1723", [self.netlist['n428'],self.netlist['n429'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1722", [self.netlist['n426'],self.netlist['n427'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1721", [self.netlist['n424'],self.netlist['n425'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1720", [self.netlist['n745'],self.netlist['n423'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1727", [self.netlist['n436'],self.netlist['n437'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1726", [self.netlist['n434'],self.netlist['n435'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1725", [self.netlist['n432'],self.netlist['n433'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2975", [self.netlist['n889'],self.port['gnd'].netconn,self.netlist['n893']], isweak=False, parent=self),
            NMOS("t4993", [self.port['vcc'].netconn,self.netlist['n1847'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4992", [self.port['vcc'].netconn,self.netlist['n1628'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1729", [self.netlist['n745'],self.netlist['n440'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1728", [self.netlist['n438'],self.netlist['n439'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4997", [self.port['vcc'].netconn,self.netlist['n1829'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2489", [self.port['gnd'].netconn,self.port['db7'].netconn,self.netlist['n652']], isweak=False, parent=self),
            NMOS("t4995", [self.port['vcc'].netconn,self.netlist['n1796'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4994", [self.port['vcc'].netconn,self.netlist['n1516'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3447", [self.netlist['n1072'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t878", [self.port['gnd'].netconn,self.netlist['n2722'],self.netlist['n1764']], isweak=False, parent=self),
            NMOS("t3142", [self.netlist['n963'],self.port['gnd'].netconn,self.netlist['n1405']], isweak=False, parent=self),
            NMOS("t4999", [self.port['vcc'].netconn,self.netlist['n1805'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2727", [self.port['gnd'].netconn,self.netlist['n2813'],self.netlist['n1582']], isweak=False, parent=self),
            NMOS("t4998", [self.port['vcc'].netconn,self.netlist['n1525'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3810", [self.netlist['n970'],self.netlist['n1203'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3283", [self.netlist['n2879'],self.port['gnd'].netconn,self.netlist['n1424']], isweak=False, parent=self),
            NMOS("t3713", [self.netlist['n1186'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t338", [self.netlist['n67'],self.netlist['n1668'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t339", [self.netlist['n70'],self.netlist['n1654'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t336", [self.netlist['n61'],self.netlist['n1661'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t337", [self.netlist['n64'],self.netlist['n1659'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t334", [self.netlist['n55'],self.netlist['n1662'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t335", [self.netlist['n58'],self.netlist['n1660'],self.netlist['n6']], isweak=False, parent=self),
            NMOS("t332", [self.netlist['n1673'],self.netlist['n72'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t333", [self.netlist['n75'],self.netlist['n1672'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t330", [self.netlist['n1668'],self.netlist['n66'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t331", [self.netlist['n1654'],self.netlist['n69'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t4866", [self.netlist['reset_0'],self.port['gnd'].netconn,self.port['reset'].netconn], isweak=False, parent=self),
            NMOS("t4863", [self.port['gnd'].netconn,self.netlist['n1460'],self.netlist['n1476']], isweak=False, parent=self),
            NMOS("t4861", [self.netlist['n1508'],self.port['gnd'].netconn,self.netlist['n1476']], isweak=False, parent=self),
            NMOS("t3026", [self.netlist['n2841'],self.port['gnd'].netconn,self.netlist['n1394']], isweak=False, parent=self),
            NMOS("t4991", [self.port['vcc'].netconn,self.netlist['n1815'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4868", [self.netlist['n1463'],self.port['gnd'].netconn,self.netlist['reset_0']], isweak=False, parent=self),
            NMOS("t4990", [self.port['vcc'].netconn,self.netlist['n1536'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1461", [self.port['gnd'].netconn,self.netlist['n1782'],self.netlist['ixl7_1']], isweak=False, parent=self),
            NMOS("t1359", [self.netlist['idb5'],self.netlist['ixl5_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t4996", [self.port['vcc'].netconn,self.netlist['n1610'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2972", [self.port['gnd'].netconn,self.netlist['n889'],self.netlist['n892']], isweak=False, parent=self),
            NMOS("t4895", [self.port['vcc'].netconn,self.netlist['res'],self.netlist['n1467']], isweak=False, parent=self),
            NMOS("t208", [self.port['gnd'].netconn,self.netlist['n2677'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t209", [self.netlist['n2678'],self.port['gnd'].netconn,self.netlist['n164']], isweak=False, parent=self),
            NMOS("t1350", [self.netlist['ixl1_1'],self.netlist['abl1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t202", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n49']], isweak=False, parent=self),
            NMOS("t200", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n48']], isweak=False, parent=self),
            NMOS("t2808", [self.netlist['n814'],self.netlist['n815'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t206", [self.port['gnd'].netconn,self.netlist['n2675'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t207", [self.netlist['n2676'],self.port['gnd'].netconn,self.netlist['n164']], isweak=False, parent=self),
            NMOS("t204", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n50']], isweak=False, parent=self),
            NMOS("t1694", [self.netlist['n413'],self.port['gnd'].netconn,self.netlist['n1690']], isweak=False, parent=self),
            NMOS("t2970", [self.netlist['Tg8'],self.netlist['n892'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1102", [self.netlist['spl5'],self.port['gnd'].netconn,self.netlist['n1749']], isweak=False, parent=self),
            NMOS("t3712", [self.port['gnd'].netconn,self.netlist['n1189'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t4893", [self.port['gnd'].netconn,self.netlist['n1473'],self.netlist['n1467']], isweak=False, parent=self),
            NMOS("t116", [self.port['ab7'].netconn,self.port['gnd'].netconn,self.netlist['n36']], isweak=False, parent=self),
            NMOS("t110", [self.port['gnd'].netconn,self.netlist['n37'],self.netlist['n36']], isweak=False, parent=self),
            NMOS("t111", [self.port['gnd'].netconn,self.netlist['n37'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t118", [self.port['ab7'].netconn,self.port['vcc'].netconn,self.netlist['n37']], isweak=False, parent=self),
            NMOS("t3732", [self.port['gnd'].netconn,self.netlist['n1523'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3733", [self.port['gnd'].netconn,self.netlist['n1809'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3730", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3731", [self.port['gnd'].netconn,self.netlist['n1608'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3736", [self.port['gnd'].netconn,self.netlist['n1602'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3737", [self.port['gnd'].netconn,self.netlist['n1613'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3734", [self.port['gnd'].netconn,self.netlist['n1841'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3735", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3738", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t3739", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t2152", [self.netlist['dbi2'],self.netlist['idb2'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t5003", [self.port['vcc'].netconn,self.netlist['n1811'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4658", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t3960", [self.port['gnd'].netconn,self.netlist['n1516'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t1259", [self.netlist['n322'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4659", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4207", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t2460", [self.netlist['n689'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t4712", [self.netlist['n1574'],self.port['vcc'].netconn,self.netlist['n1454']], isweak=False, parent=self),
            NMOS("t2469", [self.port['ab15'].netconn,self.port['gnd'].netconn,self.netlist['n688']], isweak=False, parent=self),
            NMOS("t1467", [self.netlist['ixl5'],self.netlist['ixl5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t761", [self.netlist['inch4'],self.netlist['abh4'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t4556", [self.netlist['n1798'],self.netlist['n1379'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2566", [self.netlist['n2797'],self.port['gnd'].netconn,self.netlist['n959']], isweak=False, parent=self),
            NMOS("t3938", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3939", [self.port['gnd'].netconn,self.netlist['n1519'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t2567", [self.netlist['n2797'],self.port['gnd'].netconn,self.netlist['n724']], isweak=False, parent=self),
            NMOS("t3398", [self.netlist['n2897'],self.port['gnd'].netconn,self.netlist['sum7']], isweak=False, parent=self),
            NMOS("t3399", [self.netlist['n1057'],self.netlist['n2897'],self.netlist['n1034']], isweak=False, parent=self),
            NMOS("t3428", [self.port['gnd'].netconn,self.netlist['n1067'],self.netlist['n1065']], isweak=False, parent=self),
            NMOS("t3930", [self.port['gnd'].netconn,self.netlist['n1835'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3395", [self.port['gnd'].netconn,self.netlist['n1056'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t3932", [self.port['gnd'].netconn,self.netlist['n1608'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3397", [self.netlist['n2897'],self.port['gnd'].netconn,self.netlist['n1128']], isweak=False, parent=self),
            NMOS("t3422", [self.netlist['n2902'],self.netlist['n1063'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3935", [self.port['gnd'].netconn,self.netlist['n1535'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3420", [self.netlist['n1063'],self.netlist['n2901'],self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t3393", [self.port['gnd'].netconn,self.netlist['n1056'],self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t2562", [self.netlist['n718'],self.netlist['n724'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2563", [self.netlist['n725'],self.netlist['n726'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4115", [self.netlist['n1234'],self.port['gnd'].netconn,self.netlist['n1218']], isweak=False, parent=self),
            NMOS("t1864", [self.port['gnd'].netconn,self.netlist['n518'],self.netlist['idb1']], isweak=False, parent=self),
            NMOS("t1865", [self.netlist['idb1_2'],self.port['gnd'].netconn,self.netlist['n518']], isweak=False, parent=self),
            NMOS("t2177", [self.netlist['n634'],self.netlist['n2777'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1860", [self.port['gnd'].netconn,self.netlist['n515'],self.netlist['idb2']], isweak=False, parent=self),
            NMOS("t1861", [self.port['gnd'].netconn,self.netlist['idb2_2'],self.netlist['n515']], isweak=False, parent=self),
            NMOS("t2942", [self.netlist['n875'],self.port['gnd'].netconn,self.netlist['n876']], isweak=False, parent=self),
            NMOS("t1868", [self.port['gnd'].netconn,self.netlist['n519'],self.netlist['idb0']], isweak=False, parent=self),
            NMOS("t1869", [self.port['gnd'].netconn,self.netlist['idb0_2'],self.netlist['n519']], isweak=False, parent=self),
            NMOS("t2269", [self.port['gnd'].netconn,self.netlist['sum1'],self.netlist['n632']], isweak=False, parent=self),
            NMOS("t2268", [self.port['gnd'].netconn,self.netlist['n645'],self.netlist['sum1']], isweak=False, parent=self),
            NMOS("t2266", [self.netlist['sum2'],self.port['gnd'].netconn,self.netlist['n615']], isweak=False, parent=self),
            NMOS("t2264", [self.netlist['n645'],self.port['gnd'].netconn,self.netlist['sum2']], isweak=False, parent=self),
            NMOS("t2263", [self.port['gnd'].netconn,self.netlist['sum3'],self.netlist['n627']], isweak=False, parent=self),
            NMOS("t2261", [self.netlist['n645'],self.port['gnd'].netconn,self.netlist['sum3']], isweak=False, parent=self),
            NMOS("t2260", [self.port['gnd'].netconn,self.netlist['sum4'],self.netlist['n614']], isweak=False, parent=self),
            NMOS("t959", [self.netlist['idb7'],self.netlist['tmp7_1'],self.netlist['n174']], isweak=False, parent=self),
            NMOS("t2069", [self.port['gnd'].netconn,self.netlist['n589'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2068", [self.port['gnd'].netconn,self.netlist['n590'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2179", [self.netlist['n629'],self.netlist['n2779'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2065", [self.port['vcc'].netconn,self.netlist['n580'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2064", [self.port['vcc'].netconn,self.netlist['n579'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2067", [self.netlist['n585'],self.port['gnd'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2066", [self.netlist['n586'],self.port['gnd'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t3646", [self.netlist['n1128'],self.netlist['n2930'],self.netlist['n1163']], isweak=False, parent=self),
            NMOS("t3647", [self.netlist['n2930'],self.port['gnd'].netconn,self.netlist['n1158']], isweak=False, parent=self),
            NMOS("t2063", [self.netlist['n581'],self.port['gnd'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2062", [self.netlist['n582'],self.port['gnd'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2285", [self.port['gnd'].netconn,self.netlist['phi2_1'],self.netlist['n374']], isweak=False, parent=self),
            NMOS("t2284", [self.netlist['n646'],self.port['gnd'].netconn,self.netlist['n595']], isweak=False, parent=self),
            NMOS("t2287", [self.netlist['n652'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2286", [self.netlist['n652'],self.port['gnd'].netconn,self.netlist['dbo7']], isweak=False, parent=self),
            NMOS("t2281", [self.netlist['idb7'],self.netlist['sum7'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t2280", [self.netlist['idb5'],self.netlist['sum5'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t1268", [self.netlist['n318'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1269", [self.netlist['n327'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1266", [self.netlist['n317'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1267", [self.netlist['n326'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1264", [self.netlist['n316'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1265", [self.netlist['n325'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2289", [self.port['gnd'].netconn,self.netlist['n653'],self.netlist['n652']], isweak=False, parent=self),
            NMOS("t1263", [self.netlist['n324'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1260", [self.netlist['n314'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1261", [self.netlist['n323'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t452", [self.netlist['n99'],self.netlist['n2703'],self.netlist['ald3_0']], isweak=False, parent=self),
            NMOS("t450", [self.netlist['n98'],self.netlist['n2702'],self.netlist['ald5_0']], isweak=False, parent=self),
            NMOS("t456", [self.netlist['n101'],self.netlist['n2705'],self.netlist['ald6_0']], isweak=False, parent=self),
            NMOS("t454", [self.netlist['n100'],self.netlist['n2704'],self.netlist['ald1_0']], isweak=False, parent=self),
            NMOS("t458", [self.netlist['n102'],self.netlist['n2706'],self.netlist['ald4_0']], isweak=False, parent=self),
            NMOS("t1228", [self.netlist['n308'],self.port['gnd'].netconn,self.netlist['n287']], isweak=False, parent=self),
            NMOS("t923", [self.netlist['n250'],self.netlist['n2731'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t690", [self.port['gnd'].netconn,self.netlist['n186'],self.netlist['n185']], isweak=False, parent=self),
            NMOS("t921", [self.netlist['n249'],self.netlist['n2730'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t920", [self.netlist['n244'],self.netlist['n2726'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t927", [self.netlist['n2733'],self.netlist['n244'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t926", [self.netlist['n241'],self.netlist['n2732'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t925", [self.netlist['n2736'],self.netlist['n248'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t696", [self.netlist['pch0'],self.netlist['idb0'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t699", [self.netlist['pch6'],self.netlist['idb6'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t698", [self.netlist['pch4'],self.netlist['idb4'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t929", [self.netlist['n2734'],self.netlist['n246'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t4723", [self.port['dbe'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t4724", [self.port['gnd'].netconn,self.port['phi2'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t4725", [self.port['gnd'].netconn,self.port['reset'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t4710", [self.netlist['n1450'],self.port['gnd'].netconn,self.netlist['n1452']], isweak=False, parent=self),
            NMOS("t2600", [self.netlist['n443'],self.port['gnd'].netconn,self.netlist['Te1_0']], isweak=False, parent=self),
            NMOS("t2605", [self.netlist['n738'],self.port['gnd'].netconn,self.netlist['n737']], isweak=False, parent=self),
            NMOS("t2604", [self.netlist['n736'],self.port['gnd'].netconn,self.netlist['n740']], isweak=False, parent=self),
            NMOS("t2607", [self.netlist['n169'],self.port['gnd'].netconn,self.netlist['n820']], isweak=False, parent=self),
            NMOS("t2606", [self.netlist['n736'],self.netlist['n737'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t5059", [self.port['gnd'].netconn,self.netlist['n1487'],self.netlist['n1483']], isweak=False, parent=self),
            NMOS("t4539", [self.netlist['n1622'],self.netlist['n1363'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1008", [self.netlist['n285'],self.port['gnd'].netconn,self.netlist['n455']], isweak=False, parent=self),
            NMOS("t1009", [self.netlist['n286'],self.port['gnd'].netconn,self.netlist['n423']], isweak=False, parent=self),
            NMOS("t4294", [self.netlist['n1197'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4295", [self.netlist['n1197'],self.port['gnd'].netconn,self.netlist['ir1_1']], isweak=False, parent=self),
            NMOS("t4296", [self.port['gnd'].netconn,self.netlist['i1'],self.netlist['n1290']], isweak=False, parent=self),
            NMOS("t4538", [self.netlist['n1621'],self.netlist['n1362'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1002", [self.netlist['n269'],self.netlist['n261'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1003", [self.netlist['n275'],self.netlist['n262'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1000", [self.netlist['n268'],self.netlist['n1780'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1001", [self.netlist['n272'],self.netlist['n260'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1006", [self.netlist['n271'],self.netlist['n274'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1007", [self.netlist['n277'],self.netlist['n264'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1004", [self.netlist['n270'],self.netlist['n273'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1005", [self.netlist['n276'],self.netlist['n263'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t1398", [self.netlist['idb5'],self.netlist['accb5_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t1399", [self.netlist['acca7_1'],self.netlist['idb7'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t2847", [self.netlist['n836'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t2846", [self.netlist['n837'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t2845", [self.port['gnd'].netconn,self.netlist['Tg3'],self.netlist['n906']], isweak=False, parent=self),
            NMOS("t1392", [self.netlist['idb6'],self.netlist['accb6_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t1393", [self.netlist['acca1_1'],self.netlist['idb1'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t1390", [self.netlist['idb4'],self.netlist['accb4_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t1391", [self.netlist['acca6_1'],self.netlist['idb6'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t1396", [self.netlist['idb3'],self.netlist['accb3_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t1397", [self.netlist['acca5_1'],self.netlist['idb5'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t1394", [self.netlist['idb1'],self.netlist['accb1_1'],self.netlist['n323']], isweak=False, parent=self),
            NMOS("t1395", [self.netlist['acca3_1'],self.netlist['idb3'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t4614", [self.port['gnd'].netconn,self.netlist['n1537'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4615", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4616", [self.port['gnd'].netconn,self.netlist['n1830'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4617", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4610", [self.port['gnd'].netconn,self.netlist['n1619'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4611", [self.port['gnd'].netconn,self.netlist['n1532'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4612", [self.port['gnd'].netconn,self.netlist['n1811'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4613", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t5001", [self.port['vcc'].netconn,self.netlist['n1838'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4618", [self.port['gnd'].netconn,self.netlist['n1839'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4619", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1468", [self.netlist['ixl6'],self.port['gnd'].netconn,self.netlist['n1730']], isweak=False, parent=self),
            NMOS("t2114", [self.netlist['n591'],self.netlist['n588'],self.netlist['sumab1']], isweak=False, parent=self),
            NMOS("t2116", [self.port['gnd'].netconn,self.netlist['n588'],self.netlist['n594']], isweak=False, parent=self),
            NMOS("t589", [self.port['gnd'].netconn,self.netlist['n1772'],self.netlist['pcl4_1']], isweak=False, parent=self),
            NMOS("t2110", [self.netlist['n588'],self.netlist['n587'],self.netlist['sumab2']], isweak=False, parent=self),
            NMOS("t859", [self.netlist['n2718'],self.netlist['n219'],self.netlist['ahd5_0']], isweak=False, parent=self),
            NMOS("t4530", [self.netlist['n1610'],self.netlist['n1354'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t857", [self.netlist['n2717'],self.netlist['n210'],self.netlist['ahd7_0']], isweak=False, parent=self),
            NMOS("t856", [self.port['gnd'].netconn,self.netlist['n225'],self.netlist['n233']], isweak=False, parent=self),
            NMOS("t587", [self.port['gnd'].netconn,self.netlist['n1775'],self.netlist['pcl1_1']], isweak=False, parent=self),
            NMOS("t854", [self.port['gnd'].netconn,self.netlist['n224'],self.netlist['n232']], isweak=False, parent=self),
            NMOS("t1464", [self.netlist['ixl6'],self.netlist['ixl6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t852", [self.port['gnd'].netconn,self.netlist['n223'],self.netlist['n231']], isweak=False, parent=self),
            NMOS("t582", [self.netlist['pcl7'],self.netlist['pcl7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1640", [self.port['gnd'].netconn,self.netlist['ablx1'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1641", [self.netlist['ablx0'],self.netlist['acca0'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1642", [self.netlist['ablx1'],self.netlist['acca1'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1643", [self.port['gnd'].netconn,self.netlist['ablx6'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1644", [self.netlist['ablx7'],self.port['gnd'].netconn,self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1645", [self.netlist['ablx6'],self.netlist['acca6'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1646", [self.netlist['acca7'],self.netlist['ablx7'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1131", [self.netlist['spl2_1'],self.netlist['abl2'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t4474", [self.port['gnd'].netconn,self.netlist['n1313'],self.netlist['Ts']], isweak=False, parent=self),
            NMOS("t1649", [self.netlist['n392'],self.port['gnd'].netconn,self.netlist['dbi6']], isweak=False, parent=self),
            NMOS("t4476", [self.netlist['n1314'],self.netlist['n1234'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4471", [self.port['gnd'].netconn,self.netlist['n1313'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1138", [self.netlist['idb1'],self.netlist['spl1_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t1139", [self.netlist['spl3_1'],self.netlist['abl3'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1486", [self.netlist['ixl2'],self.netlist['ixl2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3765", [self.port['gnd'].netconn,self.netlist['n1829'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t4188", [self.port['gnd'].netconn,self.netlist['n1850'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t1483", [self.netlist['ixl1'],self.netlist['ixl1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1480", [self.netlist['ixl3'],self.port['gnd'].netconn,self.netlist['n1717']], isweak=False, parent=self),
            NMOS("t1481", [self.port['gnd'].netconn,self.netlist['n1717'],self.netlist['ixl3_1']], isweak=False, parent=self),
            NMOS("t4184", [self.port['gnd'].netconn,self.netlist['n1830'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4185", [self.port['gnd'].netconn,self.netlist['n1839'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4186", [self.port['gnd'].netconn,self.netlist['n1527'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4536", [self.netlist['n1619'],self.netlist['n1360'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4180", [self.port['gnd'].netconn,self.netlist['n1843'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4181", [self.port['gnd'].netconn,self.netlist['n1816'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4182", [self.port['gnd'].netconn,self.netlist['n1629'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t1489", [self.port['gnd'].netconn,self.netlist['n1709'],self.netlist['ixl2_1']], isweak=False, parent=self),
            NMOS("t4675", [self.port['gnd'].netconn,self.netlist['n1617'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t3766", [self.port['gnd'].netconn,self.netlist['n1610'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3553", [self.netlist['n1113'],self.netlist['n1114'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4500", [self.netlist['n1515'],self.netlist['n1325'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4501", [self.netlist['n1516'],self.netlist['n1326'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4502", [self.netlist['n1517'],self.netlist['n1327'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4503", [self.netlist['n1519'],self.netlist['n1328'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4504", [self.netlist['n1521'],self.netlist['n1329'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1336", [self.netlist['abl2'],self.netlist['ablx2'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t4506", [self.netlist['n1523'],self.netlist['n1331'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4507", [self.netlist['n1525'],self.netlist['n1332'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4508", [self.netlist['n1526'],self.netlist['n1333'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4509", [self.netlist['n1527'],self.netlist['n1334'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4058", [self.port['gnd'].netconn,self.netlist['n1522'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4059", [self.port['gnd'].netconn,self.netlist['n1607'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2950", [self.netlist['n881'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t4984", [self.port['vcc'].netconn,self.netlist['n1618'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4985", [self.port['vcc'].netconn,self.netlist['n1837'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4986", [self.port['vcc'].netconn,self.netlist['n1531'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4987", [self.port['vcc'].netconn,self.netlist['n1810'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3755", [self.port['gnd'].netconn,self.netlist['n1851'],self.netlist['n1270']], isweak=False, parent=self),
            NMOS("t4981", [self.port['vcc'].netconn,self.netlist['n1828'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4982", [self.port['vcc'].netconn,self.netlist['n1524'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4983", [self.port['vcc'].netconn,self.netlist['n1804'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4988", [self.port['vcc'].netconn,self.netlist['n1623'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4989", [self.port['vcc'].netconn,self.netlist['n1842'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1337", [self.netlist['ablx2'],self.netlist['ixh2'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1738", [self.netlist['n454'],self.netlist['n455'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1739", [self.netlist['n456'],self.netlist['n457'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1734", [self.netlist['n738'],self.netlist['n447'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1735", [self.netlist['n448'],self.netlist['n449'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1736", [self.netlist['n450'],self.netlist['n451'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4903", [self.netlist['n1470'],self.netlist['n1468'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1730", [self.netlist['n739'],self.netlist['n441'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1731", [self.netlist['n979'],self.netlist['n442'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1732", [self.netlist['n443'],self.netlist['n444'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1733", [self.netlist['n445'],self.netlist['n446'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3551", [self.netlist['n1111'],self.port['gnd'].netconn,self.netlist['n1112']], isweak=False, parent=self),
            NMOS("t329", [self.netlist['n1659'],self.netlist['n63'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t328", [self.netlist['n1661'],self.netlist['n60'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t327", [self.netlist['n1660'],self.netlist['n57'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t326", [self.netlist['n1662'],self.netlist['n54'],self.netlist['n7']], isweak=False, parent=self),
            NMOS("t4870", [self.netlist['n1463'],self.netlist['n1464'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4871", [self.netlist['n1464'],self.netlist['n1466'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4872", [self.netlist['n1465'],self.port['gnd'].netconn,self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4873", [self.port['gnd'].netconn,self.netlist['n1465'],self.netlist['n1464']], isweak=False, parent=self),
            NMOS("t4874", [self.netlist['n1474'],self.port['gnd'].netconn,self.netlist['n1464']], isweak=False, parent=self),
            NMOS("t4878", [self.port['gnd'].netconn,self.netlist['n1466'],self.netlist['n1474']], isweak=False, parent=self),
            NMOS("t4879", [self.netlist['n1474'],self.port['gnd'].netconn,self.netlist['n1466']], isweak=False, parent=self),
            NMOS("t4333", [self.port['gnd'].netconn,self.netlist['n1297'],self.netlist['ir3']], isweak=False, parent=self),
            NMOS("t2697", [self.netlist['n771'],self.netlist['n768'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t211", [self.netlist['n2680'],self.port['gnd'].netconn,self.netlist['n164']], isweak=False, parent=self),
            NMOS("t210", [self.port['gnd'].netconn,self.netlist['n2679'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t213", [self.netlist['n2682'],self.port['gnd'].netconn,self.netlist['n164']], isweak=False, parent=self),
            NMOS("t212", [self.netlist['n2681'],self.port['gnd'].netconn,self.netlist['n164']], isweak=False, parent=self),
            NMOS("t254", [self.port['gnd'].netconn,self.netlist['n55'],self.netlist['abl7']], isweak=False, parent=self),
            NMOS("t2798", [self.netlist['n807'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t4254", [self.port['gnd'].netconn,self.netlist['n1259'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1809", [self.netlist['n500'],self.port['gnd'].netconn,self.netlist['ablx0']], isweak=False, parent=self),
            NMOS("t3292", [self.netlist['n2881'],self.port['gnd'].netconn,self.netlist['n1360']], isweak=False, parent=self),
            NMOS("t4629", [self.port['gnd'].netconn,self.netlist['n1819'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4886", [self.netlist['n1467'],self.port['gnd'].netconn,self.netlist['n1471']], isweak=False, parent=self),
            NMOS("t4628", [self.port['gnd'].netconn,self.netlist['n1599'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t2124", [self.netlist['n592'],self.port['gnd'].netconn,self.netlist['n575']], isweak=False, parent=self),
            NMOS("t3661", [self.netlist['n1163'],self.netlist['n1067'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2789", [self.netlist['n804'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t4158", [self.port['gnd'].netconn,self.netlist['n1824'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t3662", [self.netlist['n1164'],self.netlist['n1068'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t101", [self.port['gnd'].netconn,self.netlist['n20'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t4625", [self.port['gnd'].netconn,self.netlist['n1626'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t103", [self.netlist['ald5_0'],self.netlist['obl5'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t102", [self.netlist['n20'],self.port['gnd'].netconn,self.netlist['obl6']], isweak=False, parent=self),
            NMOS("t105", [self.port['gnd'].netconn,self.netlist['n7'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t104", [self.netlist['n6'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t107", [self.netlist['n36'],self.port['gnd'].netconn,self.netlist['obl7']], isweak=False, parent=self),
            NMOS("t4156", [self.port['gnd'].netconn,self.netlist['n1799'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t3097", [self.netlist['n954'],self.port['gnd'].netconn,self.netlist['n919']], isweak=False, parent=self),
            NMOS("t3664", [self.port['gnd'].netconn,self.netlist['n1169'],self.netlist['n1323']], isweak=False, parent=self),
            NMOS("t3095", [self.netlist['n950'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t3094", [self.netlist['n950'],self.netlist['Tg2'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3093", [self.netlist['n2853'],self.netlist['n946'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3092", [self.port['gnd'].netconn,self.netlist['n2853'],self.netlist['n948']], isweak=False, parent=self),
            NMOS("t3091", [self.netlist['n2852'],self.port['gnd'].netconn,self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t3665", [self.netlist['n1169'],self.port['gnd'].netconn,self.netlist['n1374']], isweak=False, parent=self),
            NMOS("t4154", [self.port['gnd'].netconn,self.netlist['n1831'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t3259", [self.port['gnd'].netconn,self.netlist['n1008'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3709", [self.port['gnd'].netconn,self.netlist['n1186'],self.netlist['n2']], isweak=False, parent=self),
            NMOS("t3708", [self.port['gnd'].netconn,self.netlist['n1186'],self.netlist['n1187']], isweak=False, parent=self),
            NMOS("t3707", [self.port['gnd'].netconn,self.netlist['n1188'],self.netlist['n1179']], isweak=False, parent=self),
            NMOS("t4621", [self.port['gnd'].netconn,self.netlist['n1844'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t3667", [self.netlist['n2935'],self.netlist['n2934'],self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t3703", [self.netlist['n1185'],self.port['gnd'].netconn,self.netlist['n2']], isweak=False, parent=self),
            NMOS("t3250", [self.netlist['n2873'],self.port['gnd'].netconn,self.netlist['n1003']], isweak=False, parent=self),
            NMOS("t3701", [self.netlist['n2936'],self.netlist['n1195'],self.netlist['n1185']], isweak=False, parent=self),
            NMOS("t3252", [self.netlist['n1015'],self.netlist['n2873'],self.netlist['n986']], isweak=False, parent=self),
            NMOS("t4623", [self.port['gnd'].netconn,self.netlist['n1527'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4622", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t3897", [self.port['gnd'].netconn,self.netlist['n1618'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3896", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3895", [self.port['gnd'].netconn,self.netlist['n1828'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3894", [self.port['gnd'].netconn,self.netlist['n1609'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3893", [self.port['gnd'].netconn,self.netlist['n1795'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3892", [self.port['gnd'].netconn,self.netlist['n1834'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3891", [self.port['gnd'].netconn,self.netlist['n1521'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3890", [self.port['gnd'].netconn,self.netlist['n1825'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3899", [self.port['gnd'].netconn,self.netlist['n1810'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3898", [self.port['gnd'].netconn,self.netlist['n1837'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t1414", [self.port['gnd'].netconn,self.netlist['ixh5'],self.netlist['n1725']], isweak=False, parent=self),
            NMOS("t3559", [self.netlist['idb0'],self.netlist['n1127'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2474", [self.port['ab14'].netconn,self.port['gnd'].netconn,self.netlist['n690']], isweak=False, parent=self),
            NMOS("t3236", [self.netlist['n1004'],self.netlist['n2869'],self.netlist['flagz']], isweak=False, parent=self),
            NMOS("t2478", [self.port['gnd'].netconn,self.port['ab13'].netconn,self.netlist['n687']], isweak=False, parent=self),
            NMOS("t655", [self.port['gnd'].netconn,self.netlist['n180'],self.netlist['n441']], isweak=False, parent=self),
            NMOS("t3066", [self.netlist['n935'],self.netlist['n934'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2010", [self.port['gnd'].netconn,self.netlist['n2756'],self.netlist['adda2']], isweak=False, parent=self),
            NMOS("t3067", [self.netlist['n937'],self.netlist['n936'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3232", [self.netlist['n998'],self.netlist['idb4'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3419", [self.netlist['n1063'],self.port['gnd'].netconn,self.netlist['Tr3']], isweak=False, parent=self),
            NMOS("t3418", [self.port['gnd'].netconn,self.netlist['n1063'],self.netlist['n1062']], isweak=False, parent=self),
            NMOS("t3413", [self.netlist['n2900'],self.port['gnd'].netconn,self.netlist['n1361']], isweak=False, parent=self),
            NMOS("t3412", [self.netlist['n2899'],self.port['gnd'].netconn,self.netlist['n1432']], isweak=False, parent=self),
            NMOS("t3411", [self.port['gnd'].netconn,self.netlist['n2900'],self.netlist['n1432']], isweak=False, parent=self),
            NMOS("t3230", [self.port['gnd'].netconn,self.netlist['n992'],self.netlist['n1027']], isweak=False, parent=self),
            NMOS("t3417", [self.netlist['n2901'],self.port['gnd'].netconn,self.netlist['n1333']], isweak=False, parent=self),
            NMOS("t3416", [self.netlist['n1062'],self.netlist['n918'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t654", [self.port['gnd'].netconn,self.netlist['n179'],self.netlist['n444']], isweak=False, parent=self),
            NMOS("t3414", [self.netlist['n2900'],self.netlist['n1061'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t2011", [self.port['gnd'].netconn,self.netlist['n557'],self.netlist['adda2']], isweak=False, parent=self),
            NMOS("t1811", [self.netlist['n503'],self.netlist['n499'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1810", [self.netlist['n502'],self.netlist['n498'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1813", [self.netlist['n505'],self.netlist['n497'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1812", [self.netlist['n504'],self.netlist['n496'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1815", [self.netlist['adda6in'],self.netlist['adda6'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1814", [self.netlist['adda7in'],self.netlist['adda7'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1817", [self.netlist['adda4in'],self.netlist['adda4'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1816", [self.netlist['adda5in'],self.netlist['adda5'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1819", [self.netlist['adda2in'],self.netlist['adda2'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1818", [self.netlist['adda3in'],self.netlist['adda3'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t2278", [self.netlist['idb3'],self.netlist['sum3'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t2279", [self.netlist['idb1'],self.netlist['sum1'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t3675", [self.netlist['n1175'],self.port['gnd'].netconn,self.netlist['n1172']], isweak=False, parent=self),
            NMOS("t3674", [self.netlist['n1173'],self.port['gnd'].netconn,self.netlist['n1170']], isweak=False, parent=self),
            NMOS("t3672", [self.netlist['n1173'],self.netlist['n1172'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t8", [self.port['gnd'].netconn,self.netlist['n14'],self.netlist['n22']], isweak=False, parent=self),
            NMOS("t3670", [self.netlist['n1171'],self.netlist['n2935'],self.netlist['n1138']], isweak=False, parent=self),
            NMOS("t6", [self.port['gnd'].netconn,self.netlist['n13'],self.netlist['n21']], isweak=False, parent=self),
            NMOS("t2271", [self.port['gnd'].netconn,self.netlist['n645'],self.netlist['sum0']], isweak=False, parent=self),
            NMOS("t2272", [self.port['gnd'].netconn,self.netlist['sum0'],self.netlist['n616']], isweak=False, parent=self),
            NMOS("t5", [self.netlist['n17'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2274", [self.netlist['idb2'],self.netlist['sum2'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t2275", [self.netlist['idb0'],self.netlist['sum0'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t2276", [self.netlist['idb4'],self.netlist['sum4'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t2277", [self.netlist['idb6'],self.netlist['sum6'],self.netlist['n532']], isweak=False, parent=self),
            NMOS("t3075", [self.netlist['n943'],self.netlist['n2849'],self.netlist['n945']], isweak=False, parent=self),
            NMOS("t3077", [self.netlist['n2850'],self.port['gnd'].netconn,self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3076", [self.netlist['n943'],self.port['gnd'].netconn,self.netlist['n1440']], isweak=False, parent=self),
            NMOS("t3071", [self.port['gnd'].netconn,self.netlist['n942'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t3068", [self.netlist['n939'],self.netlist['n938'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2078", [self.netlist['n1690'],self.port['vcc'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2079", [self.port['vcc'].netconn,self.netlist['n592'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2076", [self.port['vcc'].netconn,self.netlist['n595'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2077", [self.port['vcc'].netconn,self.netlist['n583'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2074", [self.netlist['n575'],self.port['gnd'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2075", [self.netlist['n591'],self.port['vcc'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2072", [self.port['gnd'].netconn,self.netlist['n594'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2073", [self.port['gnd'].netconn,self.netlist['qaddgen0'],self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2070", [self.netlist['n587'],self.port['vcc'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2071", [self.netlist['n588'],self.port['vcc'].netconn,self.netlist['n576']], isweak=False, parent=self),
            NMOS("t2296", [self.netlist['n661'],self.netlist['n654'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2297", [self.port['gnd'].netconn,self.netlist['dbi7'],self.netlist['n654']], isweak=False, parent=self),
            NMOS("t2294", [self.port['gnd'].netconn,self.netlist['n661'],self.port['db7'].netconn], isweak=False, parent=self),
            NMOS("t1258", [self.netlist['n328'],self.port['gnd'].netconn,self.netlist['n425']], isweak=False, parent=self),
            NMOS("t2292", [self.netlist['idb7'],self.netlist['dbo7'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t2293", [self.netlist['dbi7'],self.netlist['idb7'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t2951", [self.netlist['n960'],self.netlist['n882'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1253", [self.netlist['n323'],self.port['gnd'].netconn,self.netlist['n431']], isweak=False, parent=self),
            NMOS("t1252", [self.netlist['n322'],self.port['gnd'].netconn,self.netlist['n433']], isweak=False, parent=self),
            NMOS("t1251", [self.port['gnd'].netconn,self.netlist['n329'],self.netlist['n457']], isweak=False, parent=self),
            NMOS("t1250", [self.port['gnd'].netconn,self.netlist['n320'],self.netlist['n459']], isweak=False, parent=self),
            NMOS("t1257", [self.netlist['n327'],self.port['gnd'].netconn,self.netlist['n422']], isweak=False, parent=self),
            NMOS("t1256", [self.netlist['n326'],self.port['gnd'].netconn,self.netlist['n427']], isweak=False, parent=self),
            NMOS("t1255", [self.netlist['n325'],self.port['gnd'].netconn,self.netlist['n429']], isweak=False, parent=self),
            NMOS("t1254", [self.netlist['n324'],self.port['gnd'].netconn,self.netlist['n420']], isweak=False, parent=self),
            NMOS("t2736", [self.netlist['n789'],self.port['gnd'].netconn,self.netlist['n1095']], isweak=False, parent=self),
            NMOS("t651", [self.netlist['n175'],self.port['gnd'].netconn,self.netlist['n447']], isweak=False, parent=self),
            NMOS("t462", [self.netlist['n104'],self.netlist['n2708'],self.netlist['ald0_0']], isweak=False, parent=self),
            NMOS("t460", [self.netlist['n103'],self.netlist['n2707'],self.netlist['ald2_0']], isweak=False, parent=self),
            NMOS("t1672", [self.netlist['n399'],self.netlist['n403'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1929", [self.netlist['sumab7'],self.netlist['n2745'],self.netlist['addb7']], isweak=False, parent=self),
            NMOS("t1928", [self.port['gnd'].netconn,self.netlist['sumab7'],self.netlist['n538']], isweak=False, parent=self),
            NMOS("t918", [self.netlist['n241'],self.netlist['n2725'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t919", [self.netlist['n248'],self.netlist['n2729'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t916", [self.port['gnd'].netconn,self.netlist['inchi5_0'],self.netlist['n248']], isweak=False, parent=self),
            NMOS("t917", [self.netlist['inchi4_0'],self.port['gnd'].netconn,self.netlist['n244']], isweak=False, parent=self),
            NMOS("t914", [self.netlist['n2738'],self.port['gnd'].netconn,self.netlist['ahd1_0']], isweak=False, parent=self),
            NMOS("t915", [self.netlist['inchi6_0'],self.port['gnd'].netconn,self.netlist['n241']], isweak=False, parent=self),
            NMOS("t912", [self.port['gnd'].netconn,self.netlist['n2736'],self.netlist['ahd5_0']], isweak=False, parent=self),
            NMOS("t913", [self.netlist['n2737'],self.port['gnd'].netconn,self.netlist['ahd3_0']], isweak=False, parent=self),
            NMOS("t910", [self.port['gnd'].netconn,self.netlist['n2734'],self.netlist['ahd2_0']], isweak=False, parent=self),
            NMOS("t911", [self.port['gnd'].netconn,self.netlist['n2735'],self.netlist['ahd0_0']], isweak=False, parent=self),
            NMOS("t2618", [self.port['gnd'].netconn,self.netlist['n2800'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t2619", [self.netlist['n739'],self.netlist['n2801'],self.netlist['n821']], isweak=False, parent=self),
            NMOS("t2612", [self.netlist['n741'],self.port['gnd'].netconn,self.netlist['n743']], isweak=False, parent=self),
            NMOS("t2613", [self.netlist['n741'],self.netlist['n742'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2610", [self.port['gnd'].netconn,self.netlist['n445'],self.netlist['n742']], isweak=False, parent=self),
            NMOS("t2617", [self.netlist['n2800'],self.netlist['n452'],self.netlist['n11']], isweak=False, parent=self),
            NMOS("t2614", [self.netlist['n739'],self.netlist['n743'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5048", [self.port['vcc'].netconn,self.netlist['n1640'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5049", [self.port['vcc'].netconn,self.netlist['n1853'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4269", [self.netlist['n1200'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4268", [self.port['gnd'].netconn,self.netlist['i5'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4265", [self.port['gnd'].netconn,self.netlist['i6'],self.netlist['n1278']], isweak=False, parent=self),
            NMOS("t4264", [self.netlist['n1262'],self.port['gnd'].netconn,self.netlist['ir6_1']], isweak=False, parent=self),
            NMOS("t5040", [self.port['vcc'].netconn,self.netlist['n1638'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5041", [self.port['vcc'].netconn,self.netlist['n1851'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5046", [self.port['vcc'].netconn,self.netlist['n1601'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4260", [self.port['gnd'].netconn,self.netlist['i7'],self.netlist['n1279']], isweak=False, parent=self),
            NMOS("t4263", [self.netlist['n1262'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4262", [self.port['gnd'].netconn,self.netlist['i6'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t2858", [self.netlist['n841'],self.netlist['n2822'],self.netlist['n839']], isweak=False, parent=self),
            NMOS("t2854", [self.port['gnd'].netconn,self.netlist['n2821'],self.netlist['n837']], isweak=False, parent=self),
            NMOS("t2855", [self.port['gnd'].netconn,self.netlist['Ta1'],self.netlist['n872']], isweak=False, parent=self),
            NMOS("t2856", [self.port['gnd'].netconn,self.netlist['n1951'],self.netlist['n1372']], isweak=False, parent=self),
            NMOS("t2857", [self.port['gnd'].netconn,self.netlist['n839'],self.netlist['n1372']], isweak=False, parent=self),
            NMOS("t2851", [self.port['gnd'].netconn,self.netlist['n837'],self.netlist['n11']], isweak=False, parent=self),
            NMOS("t2853", [self.netlist['n2821'],self.netlist['n129'],self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t4661", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4660", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4663", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4662", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4665", [self.port['gnd'].netconn,self.netlist['n1833'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4664", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4667", [self.port['gnd'].netconn,self.netlist['n1520'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4666", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4669", [self.port['gnd'].netconn,self.netlist['n1603'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4668", [self.port['gnd'].netconn,self.netlist['n1823'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t2107", [self.netlist['n590'],self.port['gnd'].netconn,self.netlist['n562']], isweak=False, parent=self),
            NMOS("t3096", [self.netlist['n954'],self.port['gnd'].netconn,self.netlist['n1353']], isweak=False, parent=self),
            NMOS("t869", [self.netlist['n2723'],self.netlist['n224'],self.netlist['ahd2_0']], isweak=False, parent=self),
            NMOS("t2103", [self.netlist['n587'],self.netlist['n1690'],self.netlist['sumab3']], isweak=False, parent=self),
            NMOS("t2100", [self.netlist['n583'],self.port['gnd'].netconn,self.netlist['n585']], isweak=False, parent=self),
            NMOS("t863", [self.netlist['n2720'],self.netlist['n221'],self.netlist['ahd1_0']], isweak=False, parent=self),
            NMOS("t861", [self.netlist['n2719'],self.netlist['n220'],self.netlist['ahd3_0']], isweak=False, parent=self),
            NMOS("t867", [self.netlist['n2722'],self.netlist['n223'],self.netlist['ahd4_0']], isweak=False, parent=self),
            NMOS("t865", [self.netlist['n2721'],self.netlist['n222'],self.netlist['ahd6_0']], isweak=False, parent=self),
            NMOS("t1103", [self.port['gnd'].netconn,self.netlist['n1749'],self.netlist['spl5_1']], isweak=False, parent=self),
            NMOS("t4408", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t1101", [self.netlist['spl5'],self.netlist['spl5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1107", [self.netlist['spl3'],self.netlist['spl3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1105", [self.port['gnd'].netconn,self.netlist['n1746'],self.netlist['spl4_1']], isweak=False, parent=self),
            NMOS("t1104", [self.port['gnd'].netconn,self.netlist['spl4'],self.netlist['n1746']], isweak=False, parent=self),
            NMOS("t4401", [self.port['gnd'].netconn,self.netlist['n1602'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4400", [self.port['gnd'].netconn,self.netlist['n1789'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4403", [self.port['gnd'].netconn,self.netlist['n1506'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4402", [self.port['gnd'].netconn,self.netlist['n1612'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4405", [self.port['gnd'].netconn,self.netlist['n1823'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4404", [self.port['gnd'].netconn,self.netlist['n1790'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4407", [self.port['gnd'].netconn,self.netlist['n1791'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4406", [self.port['gnd'].netconn,self.netlist['n1613'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t2954", [self.netlist['n885'],self.netlist['n1952'],self.netlist['n1400']], isweak=False, parent=self),
            NMOS("t4028", [self.port['gnd'].netconn,self.netlist['n1830'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t4430", [self.port['gnd'].netconn,self.netlist['n1621'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4431", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4432", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t485", [self.port['gnd'].netconn,self.netlist['n103'],self.netlist['n111']], isweak=False, parent=self),
            NMOS("t1035", [self.netlist['tmp5'],self.netlist['tmp5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t487", [self.port['gnd'].netconn,self.netlist['n104'],self.netlist['n112']], isweak=False, parent=self),
            NMOS("t1032", [self.netlist['tmp6'],self.netlist['tmp6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1031", [self.netlist['n1751'],self.port['gnd'].netconn,self.netlist['tmp6_1']], isweak=False, parent=self),
            NMOS("t483", [self.port['gnd'].netconn,self.netlist['n102'],self.netlist['n110']], isweak=False, parent=self),
            NMOS("t4066", [self.netlist['sync'],self.port['gnd'].netconn,self.netlist['n1224']], isweak=False, parent=self),
            NMOS("t4064", [self.port['gnd'].netconn,self.netlist['n1223'],self.netlist['n2']], isweak=False, parent=self),
            NMOS("t488", [self.netlist['n105'],self.port['gnd'].netconn,self.netlist['ald7_0']], isweak=False, parent=self),
            NMOS("t489", [self.netlist['n106'],self.port['gnd'].netconn,self.netlist['ald5_0']], isweak=False, parent=self),
            NMOS("t1039", [self.netlist['n1748'],self.port['gnd'].netconn,self.netlist['tmp5_1']], isweak=False, parent=self),
            NMOS("t4060", [self.port['gnd'].netconn,self.netlist['n1513'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4315", [self.netlist['n1275'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t2627", [self.netlist['n167'],self.netlist['n2803'],self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t3771", [self.port['gnd'].netconn,self.netlist['n1535'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t4311", [self.netlist['n1275'],self.netlist['ir6'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4313", [self.netlist['ir6'],self.netlist['ir6_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t2626", [self.netlist['n2803'],self.port['gnd'].netconn,self.netlist['n846']], isweak=False, parent=self),
            NMOS("t4437", [self.port['gnd'].netconn,self.netlist['n1624'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4319", [self.netlist['n1276'],self.port['gnd'].netconn,self.netlist['n1242']], isweak=False, parent=self),
            NMOS("t4318", [self.port['gnd'].netconn,self.netlist['n1275'],self.netlist['n1241']], isweak=False, parent=self),
            NMOS("t1748", [self.netlist['n472'],self.port['gnd'].netconn,self.netlist['n485']], isweak=False, parent=self),
            NMOS("t4086", [self.port['gnd'].netconn,self.netlist['ba_0'],self.netlist['n1508']], isweak=False, parent=self),
            NMOS("t4082", [self.port['vcc'].netconn,self.port['ba'].netconn,self.netlist['n1237']], isweak=False, parent=self),
            NMOS("t1741", [self.netlist['n460'],self.netlist['n461'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1740", [self.netlist['n458'],self.netlist['n459'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1743", [self.netlist['n464'],self.netlist['n465'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1742", [self.netlist['n462'],self.netlist['n463'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4089", [self.netlist['n1231'],self.port['gnd'].netconn,self.netlist['n1234']], isweak=False, parent=self),
            NMOS("t4088", [self.port['gnd'].netconn,self.netlist['n1227'],self.netlist['ba_0']], isweak=False, parent=self),
            NMOS("t1747", [self.port['gnd'].netconn,self.netlist['phi2_1'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1746", [self.netlist['n471'],self.netlist['n470'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t679", [self.netlist['n94'],self.port['gnd'].netconn,self.netlist['n95']], isweak=False, parent=self),
            NMOS("t2620", [self.netlist['n2801'],self.port['gnd'].netconn,self.netlist['n1138']], isweak=False, parent=self),
            NMOS("t1765", [self.netlist['n486'],self.netlist['n485'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t677", [self.netlist['n176'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t903", [self.port['gnd'].netconn,self.netlist['ahd5_0'],self.netlist['n261']], isweak=False, parent=self),
            NMOS("t1935", [self.port['gnd'].netconn,self.netlist['n573'],self.netlist['adda7']], isweak=False, parent=self),
            NMOS("t3976", [self.port['gnd'].netconn,self.netlist['n1851'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3542", [self.port['gnd'].netconn,self.netlist['n1112'],self.netlist['n1569']], isweak=False, parent=self),
            NMOS("t4889", [self.netlist['n1472'],self.netlist['n1968'],self.netlist['n1463']], isweak=False, parent=self),
            NMOS("t907", [self.port['gnd'].netconn,self.netlist['ahd1_0'],self.netlist['n274']], isweak=False, parent=self),
            NMOS("t4885", [self.netlist['n1968'],self.port['gnd'].netconn,self.netlist['n1471']], isweak=False, parent=self),
            NMOS("t2628", [self.port['gnd'].netconn,self.netlist['n2804'],self.netlist['n1365']], isweak=False, parent=self),
            NMOS("t4881", [self.port['gnd'].netconn,self.netlist['n1466'],self.netlist['n1465']], isweak=False, parent=self),
            NMOS("t4883", [self.netlist['n1466'],self.netlist['n1471'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2969", [self.netlist['n830'],self.netlist['Tg1'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3611", [self.netlist['n1148'],self.port['gnd'].netconn,self.netlist['n930']], isweak=False, parent=self),
            NMOS("t260", [self.port['gnd'].netconn,self.netlist['ald6_0'],self.netlist['n1660']], isweak=False, parent=self),
            NMOS("t262", [self.netlist['n57'],self.port['gnd'].netconn,self.netlist['idb6']], isweak=False, parent=self),
            NMOS("t263", [self.port['gnd'].netconn,self.netlist['n58'],self.netlist['abl6']], isweak=False, parent=self),
            NMOS("t264", [self.port['gnd'].netconn,self.netlist['n2685'],self.netlist['n1661']], isweak=False, parent=self),
            NMOS("t2673", [self.netlist['n2807'],self.netlist['n432'],self.netlist['n1359']], isweak=False, parent=self),
            NMOS("t3612", [self.netlist['n1148'],self.port['gnd'].netconn,self.netlist['n929']], isweak=False, parent=self),
            NMOS("t2960", [self.port['gnd'].netconn,self.netlist['n1952'],self.netlist['Tg5']], isweak=False, parent=self),
            NMOS("t2961", [self.netlist['n1952'],self.port['gnd'].netconn,self.netlist['Tg6']], isweak=False, parent=self),
            NMOS("t2962", [self.port['gnd'].netconn,self.netlist['Tr7'],self.netlist['n888']], isweak=False, parent=self),
            NMOS("t4079", [self.port['ba'].netconn,self.port['gnd'].netconn,self.netlist['n1227']], isweak=False, parent=self),
            NMOS("t2215", [self.netlist['n625'],self.port['gnd'].netconn,self.netlist['sumab4']], isweak=False, parent=self),
            NMOS("t1761", [self.netlist['n479'],self.netlist['n480'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3619", [self.port['gnd'].netconn,self.netlist['n2924'],self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t3618", [self.port['gnd'].netconn,self.netlist['n1151'],self.netlist['n1382']], isweak=False, parent=self),
            NMOS("t4021", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t2743", [self.netlist['n791'],self.port['gnd'].netconn,self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t85", [self.netlist['ald3_0'],self.netlist['obl3'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t296", [self.port['gnd'].netconn,self.netlist['ald2_0'],self.netlist['n1654']], isweak=False, parent=self),
            NMOS("t1517", [self.port['gnd'].netconn,self.netlist['accb6'],self.netlist['n1728']], isweak=False, parent=self),
            NMOS("t4020", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['n1199']], isweak=False, parent=self),
            NMOS("t290", [self.port['gnd'].netconn,self.netlist['n67'],self.netlist['abl3']], isweak=False, parent=self),
            NMOS("t3088", [self.netlist['n947'],self.netlist['n2852'],self.netlist['n1383']], isweak=False, parent=self),
            NMOS("t3089", [self.netlist['n947'],self.port['gnd'].netconn,self.netlist['n1420']], isweak=False, parent=self),
            NMOS("t1931", [self.port['gnd'].netconn,self.netlist['n2746'],self.netlist['adda7']], isweak=False, parent=self),
            NMOS("t88", [self.netlist['n18'],self.port['gnd'].netconn,self.netlist['n26']], isweak=False, parent=self),
            NMOS("t3080", [self.netlist['n944'],self.port['gnd'].netconn,self.netlist['n1415']], isweak=False, parent=self),
            NMOS("t3081", [self.netlist['n944'],self.port['gnd'].netconn,self.netlist['n880']], isweak=False, parent=self),
            NMOS("t3082", [self.netlist['n2851'],self.port['gnd'].netconn,self.netlist['n1389']], isweak=False, parent=self),
            NMOS("t3083", [self.netlist['n944'],self.netlist['n2851'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3084", [self.netlist['n2851'],self.port['gnd'].netconn,self.netlist['n1337']], isweak=False, parent=self),
            NMOS("t3085", [self.netlist['n945'],self.port['gnd'].netconn,self.netlist['n1342']], isweak=False, parent=self),
            NMOS("t81", [self.port['gnd'].netconn,self.netlist['n26'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t80", [self.port['gnd'].netconn,self.netlist['n25'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t3718", [self.netlist['n1189'],self.port['gnd'].netconn,self.netlist['n1172']], isweak=False, parent=self),
            NMOS("t3719", [self.port['gnd'].netconn,self.netlist['n1193'],self.netlist['n1191']], isweak=False, parent=self),
            NMOS("t3248", [self.port['gnd'].netconn,self.netlist['n1012'],self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t3249", [self.netlist['n1015'],self.port['gnd'].netconn,self.netlist['n1397']], isweak=False, parent=self),
            NMOS("t3247", [self.netlist['n2871'],self.port['gnd'].netconn,self.netlist['n1012']], isweak=False, parent=self),
            NMOS("t3244", [self.netlist['n1012'],self.port['gnd'].netconn,self.netlist['flagv']], isweak=False, parent=self),
            NMOS("t3245", [self.netlist['n2871'],self.netlist['n2872'],self.netlist['flagv']], isweak=False, parent=self),
            NMOS("t3242", [self.netlist['n1014'],self.netlist['n2871'],self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t3715", [self.netlist['n1189'],self.port['gnd'].netconn,self.netlist['n1190']], isweak=False, parent=self),
            NMOS("t3716", [self.netlist['n1189'],self.netlist['n1191'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3717", [self.netlist['n1193'],self.netlist['n1190'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1433", [self.port['gnd'].netconn,self.netlist['n1707'],self.netlist['ixh2_1']], isweak=False, parent=self),
            NMOS("t1432", [self.port['gnd'].netconn,self.netlist['ixh2'],self.netlist['n1707']], isweak=False, parent=self),
            NMOS("t3880", [self.port['gnd'].netconn,self.netlist['n1535'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3881", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3882", [self.port['gnd'].netconn,self.netlist['n1602'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3883", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3884", [self.port['gnd'].netconn,self.netlist['n1519'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3885", [self.port['gnd'].netconn,self.netlist['n1613'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3886", [self.port['gnd'].netconn,self.netlist['n1791'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3887", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3888", [self.port['gnd'].netconn,self.netlist['n1520'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3889", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2745", [self.netlist['n464'],self.netlist['n2816'],self.netlist['n1344']], isweak=False, parent=self),
            NMOS("t4118", [self.netlist['n1235'],self.netlist['n1232'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t886", [self.netlist['n224'],self.netlist['n2714'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2448", [self.netlist['n688'],self.port['gnd'].netconn,self.netlist['n801']], isweak=False, parent=self),
            NMOS("t2445", [self.netlist['n687'],self.port['gnd'].netconn,self.netlist['n802']], isweak=False, parent=self),
            NMOS("t1434", [self.netlist['ixh1'],self.port['gnd'].netconn,self.netlist['n1714']], isweak=False, parent=self),
            NMOS("t2442", [self.port['ab12'].netconn,self.port['vcc'].netconn,self.netlist['n806']], isweak=False, parent=self),
            NMOS("t3404", [self.netlist['n466'],self.netlist['n2898'],self.netlist['n1437']], isweak=False, parent=self),
            NMOS("t3405", [self.netlist['n2898'],self.port['gnd'].netconn,self.netlist['Tg4']], isweak=False, parent=self),
            NMOS("t3407", [self.netlist['n466'],self.port['gnd'].netconn,self.netlist['n1413']], isweak=False, parent=self),
            NMOS("t3401", [self.netlist['n1059'],self.netlist['n1058'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3402", [self.netlist['n1059'],self.port['gnd'].netconn,self.netlist['n411']], isweak=False, parent=self),
            NMOS("t3403", [self.netlist['n1059'],self.port['gnd'].netconn,self.netlist['n1114']], isweak=False, parent=self),
            NMOS("t883", [self.netlist['n219'],self.netlist['n2711'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3408", [self.netlist['n2899'],self.port['gnd'].netconn,self.netlist['n1391']], isweak=False, parent=self),
            NMOS("t3409", [self.netlist['n466'],self.netlist['n2899'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t884", [self.netlist['n223'],self.netlist['n2712'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2747", [self.netlist['n2816'],self.port['gnd'].netconn,self.netlist['Tg2']], isweak=False, parent=self),
            NMOS("t1803", [self.port['gnd'].netconn,self.netlist['n499'],self.netlist['ablx3']], isweak=False, parent=self),
            NMOS("t1801", [self.netlist['n496'],self.port['gnd'].netconn,self.netlist['ablx4']], isweak=False, parent=self),
            NMOS("t1807", [self.port['gnd'].netconn,self.netlist['n501'],self.netlist['ablx1']], isweak=False, parent=self),
            NMOS("t1805", [self.netlist['n498'],self.port['gnd'].netconn,self.netlist['ablx2']], isweak=False, parent=self),
            NMOS("t3153", [self.netlist['n866'],self.netlist['n967'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3948", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3660", [self.netlist['n1130'],self.netlist['n1162'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t715", [self.port['gnd'].netconn,self.netlist['n1778'],self.netlist['pch7_1']], isweak=False, parent=self),
            NMOS("t716", [self.port['gnd'].netconn,self.netlist['n1766'],self.netlist['pch5_1']], isweak=False, parent=self),
            NMOS("t717", [self.port['gnd'].netconn,self.netlist['n1762'],self.netlist['pch3_1']], isweak=False, parent=self),
            NMOS("t710", [self.netlist['pch1'],self.netlist['abh1'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t711", [self.netlist['pch0'],self.netlist['abh0'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t713", [self.netlist['pch7'],self.netlist['pch7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3668", [self.netlist['n1171'],self.netlist['n1170'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t718", [self.port['gnd'].netconn,self.netlist['n1757'],self.netlist['pch1_1']], isweak=False, parent=self),
            NMOS("t719", [self.port['gnd'].netconn,self.netlist['n1769'],self.netlist['pch6_1']], isweak=False, parent=self),
            NMOS("t2599", [self.port['gnd'].netconn,self.netlist['n443'],self.netlist['Tr8']], isweak=False, parent=self),
            NMOS("t2598", [self.netlist['n2799'],self.netlist['n450'],self.netlist['n846']], isweak=False, parent=self),
            NMOS("t3064", [self.netlist['n932'],self.port['gnd'].netconn,self.netlist['n1077']], isweak=False, parent=self),
            NMOS("t3065", [self.netlist['n933'],self.netlist['n932'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3062", [self.netlist['n1087'],self.netlist['n931'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3060", [self.netlist['n929'],self.netlist['n2847'],self.netlist['n936']], isweak=False, parent=self),
            NMOS("t3061", [self.netlist['n2847'],self.port['gnd'].netconn,self.netlist['n934']], isweak=False, parent=self),
            NMOS("t2043", [self.port['gnd'].netconn,self.netlist['n565'],self.netlist['addb0']], isweak=False, parent=self),
            NMOS("t2590", [self.netlist['n732'],self.port['gnd'].netconn,self.netlist['n731']], isweak=False, parent=self),
            NMOS("t2041", [self.port['gnd'].netconn,self.netlist['n565'],self.netlist['adda0']], isweak=False, parent=self),
            NMOS("t2592", [self.port['gnd'].netconn,self.netlist['n733'],self.netlist['n728']], isweak=False, parent=self),
            NMOS("t2595", [self.netlist['Te1_0'],self.netlist['n866'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2594", [self.netlist['n733'],self.port['gnd'].netconn,self.netlist['n734']], isweak=False, parent=self),
            NMOS("t2597", [self.port['gnd'].netconn,self.netlist['n2799'],self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t3846", [self.port['gnd'].netconn,self.netlist['n1849'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t875", [self.port['gnd'].netconn,self.netlist['n2719'],self.netlist['n1763']], isweak=False, parent=self),
            NMOS("t3498", [self.netlist['n947'],self.netlist['n1099'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2919", [self.netlist['Tg4'],self.port['gnd'].netconn,self.netlist['n870']], isweak=False, parent=self),
            NMOS("t874", [self.port['gnd'].netconn,self.netlist['n2718'],self.netlist['n1767']], isweak=False, parent=self),
            NMOS("t2915", [self.netlist['n859'],self.netlist['n858'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2914", [self.netlist['Tx2'],self.port['gnd'].netconn,self.netlist['n858']], isweak=False, parent=self),
            NMOS("t2917", [self.netlist['n859'],self.port['gnd'].netconn,self.netlist['n857']], isweak=False, parent=self),
            NMOS("t2916", [self.port['gnd'].netconn,self.netlist['n857'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t2911", [self.netlist['n848'],self.netlist['n856'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2910", [self.netlist['n854'],self.netlist['n855'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2912", [self.netlist['n857'],self.netlist['Tx1'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t479", [self.netlist['n100'],self.port['gnd'].netconn,self.netlist['n108']], isweak=False, parent=self),
            NMOS("t876", [self.port['gnd'].netconn,self.netlist['n2720'],self.netlist['n1758']], isweak=False, parent=self),
            NMOS("t4676", [self.port['gnd'].netconn,self.netlist['n1803'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t473", [self.port['gnd'].netconn,self.netlist['n97'],self.netlist['n105']], isweak=False, parent=self),
            NMOS("t475", [self.port['gnd'].netconn,self.netlist['n98'],self.netlist['n106']], isweak=False, parent=self),
            NMOS("t477", [self.port['gnd'].netconn,self.netlist['n99'],self.netlist['n107']], isweak=False, parent=self),
            NMOS("t909", [self.port['gnd'].netconn,self.netlist['n2733'],self.netlist['ahd4_0']], isweak=False, parent=self),
            NMOS("t908", [self.port['gnd'].netconn,self.netlist['n2732'],self.netlist['ahd6_0']], isweak=False, parent=self),
            NMOS("t2625", [self.port['gnd'].netconn,self.netlist['n2802'],self.netlist['n1018']], isweak=False, parent=self),
            NMOS("t2624", [self.netlist['n2802'],self.netlist['n167'],self.netlist['Tg1']], isweak=False, parent=self),
            NMOS("t2623", [self.port['gnd'].netconn,self.netlist['n167'],self.netlist['Tg7']], isweak=False, parent=self),
            NMOS("t4674", [self.port['gnd'].netconn,self.netlist['n1836'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t1938", [self.netlist['n2762'],self.netlist['n2761'],self.netlist['addb7']], isweak=False, parent=self),
            NMOS("t678", [self.port['gnd'].netconn,self.netlist['n95'],self.netlist['n176']], isweak=False, parent=self),
            NMOS("t901", [self.port['gnd'].netconn,self.netlist['ahd0_0'],self.netlist['n264']], isweak=False, parent=self),
            NMOS("t900", [self.netlist['n2728'],self.port['gnd'].netconn,self.netlist['n264']], isweak=False, parent=self),
            NMOS("t1934", [self.netlist['n538'],self.port['gnd'].netconn,self.netlist['addb7']], isweak=False, parent=self),
            NMOS("t902", [self.netlist['n2729'],self.port['gnd'].netconn,self.netlist['n261']], isweak=False, parent=self),
            NMOS("t905", [self.port['gnd'].netconn,self.netlist['ahd3_0'],self.netlist['n273']], isweak=False, parent=self),
            NMOS("t904", [self.netlist['n2730'],self.port['gnd'].netconn,self.netlist['n273']], isweak=False, parent=self),
            NMOS("t2629", [self.netlist['n2804'],self.netlist['n167'],self.netlist['Tr7']], isweak=False, parent=self),
            NMOS("t906", [self.netlist['n2731'],self.port['gnd'].netconn,self.netlist['n274']], isweak=False, parent=self),
            NMOS("t2462", [self.netlist['n690'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t4", [self.netlist['n16'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t1652", [self.netlist['n392'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4278", [self.port['gnd'].netconn,self.netlist['i4'],self.netlist['n1298']], isweak=False, parent=self),
            NMOS("t4276", [self.netlist['n1199'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4277", [self.netlist['n1199'],self.port['gnd'].netconn,self.netlist['ir4_1']], isweak=False, parent=self),
            NMOS("t4073", [self.netlist['n1237'],self.port['gnd'].netconn,self.netlist['n1227']], isweak=False, parent=self),
            NMOS("t4270", [self.netlist['n1200'],self.port['gnd'].netconn,self.netlist['ir5_1']], isweak=False, parent=self),
            NMOS("t4271", [self.port['gnd'].netconn,self.netlist['i5'],self.netlist['n1299']], isweak=False, parent=self),
            NMOS("t2829", [self.netlist['n826'],self.port['gnd'].netconn,self.netlist['n827']], isweak=False, parent=self),
            NMOS("t2821", [self.port['gnd'].netconn,self.netlist['n821'],self.netlist['n946']], isweak=False, parent=self),
            NMOS("t2825", [self.port['gnd'].netconn,self.netlist['n822'],self.netlist['n902']], isweak=False, parent=self),
            NMOS("t2824", [self.port['gnd'].netconn,self.netlist['Tr3'],self.netlist['n903']], isweak=False, parent=self),
            NMOS("t2827", [self.port['gnd'].netconn,self.netlist['Tr4'],self.netlist['n824']], isweak=False, parent=self),
            NMOS("t2826", [self.netlist['n822'],self.netlist['n824'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4672", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4673", [self.port['gnd'].netconn,self.netlist['n1814'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4670", [self.port['gnd'].netconn,self.netlist['n1612'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4671", [self.port['gnd'].netconn,self.netlist['n1518'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t871", [self.netlist['n2724'],self.netlist['n225'],self.netlist['ahd0_0']], isweak=False, parent=self),
            NMOS("t4677", [self.port['gnd'].netconn,self.netlist['n1827'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4111", [self.port['gnd'].netconn,self.netlist['n1234'],self.netlist['n1220']], isweak=False, parent=self),
            NMOS("t1245", [self.port['gnd'].netconn,self.netlist['n315'],self.netlist['n465']], isweak=False, parent=self),
            NMOS("t4678", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t4679", [self.netlist['n1828'],self.netlist['n948'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t879", [self.port['gnd'].netconn,self.netlist['n2723'],self.netlist['n1759']], isweak=False, parent=self),
            NMOS("t1981", [self.port['gnd'].netconn,self.netlist['n549'],self.netlist['adda4']], isweak=False, parent=self),
            NMOS("t1244", [self.port['gnd'].netconn,self.netlist['n314'],self.netlist['n467']], isweak=False, parent=self),
            NMOS("t2132", [self.netlist['n525'],self.port['gnd'].netconn,self.netlist['n577']], isweak=False, parent=self),
            NMOS("t1246", [self.port['gnd'].netconn,self.netlist['n316'],self.netlist['n439']], isweak=False, parent=self),
            NMOS("t2130", [self.port['gnd'].netconn,self.netlist['n578'],self.netlist['n524']], isweak=False, parent=self),
            NMOS("t1240", [self.netlist['idb1'],self.netlist['sph1'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1241", [self.netlist['idb3'],self.netlist['sph3'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1242", [self.netlist['idb7'],self.netlist['sph7'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1243", [self.netlist['n321'],self.port['gnd'].netconn,self.netlist['flagv']], isweak=False, parent=self),
            NMOS("t2139", [self.netlist['n605'],self.netlist['n597'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2138", [self.netlist['n596'],self.netlist['n603'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1248", [self.port['gnd'].netconn,self.netlist['n318'],self.netlist['n461']], isweak=False, parent=self),
            NMOS("t1249", [self.port['gnd'].netconn,self.netlist['n319'],self.netlist['n419']], isweak=False, parent=self),
            NMOS("t1986", [self.netlist['n2768'],self.netlist['n2767'],self.netlist['addb4']], isweak=False, parent=self),
            NMOS("t4418", [self.port['gnd'].netconn,self.netlist['n1843'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4419", [self.port['gnd'].netconn,self.netlist['n1816'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t2135", [self.port['gnd'].netconn,self.netlist['n577'],self.netlist['n526']], isweak=False, parent=self),
            NMOS("t3540", [self.netlist['n1110'],self.port['gnd'].netconn,self.netlist['n1117']], isweak=False, parent=self),
            NMOS("t4412", [self.port['gnd'].netconn,self.netlist['n1837'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t1115", [self.port['gnd'].netconn,self.netlist['n1740'],self.netlist['spl2_1']], isweak=False, parent=self),
            NMOS("t4410", [self.port['gnd'].netconn,self.netlist['n1609'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t1117", [self.netlist['spl1'],self.netlist['spl1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1110", [self.netlist['spl4'],self.netlist['spl4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4417", [self.port['gnd'].netconn,self.netlist['n1838'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4414", [self.port['gnd'].netconn,self.netlist['n1842'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t1113", [self.netlist['n1743'],self.port['gnd'].netconn,self.netlist['spl3_1']], isweak=False, parent=self),
            NMOS("t1327", [self.netlist['abh7'],self.netlist['ixh7_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t3014", [self.netlist['n920'],self.netlist['n919'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5043", [self.port['vcc'].netconn,self.netlist['n1820'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1326", [self.netlist['ixh7_1'],self.netlist['idb7'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t3544", [self.port['gnd'].netconn,self.netlist['n2912'],self.netlist['n1570']], isweak=False, parent=self),
            NMOS("t2548", [self.port['gnd'].netconn,self.netlist['n718'],self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t1323", [self.netlist['abh6'],self.netlist['ixh6_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t3546", [self.netlist['n1566'],self.netlist['n2912'],self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t1322", [self.netlist['abh5'],self.netlist['ixh5_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1020", [self.netlist['tmp4'],self.netlist['abh4'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t5076", [self.netlist['n1502'],self.port['gnd'].netconn,self.port['vcc'].netconn], isweak=False, parent=self),
            NMOS("t495", [self.port['gnd'].netconn,self.netlist['n112'],self.netlist['ald0_0']], isweak=False, parent=self),
            NMOS("t494", [self.netlist['n111'],self.port['gnd'].netconn,self.netlist['ald2_0']], isweak=False, parent=self),
            NMOS("t493", [self.netlist['n110'],self.port['gnd'].netconn,self.netlist['ald4_0']], isweak=False, parent=self),
            NMOS("t492", [self.netlist['n109'],self.port['gnd'].netconn,self.netlist['ald6_0']], isweak=False, parent=self),
            NMOS("t491", [self.netlist['n108'],self.port['gnd'].netconn,self.netlist['ald1_0']], isweak=False, parent=self),
            NMOS("t490", [self.netlist['n107'],self.port['gnd'].netconn,self.netlist['ald3_0']], isweak=False, parent=self),
            NMOS("t1028", [self.port['gnd'].netconn,self.netlist['tmp7'],self.netlist['n1754']], isweak=False, parent=self),
            NMOS("t1029", [self.port['gnd'].netconn,self.netlist['n1754'],self.netlist['tmp7_1']], isweak=False, parent=self),
            NMOS("t1320", [self.netlist['ixh5_1'],self.netlist['idb5'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t499", [self.netlist['n108'],self.port['gnd'].netconn,self.netlist['n1675']], isweak=False, parent=self),
            NMOS("t3256", [self.port['gnd'].netconn,self.netlist['n1003'],self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t4307", [self.port['gnd'].netconn,self.netlist['n1278'],self.netlist['ir6']], isweak=False, parent=self),
            NMOS("t4304", [self.netlist['ir7_1'],self.port['gnd'].netconn,self.netlist['n1279']], isweak=False, parent=self),
            NMOS("t4302", [self.port['gnd'].netconn,self.netlist['i0'],self.netlist['n1302']], isweak=False, parent=self),
            NMOS("t4303", [self.netlist['ir6_1'],self.port['gnd'].netconn,self.netlist['n1278']], isweak=False, parent=self),
            NMOS("t4300", [self.netlist['n1270'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4552", [self.netlist['n1794'],self.netlist['n1375'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2014", [self.netlist['n2771'],self.netlist['n563'],self.netlist['adda2']], isweak=False, parent=self),
            NMOS("t4308", [self.port['gnd'].netconn,self.netlist['n1279'],self.netlist['ir7']], isweak=False, parent=self),
            NMOS("t4096", [self.netlist['n1226'],self.port['gnd'].netconn,self.netlist['n2']], isweak=False, parent=self),
            NMOS("t1758", [self.netlist['n477'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1504", [self.netlist['accb7'],self.netlist['ablx7'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t4092", [self.port['gnd'].netconn,self.netlist['n1226'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3019", [self.netlist['n923'],self.port['gnd'].netconn,self.netlist['n921']], isweak=False, parent=self),
            NMOS("t4090", [self.netlist['decode'],self.port['vcc'].netconn,self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1503", [self.netlist['accb6'],self.netlist['ablx6'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t1750", [self.port['gnd'].netconn,self.netlist['n473'],self.netlist['n484']], isweak=False, parent=self),
            NMOS("t3018", [self.netlist['n925'],self.port['gnd'].netconn,self.netlist['n1019']], isweak=False, parent=self),
            NMOS("t1757", [self.netlist['n476'],self.port['gnd'].netconn,self.netlist['n480']], isweak=False, parent=self),
            NMOS("t1754", [self.netlist['n474'],self.port['gnd'].netconn,self.netlist['n482']], isweak=False, parent=self),
            NMOS("t1755", [self.port['gnd'].netconn,self.netlist['n475'],self.netlist['n481']], isweak=False, parent=self),
            NMOS("t3787", [self.port['gnd'].netconn,self.netlist['n1810'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t4061", [self.netlist['n1220'],self.netlist['n1192'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1501", [self.netlist['accb4'],self.netlist['ablx4'],self.netlist['n318']], isweak=False, parent=self),
            NMOS("t3830", [self.port['gnd'].netconn,self.netlist['n1211'],self.netlist['n1209']], isweak=False, parent=self),
            NMOS("t3180", [self.netlist['n979'],self.port['gnd'].netconn,self.netlist['n1416']], isweak=False, parent=self),
            NMOS("t3158", [self.netlist['n2859'],self.netlist['n4'],self.netlist['n1341']], isweak=False, parent=self),
            NMOS("t4554", [self.netlist['n1796'],self.netlist['n1377'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3833", [self.netlist['n1215'],self.port['gnd'].netconn,self.netlist['n1216']], isweak=False, parent=self),
            NMOS("t1114", [self.port['gnd'].netconn,self.netlist['spl2'],self.netlist['n1740']], isweak=False, parent=self),
            NMOS("t3832", [self.netlist['n1216'],self.port['gnd'].netconn,self.netlist['n1214']], isweak=False, parent=self),
            NMOS("t106", [self.netlist['ald7_0'],self.netlist['obl7'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t4413", [self.port['gnd'].netconn,self.netlist['n1810'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4007", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4411", [self.port['gnd'].netconn,self.netlist['n1828'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t3837", [self.port['gnd'].netconn,self.netlist['n1217'],self.netlist['n1211']], isweak=False, parent=self),
            NMOS("t4416", [self.port['gnd'].netconn,self.netlist['n1805'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t3836", [self.netlist['n1215'],self.netlist['n1214'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1058", [self.port['gnd'].netconn,self.netlist['tmp1'],self.netlist['n1736']], isweak=False, parent=self),
            NMOS("t3426", [self.port['gnd'].netconn,self.netlist['n1065'],self.netlist['n1433']], isweak=False, parent=self),
            NMOS("t4925", [self.port['vcc'].netconn,self.netlist['n1802'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1509", [self.port['gnd'].netconn,self.netlist['accb7'],self.netlist['n1732']], isweak=False, parent=self),
            NMOS("t3931", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t4897", [self.netlist['n2'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t4415", [self.port['gnd'].netconn,self.netlist['n1610'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4892", [self.port['gnd'].netconn,self.netlist['res'],self.netlist['n1473']], isweak=False, parent=self),
            NMOS("t3424", [self.netlist['n2902'],self.port['gnd'].netconn,self.netlist['n1355']], isweak=False, parent=self),
            NMOS("t1680", [self.netlist['n401'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3933", [self.port['gnd'].netconn,self.netlist['n1809'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3390", [self.netlist['n2895'],self.port['gnd'].netconn,self.netlist['n1003']], isweak=False, parent=self),
            NMOS("t3423", [self.port['gnd'].netconn,self.netlist['n2902'],self.netlist['n1425']], isweak=False, parent=self),
            NMOS("t108", [self.netlist['n36'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t3392", [self.port['gnd'].netconn,self.netlist['n1056'],self.netlist['flagz']], isweak=False, parent=self),
            NMOS("t3937", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t273", [self.port['gnd'].netconn,self.netlist['n2686'],self.netlist['n1659']], isweak=False, parent=self),
            NMOS("t272", [self.port['gnd'].netconn,self.netlist['n61'],self.netlist['abl5']], isweak=False, parent=self),
            NMOS("t271", [self.port['gnd'].netconn,self.netlist['n60'],self.netlist['idb5']], isweak=False, parent=self),
            NMOS("t4141", [self.port['gnd'].netconn,self.netlist['n1789'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t2105", [self.port['gnd'].netconn,self.netlist['n1690'],self.netlist['n590']], isweak=False, parent=self),
            NMOS("t278", [self.port['gnd'].netconn,self.netlist['ald4_0'],self.netlist['n1659']], isweak=False, parent=self),
            NMOS("t2492", [self.netlist['Tr7'],self.netlist['n693'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3530", [self.netlist['n2910'],self.netlist['n1566'],self.netlist['n1111']], isweak=False, parent=self),
            NMOS("t4142", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t512", [self.netlist['n137'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4218", [self.port['gnd'].netconn,self.netlist['n1518'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4607", [self.port['gnd'].netconn,self.netlist['n1536'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t2493", [self.netlist['n695'],self.netlist['Tg4'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1038", [self.port['gnd'].netconn,self.netlist['tmp5'],self.netlist['n1748']], isweak=False, parent=self),
            NMOS("t4143", [self.port['gnd'].netconn,self.netlist['n1814'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4219", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t98", [self.port['ab6'].netconn,self.port['vcc'].netconn,self.netlist['n19']], isweak=False, parent=self),
            NMOS("t95", [self.port['ab6'].netconn,self.port['gnd'].netconn,self.netlist['n20']], isweak=False, parent=self),
            NMOS("t91", [self.port['gnd'].netconn,self.netlist['n19'],self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t93", [self.port['gnd'].netconn,self.netlist['n19'],self.netlist['n20']], isweak=False, parent=self),
            NMOS("t3279", [self.netlist['n2878'],self.netlist['n456'],self.netlist['n1332']], isweak=False, parent=self),
            NMOS("t3278", [self.port['gnd'].netconn,self.netlist['n2878'],self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3273", [self.port['gnd'].netconn,self.netlist['n1008'],self.netlist['n1009']], isweak=False, parent=self),
            NMOS("t3272", [self.port['gnd'].netconn,self.netlist['n1006'],self.netlist['n1009']], isweak=False, parent=self),
            NMOS("t3271", [self.netlist['n1008'],self.port['gnd'].netconn,self.netlist['n1000']], isweak=False, parent=self),
            NMOS("t3270", [self.netlist['n1006'],self.netlist['n2877'],self.netlist['n1000']], isweak=False, parent=self),
            NMOS("t3276", [self.netlist['n1010'],self.port['gnd'].netconn,self.netlist['n1002']], isweak=False, parent=self),
            NMOS("t3274", [self.netlist['n1009'],self.netlist['Tg8'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3879", [self.port['gnd'].netconn,self.netlist['n1841'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3878", [self.port['gnd'].netconn,self.netlist['n1809'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3875", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3874", [self.port['gnd'].netconn,self.netlist['n1802'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3877", [self.port['gnd'].netconn,self.netlist['n1608'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t609", [self.netlist['pcl4'],self.netlist['pcl4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3871", [self.port['gnd'].netconn,self.netlist['n1513'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3870", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3873", [self.port['gnd'].netconn,self.netlist['n1522'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t3872", [self.port['gnd'].netconn,self.netlist['n1793'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2458", [self.netlist['n688'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t606", [self.netlist['pcl3'],self.netlist['pcl3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3185", [self.netlist['Td0_0'],self.port['gnd'].netconn,self.netlist['n980']], isweak=False, parent=self),
            NMOS("t3184", [self.port['gnd'].netconn,self.netlist['n980'],self.netlist['n1402']], isweak=False, parent=self),
            NMOS("t3186", [self.netlist['n982'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t2450", [self.netlist['n689'],self.port['gnd'].netconn,self.netlist['n806']], isweak=False, parent=self),
            NMOS("t964", [self.port['vcc'].netconn,self.netlist['abl1'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t2454", [self.netlist['n690'],self.port['gnd'].netconn,self.netlist['n805']], isweak=False, parent=self),
            NMOS("t2456", [self.netlist['n687'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t5077", [self.port['gnd'].netconn,self.port['irq'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t3473", [self.port['gnd'].netconn,self.netlist['n1085'],self.netlist['n1089']], isweak=False, parent=self),
            NMOS("t3475", [self.port['gnd'].netconn,self.netlist['n1079'],self.netlist['n1080']], isweak=False, parent=self),
            NMOS("t3474", [self.netlist['n1079'],self.netlist['n1089'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3477", [self.netlist['n1079'],self.netlist['n2906'],self.netlist['n1090']], isweak=False, parent=self),
            NMOS("t1021", [self.netlist['tmp3'],self.netlist['abh3'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t3478", [self.netlist['n2906'],self.port['gnd'].netconn,self.netlist['n1088']], isweak=False, parent=self),
            NMOS("t1022", [self.netlist['tmp2'],self.netlist['abh2'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t1023", [self.netlist['tmp1'],self.netlist['abh1'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t1024", [self.netlist['tmp0'],self.netlist['abh0'],self.netlist['n179']], isweak=False, parent=self),
            NMOS("t5072", [self.port['irq'].netconn,self.netlist['n2941'],self.netlist['n1502']], isweak=False, parent=self),
            NMOS("t1026", [self.netlist['tmp7'],self.netlist['tmp7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2247", [self.netlist['n635'],self.port['gnd'].netconn,self.netlist['sumab0']], isweak=False, parent=self),
            NMOS("t5070", [self.port['gnd'].netconn,self.port['halt'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t3989", [self.port['gnd'].netconn,self.netlist['n1527'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4179", [self.port['gnd'].netconn,self.netlist['n1811'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t4245", [self.netlist['n1251'],self.netlist['n1255'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1182", [self.netlist['sph6'],self.port['gnd'].netconn,self.netlist['n1753']], isweak=False, parent=self),
            NMOS("t1837", [self.netlist['idb0_2'],self.netlist['adda0in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1836", [self.netlist['idb1_2'],self.netlist['adda1in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1835", [self.netlist['idb2_2'],self.netlist['adda2in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1834", [self.netlist['idb3_2'],self.netlist['adda3in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1833", [self.netlist['idb4_2'],self.netlist['adda4in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1832", [self.netlist['idb5_2'],self.netlist['adda5in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1831", [self.netlist['idb6_2'],self.netlist['adda6in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t1830", [self.netlist['idb7_2'],self.netlist['adda7in'],self.netlist['n417']], isweak=False, parent=self),
            NMOS("t707", [self.netlist['pch4'],self.netlist['abh4'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t706", [self.netlist['pch5'],self.netlist['abh5'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t2056", [self.port['gnd'].netconn,self.netlist['n2774'],self.netlist['n475']], isweak=False, parent=self),
            NMOS("t2057", [self.port['gnd'].netconn,self.netlist['n2776'],self.netlist['n475']], isweak=False, parent=self),
            NMOS("t703", [self.netlist['pch7'],self.netlist['idb7'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t702", [self.netlist['pch5'],self.netlist['idb5'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t2052", [self.port['gnd'].netconn,self.netlist['n2766'],self.netlist['n475']], isweak=False, parent=self),
            NMOS("t2053", [self.port['gnd'].netconn,self.netlist['n2768'],self.netlist['n475']], isweak=False, parent=self),
            NMOS("t3694", [self.netlist['n1183'],self.netlist['n1184'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3141", [self.netlist['n963'],self.port['gnd'].netconn,self.netlist['n962']], isweak=False, parent=self),
            NMOS("t2059", [self.netlist['n539'],self.port['gnd'].netconn,self.netlist['n538']], isweak=False, parent=self),
            NMOS("t709", [self.netlist['pch2'],self.netlist['abh2'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t708", [self.netlist['pch3'],self.netlist['abh3'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t3052", [self.netlist['Tg8'],self.port['gnd'].netconn,self.netlist['n931']], isweak=False, parent=self),
            NMOS("t3050", [self.netlist['n779'],self.port['gnd'].netconn,self.netlist['Tx0']], isweak=False, parent=self),
            NMOS("t3057", [self.port['gnd'].netconn,self.netlist['n2846'],self.netlist['n940']], isweak=False, parent=self),
            NMOS("t3056", [self.netlist['n2846'],self.netlist['n928'],self.netlist['n933']], isweak=False, parent=self),
            NMOS("t3505", [self.port['gnd'].netconn,self.netlist['n1107'],self.netlist['n1099']], isweak=False, parent=self),
            NMOS("t2583", [self.netlist['n448'],self.port['gnd'].netconn,self.netlist['Ts']], isweak=False, parent=self),
            NMOS("t2580", [self.netlist['n728'],self.port['gnd'].netconn,self.netlist['n725']], isweak=False, parent=self),
            NMOS("t3058", [self.netlist['n930'],self.port['gnd'].netconn,self.netlist['n938']], isweak=False, parent=self),
            NMOS("t2586", [self.netlist['n732'],self.port['gnd'].netconn,self.netlist['n646']], isweak=False, parent=self),
            NMOS("t2587", [self.port['gnd'].netconn,self.netlist['n732'],self.netlist['n727']], isweak=False, parent=self),
            NMOS("t3503", [self.netlist['n1105'],self.netlist['n468'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2585", [self.port['gnd'].netconn,self.netlist['n448'],self.netlist['Tr7']], isweak=False, parent=self),
            NMOS("t4068", [self.port['gnd'].netconn,self.netlist['n1224'],self.netlist['n1240']], isweak=False, parent=self),
            NMOS("t2908", [self.netlist['Tx0'],self.port['gnd'].netconn,self.netlist['n971']], isweak=False, parent=self),
            NMOS("t2909", [self.netlist['n4'],self.netlist['n852'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2906", [self.netlist['Tx1'],self.port['gnd'].netconn,self.netlist['n854']], isweak=False, parent=self),
            NMOS("t2907", [self.port['gnd'].netconn,self.netlist['Tx1'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t2902", [self.netlist['n847'],self.port['gnd'].netconn,self.netlist['n852']], isweak=False, parent=self),
            NMOS("t2903", [self.netlist['n847'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t2901", [self.port['gnd'].netconn,self.netlist['n848'],self.netlist['n847']], isweak=False, parent=self),
            NMOS("t3350", [self.port['gnd'].netconn,self.netlist['n2893'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3352", [self.netlist['n2893'],self.netlist['n1024'],self.netlist['n1578']], isweak=False, parent=self),
            NMOS("t2630", [self.port['gnd'].netconn,self.netlist['n746'],self.netlist['n833']], isweak=False, parent=self),
            NMOS("t300", [self.port['gnd'].netconn,self.netlist['n2689'],self.netlist['n1673']], isweak=False, parent=self),
            NMOS("t2632", [self.netlist['n2805'],self.port['gnd'].netconn,self.netlist['n746']], isweak=False, parent=self),
            NMOS("t649", [self.netlist['n173'],self.port['gnd'].netconn,self.netlist['n451']], isweak=False, parent=self),
            NMOS("t2634", [self.netlist['n745'],self.netlist['n2805'],self.netlist['Tg0']], isweak=False, parent=self),
            NMOS("t2635", [self.netlist['n747'],self.port['gnd'].netconn,self.netlist['n796']], isweak=False, parent=self),
            NMOS("t2636", [self.netlist['n424'],self.port['gnd'].netconn,self.netlist['n747']], isweak=False, parent=self),
            NMOS("t1903", [self.netlist['n2746'],self.netlist['n2745'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t643", [self.port['gnd'].netconn,self.netlist['n164'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t640", [self.netlist['n163'],self.port['gnd'].netconn,self.netlist['n166']], isweak=False, parent=self),
            NMOS("t1900", [self.port['gnd'].netconn,self.netlist['sumab2'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t1907", [self.netlist['n2752'],self.netlist['n2751'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t647", [self.netlist['n171'],self.port['gnd'].netconn,self.netlist['n168']], isweak=False, parent=self),
            NMOS("t1905", [self.netlist['n2748'],self.netlist['n2747'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t645", [self.netlist['n168'],self.netlist['n167'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3649", [self.port['gnd'].netconn,self.netlist['n2931'],self.netlist['n1143']], isweak=False, parent=self),
            NMOS("t3356", [self.port['gnd'].netconn,self.netlist['n1029'],self.netlist['n1028']], isweak=False, parent=self),
            NMOS("t4249", [self.netlist['n1250'],self.netlist['n1249'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4248", [self.netlist['n1254'],self.netlist['n1258'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1349", [self.netlist['idb1'],self.netlist['ixl1_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1348", [self.netlist['ixh6'],self.netlist['idb6'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t1345", [self.netlist['ixl6_1'],self.netlist['abl6'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1344", [self.netlist['idb6'],self.netlist['ixl6_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1347", [self.netlist['ablx6'],self.netlist['ixh6'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1346", [self.netlist['abl6'],self.netlist['ablx6'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t1341", [self.netlist['abl4'],self.netlist['ablx4'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t1340", [self.netlist['ixl4_1'],self.netlist['abl4'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1343", [self.netlist['ixh4'],self.netlist['idb4'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t1342", [self.netlist['ablx4'],self.netlist['ixh4'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t3642", [self.port['gnd'].netconn,self.netlist['n1156'],self.netlist['n1155']], isweak=False, parent=self),
            NMOS("t2839", [self.netlist['n833'],self.port['gnd'].netconn,self.netlist['n957']], isweak=False, parent=self),
            NMOS("t3643", [self.port['gnd'].netconn,self.netlist['n2929'],self.netlist['n1165']], isweak=False, parent=self),
            NMOS("t2832", [self.netlist['Tr5'],self.port['gnd'].netconn,self.netlist['n829']], isweak=False, parent=self),
            NMOS("t2652", [self.port['gnd'].netconn,self.netlist['n421'],self.netlist['n833']], isweak=False, parent=self),
            NMOS("t2836", [self.port['gnd'].netconn,self.netlist['n2820'],self.netlist['n956']], isweak=False, parent=self),
            NMOS("t2837", [self.netlist['n2820'],self.netlist['n831'],self.netlist['n830']], isweak=False, parent=self),
            NMOS("t2834", [self.netlist['n829'],self.netlist['n826'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2835", [self.port['gnd'].netconn,self.netlist['n830'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t800", [self.netlist['n1758'],self.netlist['n186'],self.netlist['inchi0_0']], isweak=False, parent=self),
            NMOS("t801", [self.port['vcc'].netconn,self.netlist['n1779'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t802", [self.netlist['n1768'],self.port['vcc'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t803", [self.port['vcc'].netconn,self.netlist['n1767'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t804", [self.netlist['n1764'],self.port['vcc'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t805", [self.port['vcc'].netconn,self.netlist['n1763'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t806", [self.netlist['n1759'],self.port['vcc'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t807", [self.port['vcc'].netconn,self.netlist['n1758'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t808", [self.netlist['n186'],self.port['vcc'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t809", [self.netlist['n2709'],self.netlist['n211'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t4645", [self.netlist['n1800'],self.netlist['n1410'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4644", [self.netlist['n1833'],self.netlist['n1403'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4643", [self.netlist['n1616'],self.netlist['n1417'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4642", [self.netlist['n1827'],self.netlist['n1404'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4641", [self.netlist['n1803'],self.netlist['n1409'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4640", [self.netlist['n1617'],self.netlist['n1416'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1230", [self.netlist['n309'],self.port['gnd'].netconn,self.netlist['flagi']], isweak=False, parent=self),
            NMOS("t1233", [self.port['gnd'].netconn,self.netlist['idb5'],self.netlist['n308']], isweak=False, parent=self),
            NMOS("t4095", [self.netlist['n1240'],self.port['gnd'].netconn,self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1235", [self.netlist['idb4'],self.netlist['sph4'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t2129", [self.netlist['n576'],self.port['gnd'].netconn,self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1237", [self.netlist['idb2'],self.netlist['sph2'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1236", [self.netlist['idb0'],self.netlist['sph0'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1239", [self.netlist['idb5'],self.netlist['sph5'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t1238", [self.netlist['idb6'],self.netlist['sph6'],self.netlist['n172']], isweak=False, parent=self),
            NMOS("t2126", [self.port['gnd'].netconn,self.netlist['n575'],self.netlist['n529']], isweak=False, parent=self),
            NMOS("t3645", [self.netlist['n2929'],self.netlist['n1128'],self.netlist['n1164']], isweak=False, parent=self),
            NMOS("t2120", [self.port['gnd'].netconn,self.netlist['qaddgen0'],self.netlist['n571']], isweak=False, parent=self),
            NMOS("t2121", [self.netlist['n592'],self.netlist['n591'],self.netlist['sumab0']], isweak=False, parent=self),
            NMOS("t2122", [self.netlist['n591'],self.port['gnd'].netconn,self.netlist['qaddgen0']], isweak=False, parent=self),
            NMOS("t4093", [self.netlist['decode'],self.port['gnd'].netconn,self.netlist['n1226']], isweak=False, parent=self),
            NMOS("t1168", [self.netlist['sph0'],self.netlist['abh0'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1699", [self.port['vcc'].netconn,self.netlist['ablx5'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1698", [self.port['vcc'].netconn,self.netlist['ablx6'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1161", [self.netlist['sph7'],self.netlist['abh7'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1160", [self.netlist['sph7_1'],self.netlist['abh7'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1691", [self.netlist['n584'],self.port['gnd'].netconn,self.netlist['n413']], isweak=False, parent=self),
            NMOS("t1162", [self.netlist['sph6'],self.netlist['abh6'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1697", [self.port['vcc'].netconn,self.netlist['ablx7'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t1696", [self.netlist['n414'],self.port['gnd'].netconn,self.netlist['n584']], isweak=False, parent=self),
            NMOS("t1167", [self.netlist['sph1'],self.netlist['abh1'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t1166", [self.netlist['sph2'],self.netlist['abh2'],self.netlist['n286']], isweak=False, parent=self),
            NMOS("t4124", [self.port['gnd'].netconn,self.netlist['n1839'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t384", [self.netlist['n81'],self.netlist['n82'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2783", [self.netlist['n802'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2282", [self.port['gnd'].netconn,self.netlist['n576'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5060", [self.netlist['n1485'],self.port['gnd'].netconn,self.netlist['n4']], isweak=False, parent=self),
            NMOS("t5061", [self.port['gnd'].netconn,self.netlist['n1485'],self.netlist['n1484']], isweak=False, parent=self),
            NMOS("t5062", [self.netlist['n1489'],self.netlist['n1'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t5063", [self.port['nmi'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t5064", [self.port['gnd'].netconn,self.port['phi1'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t5065", [self.port['halt'].netconn,self.netlist['n2941'],self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t5066", [self.netlist['n1493'],self.netlist['halt_0'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1588", [self.netlist['acca0'],self.netlist['acca0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1587", [self.port['gnd'].netconn,self.netlist['acca1'],self.netlist['n1718']], isweak=False, parent=self),
            NMOS("t1586", [self.port['gnd'].netconn,self.netlist['n1718'],self.netlist['acca1_1']], isweak=False, parent=self),
            NMOS("t1585", [self.port['gnd'].netconn,self.netlist['acca2'],self.netlist['n1711']], isweak=False, parent=self),
            NMOS("t1584", [self.netlist['n1711'],self.port['gnd'].netconn,self.netlist['acca2_1']], isweak=False, parent=self),
            NMOS("t1767", [self.netlist['adda0in'],self.port['gnd'].netconn,self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1766", [self.netlist['adda0in'],self.netlist['idb1_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t4331", [self.port['gnd'].netconn,self.netlist['n1290'],self.netlist['ir1']], isweak=False, parent=self),
            NMOS("t1764", [self.netlist['n484'],self.netlist['n474'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1763", [self.netlist['n482'],self.netlist['n483'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1762", [self.netlist['n476'],self.netlist['n481'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4335", [self.port['gnd'].netconn,self.netlist['n1299'],self.netlist['ir5']], isweak=False, parent=self),
            NMOS("t4334", [self.port['gnd'].netconn,self.netlist['n1298'],self.netlist['ir4']], isweak=False, parent=self),
            NMOS("t1262", [self.netlist['n315'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3992", [self.port['gnd'].netconn,self.netlist['n1538'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t1769", [self.netlist['adda2in'],self.netlist['idb3_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t1768", [self.netlist['adda1in'],self.netlist['idb2_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t4122", [self.port['gnd'].netconn,self.netlist['n1638'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t1564", [self.netlist['n1731'],self.port['gnd'].netconn,self.netlist['acca6_1']], isweak=False, parent=self),
            NMOS("t1567", [self.port['gnd'].netconn,self.netlist['acca5'],self.netlist['n1727']], isweak=False, parent=self),
            NMOS("t1566", [self.port['gnd'].netconn,self.netlist['n1727'],self.netlist['acca5_1']], isweak=False, parent=self),
            NMOS("t3548", [self.port['gnd'].netconn,self.netlist['n2913'],self.netlist['n1567']], isweak=False, parent=self),
            NMOS("t1569", [self.netlist['acca4'],self.netlist['acca4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1568", [self.netlist['acca3'],self.netlist['acca3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1999", [self.netlist['n2769'],self.netlist['n562'],self.netlist['adda3']], isweak=False, parent=self),
            NMOS("t4439", [self.port['gnd'].netconn,self.netlist['n1805'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4427", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4426", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4425", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4424", [self.netlist['n1849'],self.port['gnd'].netconn,self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4423", [self.port['gnd'].netconn,self.netlist['n1533'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4422", [self.port['gnd'].netconn,self.netlist['n1797'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4421", [self.port['gnd'].netconn,self.netlist['n1517'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4420", [self.port['gnd'].netconn,self.netlist['n1629'],self.netlist['n1260']], isweak=False, parent=self),
            NMOS("t4429", [self.port['gnd'].netconn,self.netlist['n1638'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4428", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4120", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t644", [self.netlist['n166'],self.netlist['n165'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4009", [self.port['gnd'].netconn,self.netlist['n1835'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t2766", [self.port['gnd'].netconn,self.netlist['n646'],self.netlist['n953']], isweak=False, parent=self),
            NMOS("t963", [self.port['vcc'].netconn,self.netlist['abh1'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t3997", [self.port['gnd'].netconn,self.netlist['n1796'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4121", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t1427", [self.netlist['ixh1'],self.netlist['ixh1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4008", [self.port['gnd'].netconn,self.netlist['n1529'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t3850", [self.port['gnd'].netconn,self.netlist['n1525'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t922", [self.netlist['n246'],self.netlist['n2727'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t246", [self.port['gnd'].netconn,self.netlist['n2683'],self.netlist['n1662']], isweak=False, parent=self),
            NMOS("t244", [self.netlist['n2689'],self.netlist['n46'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t245", [self.netlist['n2690'],self.netlist['n50'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t242", [self.netlist['n2687'],self.netlist['n45'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t243", [self.netlist['n2688'],self.netlist['n49'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t240", [self.netlist['n2685'],self.netlist['n44'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t241", [self.netlist['n2686'],self.netlist['n48'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t519", [self.netlist['n1647'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2831", [self.netlist['n827'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t4581", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1995", [self.port['gnd'].netconn,self.netlist['n2754'],self.netlist['adda3']], isweak=False, parent=self),
            NMOS("t4935", [self.port['vcc'].netconn,self.netlist['n1803'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4934", [self.port['vcc'].netconn,self.netlist['n1523'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4937", [self.port['vcc'].netconn,self.netlist['n1836'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4936", [self.port['vcc'].netconn,self.netlist['n1617'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4931", [self.port['vcc'].netconn,self.netlist['n1794'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t697", [self.netlist['pch2'],self.netlist['idb2'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t4933", [self.port['vcc'].netconn,self.netlist['n1827'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4932", [self.port['vcc'].netconn,self.netlist['n1608'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t924", [self.netlist['n247'],self.netlist['n2728'],self.netlist['n163']], isweak=False, parent=self),
            NMOS("t4939", [self.port['vcc'].netconn,self.netlist['n1809'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4938", [self.port['vcc'].netconn,self.netlist['n1530'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4720", [self.netlist['n1454'],self.port['gnd'].netconn,self.netlist['n1453']], isweak=False, parent=self),
            NMOS("t4582", [self.port['gnd'].netconn,self.netlist['n1803'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t2666", [self.netlist['n757'],self.netlist['n756'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1996", [self.netlist['n559'],self.port['gnd'].netconn,self.netlist['adda3']], isweak=False, parent=self),
            NMOS("t928", [self.netlist['n249'],self.netlist['n2737'],self.netlist['n164']], isweak=False, parent=self),
            NMOS("t3264", [self.netlist['n1006'],self.netlist['n1576'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3265", [self.netlist['n1006'],self.netlist['n2875'],self.netlist['n998']], isweak=False, parent=self),
            NMOS("t3266", [self.netlist['n1006'],self.netlist['n2876'],self.netlist['n1011']], isweak=False, parent=self),
            NMOS("t3267", [self.port['gnd'].netconn,self.netlist['flagi'],self.netlist['n1576']], isweak=False, parent=self),
            NMOS("t3260", [self.netlist['n2875'],self.port['gnd'].netconn,self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3263", [self.netlist['flagi'],self.netlist['n1011'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3268", [self.netlist['n2876'],self.port['gnd'].netconn,self.netlist['n1008']], isweak=False, parent=self),
            NMOS("t3269", [self.netlist['n2877'],self.port['gnd'].netconn,self.netlist['n1010']], isweak=False, parent=self),
            NMOS("t399", [self.netlist['n1675'],self.netlist['n1674'],self.netlist['incli0_0']], isweak=False, parent=self),
            NMOS("t2943", [self.netlist['n877'],self.netlist['n876'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t390", [self.netlist['n1663'],self.port['vcc'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t391", [self.port['vcc'].netconn,self.netlist['n1676'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t392", [self.port['vcc'].netconn,self.netlist['n1652'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t393", [self.port['vcc'].netconn,self.netlist['n1675'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t394", [self.port['vcc'].netconn,self.netlist['n1674'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t395", [self.netlist['n1676'],self.netlist['n1652'],self.netlist['incli2_0']], isweak=False, parent=self),
            NMOS("t397", [self.netlist['n1652'],self.netlist['n1675'],self.netlist['incli1_0']], isweak=False, parent=self),
            NMOS("t2765", [self.netlist['n454'],self.netlist['n2818'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t2763", [self.netlist['n2818'],self.port['gnd'].netconn,self.netlist['n1366']], isweak=False, parent=self),
            NMOS("t2944", [self.netlist['Ta0'],self.netlist['n878'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3868", [self.port['gnd'].netconn,self.netlist['n1514'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3869", [self.port['gnd'].netconn,self.netlist['n1808'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3866", [self.port['gnd'].netconn,self.netlist['n1809'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3867", [self.port['gnd'].netconn,self.netlist['n1608'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3864", [self.port['gnd'].netconn,self.netlist['n1627'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3865", [self.port['gnd'].netconn,self.netlist['n1841'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3862", [self.port['gnd'].netconn,self.netlist['n1613'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3863", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3860", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3861", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3192", [self.netlist['n984'],self.port['gnd'].netconn,self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t3193", [self.netlist['n984'],self.port['gnd'].netconn,self.netlist['n1370']], isweak=False, parent=self),
            NMOS("t3190", [self.netlist['n983'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1460", [self.port['gnd'].netconn,self.netlist['ixl7'],self.netlist['n1782']], isweak=False, parent=self),
            NMOS("t3196", [self.netlist['n985'],self.netlist['n2862'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t3197", [self.netlist['n985'],self.netlist['n2862'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t3194", [self.netlist['n984'],self.port['gnd'].netconn,self.netlist['n1397']], isweak=False, parent=self),
            NMOS("t3198", [self.netlist['n2862'],self.port['gnd'].netconn,self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t3199", [self.netlist['n2862'],self.port['gnd'].netconn,self.netlist['flagz']], isweak=False, parent=self),
            NMOS("t2948", [self.netlist['n881'],self.port['gnd'].netconn,self.netlist['n882']], isweak=False, parent=self),
            NMOS("t3462", [self.netlist['n2905'],self.port['gnd'].netconn,self.netlist['n1084']], isweak=False, parent=self),
            NMOS("t3463", [self.netlist['n1087'],self.netlist['n2905'],self.netlist['n1088']], isweak=False, parent=self),
            NMOS("t3460", [self.port['gnd'].netconn,self.netlist['n2904'],self.netlist['n1086']], isweak=False, parent=self),
            NMOS("t3461", [self.netlist['n1085'],self.port['gnd'].netconn,self.netlist['n1086']], isweak=False, parent=self),
            NMOS("t3467", [self.netlist['n1090'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t3999", [self.port['gnd'].netconn,self.netlist['n1628'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t3465", [self.netlist['n1090'],self.port['gnd'].netconn,self.netlist['n1084']], isweak=False, parent=self),
            NMOS("t4275", [self.port['gnd'].netconn,self.netlist['i4'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4006", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t3469", [self.netlist['n2904'],self.netlist['n1087'],self.netlist['n1082']], isweak=False, parent=self),
            NMOS("t3457", [self.netlist['Tg7'],self.netlist['n1082'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1992", [self.netlist['sumab3'],self.port['gnd'].netconn,self.netlist['n559']], isweak=False, parent=self),
            NMOS("t3456", [self.netlist['Tg6'],self.netlist['n1080'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2769", [self.netlist['n749'],self.port['gnd'].netconn,self.netlist['n799']], isweak=False, parent=self),
            NMOS("t4952", [self.port['vcc'].netconn,self.netlist['n1612'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5058", [self.netlist['n1487'],self.port['gnd'].netconn,self.netlist['res']], isweak=False, parent=self),
            NMOS("t4001", [self.port['gnd'].netconn,self.netlist['n1515'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t3452", [self.netlist['n1075'],self.port['gnd'].netconn,self.netlist['n1076']], isweak=False, parent=self),
            NMOS("t1828", [self.netlist['n518'],self.netlist['adda1in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t1829", [self.netlist['n519'],self.netlist['adda0in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t3998", [self.port['gnd'].netconn,self.netlist['n1516'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4293", [self.port['gnd'].netconn,self.netlist['i1'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4056", [self.port['gnd'].netconn,self.netlist['n1514'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t1820", [self.netlist['adda1in'],self.netlist['adda1'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1821", [self.netlist['adda0in'],self.netlist['adda0'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1822", [self.netlist['n506'],self.netlist['adda7in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t1823", [self.netlist['n507'],self.netlist['adda6in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t1824", [self.netlist['n510'],self.netlist['adda5in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t1825", [self.netlist['n511'],self.netlist['adda4in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t1826", [self.netlist['n514'],self.netlist['adda3in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t1827", [self.netlist['n515'],self.netlist['adda2in'],self.netlist['n415']], isweak=False, parent=self),
            NMOS("t732", [self.netlist['pch5'],self.netlist['pch5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2020", [self.port['gnd'].netconn,self.netlist['addb2'],self.netlist['n502']], isweak=False, parent=self),
            NMOS("t2023", [self.netlist['n2757'],self.netlist['sumab1'],self.netlist['addb1']], isweak=False, parent=self),
            NMOS("t2022", [self.netlist['sumab1'],self.port['gnd'].netconn,self.netlist['n567']], isweak=False, parent=self),
            NMOS("t2025", [self.port['gnd'].netconn,self.netlist['n2758'],self.netlist['adda1']], isweak=False, parent=self),
            NMOS("t737", [self.netlist['pch4'],self.netlist['pch4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3689", [self.port['gnd'].netconn,self.netlist['n1182'],self.netlist['n1180']], isweak=False, parent=self),
            NMOS("t3686", [self.netlist['n1180'],self.port['gnd'].netconn,self.netlist['Tg7']], isweak=False, parent=self),
            NMOS("t2028", [self.netlist['n567'],self.port['gnd'].netconn,self.netlist['addb1']], isweak=False, parent=self),
            NMOS("t738", [self.netlist['pch3'],self.netlist['pch3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3682", [self.netlist['n1177'],self.netlist['n1178'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3683", [self.netlist['n2'],self.netlist['n1179'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3681", [self.netlist['n1175'],self.port['gnd'].netconn,self.netlist['n1178']], isweak=False, parent=self),
            NMOS("t5051", [self.netlist['n1483'],self.netlist['n1470'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4057", [self.port['gnd'].netconn,self.netlist['n1529'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t3049", [self.netlist['n779'],self.port['gnd'].netconn,self.netlist['n943']], isweak=False, parent=self),
            NMOS("t3518", [self.netlist['n1115'],self.netlist['n2907'],self.netlist['n1093']], isweak=False, parent=self),
            NMOS("t4299", [self.port['gnd'].netconn,self.netlist['i0'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t3044", [self.netlist['n527'],self.netlist['n2845'],self.netlist['n1094']], isweak=False, parent=self),
            NMOS("t3045", [self.netlist['n2845'],self.port['gnd'].netconn,self.netlist['n926']], isweak=False, parent=self),
            NMOS("t3046", [self.port['gnd'].netconn,self.netlist['n483'],self.netlist['Tx0']], isweak=False, parent=self),
            NMOS("t3515", [self.port['gnd'].netconn,self.netlist['n1125'],self.netlist['n1370']], isweak=False, parent=self),
            NMOS("t3040", [self.netlist['n2844'],self.netlist['n479'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3513", [self.netlist['n1126'],self.netlist['n2908'],self.netlist['flagv']], isweak=False, parent=self),
            NMOS("t3510", [self.netlist['n1108'],self.port['gnd'].netconn,self.netlist['n1123']], isweak=False, parent=self),
            NMOS("t3043", [self.netlist['n483'],self.port['gnd'].netconn,self.netlist['n1092']], isweak=False, parent=self),
            NMOS("t5052", [self.netlist['n1485'],self.netlist['n1486'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2933", [self.netlist['n869'],self.netlist['n2832'],self.netlist['n862']], isweak=False, parent=self),
            NMOS("t4054", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2931", [self.netlist['n869'],self.netlist['n870'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t521", [self.port['gnd'].netconn,self.netlist['n133'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2936", [self.netlist['n873'],self.netlist['n872'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2935", [self.netlist['n862'],self.netlist['Tg3'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5054", [self.netlist['n1470'],self.port['gnd'].netconn,self.netlist['n1487']], isweak=False, parent=self),
            NMOS("t1914", [self.netlist['n542'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t1915", [self.netlist['n551'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t1916", [self.netlist['n554'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t1917", [self.netlist['n555'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t1910", [self.netlist['n2758'],self.netlist['n2757'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t1911", [self.netlist['n2760'],self.netlist['n2759'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t1912", [self.netlist['n538'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t652", [self.port['gnd'].netconn,self.netlist['n177'],self.netlist['n446']], isweak=False, parent=self),
            NMOS("t1412", [self.netlist['ixh6'],self.port['gnd'].netconn,self.netlist['n1729']], isweak=False, parent=self),
            NMOS("t1918", [self.netlist['n549'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t1919", [self.netlist['n559'],self.port['gnd'].netconn,self.netlist['n473']], isweak=False, parent=self),
            NMOS("t4002", [self.port['gnd'].netconn,self.netlist['n1615'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t972", [self.port['vcc'].netconn,self.netlist['idb4'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t520", [self.netlist['n1647'],self.port['vcc'].netconn,self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4208", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4055", [self.port['gnd'].netconn,self.netlist['n1794'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2840", [self.netlist['Tg2'],self.port['gnd'].netconn,self.netlist['n834']], isweak=False, parent=self),
            NMOS("t2484", [self.port['ab12'].netconn,self.port['gnd'].netconn,self.netlist['n689']], isweak=False, parent=self),
            NMOS("t2335", [self.port['db4'].netconn,self.port['vcc'].netconn,self.netlist['n666']], isweak=False, parent=self),
            NMOS("t2337", [self.port['db5'].netconn,self.port['vcc'].netconn,self.netlist['n667']], isweak=False, parent=self),
            NMOS("t2488", [self.port['db7'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2330", [self.port['db6'].netconn,self.port['gnd'].netconn,self.port['gnd'].netconn], isweak=False, parent=self),
            NMOS("t2806", [self.port['gnd'].netconn,self.netlist['n812'],self.netlist['abh3']], isweak=False, parent=self),
            NMOS("t2805", [self.netlist['n812'],self.netlist['n813'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t2803", [self.port['gnd'].netconn,self.netlist['n810'],self.netlist['abh2']], isweak=False, parent=self),
            NMOS("t2802", [self.netlist['n810'],self.netlist['n811'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t1358", [self.netlist['ixh3'],self.netlist['idb3'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t2800", [self.port['gnd'].netconn,self.netlist['n808'],self.netlist['abh5']], isweak=False, parent=self),
            NMOS("t1356", [self.netlist['abl3'],self.netlist['ablx3'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t1357", [self.netlist['ablx3'],self.netlist['ixh3'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1354", [self.netlist['idb3'],self.netlist['ixl3_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t1355", [self.netlist['ixl3_1'],self.netlist['abl3'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1352", [self.netlist['ablx1'],self.netlist['ixh1'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1353", [self.netlist['ixh1'],self.netlist['idb1'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t2809", [self.port['gnd'].netconn,self.netlist['n814'],self.netlist['abh6']], isweak=False, parent=self),
            NMOS("t1351", [self.netlist['abl1'],self.netlist['ablx1'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t813", [self.netlist['n2713'],self.netlist['n213'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t812", [self.netlist['n2712'],self.netlist['n216'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t811", [self.netlist['n2711'],self.netlist['n212'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t810", [self.netlist['n2710'],self.netlist['n215'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t816", [self.netlist['n2716'],self.netlist['n218'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t815", [self.netlist['n2715'],self.netlist['n214'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t814", [self.netlist['n2714'],self.netlist['n217'],self.netlist['n95']], isweak=False, parent=self),
            NMOS("t4650", [self.netlist['n1624'],self.netlist['n1414'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4651", [self.netlist['n1815'],self.netlist['n1407'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4652", [self.netlist['n1623'],self.netlist['n1415'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4653", [self.netlist['n1524'],self.netlist['n1420'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4654", [self.netlist['n1792'],self.netlist['n1411'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4655", [self.netlist['n1510'],self.netlist['n1423'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4656", [self.netlist['n1820'],self.netlist['n1001'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4657", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['n1313']], isweak=False, parent=self),
            NMOS("t2158", [self.netlist['n607'],self.port['gnd'].netconn,self.port['db0'].netconn], isweak=False, parent=self),
            NMOS("t1227", [self.netlist['n309'],self.port['gnd'].netconn,self.netlist['n287']], isweak=False, parent=self),
            NMOS("t2151", [self.netlist['dbi1'],self.port['gnd'].netconn,self.netlist['n605']], isweak=False, parent=self),
            NMOS("t2150", [self.netlist['dbi2'],self.port['gnd'].netconn,self.netlist['n603']], isweak=False, parent=self),
            NMOS("t2153", [self.netlist['idb1'],self.netlist['dbi1'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t1229", [self.netlist['n308'],self.port['gnd'].netconn,self.netlist['flagh']], isweak=False, parent=self),
            NMOS("t2155", [self.netlist['dbo1'],self.netlist['idb1'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t2154", [self.netlist['idb2'],self.netlist['dbo2'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t2157", [self.port['gnd'].netconn,self.netlist['n596'],self.port['db2'].netconn], isweak=False, parent=self),
            NMOS("t2156", [self.netlist['n597'],self.port['gnd'].netconn,self.port['db1'].netconn], isweak=False, parent=self),
            NMOS("t1178", [self.port['gnd'].netconn,self.netlist['abh1'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1179", [self.port['gnd'].netconn,self.netlist['abh0'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1172", [self.port['gnd'].netconn,self.netlist['abh7'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1173", [self.port['gnd'].netconn,self.netlist['abh6'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1170", [self.netlist['sph7'],self.netlist['sph7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1176", [self.port['gnd'].netconn,self.netlist['abh3'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1177", [self.port['gnd'].netconn,self.netlist['abh2'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1174", [self.port['gnd'].netconn,self.netlist['abh5'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t1175", [self.port['gnd'].netconn,self.netlist['abh4'],self.netlist['n181']], isweak=False, parent=self),
            NMOS("t2591", [self.netlist['n732'],self.netlist['n734'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1598", [self.netlist['n375'],self.port['gnd'].netconn,self.netlist['flagz']], isweak=False, parent=self),
            NMOS("t1599", [self.netlist['n376'],self.port['gnd'].netconn,self.netlist['n287']], isweak=False, parent=self),
            NMOS("t4257", [self.port['gnd'].netconn,self.netlist['i7'],self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4250", [self.netlist['n1252'],self.port['gnd'].netconn,self.port['db2'].netconn], isweak=False, parent=self),
            NMOS("t4251", [self.port['gnd'].netconn,self.netlist['n1253'],self.port['db3'].netconn], isweak=False, parent=self),
            NMOS("t4252", [self.netlist['n1254'],self.port['gnd'].netconn,self.port['db4'].netconn], isweak=False, parent=self),
            NMOS("t4596", [self.port['gnd'].netconn,self.netlist['n1824'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t5095", [self.port['vcc'].netconn,self.port['vma'].netconn,self.netlist['n1500']], isweak=False, parent=self),
            NMOS("t1591", [self.netlist['n1710'],self.port['gnd'].netconn,self.netlist['acca0_1']], isweak=False, parent=self),
            NMOS("t1592", [self.port['gnd'].netconn,self.netlist['acca0'],self.netlist['n1710']], isweak=False, parent=self),
            NMOS("t4258", [self.netlist['n1260'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t4259", [self.netlist['n1260'],self.port['gnd'].netconn,self.netlist['ir7_1']], isweak=False, parent=self),
            NMOS("t1597", [self.netlist['n375'],self.port['gnd'].netconn,self.netlist['n287']], isweak=False, parent=self),
            NMOS("t1770", [self.netlist['n381'],self.netlist['adda1in'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1771", [self.netlist['adda2in'],self.netlist['n381'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1772", [self.netlist['adda4in'],self.netlist['idb5_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t1773", [self.netlist['adda3in'],self.netlist['idb4_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t1774", [self.port['gnd'].netconn,self.netlist['adda4in'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1775", [self.port['gnd'].netconn,self.netlist['adda3in'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t4324", [self.netlist['ir4_1'],self.port['gnd'].netconn,self.netlist['n1298']], isweak=False, parent=self),
            NMOS("t4325", [self.netlist['ir5_1'],self.port['gnd'].netconn,self.netlist['n1299']], isweak=False, parent=self),
            NMOS("t4320", [self.netlist['n1276'],self.port['gnd'].netconn,self.netlist['n1245']], isweak=False, parent=self),
            NMOS("t4321", [self.netlist['ir1_1'],self.port['gnd'].netconn,self.netlist['n1290']], isweak=False, parent=self),
            NMOS("t4322", [self.netlist['ir2_1'],self.port['gnd'].netconn,self.netlist['n1296']], isweak=False, parent=self),
            NMOS("t4323", [self.netlist['ir3_1'],self.port['gnd'].netconn,self.netlist['n1297']], isweak=False, parent=self),
            NMOS("t1576", [self.port['gnd'].netconn,self.netlist['n1719'],self.netlist['acca3_1']], isweak=False, parent=self),
            NMOS("t1577", [self.port['gnd'].netconn,self.netlist['acca3'],self.netlist['n1719']], isweak=False, parent=self),
            NMOS("t1574", [self.netlist['n1723'],self.port['gnd'].netconn,self.netlist['acca4_1']], isweak=False, parent=self),
            NMOS("t1575", [self.port['gnd'].netconn,self.netlist['acca4'],self.netlist['n1723']], isweak=False, parent=self),
            NMOS("t1290", [self.netlist['n329'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1578", [self.netlist['acca1'],self.netlist['acca1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1579", [self.netlist['acca2'],self.netlist['acca2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4136", [self.port['gnd'].netconn,self.netlist['n1799'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t2642", [self.netlist['n749'],self.netlist['n748'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1469", [self.port['gnd'].netconn,self.netlist['n1730'],self.netlist['ixl6_1']], isweak=False, parent=self),
            NMOS("t4161", [self.port['gnd'].netconn,self.netlist['n1833'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t1684", [self.netlist['dbi3'],self.port['gnd'].netconn,self.netlist['n403']], isweak=False, parent=self),
            NMOS("t1685", [self.netlist['idb4'],self.netlist['dbi4'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t1686", [self.netlist['dbi3'],self.netlist['idb3'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t1687", [self.netlist['idb4'],self.netlist['dbo4'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t4434", [self.port['gnd'].netconn,self.netlist['n1533'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4435", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t4436", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t1683", [self.netlist['dbi4'],self.port['gnd'].netconn,self.netlist['n407']], isweak=False, parent=self),
            NMOS("t4438", [self.port['gnd'].netconn,self.netlist['n1619'],self.netlist['i6']], isweak=False, parent=self),
            NMOS("t2111", [self.netlist['n587'],self.port['gnd'].netconn,self.netlist['n589']], isweak=False, parent=self),
            NMOS("t1688", [self.netlist['idb3'],self.netlist['dbo3'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t1689", [self.port['gnd'].netconn,self.netlist['n399'],self.port['db3'].netconn], isweak=False, parent=self),
            NMOS("t1951", [self.port['gnd'].netconn,self.netlist['n542'],self.netlist['adda6']], isweak=False, parent=self),
            NMOS("t588", [self.netlist['n1773'],self.port['gnd'].netconn,self.netlist['pcl6_1']], isweak=False, parent=self),
            NMOS("t4209", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t991", [self.netlist['n277'],self.port['gnd'].netconn,self.netlist['abh0']], isweak=False, parent=self),
            NMOS("t585", [self.netlist['n1777'],self.port['gnd'].netconn,self.netlist['pcl5_1']], isweak=False, parent=self),
            NMOS("t3133", [self.port['gnd'].netconn,self.netlist['Ta0'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t584", [self.port['gnd'].netconn,self.netlist['n1774'],self.netlist['pcl7_1']], isweak=False, parent=self),
            NMOS("t664", [self.netlist['n174'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t728", [self.netlist['pch4'],self.port['gnd'].netconn,self.netlist['n1765']], isweak=False, parent=self),
            NMOS("t586", [self.port['gnd'].netconn,self.netlist['n1776'],self.netlist['pcl3_1']], isweak=False, parent=self),
            NMOS("t2118", [self.netlist['n594'],self.port['gnd'].netconn,self.netlist['n570']], isweak=False, parent=self),
            NMOS("t3139", [self.netlist['n962'],self.netlist['n875'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t850", [self.port['gnd'].netconn,self.netlist['n222'],self.netlist['n230']], isweak=False, parent=self),
            NMOS("t727", [self.netlist['pch6'],self.port['gnd'].netconn,self.netlist['n1769']], isweak=False, parent=self),
            NMOS("t1136", [self.netlist['idb6'],self.netlist['spl6_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t1137", [self.netlist['spl1_1'],self.netlist['abl1'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t251", [self.port['gnd'].netconn,self.netlist['ald7_0'],self.netlist['n1662']], isweak=False, parent=self),
            NMOS("t253", [self.port['gnd'].netconn,self.netlist['n54'],self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t255", [self.port['gnd'].netconn,self.netlist['n2684'],self.netlist['n1660']], isweak=False, parent=self),
            NMOS("t1134", [self.netlist['idb4'],self.netlist['spl4_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t1135", [self.netlist['spl6_1'],self.netlist['abl6'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1247", [self.port['gnd'].netconn,self.netlist['n317'],self.netlist['n463']], isweak=False, parent=self),
            NMOS("t2404", [self.netlist['n682'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t1133", [self.netlist['spl4_1'],self.netlist['abl4'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t4926", [self.port['vcc'].netconn,self.netlist['n1616'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4927", [self.port['vcc'].netconn,self.netlist['n1835'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4924", [self.port['vcc'].netconn,self.netlist['n1522'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t371", [self.netlist['n77'],self.port['gnd'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t4922", [self.port['vcc'].netconn,self.netlist['n1607'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1130", [self.netlist['idb0'],self.netlist['spl0_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t4920", [self.port['vcc'].netconn,self.netlist['n1513'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4921", [self.port['vcc'].netconn,self.netlist['n1793'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4928", [self.port['vcc'].netconn,self.netlist['n1529'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4929", [self.port['vcc'].netconn,self.netlist['n1808'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1648", [self.netlist['n391'],self.netlist['n388'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2649", [self.port['gnd'].netconn,self.netlist['n426'],self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t3917", [self.port['gnd'].netconn,self.netlist['n1849'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2777", [self.port['gnd'].netconn,self.netlist['n800'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t4578", [self.netlist['n1826'],self.netlist['n1401'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3212", [self.port['gnd'].netconn,self.netlist['n987'],self.netlist['n991']], isweak=False, parent=self),
            NMOS("t3215", [self.netlist['n782'],self.netlist['n991'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3214", [self.netlist['n989'],self.port['gnd'].netconn,self.netlist['n1037']], isweak=False, parent=self),
            NMOS("t3217", [self.netlist['n993'],self.netlist['idb3'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2648", [self.netlist['n454'],self.netlist['n753'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3219", [self.netlist['flagn'],self.netlist['n994'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3218", [self.netlist['idb2'],self.netlist['n1578'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t389", [self.port['vcc'].netconn,self.netlist['n1665'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t388", [self.port['vcc'].netconn,self.netlist['n1664'],self.netlist['n94']], isweak=False, parent=self),
            NMOS("t383", [self.netlist['n78'],self.port['gnd'].netconn,self.netlist['n85']], isweak=False, parent=self),
            NMOS("t382", [self.netlist['n2692'],self.netlist['n78'],self.netlist['n42']], isweak=False, parent=self),
            NMOS("t380", [self.port['gnd'].netconn,self.netlist['n2692'],self.netlist['n80']], isweak=False, parent=self),
            NMOS("t387", [self.netlist['n1666'],self.port['vcc'].netconn,self.netlist['n94']], isweak=False, parent=self),
            NMOS("t386", [self.netlist['n86'],self.netlist['n85'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t385", [self.netlist['n84'],self.netlist['n83'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3526", [self.port['gnd'].netconn,self.netlist['flagv'],self.netlist['n1103']], isweak=False, parent=self),
            NMOS("t665", [self.netlist['n181'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3037", [self.netlist['n2843'],self.port['gnd'].netconn,self.netlist['n1367']], isweak=False, parent=self),
            NMOS("t4189", [self.port['gnd'].netconn,self.netlist['n1599'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t3859", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3858", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3853", [self.port['gnd'].netconn,self.netlist['n1516'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3852", [self.port['gnd'].netconn,self.netlist['n1796'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3851", [self.port['gnd'].netconn,self.netlist['n1829'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t4041", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t3857", [self.port['gnd'].netconn,self.netlist['n1792'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3856", [self.port['gnd'].netconn,self.netlist['n1801'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3855", [self.port['gnd'].netconn,self.netlist['n1615'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3854", [self.port['gnd'].netconn,self.netlist['n1847'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t4187", [self.port['gnd'].netconn,self.netlist['n1598'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t3328", [self.port['gnd'].netconn,self.netlist['n2886'],self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t663", [self.netlist['n180'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3458", [self.netlist['n1084'],self.netlist['n1083'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3325", [self.port['gnd'].netconn,self.netlist['n2886'],self.netlist['n1043']], isweak=False, parent=self),
            NMOS("t3324", [self.netlist['n2886'],self.netlist['n1042'],self.netlist['n1014']], isweak=False, parent=self),
            NMOS("t3455", [self.netlist['n1079'],self.netlist['n1078'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3454", [self.netlist['n1077'],self.netlist['n1075'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3453", [self.netlist['n1074'],self.netlist['n1076'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3320", [self.netlist['n1042'],self.port['gnd'].netconn,self.netlist['n1040']], isweak=False, parent=self),
            NMOS("t3323", [self.netlist['n1042'],self.port['gnd'].netconn,self.netlist['n1370']], isweak=False, parent=self),
            NMOS("t3322", [self.port['gnd'].netconn,self.netlist['n1040'],self.netlist['n1397']], isweak=False, parent=self),
            NMOS("t1488", [self.port['gnd'].netconn,self.netlist['ixl2'],self.netlist['n1709']], isweak=False, parent=self),
            NMOS("t4183", [self.port['gnd'].netconn,self.netlist['n1517'],self.netlist['n1262']], isweak=False, parent=self),
            NMOS("t3527", [self.port['gnd'].netconn,self.netlist['n2910'],self.netlist['n1104']], isweak=False, parent=self),
            NMOS("t2031", [self.netlist['n2774'],self.netlist['n2773'],self.netlist['addb1']], isweak=False, parent=self),
            NMOS("t729", [self.netlist['pch2'],self.port['gnd'].netconn,self.netlist['n1761']], isweak=False, parent=self),
            NMOS("t2037", [self.port['gnd'].netconn,self.netlist['sumab0'],self.netlist['n565']], isweak=False, parent=self),
            NMOS("t2035", [self.netlist['addb1'],self.port['gnd'].netconn,self.netlist['n493']], isweak=False, parent=self),
            NMOS("t725", [self.port['gnd'].netconn,self.netlist['pch3'],self.netlist['n1762']], isweak=False, parent=self),
            NMOS("t724", [self.port['gnd'].netconn,self.netlist['pch5'],self.netlist['n1766']], isweak=False, parent=self),
            NMOS("t2038", [self.netlist['n2759'],self.netlist['sumab0'],self.netlist['addb0']], isweak=False, parent=self),
            NMOS("t726", [self.port['gnd'].netconn,self.netlist['pch1'],self.netlist['n1757']], isweak=False, parent=self),
            NMOS("t721", [self.port['gnd'].netconn,self.netlist['n1761'],self.netlist['pch2_1']], isweak=False, parent=self),
            NMOS("t720", [self.port['gnd'].netconn,self.netlist['n1765'],self.netlist['pch4_1']], isweak=False, parent=self),
            NMOS("t723", [self.port['gnd'].netconn,self.netlist['pch7'],self.netlist['n1778']], isweak=False, parent=self),
            NMOS("t722", [self.port['gnd'].netconn,self.netlist['n1760'],self.netlist['pch0_1']], isweak=False, parent=self),
            NMOS("t3039", [self.port['gnd'].netconn,self.netlist['n2844'],self.netlist['n1438']], isweak=False, parent=self),
            NMOS("t623", [self.netlist['idb1'],self.port['gnd'].netconn,self.netlist['n135']], isweak=False, parent=self),
            NMOS("t3030", [self.netlist['n1068'],self.netlist['n2841'],self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t3033", [self.netlist['n2843'],self.port['gnd'].netconn,self.netlist['n1442']], isweak=False, parent=self),
            NMOS("t3520", [self.netlist['n1115'],self.netlist['n1569'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3035", [self.netlist['n926'],self.port['gnd'].netconn,self.netlist['Tx0']], isweak=False, parent=self),
            NMOS("t3034", [self.netlist['n471'],self.netlist['n2843'],self.netlist['n926']], isweak=False, parent=self),
            NMOS("t3525", [self.port['gnd'].netconn,self.netlist['n2909'],self.netlist['n1127']], isweak=False, parent=self),
            NMOS("t3524", [self.netlist['n2909'],self.netlist['n1109'],self.netlist['n1110']], isweak=False, parent=self),
            NMOS("t4497", [self.netlist['n1509'],self.netlist['n1322'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1966", [self.netlist['n551'],self.port['gnd'].netconn,self.netlist['adda5']], isweak=False, parent=self),
            NMOS("t621", [self.port['gnd'].netconn,self.netlist['idb0'],self.netlist['n136']], isweak=False, parent=self),
            NMOS("t622", [self.netlist['idb0'],self.netlist['pcl0'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t1962", [self.netlist['sumab5'],self.port['gnd'].netconn,self.netlist['n551']], isweak=False, parent=self),
            NMOS("t624", [self.netlist['idb1'],self.netlist['pcl1'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t625", [self.port['gnd'].netconn,self.netlist['idb2'],self.netlist['n134']], isweak=False, parent=self),
            NMOS("t626", [self.netlist['idb2'],self.netlist['pcl2'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t627", [self.netlist['idb4'],self.netlist['pcl4'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t628", [self.netlist['idb6'],self.netlist['pcl6'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t629", [self.netlist['idb3'],self.netlist['pcl3'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t4052", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4649", [self.netlist['n1625'],self.netlist['n1413'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4053", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t4062", [self.netlist['n1223'],self.netlist['n1222'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4050", [self.port['gnd'].netconn,self.netlist['n1796'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t3145", [self.port['gnd'].netconn,self.netlist['n877'],self.netlist['n1418']], isweak=False, parent=self),
            NMOS("t3144", [self.port['gnd'].netconn,self.netlist['n877'],self.netlist['Tx2']], isweak=False, parent=self),
            NMOS("t3147", [self.netlist['n877'],self.port['gnd'].netconn,self.netlist['n967']], isweak=False, parent=self),
            NMOS("t4051", [self.port['gnd'].netconn,self.netlist['n1815'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t2498", [self.port['gnd'].netconn,self.netlist['Tr8'],self.netlist['n698']], isweak=False, parent=self),
            NMOS("t3143", [self.netlist['n963'],self.port['gnd'].netconn,self.netlist['n1419']], isweak=False, parent=self),
            NMOS("t2329", [self.netlist['n665'],self.port['gnd'].netconn,self.netlist['dbo6']], isweak=False, parent=self),
            NMOS("t2494", [self.netlist['n700'],self.port['gnd'].netconn,self.netlist['n979']], isweak=False, parent=self),
            NMOS("t2327", [self.port['gnd'].netconn,self.port['db6'].netconn,self.netlist['n665']], isweak=False, parent=self),
            NMOS("t2496", [self.netlist['n699'],self.netlist['n2793'],self.netlist['n695']], isweak=False, parent=self),
            NMOS("t2497", [self.netlist['n699'],self.port['gnd'].netconn,self.netlist['n693']], isweak=False, parent=self),
            NMOS("t2322", [self.netlist['n662'],self.port['gnd'].netconn,self.netlist['n665']], isweak=False, parent=self),
            NMOS("t2320", [self.port['db6'].netconn,self.port['vcc'].netconn,self.netlist['n662']], isweak=False, parent=self),
            NMOS("t4505", [self.netlist['n1522'],self.netlist['n1330'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2717", [self.netlist['n528'],self.port['gnd'].netconn,self.netlist['n780']], isweak=False, parent=self),
            NMOS("t2812", [self.port['gnd'].netconn,self.netlist['n816'],self.netlist['abh4']], isweak=False, parent=self),
            NMOS("t1368", [self.netlist['ixh7'],self.netlist['idb7'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t2814", [self.netlist['n818'],self.netlist['n819'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t2815", [self.port['gnd'].netconn,self.netlist['n818'],self.netlist['abh1']], isweak=False, parent=self),
            NMOS("t2817", [self.port['gnd'].netconn,self.netlist['n820'],self.netlist['n1407']], isweak=False, parent=self),
            NMOS("t1363", [self.netlist['ixh5'],self.netlist['idb5'],self.netlist['n328']], isweak=False, parent=self),
            NMOS("t1362", [self.netlist['ablx5'],self.netlist['ixh5'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1361", [self.netlist['abl5'],self.netlist['ablx5'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t1360", [self.netlist['ixl5_1'],self.netlist['abl5'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1367", [self.netlist['ablx7'],self.netlist['ixh7'],self.netlist['n319']], isweak=False, parent=self),
            NMOS("t1366", [self.netlist['abl7'],self.netlist['ablx7'],self.netlist['n326']], isweak=False, parent=self),
            NMOS("t1365", [self.netlist['ixl7_1'],self.netlist['abl7'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1364", [self.netlist['idb7'],self.netlist['ixl7_1'],self.netlist['n320']], isweak=False, parent=self),
            NMOS("t3763", [self.port['gnd'].netconn,self.netlist['n1797'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t538", [self.port['gnd'].netconn,self.netlist['incl0'],self.netlist['n119']], isweak=False, parent=self),
            NMOS("t1848", [self.port['gnd'].netconn,self.netlist['n510'],self.netlist['idb5']], isweak=False, parent=self),
            NMOS("t828", [self.netlist['n229'],self.port['gnd'].netconn,self.netlist['n1758']], isweak=False, parent=self),
            NMOS("t3373", [self.netlist['n1049'],self.port['gnd'].netconn,self.netlist['n1047']], isweak=False, parent=self),
            NMOS("t826", [self.netlist['n227'],self.port['gnd'].netconn,self.netlist['n1767']], isweak=False, parent=self),
            NMOS("t827", [self.netlist['n228'],self.port['gnd'].netconn,self.netlist['n1763']], isweak=False, parent=self),
            NMOS("t536", [self.netlist['n140'],self.port['gnd'].netconn,self.netlist['n120']], isweak=False, parent=self),
            NMOS("t537", [self.netlist['incl1'],self.port['gnd'].netconn,self.netlist['n115']], isweak=False, parent=self),
            NMOS("t530", [self.port['gnd'].netconn,self.netlist['n136'],self.netlist['n128']], isweak=False, parent=self),
            NMOS("t531", [self.port['gnd'].netconn,self.netlist['n137'],self.netlist['n126']], isweak=False, parent=self),
            NMOS("t532", [self.netlist['n139'],self.port['gnd'].netconn,self.netlist['n124']], isweak=False, parent=self),
            NMOS("t533", [self.port['gnd'].netconn,self.netlist['n138'],self.netlist['n122']], isweak=False, parent=self),
            NMOS("t2924", [self.port['gnd'].netconn,self.netlist['n862'],self.netlist['res']], isweak=False, parent=self),
            NMOS("t2925", [self.netlist['n864'],self.port['gnd'].netconn,self.netlist['n865']], isweak=False, parent=self),
            NMOS("t2927", [self.netlist['n865'],self.netlist['n866'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2922", [self.netlist['n2831'],self.netlist['n861'],self.netlist['n864']], isweak=False, parent=self),
            NMOS("t2923", [self.port['gnd'].netconn,self.netlist['n2831'],self.netlist['n971']], isweak=False, parent=self),
            NMOS("t2143", [self.netlist['n603'],self.port['vcc'].netconn,self.netlist['n606']], isweak=False, parent=self),
            NMOS("t1215", [self.netlist['sph0'],self.netlist['sph0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2141", [self.netlist['n600'],self.port['gnd'].netconn,self.netlist['dbi1']], isweak=False, parent=self),
            NMOS("t1213", [self.port['gnd'].netconn,self.netlist['n1735'],self.netlist['sph0_1']], isweak=False, parent=self),
            NMOS("t2147", [self.netlist['n600'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1211", [self.netlist['n1738'],self.port['gnd'].netconn,self.netlist['sph1_1']], isweak=False, parent=self),
            NMOS("t1210", [self.port['gnd'].netconn,self.netlist['sph1'],self.netlist['n1738']], isweak=False, parent=self),
            NMOS("t4683", [self.netlist['n1832'],self.netlist['n1427'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4682", [self.netlist['n1831'],self.netlist['n1426'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4681", [self.netlist['n1830'],self.netlist['n1425'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4680", [self.netlist['n1829'],self.netlist['n1424'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4687", [self.netlist['n1838'],self.netlist['n1431'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4686", [self.netlist['n1837'],self.netlist['n1430'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4685", [self.netlist['n1835'],self.netlist['n1429'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4684", [self.netlist['n1834'],self.netlist['n1428'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4135", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4134", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4689", [self.netlist['n1840'],self.netlist['n1433'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4688", [self.netlist['n1839'],self.netlist['n1432'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4131", [self.port['gnd'].netconn,self.netlist['n1833'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4130", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4133", [self.port['gnd'].netconn,self.netlist['n1824'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4132", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t1840", [self.netlist['n506'],self.port['gnd'].netconn,self.netlist['idb7']], isweak=False, parent=self),
            NMOS("t4980", [self.port['vcc'].netconn,self.netlist['n1609'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2718", [self.netlist['n528'],self.port['gnd'].netconn,self.netlist['n778']], isweak=False, parent=self),
            NMOS("t5019", [self.port['vcc'].netconn,self.netlist['n1812'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4221", [self.port['gnd'].netconn,self.netlist['n1617'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4220", [self.port['gnd'].netconn,self.netlist['n1836'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4222", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4225", [self.netlist['n1244'],self.netlist['n1242'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4224", [self.netlist['n1243'],self.netlist['n1241'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4227", [self.netlist['n1243'],self.port['gnd'].netconn,self.port['db6'].netconn], isweak=False, parent=self),
            NMOS("t4229", [self.netlist['n1245'],self.netlist['n8'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4228", [self.port['gnd'].netconn,self.netlist['n1244'],self.port['db7'].netconn], isweak=False, parent=self),
            NMOS("t5084", [self.port['gnd'].netconn,self.netlist['vma_0'],self.netlist['n1472']], isweak=False, parent=self),
            NMOS("t5085", [self.port['gnd'].netconn,self.netlist['n1499'],self.netlist['vma_0']], isweak=False, parent=self),
            NMOS("t5083", [self.port['gnd'].netconn,self.netlist['vma_0'],self.netlist['n1508']], isweak=False, parent=self),
            NMOS("t5080", [self.port['gnd'].netconn,self.netlist['vma_0'],self.netlist['n2']], isweak=False, parent=self),
            NMOS("t5081", [self.netlist['vma_0'],self.port['gnd'].netconn,self.netlist['n1489']], isweak=False, parent=self),
            NMOS("t4359", [self.netlist['n1295'],self.port['gnd'].netconn,self.netlist['n1258']], isweak=False, parent=self),
            NMOS("t4358", [self.port['gnd'].netconn,self.netlist['n1292'],self.netlist['n1257']], isweak=False, parent=self),
            NMOS("t2328", [self.netlist['n665'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t1785", [self.netlist['adda5in'],self.netlist['n379'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1784", [self.netlist['n379'],self.netlist['adda6in'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1787", [self.port['gnd'].netconn,self.netlist['adda7in'],self.netlist['n418']], isweak=False, parent=self),
            NMOS("t1786", [self.netlist['adda7in'],self.netlist['n765'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t1783", [self.netlist['adda6in'],self.netlist['idb7_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t1782", [self.netlist['adda5in'],self.netlist['idb6_2'],self.netlist['n416']], isweak=False, parent=self),
            NMOS("t1543", [self.port['gnd'].netconn,self.netlist['n1704'],self.netlist['accb0_1']], isweak=False, parent=self),
            NMOS("t1541", [self.netlist['accb0'],self.netlist['accb0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1547", [self.netlist['acca2'],self.netlist['idb2'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t1546", [self.netlist['acca1'],self.netlist['idb1'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t1545", [self.netlist['acca0'],self.netlist['idb0'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t2495", [self.netlist['n2793'],self.port['gnd'].netconn,self.netlist['n846']], isweak=False, parent=self),
            NMOS("t4531", [self.netlist['n1611'],self.netlist['n1355'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t1549", [self.netlist['acca4'],self.netlist['idb4'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t1548", [self.netlist['acca3'],self.netlist['idb3'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t3149", [self.netlist['n965'],self.port['gnd'].netconn,self.netlist['n1379']], isweak=False, parent=self),
            NMOS("t1147", [self.netlist['sph2_1'],self.netlist['idb2'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1146", [self.netlist['sph0_1'],self.netlist['abh0'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1145", [self.netlist['sph0_1'],self.netlist['idb0'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1144", [self.netlist['idb7'],self.netlist['spl7_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t1143", [self.netlist['spl7_1'],self.netlist['abl7'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1142", [self.netlist['idb5'],self.netlist['spl5_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t1141", [self.netlist['spl5_1'],self.netlist['abl5'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1140", [self.netlist['idb3'],self.netlist['spl3_1'],self.netlist['n177']], isweak=False, parent=self),
            NMOS("t3623", [self.netlist['n2926'],self.netlist['n2925'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t1149", [self.netlist['sph4_1'],self.netlist['idb4'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1148", [self.netlist['sph2_1'],self.netlist['abh2'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t2811", [self.netlist['n816'],self.netlist['n817'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t1369", [self.netlist['idb0'],self.netlist['accb0'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t1737", [self.netlist['n452'],self.netlist['n453'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2818", [self.netlist['n820'],self.port['gnd'].netconn,self.netlist['Tg6']], isweak=False, parent=self),
            NMOS("t660", [self.netlist['n172'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t599", [self.port['gnd'].netconn,self.netlist['pcl0'],self.netlist['n1770']], isweak=False, parent=self),
            NMOS("t661", [self.netlist['n179'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4912", [self.netlist['n1480'],self.netlist['n1606'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4911", [self.port['gnd'].netconn,self.netlist['n1479'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4910", [self.netlist['n1606'],self.netlist['n1478'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4917", [self.netlist['n1480'],self.port['gnd'].netconn,self.netlist['n1481']], isweak=False, parent=self),
            NMOS("t4916", [self.port['gnd'].netconn,self.netlist['n1481'],self.netlist['n1606']], isweak=False, parent=self),
            NMOS("t4914", [self.netlist['n1480'],self.port['gnd'].netconn,self.netlist['n1479']], isweak=False, parent=self),
            NMOS("t4919", [self.netlist['n1481'],self.port['gnd'].netconn,self.netlist['n1480']], isweak=False, parent=self),
            NMOS("t662", [self.netlist['n173'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t436", [self.netlist['n99'],self.netlist['n2697'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2519", [self.netlist['n866'],self.netlist['n705'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t432", [self.netlist['n97'],self.netlist['n2693'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t46", [self.port['gnd'].netconn,self.port['ab0'].netconn,self.netlist['n21']], isweak=False, parent=self),
            NMOS("t45", [self.port['ab5'].netconn,self.port['vcc'].netconn,self.netlist['n18']], isweak=False, parent=self),
            NMOS("t3202", [self.netlist['n2863'],self.netlist['n2864'],self.netlist['n1370']], isweak=False, parent=self),
            NMOS("t3203", [self.netlist['n2864'],self.port['gnd'].netconn,self.netlist['n985']], isweak=False, parent=self),
            NMOS("t3201", [self.netlist['n986'],self.netlist['n2863'],self.netlist['n1003']], isweak=False, parent=self),
            NMOS("t3206", [self.port['gnd'].netconn,self.netlist['n987'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3205", [self.port['gnd'].netconn,self.netlist['n988'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3208", [self.netlist['n2865'],self.port['gnd'].netconn,self.netlist['n988']], isweak=False, parent=self),
            NMOS("t3209", [self.netlist['n990'],self.netlist['n2865'],self.netlist['n1006']], isweak=False, parent=self),
            NMOS("t2321", [self.netlist['n662'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t438", [self.netlist['n100'],self.netlist['n2699'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3876", [self.port['gnd'].netconn,self.netlist['n1794'],self.netlist['n1198']], isweak=False, parent=self),
            NMOS("t2952", [self.netlist['n883'],self.netlist['n884'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t539", [self.netlist['incl3'],self.port['gnd'].netconn,self.netlist['n114']], isweak=False, parent=self),
            NMOS("t3448", [self.netlist['obl6'],self.netlist['ald6_0'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t3449", [self.port['gnd'].netconn,self.netlist['n1074'],self.netlist['n1417']], isweak=False, parent=self),
            NMOS("t280", [self.netlist['n63'],self.port['gnd'].netconn,self.netlist['idb4']], isweak=False, parent=self),
            NMOS("t281", [self.port['gnd'].netconn,self.netlist['n64'],self.netlist['abl4']], isweak=False, parent=self),
            NMOS("t287", [self.port['gnd'].netconn,self.netlist['ald3_0'],self.netlist['n1668']], isweak=False, parent=self),
            NMOS("t3338", [self.netlist['n1034'],self.netlist['n2888'],self.netlist['n1128']], isweak=False, parent=self),
            NMOS("t3339", [self.netlist['n2889'],self.netlist['n1024'],self.netlist['n645']], isweak=False, parent=self),
            NMOS("t3336", [self.netlist['n2888'],self.port['gnd'].netconn,self.netlist['sum7']], isweak=False, parent=self),
            NMOS("t3334", [self.netlist['n2887'],self.netlist['n1043'],self.netlist['flagn']], isweak=False, parent=self),
            NMOS("t3443", [self.netlist['n1070'],self.port['gnd'].netconn,self.netlist['abh0']], isweak=False, parent=self),
            NMOS("t3332", [self.netlist['n1043'],self.port['gnd'].netconn,self.netlist['n1044']], isweak=False, parent=self),
            NMOS("t3333", [self.netlist['n1044'],self.port['gnd'].netconn,self.netlist['flagn']], isweak=False, parent=self),
            NMOS("t3446", [self.netlist['n1072'],self.port['gnd'].netconn,self.netlist['n1071']], isweak=False, parent=self),
            NMOS("t3331", [self.port['gnd'].netconn,self.netlist['n2887'],self.netlist['n1347']], isweak=False, parent=self),
            NMOS("t2515", [self.netlist['n701'],self.port['gnd'].netconn,self.netlist['Td0_0']], isweak=False, parent=self),
            NMOS("t2514", [self.netlist['n702'],self.port['gnd'].netconn,self.netlist['n703']], isweak=False, parent=self),
            NMOS("t825", [self.netlist['n226'],self.port['gnd'].netconn,self.netlist['n1779']], isweak=False, parent=self),
            NMOS("t3514", [self.netlist['n2908'],self.port['gnd'].netconn,self.netlist['flagn']], isweak=False, parent=self),
            NMOS("t3189", [self.port['gnd'].netconn,self.netlist['n983'],self.netlist['n982']], isweak=False, parent=self),
            NMOS("t2799", [self.netlist['n808'],self.netlist['n809'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t2518", [self.netlist['n704'],self.netlist['n703'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2797", [self.netlist['n807'],self.port['gnd'].netconn,self.netlist['n819']], isweak=False, parent=self),
            NMOS("t2795", [self.netlist['n806'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2794", [self.netlist['n806'],self.port['gnd'].netconn,self.netlist['n817']], isweak=False, parent=self),
            NMOS("t2792", [self.netlist['n805'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2791", [self.netlist['n805'],self.port['gnd'].netconn,self.netlist['n815']], isweak=False, parent=self),
            NMOS("t758", [self.netlist['inch1'],self.netlist['pch1_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t3535", [self.port['gnd'].netconn,self.netlist['n1111'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3537", [self.port['gnd'].netconn,self.netlist['n1121'],self.netlist['n1116']], isweak=False, parent=self),
            NMOS("t2559", [self.port['gnd'].netconn,self.netlist['n165'],self.netlist['n723']], isweak=False, parent=self),
            NMOS("t3531", [self.netlist['n1566'],self.netlist['n2911'],self.netlist['n1057']], isweak=False, parent=self),
            NMOS("t3532", [self.port['gnd'].netconn,self.netlist['n1111'],self.netlist['n1568']], isweak=False, parent=self),
            NMOS("t2008", [self.netlist['n2755'],self.netlist['sumab2'],self.netlist['addb2']], isweak=False, parent=self),
            NMOS("t2007", [self.port['gnd'].netconn,self.netlist['sumab2'],self.netlist['n557']], isweak=False, parent=self),
            NMOS("t752", [self.netlist['inch0'],self.netlist['abh0'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t753", [self.netlist['inch0'],self.netlist['pch0_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t3538", [self.netlist['n1116'],self.port['gnd'].netconn,self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t755", [self.netlist['inch2'],self.netlist['abh2'],self.netlist['n140']], isweak=False, parent=self),
            NMOS("t2001", [self.netlist['n2770'],self.netlist['n2769'],self.netlist['addb3']], isweak=False, parent=self),
            NMOS("t757", [self.netlist['inch2'],self.netlist['pch2_1'],self.netlist['n138']], isweak=False, parent=self),
            NMOS("t3844", [self.port['gnd'].netconn,self.netlist['n1598'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3845", [self.port['gnd'].netconn,self.netlist['n1527'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3028", [self.port['gnd'].netconn,self.netlist['n2840'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3847", [self.port['gnd'].netconn,self.netlist['n1817'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3840", [self.port['gnd'].netconn,self.netlist['n1217'],self.netlist['Tg8']], isweak=False, parent=self),
            NMOS("t3841", [self.netlist['n1083'],self.netlist['n1218'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3842", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3843", [self.port['gnd'].netconn,self.netlist['n1599'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3020", [self.port['gnd'].netconn,self.netlist['n2839'],self.netlist['n922']], isweak=False, parent=self),
            NMOS("t3021", [self.netlist['n923'],self.netlist['n922'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3848", [self.port['gnd'].netconn,self.netlist['n1806'],self.netlist['i1']], isweak=False, parent=self),
            NMOS("t3027", [self.port['gnd'].netconn,self.netlist['n2842'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3025", [self.netlist['n434'],self.netlist['n2840'],self.netlist['n1394']], isweak=False, parent=self),
            NMOS("t2889", [self.netlist['n704'],self.netlist['n2829'],self.netlist['n1320']], isweak=False, parent=self),
            NMOS("t3470", [self.netlist['n1086'],self.port['gnd'].netconn,self.netlist['n1138']], isweak=False, parent=self),
            NMOS("t2888", [self.netlist['n704'],self.port['gnd'].netconn,self.netlist['Tx1']], isweak=False, parent=self),
            NMOS("t1960", [self.port['gnd'].netconn,self.netlist['addb6'],self.netlist['n522']], isweak=False, parent=self),
            NMOS("t632", [self.netlist['n158'],self.netlist['n157'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t631", [self.netlist['idb7'],self.netlist['pcl7'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t630", [self.netlist['idb5'],self.netlist['pcl5'],self.netlist['n137']], isweak=False, parent=self),
            NMOS("t637", [self.netlist['n162'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1977", [self.port['gnd'].netconn,self.netlist['sumab4'],self.netlist['n549']], isweak=False, parent=self),
            NMOS("t635", [self.netlist['n162'],self.port['gnd'].netconn,self.netlist['n158']], isweak=False, parent=self),
            NMOS("t634", [self.netlist['n161'],self.port['gnd'].netconn,self.netlist['n159']], isweak=False, parent=self),
            NMOS("t1978", [self.netlist['n2751'],self.netlist['sumab4'],self.netlist['addb4']], isweak=False, parent=self),
            NMOS("t2140", [self.netlist['n606'],self.port['gnd'].netconn,self.netlist['dbi2']], isweak=False, parent=self),
            NMOS("t1623", [self.netlist['n2744'],self.netlist['n382'],self.netlist['acca3']], isweak=False, parent=self),
            NMOS("t2928", [self.netlist['n866'],self.port['gnd'].netconn,self.netlist['n867']], isweak=False, parent=self),
            NMOS("t3476", [self.netlist['n1085'],self.netlist['n1088'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1963", [self.netlist['n2749'],self.netlist['sumab5'],self.netlist['addb5']], isweak=False, parent=self),
            NMOS("t1212", [self.port['gnd'].netconn,self.netlist['sph0'],self.netlist['n1735']], isweak=False, parent=self),
            NMOS("t3154", [self.port['gnd'].netconn,self.netlist['n970'],self.netlist['n704']], isweak=False, parent=self),
            NMOS("t3155", [self.netlist['n969'],self.port['gnd'].netconn,self.netlist['n1398']], isweak=False, parent=self),
            NMOS("t3152", [self.netlist['n966'],self.port['gnd'].netconn,self.netlist['n1422']], isweak=False, parent=self),
            NMOS("t2144", [self.port['vcc'].netconn,self.netlist['n605'],self.netlist['n600']], isweak=False, parent=self),
            NMOS("t3150", [self.port['gnd'].netconn,self.netlist['n965'],self.netlist['n966']], isweak=False, parent=self),
            NMOS("t2311", [self.netlist['n1785'],self.port['gnd'].netconn,self.netlist['n659']], isweak=False, parent=self),
            NMOS("t2310", [self.port['gnd'].netconn,self.netlist['n658'],self.netlist['n539']], isweak=False, parent=self),
            NMOS("t2315", [self.netlist['n1785'],self.port['gnd'].netconn,self.netlist['n573']], isweak=False, parent=self),
            NMOS("t2314", [self.port['gnd'].netconn,self.netlist['n1785'],self.netlist['n540']], isweak=False, parent=self),
            NMOS("t159", [self.netlist['n39'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t5031", [self.port['vcc'].netconn,self.netlist['n1813'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5030", [self.port['vcc'].netconn,self.netlist['n1534'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4139", [self.port['gnd'].netconn,self.netlist['n1831'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4138", [self.port['gnd'].netconn,self.netlist['n1790'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t839", [self.netlist['n232'],self.port['gnd'].netconn,self.netlist['ahd2_0']], isweak=False, parent=self),
            NMOS("t2176", [self.netlist['n2784'],self.netlist['n617'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t2175", [self.netlist['n2783'],self.netlist['n613'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t2174", [self.netlist['n2782'],self.netlist['n622'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t2173", [self.netlist['n2781'],self.netlist['n614'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t2172", [self.netlist['n2780'],self.netlist['n627'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t2171", [self.netlist['n2779'],self.netlist['n615'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t528", [self.port['gnd'].netconn,self.netlist['n134'],self.netlist['n131']], isweak=False, parent=self),
            NMOS("t527", [self.netlist['n136'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t830", [self.netlist['n231'],self.port['gnd'].netconn,self.netlist['n1764']], isweak=False, parent=self),
            NMOS("t833", [self.netlist['n226'],self.port['gnd'].netconn,self.netlist['ahd7_0']], isweak=False, parent=self),
            NMOS("t832", [self.netlist['n233'],self.port['gnd'].netconn,self.netlist['n186']], isweak=False, parent=self),
            NMOS("t835", [self.netlist['n228'],self.port['gnd'].netconn,self.netlist['ahd3_0']], isweak=False, parent=self),
            NMOS("t834", [self.netlist['n227'],self.port['gnd'].netconn,self.netlist['ahd5_0']], isweak=False, parent=self),
            NMOS("t837", [self.netlist['n230'],self.port['gnd'].netconn,self.netlist['ahd6_0']], isweak=False, parent=self),
            NMOS("t836", [self.netlist['n229'],self.port['gnd'].netconn,self.netlist['ahd1_0']], isweak=False, parent=self),
            NMOS("t1208", [self.netlist['sph1'],self.netlist['sph1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2774", [self.netlist['n797'],self.port['gnd'].netconn,self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t2953", [self.port['gnd'].netconn,self.netlist['n2833'],self.netlist['n1329']], isweak=False, parent=self),
            NMOS("t2776", [self.netlist['n798'],self.netlist['n799'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2955", [self.netlist['n2833'],self.netlist['n885'],self.netlist['Tg1']], isweak=False, parent=self),
            NMOS("t2770", [self.netlist['n796'],self.netlist['n2819'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t2957", [self.netlist['n1952'],self.port['gnd'].netconn,self.netlist['Tg3']], isweak=False, parent=self),
            NMOS("t4523", [self.netlist['n1601'],self.netlist['n1347'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2959", [self.netlist['n1952'],self.port['gnd'].netconn,self.netlist['Tg4']], isweak=False, parent=self),
            NMOS("t1201", [self.netlist['n1744'],self.port['gnd'].netconn,self.netlist['sph3_1']], isweak=False, parent=self),
            NMOS("t1202", [self.port['gnd'].netconn,self.netlist['sph2'],self.netlist['n1741']], isweak=False, parent=self),
            NMOS("t1203", [self.port['gnd'].netconn,self.netlist['n1741'],self.netlist['sph2_1']], isweak=False, parent=self),
            NMOS("t2779", [self.netlist['n801'],self.port['gnd'].netconn,self.netlist['n574']], isweak=False, parent=self),
            NMOS("t1205", [self.netlist['sph2'],self.netlist['sph2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4521", [self.netlist['n1599'],self.netlist['n1345'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4698", [self.netlist['n1849'],self.netlist['n1442'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4699", [self.netlist['n1850'],self.netlist['n1443'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4128", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4129", [self.port['gnd'].netconn,self.netlist['n1605'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4694", [self.netlist['n1845'],self.netlist['n1438'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4695", [self.netlist['n1846'],self.netlist['n1439'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4696", [self.netlist['n1847'],self.netlist['n1440'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4697", [self.netlist['n1848'],self.netlist['n1441'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4690", [self.netlist['n1841'],self.netlist['n1434'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4691", [self.netlist['n1842'],self.netlist['n1435'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4692", [self.netlist['n1843'],self.netlist['n1436'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4527", [self.netlist['n1607'],self.netlist['n1351'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3776", [self.port['gnd'].netconn,self.netlist['n1794'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3801", [self.port['gnd'].netconn,self.netlist['n1812'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t4525", [self.netlist['n1604'],self.netlist['n1349'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t3802", [self.port['gnd'].netconn,self.netlist['n1625'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t4137", [self.port['gnd'].netconn,self.netlist['n1823'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t3803", [self.port['gnd'].netconn,self.netlist['n1538'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3772", [self.port['gnd'].netconn,self.netlist['n1793'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t3805", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t4232", [self.netlist['n1247'],self.port['gnd'].netconn,self.port['db5'].netconn], isweak=False, parent=self),
            NMOS("t1375", [self.netlist['idb6'],self.netlist['accb6'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t1376", [self.netlist['ixl6'],self.netlist['idb6'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1377", [self.netlist['idb1'],self.netlist['accb1'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t1370", [self.netlist['ixl0'],self.netlist['idb0'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1371", [self.netlist['idb2'],self.netlist['accb2'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t1372", [self.netlist['ixl2'],self.netlist['idb2'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1373", [self.netlist['idb4'],self.netlist['accb4'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t4239", [self.netlist['n1250'],self.port['gnd'].netconn,self.port['db0'].netconn], isweak=False, parent=self),
            NMOS("t1378", [self.netlist['ixl1'],self.netlist['idb1'],self.netlist['n322']], isweak=False, parent=self),
            NMOS("t1379", [self.netlist['idb3'],self.netlist['accb3'],self.netlist['n324']], isweak=False, parent=self),
            NMOS("t4348", [self.netlist['ir3'],self.netlist['ir3_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t4349", [self.netlist['ir4'],self.netlist['ir4_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t1799", [self.port['gnd'].netconn,self.netlist['n497'],self.netlist['ablx5']], isweak=False, parent=self),
            NMOS("t4342", [self.netlist['n1294'],self.netlist['ir2'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4343", [self.netlist['n1292'],self.netlist['ir3'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4341", [self.netlist['n1291'],self.netlist['ir1'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1792", [self.netlist['n492'],self.netlist['n500'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1793", [self.netlist['n493'],self.netlist['n501'],self.netlist['n477']], isweak=False, parent=self),
            NMOS("t1790", [self.port['gnd'].netconn,self.netlist['n416'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1791", [self.netlist['n418'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1558", [self.netlist['acca5'],self.netlist['acca5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1559", [self.netlist['acca6'],self.netlist['acca6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2841", [self.netlist['n831'],self.netlist['n834'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t1554", [self.netlist['acca7'],self.netlist['acca7_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1556", [self.port['gnd'].netconn,self.netlist['n1783'],self.netlist['acca7_1']], isweak=False, parent=self),
            NMOS("t1557", [self.port['gnd'].netconn,self.netlist['acca7'],self.netlist['n1783']], isweak=False, parent=self),
            NMOS("t1550", [self.netlist['acca5'],self.netlist['idb5'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t1551", [self.netlist['acca6'],self.netlist['idb6'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t1552", [self.netlist['acca7'],self.netlist['idb7'],self.netlist['n314']], isweak=False, parent=self),
            NMOS("t1969", [self.netlist['n2765'],self.netlist['n554'],self.netlist['adda5']], isweak=False, parent=self),
            NMOS("t3427", [self.netlist['n1067'],self.port['gnd'].netconn,self.netlist['n1362']], isweak=False, parent=self),
            NMOS("t1150", [self.netlist['sph4_1'],self.netlist['abh4'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1151", [self.netlist['sph6_1'],self.netlist['idb6'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1152", [self.netlist['sph6_1'],self.netlist['abh6'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1153", [self.netlist['sph1_1'],self.netlist['idb1'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1154", [self.netlist['sph1_1'],self.netlist['abh1'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1155", [self.netlist['sph3_1'],self.netlist['idb3'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1156", [self.netlist['sph3_1'],self.netlist['abh3'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1157", [self.netlist['sph5_1'],self.netlist['idb5'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1158", [self.netlist['sph5_1'],self.netlist['abh5'],self.netlist['n171']], isweak=False, parent=self),
            NMOS("t1159", [self.netlist['sph7_1'],self.netlist['idb7'],self.netlist['n180']], isweak=False, parent=self),
            NMOS("t1968", [self.netlist['n551'],self.port['gnd'].netconn,self.netlist['addb5']], isweak=False, parent=self),
            NMOS("t4105", [self.port['gnd'].netconn,self.netlist['n1233'],self.netlist['n1229']], isweak=False, parent=self),
            NMOS("t86", [self.netlist['n18'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t3425", [self.netlist['n2903'],self.netlist['n1051'],self.netlist['n1340']], isweak=False, parent=self),
            NMOS("t3988", [self.port['gnd'].netconn,self.netlist['n1840'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4287", [self.netlist['n1198'],self.port['gnd'].netconn,self.netlist['n1259']], isweak=False, parent=self),
            NMOS("t5029", [self.port['vcc'].netconn,self.netlist['n1840'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2561", [self.netlist['n722'],self.netlist['n723'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3981", [self.port['gnd'].netconn,self.netlist['n1821'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3980", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3983", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4148", [self.port['gnd'].netconn,self.netlist['n1827'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t3982", [self.port['gnd'].netconn,self.netlist['n1639'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4909", [self.netlist['n1479'],self.port['gnd'].netconn,self.netlist['n1478']], isweak=False, parent=self),
            NMOS("t4149", [self.port['gnd'].netconn,self.netlist['n1803'],self.netlist['n1200']], isweak=False, parent=self),
            NMOS("t4904", [self.netlist['n1470'],self.port['gnd'].netconn,self.netlist['n1486']], isweak=False, parent=self),
            NMOS("t3985", [self.port['gnd'].netconn,self.netlist['n1599'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t4907", [self.netlist['n1478'],self.port['gnd'].netconn,self.netlist['n1477']], isweak=False, parent=self),
            NMOS("t4900", [self.netlist['n2'],self.port['gnd'].netconn,self.netlist['n1468']], isweak=False, parent=self),
            NMOS("t693", [self.port['gnd'].netconn,self.netlist['n138'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3984", [self.port['gnd'].netconn,self.netlist['n1851'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t3987", [self.port['gnd'].netconn,self.netlist['n1845'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t5012", [self.port['vcc'].netconn,self.netlist['n1611'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3986", [self.port['gnd'].netconn,self.netlist['n1598'],self.netlist['i2']], isweak=False, parent=self),
            NMOS("t58", [self.port['ab3'].netconn,self.port['gnd'].netconn,self.netlist['n25']], isweak=False, parent=self),
            NMOS("t2054", [self.port['gnd'].netconn,self.netlist['n2770'],self.netlist['n475']], isweak=False, parent=self),
            NMOS("t4638", [self.netlist['n1814'],self.netlist['n1408'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2055", [self.port['gnd'].netconn,self.netlist['n2772'],self.netlist['n475']], isweak=False, parent=self),
            NMOS("t51", [self.port['ab2'].netconn,self.port['gnd'].netconn,self.netlist['n22']], isweak=False, parent=self),
            NMOS("t4639", [self.netlist['n1836'],self.netlist['n1402'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t54", [self.port['ab4'].netconn,self.port['gnd'].netconn,self.netlist['n23']], isweak=False, parent=self),
            NMOS("t705", [self.netlist['pch6'],self.netlist['abh6'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t57", [self.port['ab1'].netconn,self.port['gnd'].netconn,self.netlist['n24']], isweak=False, parent=self),
            NMOS("t4140", [self.port['gnd'].netconn,self.netlist['n1798'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t704", [self.netlist['pch7'],self.netlist['abh7'],self.netlist['n161']], isweak=False, parent=self),
            NMOS("t3239", [self.netlist['n1004'],self.netlist['n2870'],self.netlist['n1013']], isweak=False, parent=self),
            NMOS("t3238", [self.netlist['n2870'],self.port['gnd'].netconn,self.netlist['flagc']], isweak=False, parent=self),
            NMOS("t3237", [self.port['gnd'].netconn,self.netlist['n2869'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t2050", [self.port['gnd'].netconn,self.netlist['addb0'],self.netlist['n492']], isweak=False, parent=self),
            NMOS("t3234", [self.netlist['n1003'],self.netlist['n1002'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3233", [self.netlist['n1001'],self.netlist['n1000'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4634", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t3231", [self.netlist['n2868'],self.port['gnd'].netconn,self.netlist['n1027']], isweak=False, parent=self),
            NMOS("t2051", [self.netlist['n2764'],self.port['gnd'].netconn,self.netlist['n475']], isweak=False, parent=self),
            NMOS("t4635", [self.netlist['n1612'],self.netlist['n1418'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t701", [self.netlist['pch3'],self.netlist['idb3'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t4144", [self.port['gnd'].netconn,self.netlist['n1622'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t700", [self.netlist['pch1'],self.netlist['idb1'],self.netlist['n162']], isweak=False, parent=self),
            NMOS("t4145", [self.port['gnd'].netconn,self.netlist['n1608'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t4146", [self.port['gnd'].netconn,self.netlist['n1616'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t2356", [self.netlist['n672'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t4631", [self.port['gnd'].netconn,self.netlist['n1600'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t2355", [self.netlist['n671'],self.port['gnd'].netconn,self.netlist['n1574']], isweak=False, parent=self),
            NMOS("t3696", [self.port['gnd'].netconn,self.netlist['n1083'],self.netlist['n1195']], isweak=False, parent=self),
            NMOS("t3690", [self.netlist['n1182'],self.port['gnd'].netconn,self.netlist['n1086']], isweak=False, parent=self),
            NMOS("t3693", [self.port['gnd'].netconn,self.netlist['n1185'],self.netlist['n1181']], isweak=False, parent=self),
            NMOS("t3692", [self.port['gnd'].netconn,self.netlist['n1181'],self.netlist['n1182']], isweak=False, parent=self),
            NMOS("t1724", [self.netlist['n430'],self.netlist['n431'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3309", [self.netlist['n1024'],self.netlist['n1579'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t357", [self.port['gnd'].netconn,self.netlist['n10'],self.netlist['n1083']], isweak=False, parent=self),
            NMOS("t299", [self.port['gnd'].netconn,self.netlist['n70'],self.netlist['abl2']], isweak=False, parent=self),
            NMOS("t298", [self.netlist['n69'],self.port['gnd'].netconn,self.netlist['idb2']], isweak=False, parent=self),
            NMOS("t3303", [self.netlist['n2884'],self.netlist['n1022'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t3302", [self.netlist['n1022'],self.port['gnd'].netconn,self.netlist['n1414']], isweak=False, parent=self),
            NMOS("t3301", [self.netlist['n2884'],self.port['gnd'].netconn,self.netlist['n1436']], isweak=False, parent=self),
            NMOS("t3300", [self.port['gnd'].netconn,self.netlist['n2884'],self.netlist['n1343']], isweak=False, parent=self),
            NMOS("t291", [self.port['gnd'].netconn,self.netlist['n2688'],self.netlist['n1654']], isweak=False, parent=self),
            NMOS("t3306", [self.netlist['n1022'],self.port['gnd'].netconn,self.netlist['Tg5']], isweak=False, parent=self),
            NMOS("t3304", [self.netlist['n438'],self.netlist['n1956'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t2589", [self.port['gnd'].netconn,self.netlist['n732'],self.netlist['n959']], isweak=False, parent=self),
            NMOS("t4350", [self.netlist['ir5'],self.netlist['ir5_1'],self.netlist['decode_1']], isweak=False, parent=self),
            NMOS("t3509", [self.netlist['n2907'],self.port['gnd'].netconn,self.netlist['n1096']], isweak=False, parent=self),
            NMOS("t3493", [self.netlist['n1095'],self.port['gnd'].netconn,self.netlist['Ta1']], isweak=False, parent=self),
            NMOS("t3491", [self.netlist['n782'],self.port['gnd'].netconn,self.netlist['n1097']], isweak=False, parent=self),
            NMOS("t3949", [self.port['gnd'].netconn,self.netlist['n1615'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3496", [self.netlist['n782'],self.port['gnd'].netconn,self.netlist['n1095']], isweak=False, parent=self),
            NMOS("t3494", [self.netlist['n1096'],self.port['gnd'].netconn,self.netlist['n1095']], isweak=False, parent=self),
            NMOS("t3945", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3944", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3947", [self.port['gnd'].netconn,self.netlist['n1521'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3946", [self.port['gnd'].netconn,self.netlist['n1825'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3941", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3940", [self.port['gnd'].netconn,self.netlist['n1613'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3943", [self.port['gnd'].netconn,self.netlist['n1604'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t3942", [self.port['gnd'].netconn,self.netlist['n1791'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t2788", [self.netlist['n804'],self.port['gnd'].netconn,self.netlist['n813']], isweak=False, parent=self),
            NMOS("t2582", [self.netlist['n718'],self.netlist['n731'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4357", [self.netlist['n1294'],self.port['gnd'].netconn,self.netlist['n1256']], isweak=False, parent=self),
            NMOS("t2780", [self.netlist['n801'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t2782", [self.netlist['n802'],self.port['gnd'].netconn,self.netlist['n809']], isweak=False, parent=self),
            NMOS("t4356", [self.port['gnd'].netconn,self.netlist['n1291'],self.netlist['n1255']], isweak=False, parent=self),
            NMOS("t2785", [self.netlist['n803'],self.port['gnd'].netconn,self.netlist['n811']], isweak=False, parent=self),
            NMOS("t2786", [self.netlist['n803'],self.port['gnd'].netconn,self.netlist['n1646']], isweak=False, parent=self),
            NMOS("t3017", [self.netlist['n925'],self.netlist['n921'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3016", [self.netlist['n924'],self.netlist['n2839'],self.netlist['n1061']], isweak=False, parent=self),
            NMOS("t749", [self.netlist['pch0'],self.netlist['pch0_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t2581", [self.netlist['n727'],self.netlist['n730'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3545", [self.port['gnd'].netconn,self.netlist['n1111'],self.netlist['n1570']], isweak=False, parent=self),
            NMOS("t3012", [self.port['gnd'].netconn,self.netlist['n918'],self.netlist['n920']], isweak=False, parent=self),
            NMOS("t3547", [self.netlist['n2913'],self.netlist['n1566'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3010", [self.netlist['n2838'],self.netlist['n919'],self.netlist['Ta0']], isweak=False, parent=self),
            NMOS("t743", [self.netlist['pch2'],self.netlist['pch2_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3978", [self.port['gnd'].netconn,self.netlist['n1820'],self.netlist['n1266']], isweak=False, parent=self),
            NMOS("t2544", [self.netlist['n2796'],self.port['gnd'].netconn,self.netlist['n11']], isweak=False, parent=self),
            NMOS("t2013", [self.port['gnd'].netconn,self.netlist['n557'],self.netlist['addb2']], isweak=False, parent=self),
            NMOS("t2542", [self.netlist['n2796'],self.netlist['n2795'],self.netlist['n836']], isweak=False, parent=self),
            NMOS("t2543", [self.netlist['n2796'],self.port['gnd'].netconn,self.netlist['n717']], isweak=False, parent=self),
            NMOS("t2016", [self.netlist['n2772'],self.netlist['n2771'],self.netlist['addb2']], isweak=False, parent=self),
            NMOS("t744", [self.netlist['pch1'],self.netlist['pch1_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t3831", [self.netlist['n1212'],self.port['gnd'].netconn,self.netlist['n1183']], isweak=False, parent=self),
            NMOS("t3786", [self.port['gnd'].netconn,self.netlist['n1618'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3785", [self.port['gnd'].netconn,self.netlist['n1804'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3784", [self.port['gnd'].netconn,self.netlist['n1524'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3783", [self.port['gnd'].netconn,self.netlist['n1828'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3782", [self.port['gnd'].netconn,self.netlist['n1795'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3781", [self.port['gnd'].netconn,self.netlist['n1825'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3780", [self.port['gnd'].netconn,self.netlist['n1519'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3839", [self.netlist['n1214'],self.netlist['n1217'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3502", [self.netlist['flagv'],self.netlist['n1104'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t5042", [self.port['vcc'].netconn,self.netlist['n1600'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3789", [self.port['gnd'].netconn,self.netlist['n1842'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t3788", [self.port['gnd'].netconn,self.netlist['n1623'],self.netlist['n1197']], isweak=False, parent=self),
            NMOS("t1544", [self.port['gnd'].netconn,self.netlist['accb0'],self.netlist['n1704']], isweak=False, parent=self),
            NMOS("t3485", [self.netlist['n1093'],self.port['gnd'].netconn,self.netlist['n1443']], isweak=False, parent=self),
            NMOS("t1948", [self.netlist['n2748'],self.netlist['sumab6'],self.netlist['addb6']], isweak=False, parent=self),
            NMOS("t1947", [self.port['gnd'].netconn,self.netlist['sumab6'],self.netlist['n542']], isweak=False, parent=self),
            NMOS("t1945", [self.port['gnd'].netconn,self.netlist['addb7'],self.netlist['n523']], isweak=False, parent=self),
            NMOS("t605", [self.netlist['pcl6'],self.netlist['pcl6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t602", [self.netlist['pcl5'],self.netlist['pcl5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1941", [self.port['gnd'].netconn,self.netlist['n2762'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t1940", [self.netlist['n540'],self.port['gnd'].netconn,self.netlist['addb7']], isweak=False, parent=self),
            NMOS("t2304", [self.netlist['n411'],self.port['gnd'].netconn,self.netlist['n1785']], isweak=False, parent=self),
            NMOS("t2305", [self.netlist['n411'],self.port['gnd'].netconn,self.netlist['n658']], isweak=False, parent=self),
            NMOS("t594", [self.netlist['pcl3'],self.port['gnd'].netconn,self.netlist['n1776']], isweak=False, parent=self),
            NMOS("t2302", [self.netlist['n654'],self.port['vcc'].netconn,self.netlist['n651']], isweak=False, parent=self),
            NMOS("t2303", [self.port['gnd'].netconn,self.netlist['n532'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2308", [self.port['gnd'].netconn,self.netlist['n658'],self.netlist['n579']], isweak=False, parent=self),
            NMOS("t2309", [self.netlist['n659'],self.port['gnd'].netconn,self.netlist['n579']], isweak=False, parent=self),
            NMOS("t3163", [self.netlist['n4'],self.port['gnd'].netconn,self.netlist['n1149']], isweak=False, parent=self),
            NMOS("t3161", [self.netlist['n4'],self.netlist['n2860'],self.netlist['Tx2']], isweak=False, parent=self),
            NMOS("t3160", [self.netlist['n2860'],self.port['gnd'].netconn,self.netlist['n976']], isweak=False, parent=self),
            NMOS("t3167", [self.netlist['n2861'],self.port['gnd'].netconn,self.netlist['n978']], isweak=False, parent=self),
            NMOS("t3166", [self.netlist['n973'],self.netlist['n866'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3165", [self.netlist['n971'],self.port['gnd'].netconn,self.netlist['n1412']], isweak=False, parent=self),
            NMOS("t3164", [self.port['gnd'].netconn,self.netlist['n971'],self.netlist['n1408']], isweak=False, parent=self),
            NMOS("t687", [self.port['gnd'].netconn,self.netlist['n184'],self.netlist['n78']], isweak=False, parent=self),
            NMOS("t3500", [self.netlist['n1567'],self.netlist['idb1'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t2160", [self.netlist['n607'],self.netlist['n611'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2161", [self.netlist['n612'],self.port['gnd'].netconn,self.netlist['dbi0']], isweak=False, parent=self),
            NMOS("t518", [self.port['gnd'].netconn,self.netlist['n1647'],self.netlist['n133']], isweak=False, parent=self),
            NMOS("t2163", [self.netlist['n611'],self.port['vcc'].netconn,self.netlist['n612']], isweak=False, parent=self),
            NMOS("t2164", [self.netlist['n612'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3699", [self.port['gnd'].netconn,self.netlist['n2936'],self.netlist['n1192']], isweak=False, parent=self),
            NMOS("t2166", [self.netlist['dbi0'],self.port['gnd'].netconn,self.netlist['n611']], isweak=False, parent=self),
            NMOS("t2167", [self.netlist['dbi0'],self.netlist['idb0'],self.netlist['n531']], isweak=False, parent=self),
            NMOS("t2168", [self.netlist['idb0'],self.netlist['dbo0'],self.netlist['n983']], isweak=False, parent=self),
            NMOS("t2169", [self.netlist['n2777'],self.netlist['n616'],self.netlist['phi2_1']], isweak=False, parent=self),
            NMOS("t510", [self.netlist['n132'],self.netlist['n131'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t511", [self.netlist['n139'],self.port['gnd'].netconn,self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1387", [self.netlist['acca2_1'],self.netlist['idb2'],self.netlist['n315']], isweak=False, parent=self),
            NMOS("t3770", [self.port['gnd'].netconn,self.netlist['n1822'],self.netlist['i0']], isweak=False, parent=self),
            NMOS("t1899", [self.port['gnd'].netconn,self.netlist['sumab3'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t1898", [self.port['gnd'].netconn,self.netlist['sumab4'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t2764", [self.netlist['n454'],self.port['gnd'].netconn,self.netlist['Tr5']], isweak=False, parent=self),
            NMOS("t2941", [self.netlist['n874'],self.port['gnd'].netconn,self.netlist['n877']], isweak=False, parent=self),
            NMOS("t2946", [self.netlist['n880'],self.port['gnd'].netconn,self.netlist['n885']], isweak=False, parent=self),
            NMOS("t2947", [self.port['gnd'].netconn,self.netlist['n881'],self.netlist['n884']], isweak=False, parent=self),
            NMOS("t2760", [self.netlist['n795'],self.port['gnd'].netconn,self.netlist['n1019']], isweak=False, parent=self),
            NMOS("t2761", [self.netlist['n795'],self.port['gnd'].netconn,self.netlist['n1441']], isweak=False, parent=self),
            NMOS("t1891", [self.netlist['n536'],self.netlist['n537'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1890", [self.netlist['n535'],self.netlist['n534'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t1893", [self.netlist['n572'],self.port['gnd'].netconn,self.netlist['abh7']], isweak=False, parent=self),
            NMOS("t1892", [self.netlist['n572'],self.netlist['n574'],self.netlist['n1647']], isweak=False, parent=self),
            NMOS("t1895", [self.port['gnd'].netconn,self.netlist['sumab7'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t1897", [self.port['gnd'].netconn,self.netlist['sumab5'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t1896", [self.netlist['sumab6'],self.port['gnd'].netconn,self.netlist['n578']], isweak=False, parent=self),
            NMOS("t4119", [self.port['gnd'].netconn,self.netlist['n1852'],self.netlist['i4']], isweak=False, parent=self),
            NMOS("t3698", [self.port['gnd'].netconn,self.netlist['n2936'],self.netlist['n1184']], isweak=False, parent=self),
            NMOS("t2040", [self.port['gnd'].netconn,self.netlist['n2760'],self.netlist['adda0']], isweak=False, parent=self),
            NMOS("t1415", [self.netlist['n1725'],self.port['gnd'].netconn,self.netlist['ixh5_1']], isweak=False, parent=self),
            NMOS("t4112", [self.netlist['n1234'],self.port['gnd'].netconn,self.netlist['n1232']], isweak=False, parent=self),
            NMOS("t1417", [self.netlist['ixh3'],self.netlist['ixh3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4110", [self.netlist['n1231'],self.port['gnd'].netconn,self.netlist['n2']], isweak=False, parent=self),
            NMOS("t1411", [self.netlist['ixh5'],self.netlist['ixh5_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4116", [self.port['gnd'].netconn,self.netlist['n1235'],self.netlist['Tg7']], isweak=False, parent=self),
            NMOS("t1413", [self.port['gnd'].netconn,self.netlist['n1729'],self.netlist['ixh6_1']], isweak=False, parent=self),
            NMOS("t4114", [self.port['gnd'].netconn,self.netlist['n1234'],self.netlist['n1086']], isweak=False, parent=self),
            NMOS("t5047", [self.port['vcc'].netconn,self.netlist['n1821'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1091", [self.netlist['spl0'],self.netlist['abl0'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t1090", [self.netlist['spl1'],self.netlist['abl1'],self.netlist['n178']], isweak=False, parent=self),
            NMOS("t1093", [self.port['gnd'].netconn,self.netlist['n1755'],self.netlist['spl7_1']], isweak=False, parent=self),
            NMOS("t1092", [self.port['gnd'].netconn,self.netlist['spl7'],self.netlist['n1755']], isweak=False, parent=self),
            NMOS("t1095", [self.netlist['n1752'],self.port['gnd'].netconn,self.netlist['spl6_1']], isweak=False, parent=self),
            NMOS("t1094", [self.netlist['spl6'],self.port['gnd'].netconn,self.netlist['n1752']], isweak=False, parent=self),
            NMOS("t4599", [self.port['gnd'].netconn,self.netlist['n1510'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4598", [self.port['gnd'].netconn,self.netlist['n1800'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4597", [self.port['gnd'].netconn,self.netlist['n1520'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t1098", [self.netlist['spl6'],self.netlist['spl6_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t4595", [self.port['gnd'].netconn,self.netlist['n1509'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4594", [self.port['gnd'].netconn,self.netlist['n1832'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4593", [self.port['gnd'].netconn,self.netlist['n1799'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4592", [self.port['gnd'].netconn,self.netlist['n1519'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4591", [self.port['gnd'].netconn,self.netlist['n1603'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4590", [self.port['gnd'].netconn,self.netlist['n1831'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t4037", [self.port['gnd'].netconn,self.netlist['n1538'],self.netlist['i3']], isweak=False, parent=self),
            NMOS("t1305", [self.netlist['ixh0_1'],self.netlist['idb0'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t990", [self.netlist['n276'],self.port['gnd'].netconn,self.netlist['abh2']], isweak=False, parent=self),
            NMOS("t1306", [self.netlist['abh0'],self.netlist['ixh0_1'],self.netlist['n329']], isweak=False, parent=self),
            NMOS("t1309", [self.netlist['ixh2_1'],self.netlist['idb2'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t1308", [self.netlist['ixh1_1'],self.netlist['idb1'],self.netlist['n285']], isweak=False, parent=self),
            NMOS("t4205", [self.port['gnd'].netconn,self.netlist['n1619'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4204", [self.port['gnd'].netconn,self.netlist['n1537'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4203", [self.port['gnd'].netconn,self.netlist['n1611'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4202", [self.port['gnd'].netconn,self.netlist['n1830'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4201", [self.port['gnd'].netconn,self.netlist['n1620'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4200", [self.port['gnd'].netconn,self.netlist['n1839'],self.netlist['i5']], isweak=False, parent=self),
            NMOS("t4575", [self.netlist['n1822'],self.netlist['n1398'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t2046", [self.netlist['n2776'],self.netlist['n2775'],self.netlist['addb0']], isweak=False, parent=self),
            NMOS("t4577", [self.netlist['n1825'],self.netlist['n1400'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4576", [self.netlist['n1824'],self.netlist['n1399'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4571", [self.netlist['n1817'],self.netlist['n1394'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4570", [self.netlist['n1816'],self.netlist['n1393'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4573", [self.netlist['n1819'],self.netlist['n1396'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t4572", [self.netlist['n1818'],self.netlist['n1395'],self.netlist['decode']], isweak=False, parent=self),
            NMOS("t497", [self.netlist['n106'],self.port['gnd'].netconn,self.netlist['n1665']], isweak=False, parent=self),
            NMOS("t4579", [self.port['gnd'].netconn,self.netlist['n1826'],self.netlist['i7']], isweak=False, parent=self),
            NMOS("t648", [self.netlist['n172'],self.port['gnd'].netconn,self.netlist['n453']], isweak=False, parent=self),
            NMOS("t1529", [self.netlist['accb3'],self.port['gnd'].netconn,self.netlist['n1713']], isweak=False, parent=self),
            NMOS("t1528", [self.port['gnd'].netconn,self.netlist['n1713'],self.netlist['accb3_1']], isweak=False, parent=self),
            NMOS("t1908", [self.netlist['n2754'],self.netlist['n2753'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t1521", [self.netlist['accb4'],self.netlist['accb4_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1520", [self.netlist['accb3'],self.netlist['accb3_1'],self.port['vcc'].netconn], isweak=True, parent=self),
            NMOS("t1527", [self.port['gnd'].netconn,self.netlist['accb4'],self.netlist['n1720']], isweak=False, parent=self),
            NMOS("t1526", [self.port['gnd'].netconn,self.netlist['n1720'],self.netlist['accb4_1']], isweak=False, parent=self),
            NMOS("t2639", [self.netlist['n424'],self.port['gnd'].netconn,self.netlist['n748']], isweak=False, parent=self),
            NMOS("t1901", [self.port['gnd'].netconn,self.netlist['sumab1'],self.netlist['n578']], isweak=False, parent=self),
            NMOS("t3099", [self.port['gnd'].netconn,self.netlist['n2854'],self.netlist['n1325']], isweak=False, parent=self),
            NMOS("t646", [self.netlist['n169'],self.netlist['n170'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3098", [self.netlist['n954'],self.port['gnd'].netconn,self.netlist['n1376']], isweak=False, parent=self),
            NMOS("t1906", [self.netlist['n2750'],self.netlist['n2749'],self.netlist['n472']], isweak=False, parent=self),
            NMOS("t1635", [self.netlist['ablx4'],self.netlist['acca4'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1634", [self.netlist['ablx5'],self.netlist['acca5'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1637", [self.netlist['ablx2'],self.netlist['acca2'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1636", [self.netlist['ablx3'],self.netlist['acca3'],self.netlist['n325']], isweak=False, parent=self),
            NMOS("t1631", [self.port['gnd'].netconn,self.netlist['ablx4'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1630", [self.port['gnd'].netconn,self.netlist['ablx5'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1633", [self.port['gnd'].netconn,self.netlist['ablx2'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1632", [self.port['gnd'].netconn,self.netlist['ablx3'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1639", [self.port['gnd'].netconn,self.netlist['ablx0'],self.netlist['n316']], isweak=False, parent=self),
            NMOS("t1638", [self.netlist['idb1'],self.port['gnd'].netconn,self.netlist['n321']], isweak=False, parent=self),
            NMOS("t3606", [self.port['gnd'].netconn,self.netlist['n1148'],self.netlist['n1075']], isweak=False, parent=self),
            NMOS("t3437", [self.netlist['n1068'],self.port['gnd'].netconn,self.netlist['n1392']], isweak=False, parent=self),
            NMOS("t4376", [self.netlist['ir0_1'],self.port['gnd'].netconn,self.netlist['n1302']], isweak=False, parent=self),
            NMOS("t4375", [self.port['rw'].netconn,self.port['vcc'].netconn,self.netlist['n1306']], isweak=False, parent=self),
            NMOS("t4370", [self.netlist['n1307'],self.port['gnd'].netconn,self.netlist['ob']], isweak=False, parent=self),
            NMOS("t4378", [self.port['gnd'].netconn,self.netlist['n1302'],self.netlist['ir0']], isweak=False, parent=self),
            NMOS("t2731", [self.netlist['flagh'],self.netlist['n784'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t2733", [self.netlist['n787'],self.netlist['n781'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t4979", [self.port['vcc'].netconn,self.netlist['n1795'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4978", [self.port['vcc'].netconn,self.netlist['n1515'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t5025", [self.port['vcc'].netconn,self.netlist['n1849'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t1717", [self.netlist['n757'],self.netlist['n419'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4971", [self.port['vcc'].netconn,self.netlist['n1792'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t2735", [self.port['gnd'].netconn,self.netlist['n789'],self.netlist['n1392']], isweak=False, parent=self),
            NMOS("t4973", [self.port['vcc'].netconn,self.netlist['n1825'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4972", [self.port['vcc'].netconn,self.netlist['n1605'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4975", [self.port['vcc'].netconn,self.netlist['n1801'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4974", [self.port['vcc'].netconn,self.netlist['n1521'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4977", [self.port['vcc'].netconn,self.netlist['n1834'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t4976", [self.port['vcc'].netconn,self.netlist['n1615'],self.netlist['sync']], isweak=False, parent=self),
            NMOS("t3255", [self.port['gnd'].netconn,self.netlist['n2874'],self.netlist['n1446']], isweak=False, parent=self),
            NMOS("t2225", [self.netlist['n629'],self.netlist['n2790'],self.netlist['sumab2']], isweak=False, parent=self),
            NMOS("t3706", [self.netlist['n1188'],self.netlist['n1187'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3609", [self.netlist['n2923'],self.netlist['n2922'],self.netlist['n842']], isweak=False, parent=self),
            NMOS("t3704", [self.netlist['n1185'],self.port['gnd'].netconn,self.netlist['n1186']], isweak=False, parent=self),
            NMOS("t198", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n47']], isweak=False, parent=self),
            NMOS("t196", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n46']], isweak=False, parent=self),
            NMOS("t3251", [self.netlist['n2873'],self.port['gnd'].netconn,self.netlist['n1004']], isweak=False, parent=self),
            NMOS("t194", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n45']], isweak=False, parent=self),
            NMOS("t61", [self.port['gnd'].netconn,self.port['ab5'].netconn,self.netlist['n26']], isweak=False, parent=self),
            NMOS("t190", [self.netlist['n42'],self.port['gnd'].netconn,self.netlist['n43']], isweak=False, parent=self),
            NMOS("t3228", [self.port['gnd'].netconn,self.netlist['n2867'],self.netlist['n994']], isweak=False, parent=self),
            NMOS("t3229", [self.netlist['n996'],self.netlist['n2868'],self.netlist['sum7']], isweak=False, parent=self),
            NMOS("t358", [self.port['gnd'].netconn,self.netlist['n768'],self.netlist['n770']], isweak=False, parent=self),
            NMOS("t3253", [self.netlist['n2874'],self.netlist['n1013'],self.netlist['n1370']], isweak=False, parent=self),
            NMOS("t354", [self.port['gnd'].netconn,self.netlist['n1646'],self.netlist['enrwa']], isweak=False, parent=self),
            NMOS("t3221", [self.port['gnd'].netconn,self.netlist['flagn'],self.netlist['n997']], isweak=False, parent=self),
            NMOS("t3222", [self.netlist['n997'],self.netlist['n996'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3223", [self.netlist['n2866'],self.port['gnd'].netconn,self.netlist['n993']], isweak=False, parent=self),
            NMOS("t3224", [self.port['gnd'].netconn,self.netlist['n992'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3225", [self.netlist['n996'],self.netlist['n2866'],self.netlist['n1107']], isweak=False, parent=self),
            NMOS("t3226", [self.netlist['n996'],self.netlist['n2867'],self.netlist['n992']], isweak=False, parent=self),
            NMOS("t353", [self.netlist['n1646'],self.port['vcc'].netconn,self.netlist['n5']], isweak=False, parent=self),
            NMOS("t4240", [self.port['gnd'].netconn,self.netlist['n1251'],self.port['db1'].netconn], isweak=False, parent=self),
            NMOS("t4247", [self.netlist['n1253'],self.netlist['n1257'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t4246", [self.netlist['n1252'],self.netlist['n1256'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3314", [self.netlist['n2885'],self.port['gnd'].netconn,self.netlist['n1056']], isweak=False, parent=self),
            NMOS("t3316", [self.netlist['n2885'],self.netlist['n1039'],self.netlist['n984']], isweak=False, parent=self),
            NMOS("t3317", [self.netlist['n1039'],self.port['gnd'].netconn,self.netlist['n1015']], isweak=False, parent=self),
            NMOS("t3310", [self.netlist['n1025'],self.netlist['flagz'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3311", [self.netlist['n1027'],self.netlist['n1096'],self.port['phi2'].netconn], isweak=False, parent=self),
            NMOS("t3312", [self.netlist['n1028'],self.netlist['n749'],self.port['phi1'].netconn], isweak=False, parent=self),
            NMOS("t3313", [self.netlist['n2885'],self.port['gnd'].netconn,self.netlist['n1041']], isweak=False, parent=self),
            NMOS("t3318", [self.netlist['n1039'],self.port['gnd'].netconn,self.netlist['n1042']], isweak=False, parent=self),
        ])
