import gate
import net
from count4 import count4
#from count4_lcc import count4



class count16( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict([("COUT", gate.OUT),
                         ("CIN", gate.IN),
                         ("RSTB", gate.IN),
                         ("PHI", gate.IN) ])
        for i in range (0, 16) :
            portlist["Q%d"% i] = gate.OUT
 
        gate.module.__init__( self, name, portlist, mapping, parent)
        
        self.netlist['c0'] = net.net('c0', parent=self)
        self.netlist['c1'] = net.net('c1', parent=self)
        self.netlist['c2'] = net.net('c2', parent=self)

        self.gatelist = [ 
            count4("count4_0_u", dict( [('Q0', self.port['Q0'].netconn), 
                                        ('Q1', self.port['Q1'].netconn), 
                                        ('Q2', self.port['Q2'].netconn), 
                                        ('Q3', self.port['Q3'].netconn), 
                                        ('PHI', self.port['PHI'].netconn), 
                                        ('RSTB', self.port['RSTB'].netconn), 
                                        ('CIN', self.port['CIN'].netconn), 
                                        ('COUT', self.netlist['c0'])]), self ),
            count4("count4_1_u", dict( [('Q0', self.port['Q4'].netconn), 
                                        ('Q1', self.port['Q5'].netconn), 
                                        ('Q2', self.port['Q6'].netconn), 
                                        ('Q3', self.port['Q7'].netconn), 
                                        ('PHI', self.port['PHI'].netconn), 
                                        ('RSTB', self.port['RSTB'].netconn), 
                                        ('CIN', self.netlist['c0']), 
                                        ('COUT', self.netlist['c1'])]), self),
            count4("count4_2_u", dict( [('Q0', self.port['Q8'].netconn), 
                                        ('Q1', self.port['Q9'].netconn), 
                                        ('Q2', self.port['Q10'].netconn), 
                                        ('Q3', self.port['Q11'].netconn), 
                                        ('PHI', self.port['PHI'].netconn), 
                                        ('RSTB', self.port['RSTB'].netconn), 
                                        ('CIN', self.netlist['c1']), 
                                        ('COUT', self.netlist['c2'])]), self),
            count4("count4_3_u", dict( [('Q0', self.port['Q12'].netconn), 
                                        ('Q1', self.port['Q13'].netconn), 
                                        ('Q2', self.port['Q14'].netconn), 
                                        ('Q3', self.port['Q15'].netconn), 
                                        ('PHI', self.port['PHI'].netconn), 
                                        ('RSTB', self.port['RSTB'].netconn), 
                                        ('CIN', self.netlist['c2']), 
                                        ('COUT', self.port['COUT'].netconn)]), self)
            ]
        
