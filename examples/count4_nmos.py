import gate
import net
from nmos_lib import NMOS_INV, NMOS_AND2, NMOS_AND3, NMOS_AND4, NMOS_AND5, NMOS_OR2, NMOS_DFF



class count4_nmos( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("Q0", gate.OUT),
                          ("Q1", gate.OUT),
                          ("Q2", gate.OUT),
                          ("Q3", gate.OUT),
                          ("COUT", gate.OUT),
                          ("CIN", gate.IN),
                          ("RSTB", gate.IN),
                          ("PHI", gate.IN) ])
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)
        
        for n in [ 'd0', 'd1', 'd2', 'd3', 'q0b', 'q1b', 'q2b', 'q3b' ] : 
            self.netlist[n] = net.net(n, parent=self)

        for i in range(0, 15):
            n = "n%d" % i
            self.netlist[n] = net.net(n, parent=self)   
         
        self.gatelist.extend([
            NMOS_DFF("dff0_u", dict([('Q',self.port['Q0'].netconn), ('D',self.netlist['d0']),
                                     ('RSTB',self.port['RSTB'].netconn),('PHI', self.port['PHI'].netconn)]), self),
            NMOS_DFF("dff1_u", dict([('Q',self.port['Q1'].netconn), ('D',self.netlist['d1']),
                                     ('RSTB',self.port['RSTB'].netconn),('PHI', self.port['PHI'].netconn)]), self),
            NMOS_DFF("dff2_u", dict([('Q',self.port['Q2'].netconn), ('D',self.netlist['d2']),
                                     ('RSTB',self.port['RSTB'].netconn),('PHI', self.port['PHI'].netconn)]), self),
            NMOS_DFF("dff3_u", dict([('Q',self.port['Q3'].netconn), ('D',self.netlist['d3']),
                                     ('RSTB',self.port['RSTB'].netconn),('PHI', self.port['PHI'].netconn)]), self),

            NMOS_INV("inv4_u", dict([('OUT', self.netlist['q0b']), ('IN', self.port['Q0'].netconn)]), self),
            NMOS_INV("inv5_u", dict([('OUT', self.netlist['q1b']), ('IN', self.port['Q1'].netconn)]), self),
            NMOS_INV("inv6_u", dict([('OUT', self.netlist['q2b']), ('IN', self.port['Q2'].netconn)]), self),
            NMOS_INV("inv7_u", dict([('OUT', self.netlist['q3b']), ('IN', self.port['Q3'].netconn)]), self),
            
            NMOS_AND2("and8_u",  dict([('OUT', self.netlist['n12']), ('I0',self.port['CIN'].netconn), 
                                       ('I1', self.netlist['q0b'])]), self),
            NMOS_INV("inv9_u", dict([('OUT', self.netlist['n14']), ('IN', self.port['CIN'].netconn)]), self),
            NMOS_AND2("and10_u",  dict([('OUT', self.netlist['n13']), ('I0',self.port['Q0'].netconn), 
                                        ('I1', self.netlist['n14'])]), self),
            NMOS_OR2("or11_u", dict([('OUT',self.netlist['d0']), ('I0',self.netlist['n12']), 
                                     ('I1',self.netlist['n13'])]), self),
            
            NMOS_AND2("and12_u",  dict([('OUT', self.netlist['n0']), ('I0',self.port['Q0'].netconn), 
                                        ('I1',self.port['CIN'].netconn)]), self),
            NMOS_INV("inv13_u", dict([('OUT',self.netlist['n1']), ('IN', self.netlist['n0'])]), self),

            NMOS_AND2("and14_u",  dict([('OUT', self.netlist['n2']), ('I0',self.netlist['q1b']), 
                                        ('I1',self.netlist['n0'])]), self),
            NMOS_AND2("and15_u",  dict([('OUT', self.netlist['n3']), ('I0',self.port['Q1'].netconn), 
                                        ('I1',self.netlist['n1'])]), self),
            NMOS_OR2("or16_u", dict([('OUT',self.netlist['d1']), ('I0',self.netlist['n3']), 
                                     ('I1',self.netlist['n2'])]), self),
            
            NMOS_AND3("and17_u", dict([('OUT',self.netlist['n4']), ('I0',self.port['Q1'].netconn), 
                                       ('I1',self.port['Q0'].netconn),('I2',self.port['CIN'].netconn)]), self),
            NMOS_INV("inv18_u", dict([('OUT',self.netlist['n5']), ('IN',self.netlist['n4'])]), self),

            NMOS_AND2("and19_u",  dict([('OUT', self.netlist['n6']), ('I0',self.netlist['q2b']), ('I1',self.netlist['n4'])]), self),
            NMOS_AND2("and20_u",  dict([('OUT', self.netlist['n7']), ('I0',self.port['Q2'].netconn), ('I1',self.netlist['n5'])]), self),

            NMOS_OR2("or21_u", dict([('OUT',self.netlist['d2']), ('I0',self.netlist['n6']),('I1', self.netlist['n7'])]), self),
        
            NMOS_AND4("and22_u", dict([('OUT',self.netlist['n8']), ('I0',self.port['Q2'].netconn), 
                                       ('I1',self.port['Q1'].netconn),('I2',self.port['Q0'].netconn), 
                                       ('I3',self.port['CIN'].netconn)]), self),
            NMOS_INV("inv23_u", dict([('OUT',self.netlist['n9']), ('IN', self.netlist['n8'])]), self),
            NMOS_AND2("and24_u",  dict([('OUT', self.netlist['n10']), ('I0',self.netlist['q3b']), ('I1',self.netlist['n8'])]), self),
            NMOS_AND2("and25_u",  dict([('OUT', self.netlist['n11']), ('I0',self.port['Q3'].netconn), ('I1',self.netlist['n9'])]), self),
            NMOS_OR2("or26_u", dict([('OUT',self.netlist['d3']), ('I0',self.netlist['n11']), ('I1',self.netlist['n10'])]), self),
        
            NMOS_AND5("and27_u", dict([('OUT',self.port['COUT'].netconn),('I0', self.port['CIN'].netconn),
                                       ('I1',self.port['Q0'].netconn),('I2',self.port['Q1'].netconn),
                                       ('I3',self.port['Q2'].netconn),('I4',self.port['Q3'].netconn)]), self)
            
            ])
