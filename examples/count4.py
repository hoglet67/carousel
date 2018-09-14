import gate
import net
from primitive import DFF, INV, AND, OR, NAND



class count4( gate.module ) :
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
            DFF("dff0_u", [self.port['Q0'].netconn, self.netlist['d0'], self.port['RSTB'].netconn, self.port['PHI'].netconn], self),
            DFF("dff1_u", [self.port['Q1'].netconn, self.netlist['d1'], self.port['RSTB'].netconn, self.port['PHI'].netconn], self),
            DFF("dff2_u", [self.port['Q2'].netconn, self.netlist['d2'], self.port['RSTB'].netconn, self.port['PHI'].netconn], self),
            DFF("dff3_u", [self.port['Q3'].netconn, self.netlist['d3'], self.port['RSTB'].netconn, self.port['PHI'].netconn], self),
            
            INV("inv4_u", [self.netlist['q0b'], self.port['Q0'].netconn], self),
            INV("inv5_u", [self.netlist['q1b'], self.port['Q1'].netconn], self),
            INV("inv6_u", [self.netlist['q2b'], self.port['Q2'].netconn], self),
            INV("inv7_u", [self.netlist['q3b'], self.port['Q3'].netconn], self),
            
            AND("and8_u", [self.netlist['n12'], self.port['CIN'].netconn, self.netlist['q0b']], self),
            INV("inv9_u", [self.netlist['n14'], self.port['CIN'].netconn], self),
            AND("and10_u", [self.netlist['n13'], self.port['Q0'].netconn, self.netlist['n14']], self),
            OR("or11_u", [self.netlist['d0'], self.netlist['n12'], self.netlist['n13']], self),
            
            AND("and12_u", [self.netlist['n0'], self.port['Q0'].netconn, self.port['CIN'].netconn], self),
            INV("inv13_u", [self.netlist['n1'], self.netlist['n0']], self),
            AND("and14_u", [self.netlist['n2'], self.netlist['q1b'], self.netlist['n0']], self),
            AND("and15_u", [self.netlist['n3'], self.port['Q1'].netconn, self.netlist['n1']], self),
            OR("or16_u", [self.netlist['d1'], self.netlist['n3'], self.netlist['n2']], self),
            
            AND("and17_u", [self.netlist['n4'], self.port['Q1'].netconn, self.port['Q0'].netconn, 
                            self.port['CIN'].netconn], self),
            INV("inv18_u", [self.netlist['n5'], self.netlist['n4']], self),
            AND("and19_u", [self.netlist['n6'], self.netlist['q2b'], self.netlist['n4']], self),
            AND("and20_u", [self.netlist['n7'], self.port['Q2'].netconn, self.netlist['n5']], self),
            OR("or21_u", [self.netlist['d2'], self.netlist['n6'], self.netlist['n7']], self),
        
            AND("and22_u", [self.netlist['n8'], self.port['Q2'].netconn, self.port['Q1'].netconn, 
                            self.port['Q0'].netconn, self.port['CIN'].netconn], self),
            INV("inv23_u", [self.netlist['n9'], self.netlist['n8']], self),
            AND("and24_u", [self.netlist['n10'], self.netlist['q3b'], self.netlist['n8']], self),
            AND("and25_u", [self.netlist['n11'], self.port['Q3'].netconn, self.netlist['n9']], self),
            OR("or26_u", [self.netlist['d3'], self.netlist['n11'], self.netlist['n10']], self),
        
            AND("and27_u", [self.port['COUT'].netconn, self.port['CIN'].netconn,self.port['Q0'].netconn,self.port['Q1'].netconn,self.port['Q2'].netconn,self.port['Q3'].netconn], self) ])
