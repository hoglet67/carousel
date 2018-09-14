import gate
import net
from primitive import DFF, INV, AND, OR, NAND
from nmos_lib import NMOS_INV, NMOS_AND2, NMOS_AND3, NMOS_AND4, NMOS_AND5, NMOS_OR2, NMOS_DFF



class count2_nmos( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("Q0", gate.OUT),
                          ("Q1", gate.OUT),
                          ("RSTB", gate.IN),
                          ("PHI", gate.IN) ])
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)
        
        for n in [ 'd0', 'd1','q0b', 'q1b' , 'd1a', 'd1b'] : 
            self.netlist[n] = net.net(n, parent=self)

        for i in range(0, 2):
            n = "n%d" % i
            self.netlist[n] = net.net(n, parent=self)   
         
        self.gatelist.extend([
                NMOS_DFF("dff0_u", dict([('Q',self.port['Q0'].netconn), ('D',self.netlist['d0']),
                                         ('RSTB',self.port['RSTB'].netconn),('PHI', self.port['PHI'].netconn)]), self),
                NMOS_INV("inv6_u", dict([('OUT', self.netlist['d0']), ('IN', self.port['Q0'].netconn)]), self),
                
                DFF("dff1_u", [self.port['Q1'].netconn, self.netlist['d1'], self.port['RSTB'].netconn, self.port['PHI'].netconn], self),
                INV("inv4_u", [self.netlist['q0b'], self.port['Q0'].netconn], self),
                INV("inv5_u", [self.netlist['q1b'], self.port['Q1'].netconn], self),
                AND("and7_u", [self.netlist['d1a'], self.port['Q0'].netconn, self.netlist['q1b']], self),
                AND("and8_u", [self.netlist['d1b'], self.port['Q1'].netconn, self.netlist['q0b']], self),
                OR("or9_u", [self.netlist['d1'],self.netlist['d1a'],self.netlist['d1b'] ], self)
                ])
