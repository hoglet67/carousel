import gate
import net
from primitive import PMOS, NMOS, PULLUP, UPMOS, NMOS


'''
Simple Library of NMOS gates for benchmarking.

All transistors are bi-dir types.
'''



class NMOS_INV( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('IN', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)        

        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['IN'].netconn], self),
                ])

class NMOS_BUF( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('IN', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)        

        # Add depln mode pullups
        self.netlist['n0'] = net.net('n0', pullup_str=100, parent=self)
        self.port['OUT'].netconn.pullup_str =100

        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['vss'], self.netlist['n0']], self),
                NMOS("NMOS_1_u", [self.netlist['n0'], self.netlist['vss'], self.port['IN'].netconn], self),
                ])
 
class NMOS_AND2( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        for i in ('n0', 'n1'):
            self.netlist[i]=net.net(i, parent=self)

        # Add depln mode pullups
        self.netlist['n0'].pullup_str =100
        self.port['OUT'].netconn.pullup_str =100

        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.netlist['n0'], self.netlist['n1'], self.port['I0'].netconn], self ),
                NMOS("NMOS_1_u", [self.netlist['n1'], self.netlist['vss'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.port['OUT'].netconn, self.netlist['vss'], self.netlist['n0']], self),
                ])

class NMOS_AND3( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        for i in ('n0', 'n1', 'n2'):
            self.netlist[i]=net.net(i, parent=self)
        # Add depln mode pullups
        self.netlist['n0'].pullup_str =100
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.netlist['n0'], self.netlist['n1'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['n1'], self.netlist['n2'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.netlist['n2'], self.netlist['vss'], self.port['I2'].netconn], self),
                NMOS("NMOS_3_u", [self.port['OUT'].netconn, self.netlist['vss'], self.netlist['n0']], self),
                ])
                             
class NMOS_AND4( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN),
                          ('I3', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        for i in ('n0', 'n1', 'n2', 'n3'):
            self.netlist[i]=net.net(i, parent=self)
        # Add depln mode pullups
        self.netlist['n0'].pullup_str =100
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.netlist['n0'], self.netlist['n1'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['n1'], self.netlist['n2'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.netlist['n2'], self.netlist['n3'], self.port['I2'].netconn], self),
                NMOS("NMOS_3_u", [self.netlist['n3'], self.netlist['vss'], self.port['I3'].netconn], self),
                NMOS("NMOS_4_u", [self.port['OUT'].netconn, self.netlist['vss'], self.netlist['n0']], self),
                ])

class NMOS_AND5( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN),
                          ('I3', gate.IN),
                          ('I4', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        for i in ('n0', 'n1', 'n2', 'n3', 'n4'):
            self.netlist[i]=net.net(i, parent=self)
        # Add depln mode pullups
        self.netlist['n0'].pullup_str =100
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.netlist['n0'], self.netlist['n1'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['n1'], self.netlist['n2'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.netlist['n2'], self.netlist['n3'], self.port['I2'].netconn], self),
                NMOS("NMOS_3_u", [self.netlist['n3'], self.netlist['n4'], self.port['I3'].netconn], self),
                NMOS("NMOS_4_u", [self.netlist['n4'], self.netlist['vss'], self.port['I4'].netconn], self),
                NMOS("NMOS_5_u", [self.port['OUT'].netconn, self.netlist['vss'], self.netlist['n0']], self),
                ])

class NMOS_NAND4( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN),
                          ('I3', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        for i in ('n0', 'n1', 'n2', 'n3'):
            self.netlist[i]=net.net(i, parent=self)
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['n1'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['n1'], self.netlist['n2'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.netlist['n2'], self.netlist['n3'], self.port['I2'].netconn], self),
                NMOS("NMOS_3_u", [self.netlist['n3'], self.netlist['vss'], self.port['I3'].netconn], self),
                ])

class NMOS_NAND5( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN),
                          ('I3', gate.IN),
                          ('I4', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        for i in ('n0', 'n1', 'n2', 'n3', 'n4'):
            self.netlist[i]=net.net(i, parent=self)
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['n1'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['n1'], self.netlist['n2'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.netlist['n2'], self.netlist['n3'], self.port['I2'].netconn], self),
                NMOS("NMOS_3_u", [self.netlist['n3'], self.netlist['n4'], self.port['I3'].netconn], self),
                NMOS("NMOS_4_u", [self.netlist['n4'], self.netlist['vss'], self.port['I4'].netconn], self),
                ])
                             

class NMOS_OR2( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        self.netlist['n0']=net.net('n0', parent=self)
        # Add depln mode pullups
        self.netlist['n0'].pullup_str =100
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.netlist['n0'], self.netlist['vss'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['n0'], self.netlist['vss'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.port['OUT'].netconn, self.netlist['vss'], self.netlist['n0']], self),
                ])

class NMOS_NOR2( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I1'].netconn], self),
                ])

class NMOS_NOR3( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I1'].netconn], self),
                NMOS("NMOS_3_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I2'].netconn], self),
                ])

class NMOS_NOR4( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN),
                          ('I3', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I1'].netconn], self),
                NMOS("NMOS_3_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I2'].netconn], self),
                NMOS("NMOS_4_u", [self.port['OUT'].netconn, self.netlist['vss'], self.port['I3'].netconn], self),
                ])
                             
class NMOS_XOR2( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
        self.netlist['i0b']=net.net('i0b', parent=self, pullup_str=100)
        self.netlist['i1b']=net.net('i1b', parent=self, pullup_str=100)
        self.netlist['n0']=net.net('n0', parent=self)
        self.netlist['n1']=net.net('n1', parent=self)

  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.netlist['i0b'], self.netlist['vss'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['i1b'], self.netlist['vss'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.port['OUT'].netconn, self.netlist['n0'], self.netlist['i0b']], self),
                NMOS("NMOS_3_u", [self.netlist['n0'], self.netlist['vss'], self.netlist['i1b']], self),
                NMOS("NMOS_4_u", [self.port['OUT'].netconn, self.netlist['n1'], self.port['I0'].netconn], self),
                NMOS("NMOS_5_u", [self.netlist['n1'], self.netlist['vss'], self.port['I1'].netconn], self),

                ])


class NMOS_NMAJ( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('OUT', gate.OUT),
                          ('I0', gate.IN),
                          ('I1', gate.IN),
                          ('I2', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      
        
        # Add depln mode pullups
        self.port['OUT'].netconn.pullup_str =100
        self.netlist['n0']=net.net('n0', parent=self)
        self.netlist['n1']=net.net('n1', parent=self)

  
        self.gatelist.extend([
                NMOS("NMOS_0_u", [self.port['OUT'].netconn, self.netlist['n0'], self.port['I0'].netconn], self),
                NMOS("NMOS_1_u", [self.port['OUT'].netconn, self.netlist['n1'], self.port['I1'].netconn], self),
                NMOS("NMOS_2_u", [self.netlist['n0'], self.netlist['vss'], self.port['I1'].netconn], self),
                NMOS("NMOS_3_u", [self.netlist['n1'], self.netlist['vss'], self.port['I0'].netconn], self),
                # This has to be a bidir gate to work
                NMOS("NMOS_4_u", [self.netlist['n1'], self.netlist['n0'], self.port['I2'].netconn], self),
                ])



class NMOS_DFF( gate.module ):
    def __init__( self, name, mapping, parent=None ):
        portlist = dict( [('Q', gate.OUT),
                          ('D', gate.IN),
                          ('RSTB', gate.IN),
                          ('PHI', gate.IN)] )
        gate.module.__init__( self, name=name, portlist=portlist, mapping=mapping, parent=parent)      

        for i in ( 'phib', 'rst', 'n0'):
            self.netlist[i]=net.net(i, parent=self, pullup_str=100)
        self.netlist['n1']=net.net('n1', parent=self, charge_storage=True)
        self.netlist['n2']=net.net('n2', parent=self, charge_storage=True)
        self.port['Q'].netconn.pullup_str += 100

  
        self.gatelist.extend([
                # Inverters for the clock and reset signals
                NMOS("NMOS_0_u", [self.netlist['phib'], self.netlist['vss'], self.port['PHI'].netconn], self),
                NMOS("NMOS_1_u", [self.netlist['rst'], self.netlist['vss'], self.port['RSTB'].netconn], self),
                # 2 half latches                
                NMOS("NMOS_2_u", [self.netlist['n0'], self.netlist['vss'], self.netlist['n1']], self),
                NMOS("NMOS_3_u", [self.netlist['n1'], self.port['D'].netconn, self.netlist['phib']], self),
                NMOS("NMOS_4_u", [self.port['Q'].netconn, self.netlist['vss'], self.netlist['n2']], self),
                NMOS("NMOS_5_u", [self.netlist['n2'], self.netlist['n0'], self.port['PHI'].netconn], self),
                # Reset first and second latches in opposite directions - must be strong drivers to win contention vs pass gates
                NMOS("NMOS_6_u", [self.netlist['n1'], self.netlist['vss'], self.netlist['rst']], self),
                NMOS("NMOS_7_u", [self.netlist['n2'], self.netlist['vdd'], self.netlist['rst']], self),
                ])
                             

                             
