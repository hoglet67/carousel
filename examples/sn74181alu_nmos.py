# 
#
# Based on original code in verilog distributed with the ISCAS benchmark set:
#
#/****************************************************************************
# *                                                                          *
# *  VERILOG HIGH-LEVEL DESCRIPTION OF THE TI 74181 CIRCUIT                  *
# *                                                                          *
# *  Function: 4-bit ALU/Function Generator                                  *
# *                                                                          *
# *  Written by: Mark C. Hansen                                              *
# *                                                                          *
# *  Last modified: Dec 11, 1997                                             *
# *                                                                          *
# ****************************************************************************/

import gate
import net
from nmos_lib import NMOS_INV, NMOS_BUF, \
    NMOS_AND2, NMOS_AND3, NMOS_AND4, \
    NMOS_NOR2, NMOS_NOR3, NMOS_NOR4, \
    NMOS_OR2, NMOS_NAND4, NMOS_NAND5, \
    NMOS_XOR2

class sn74181alu_nmos( gate.module ):
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("A%d"%i, gate.IN) for i in range (0,4)] +
                         [("B%d"%i, gate.IN) for i in range (0,4)] +
                         [("S%d"%i, gate.IN) for i in range (0,4)] +
                         [("CN", gate.IN), ("M", gate.IN)] +
                         [("F%d"%i, gate.OUT) for i in range (0,4)] +
                         [("AEB", gate.OUT), ("X", gate.OUT)] +
                         [("Y", gate.OUT), ("CN4", gate.OUT)])

        gate.module.__init__( self, name, portlist, mapping, parent)

        for name in ['E', 'D', 'C', 'Bb' ]:
            for i in range(0, 4):
                n = "%s%d" % (name,i)
                self.netlist[n] = net.net(n, parent=self)   

        self.netlist['CNb'] = net.net('CNb', parent=self)   

        self.gatelist.extend([
                NMOS_INV("Cinv", dict([('OUT', self.netlist['CNb']), ('IN', self.port['CN'].netconn)]), self),
                emodule("Emod1", dict( [('A0', self.port['A0'].netconn),
                                        ('A1', self.port['A1'].netconn),
                                        ('A2', self.port['A2'].netconn),
                                        ('A3', self.port['A3'].netconn),
                                        ('B0', self.port['B0'].netconn),
                                        ('B1', self.port['B1'].netconn),
                                        ('B2', self.port['B2'].netconn),
                                        ('B3', self.port['B3'].netconn),
                                        ('S0', self.port['S0'].netconn),
                                        ('S1', self.port['S1'].netconn),
                                        ('S2', self.port['S2'].netconn),
                                        ('S3', self.port['S3'].netconn),
                                        ('E0', self.netlist['E0']),
                                        ('E1', self.netlist['E1']),
                                        ('E2', self.netlist['E2']),
                                        ('E3', self.netlist['E3']),
                                        ('Bb0', self.netlist['Bb0']),
                                        ('Bb1', self.netlist['Bb1']),
                                        ('Bb2', self.netlist['Bb2']),
                                        ('Bb3', self.netlist['Bb3'])]), self),

                dmodule("Dmod1", dict( [('A0', self.port['A0'].netconn),
                                        ('A1', self.port['A1'].netconn),
                                        ('A2', self.port['A2'].netconn),
                                        ('A3', self.port['A3'].netconn),
                                        ('B0', self.port['B0'].netconn),
                                        ('B1', self.port['B1'].netconn),
                                        ('B2', self.port['B2'].netconn),
                                        ('B3', self.port['B3'].netconn),
                                        ('Bb0', self.netlist['Bb0']),
                                        ('Bb1', self.netlist['Bb1']),
                                        ('Bb2', self.netlist['Bb2']),
                                        ('Bb3', self.netlist['Bb3']),
                                        ('S0', self.port['S0'].netconn),
                                        ('S1', self.port['S1'].netconn),
                                        ('S2', self.port['S2'].netconn),
                                        ('S3', self.port['S3'].netconn),
                                        ('D0', self.netlist['D0']),
                                        ('D1', self.netlist['D1']),
                                        ('D2', self.netlist['D2']),
                                        ('D3', self.netlist['D3'])]), self),

                clamodule("CLAmod3", dict( [('Gb0', self.netlist['E0']),
                                            ('Gb1', self.netlist['E1']),
                                            ('Gb2', self.netlist['E2']),
                                            ('Gb3', self.netlist['E3']),
                                            ('Pb0', self.netlist['D0']),
                                            ('Pb1', self.netlist['D1']),
                                            ('Pb2', self.netlist['D2']),
                                            ('Pb3', self.netlist['D3']),
                                            ('CNb', self.netlist['CNb']),
                                            ('C0', self.netlist['C0']),
                                            ('C1', self.netlist['C1']),
                                            ('C2', self.netlist['C2']),
                                            ('C3', self.netlist['C3']),
                                            ('X', self.port['X'].netconn),
                                            ('Y', self.port['Y'].netconn),
                                            ('CN4', self.port['CN4'].netconn)]), self),

                summodule("Summod4", dict( [('E0', self.netlist['E0']),
                                            ('E1', self.netlist['E1']),
                                            ('E2', self.netlist['E2']),
                                            ('E3', self.netlist['E3']),
                                            ('D0', self.netlist['D0']),
                                            ('D1', self.netlist['D1']),
                                            ('D2', self.netlist['D2']),
                                            ('D3', self.netlist['D3']),
                                            ('C0', self.netlist['C0']),
                                            ('C1', self.netlist['C1']),
                                            ('C2', self.netlist['C2']),
                                            ('C3', self.netlist['C3']),
                                            ('M', self.port['M'].netconn),
                                            ('F0', self.port['F0'].netconn),
                                            ('F1', self.port['F1'].netconn),
                                            ('F2', self.port['F2'].netconn),
                                            ('F3', self.port['F3'].netconn),
                                            ('AEB', self.port['AEB'].netconn)]), self) ])


class emodule( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("A%d"%i, gate.IN) for i in range (0,4)] +
                         [("B%d"%i, gate.IN) for i in range (0,4)] +
                         [("S%d"%i, gate.IN) for i in range (0,4)] +
                         [("E%d"%i, gate.OUT) for i in range (0,4)] +
                         [("Bb%d"%i, gate.OUT) for i in range (0,4)])

        gate.module.__init__( self, name, portlist, mapping, parent)
        
        for i in range(0, 4):
            n = "ABS3%d" % i
            self.netlist[n] = net.net(n, parent=self)   
            n = "ABbS2%d" % i
            self.netlist[n] = net.net(n, parent=self)   


        self.gatelist = [
                NMOS_INV("Bb0gate",dict([('OUT',self.port["Bb0"].netconn), ('IN',self.port["B0"].netconn)]), self),
                NMOS_INV("Bb1gate",dict([('OUT',self.port["Bb1"].netconn), ('IN',self.port["B1"].netconn)]), self),
                NMOS_INV("Bb2gate",dict([('OUT',self.port["Bb2"].netconn), ('IN',self.port["B2"].netconn)]), self),
                NMOS_INV("Bb3gate",dict([('OUT',self.port["Bb3"].netconn), ('IN',self.port["B3"].netconn)]), self),
                
                NMOS_AND3("ABS30gate",  dict([('OUT',self.netlist["ABS30"]), ('I0',self.port["A0"].netconn), ('I1',self.port["B0"].netconn), ('I2',self.port["S3"].netconn)]), self),
                NMOS_AND3("ABS31gate",  dict([('OUT',self.netlist["ABS31"]), ('I0',self.port["A1"].netconn), ('I1',self.port["B1"].netconn), ('I2',self.port["S3"].netconn)]), self),
                NMOS_AND3("ABS32gate",  dict([('OUT',self.netlist["ABS32"]), ('I0',self.port["A2"].netconn), ('I1',self.port["B2"].netconn), ('I2',self.port["S3"].netconn)]), self),
                NMOS_AND3("ABS33gate",  dict([('OUT',self.netlist["ABS33"]), ('I0',self.port["A3"].netconn), ('I1',self.port["B3"].netconn), ('I2',self.port["S3"].netconn)]), self),                
                NMOS_AND3("ABbS20gate", dict([('OUT',self.netlist["ABbS20"]), ('I0',self.port["A0"].netconn), ('I1',self.port["Bb0"].netconn), ('I2',self.port["S2"].netconn)]), self),
                NMOS_AND3("ABbS21gate", dict([('OUT',self.netlist["ABbS21"]), ('I0',self.port["A1"].netconn), ('I1',self.port["Bb1"].netconn), ('I2',self.port["S2"].netconn)]), self),
                NMOS_AND3("ABbS22gate", dict([('OUT',self.netlist["ABbS22"]), ('I0',self.port["A2"].netconn), ('I1',self.port["Bb2"].netconn), ('I2',self.port["S2"].netconn)]), self),
                NMOS_AND3("ABbS23gate", dict([('OUT',self.netlist["ABbS23"]), ('I0',self.port["A3"].netconn), ('I1',self.port["Bb3"].netconn), ('I2',self.port["S2"].netconn)]), self),
                
                NMOS_NOR2("E0gate", dict([('OUT',self.port["E0"].netconn), ('I0',self.netlist["ABS30"]), ('I1',self.netlist["ABbS20"])]), self),
                NMOS_NOR2("E1gate", dict([('OUT',self.port["E1"].netconn), ('I0',self.netlist["ABS31"]), ('I1',self.netlist["ABbS21"])]), self),
                NMOS_NOR2("E2gate", dict([('OUT',self.port["E2"].netconn), ('I0',self.netlist["ABS32"]), ('I1',self.netlist["ABbS22"])]), self),
                NMOS_NOR2("E3gate", dict([('OUT',self.port["E3"].netconn), ('I0',self.netlist["ABS33"]), ('I1',self.netlist["ABbS23"])]), self)]

class dmodule( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("A%d"%i, gate.IN) for i in range (0,4)] +
                         [("B%d"%i, gate.IN) for i in range (0,4)] +
                         [("Bb%d"%i, gate.IN) for i in range (0,4)] +
                         [("S%d"%i, gate.IN) for i in range (0,4)] +
                         [("D%d"%i, gate.OUT) for i in range (0,4)])

        gate.module.__init__( self, name, portlist, mapping, parent)
        
        for i in range(0, 4):
            n = "BbS1%d" % i
            self.netlist[n] = net.net(n, parent=self)   
            n = "BS0%d" % i
            self.netlist[n] = net.net(n, parent=self)   


        self.gatelist.extend([
                NMOS_AND2("BbS10gate", dict([('OUT',self.netlist["BbS10"]), ('I0',self.port["Bb0"].netconn), ('I1',self.port["S1"].netconn)]), self),
                NMOS_AND2("BbS11gate", dict([('OUT',self.netlist["BbS11"]), ('I0',self.port["Bb1"].netconn), ('I1',self.port["S1"].netconn)]), self),
                NMOS_AND2("BbS12gate", dict([('OUT',self.netlist["BbS12"]), ('I0',self.port["Bb2"].netconn), ('I1',self.port["S1"].netconn)]), self),
                NMOS_AND2("BbS13gate", dict([('OUT',self.netlist["BbS13"]), ('I0',self.port["Bb3"].netconn), ('I1',self.port["S1"].netconn)]), self),
                NMOS_AND2("BS00gate",  dict([('OUT',self.netlist["BS00"]), ('I0',self.port["B0"].netconn), ('I1',self.port["S0"].netconn)]), self),
                NMOS_AND2("BS01gate",  dict([('OUT',self.netlist["BS01"]), ('I0',self.port["B1"].netconn), ('I1',self.port["S0"].netconn)]), self),
                NMOS_AND2("BS02gate",  dict([('OUT',self.netlist["BS02"]), ('I0',self.port["B2"].netconn), ('I1',self.port["S0"].netconn)]), self),
                NMOS_AND2("BS03gate",  dict([('OUT',self.netlist["BS03"]), ('I0',self.port["B3"].netconn), ('I1',self.port["S0"].netconn)]), self),

                NMOS_NOR3("D0gate", dict([('OUT',self.port["D0"].netconn), ('I0',self.netlist["BbS10"]),('I1',self.netlist["BS00"]),('I2', self.port["A0"].netconn)]), self),
                NMOS_NOR3("D1gate", dict([('OUT',self.port["D1"].netconn), ('I0',self.netlist["BbS11"]),('I1',self.netlist["BS01"]),('I2', self.port["A1"].netconn)]), self),
                NMOS_NOR3("D2gate", dict([('OUT',self.port["D2"].netconn), ('I0',self.netlist["BbS12"]),('I1',self.netlist["BS02"]),('I2', self.port["A2"].netconn)]), self),
                NMOS_NOR3("D3gate", dict([('OUT',self.port["D3"].netconn), ('I0',self.netlist["BbS13"]),('I1',self.netlist["BS03"]),('I2', self.port["A3"].netconn)]), self)])


class clamodule( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("Gb%d"%i, gate.IN) for i in range (0,4)] +
                         [("Pb%d"%i, gate.IN) for i in range (0,4)] +
                         [("C%d"%i, gate.OUT) for i in range (0,4)] +
                         [("CNb", gate.IN),("CN4", gate.OUT),("X", gate.OUT),("Y", gate.OUT)] )
        gate.module.__init__( self, name, portlist, mapping, parent)

        for i in range(0, 4):
            n = "Pbuf%d" % i
            self.netlist[n] = net.net(n, parent=self)   

        for n in [ "CNbGb0","Pb0Gb1","CNbGb01", "Pb1Gb2", "Pb0Gb12", "Pb1Gb23", "Pb0Gb123", "CNbGb012", "Pb2Gb3", "XCNb"] :
            self.netlist[n] = net.net(n, parent=self)

        self.gatelist.extend([
                NMOS_INV("C0gate", dict([('OUT',self.port["C0"].netconn),('IN', self.port["CNb"].netconn)]), self),

                NMOS_BUF("Pb0gate", dict([('OUT',self.netlist['Pbuf0']),('IN',self.port["Pb0"].netconn)]), self),
                NMOS_BUF("Pb1gate", dict([('OUT',self.netlist['Pbuf1']),('IN',self.port["Pb1"].netconn)]), self),
                NMOS_BUF("Pb2gate", dict([('OUT',self.netlist['Pbuf2']),('IN',self.port["Pb2"].netconn)]), self),
                NMOS_BUF("Pb3gate", dict([('OUT',self.netlist['Pbuf3']),('IN',self.port["Pb3"].netconn)]), self),

                NMOS_AND2("CNbGb0gate", dict([('OUT',self.netlist["CNbGb0"]),('I0',self.port["CNb"].netconn),('I1',self.port["Gb0"].netconn)]), self),
                NMOS_AND2("Pb0Gb1gate", dict([('OUT',self.netlist["Pb0Gb1"]),('I0',self.port["Pb0"].netconn),('I1',self.port["Gb1"].netconn)]), self),
                NMOS_AND2("Pb1Gb2gate", dict([('OUT',self.netlist["Pb1Gb2"]),('I0',self.port["Pb1"].netconn),('I1',self.port["Gb2"].netconn)]), self),
                NMOS_AND2("Pb2Gb3gate", dict([('OUT',self.netlist["Pb2Gb3"]),('I0',self.port["Pb2"].netconn),('I1',self.port["Gb3"].netconn)]), self),

                NMOS_AND3("CNbGb01gate", dict([('OUT',self.netlist["CNbGb01"]),('I0',self.port["CNb"].netconn),('I1',self.port["Gb0"].netconn),('I2',self.port["Gb1"].netconn)]), self),
                NMOS_AND3("Pb0Gb12gate", dict([('OUT',self.netlist["Pb0Gb12"]),('I0',self.port["Pb0"].netconn),('I1',self.port["Gb1"].netconn),('I2',self.port["Gb2"].netconn)]), self),
                NMOS_AND3("Pb1Gb23gate", dict([('OUT',self.netlist["Pb1Gb23"]),('I0',self.port["Pb1"].netconn),('I1',self.port["Gb2"].netconn),('I2',self.port["Gb3"].netconn)]), self),
                NMOS_AND4("Pb0Gb123gate", dict([('OUT',self.netlist["Pb0Gb123"]),('I0',self.port["Pb0"].netconn),('I1',self.port["Gb1"].netconn),('I2',self.port["Gb2"].netconn),('I3',self.port["Gb3"].netconn)]), self),
                NMOS_AND4("CNbGb012gate", dict([('OUT',self.netlist["CNbGb012"]),('I0',self.port["CNb"].netconn),('I1',self.port["Gb0"].netconn),('I2',self.port["Gb1"].netconn),('I3',self.port["Gb2"].netconn)]), self),


                NMOS_NAND4("Xgate", dict([('OUT',self.port["X"].netconn),('I0',self.port["Gb0"].netconn),('I1',self.port["Gb1"].netconn),('I2',self.port["Gb2"].netconn),('I3',self.port["Gb3"].netconn)]), self),
                NMOS_NOR4("Ygate", dict([('OUT', self.port["Y"].netconn),('I0',self.netlist["Pbuf3"]),('I1',self.netlist["Pb2Gb3"]),('I2',self.netlist["Pb1Gb23"]),('I3',self.netlist["Pb0Gb123"])]), self),
                NMOS_NAND5("XCNbgate", dict([('OUT',self.netlist["XCNb"]),('I0',self.port["Gb0"].netconn),('I1',self.port["Gb1"].netconn),('I2',self.port["Gb2"].netconn),('I3',self.port["Gb3"].netconn),('I4',self.port["CNb"].netconn)]), self),
                NMOS_AND2("CN4gate", dict([('OUT',self.port["CN4"].netconn),('I0',self.port["Y"].netconn),('I1',self.netlist["XCNb"])]), self),
                NMOS_NOR4("C3gate", dict([('OUT',self.port["C3"].netconn),('I0',self.netlist["Pbuf2"]),('I1',self.netlist["Pb1Gb2"]),('I2',self.netlist["Pb0Gb12"]),('I3',self.netlist["CNbGb012"])]), self),
                NMOS_NOR3("C2gate", dict([('OUT',self.port["C2"].netconn),('I0',self.netlist["Pbuf1"]),('I1',self.netlist["Pb0Gb1"]),('I2',self.netlist["CNbGb01"])]), self),
                NMOS_NOR2("C1gate", dict([('OUT',self.port["C1"].netconn),('I0',self.netlist["Pbuf0"]),('I1',self.netlist["CNbGb0"])]), self)])



class summodule( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("E%d"%i, gate.IN) for i in range (0,4)] +
                         [("D%d"%i, gate.IN) for i in range (0,4)] +
                         [("C%d"%i, gate.IN) for i in range (0,4)] +
                         [("F%d"%i, gate.OUT) for i in range (0,4)] +
                         [("AEB", gate.OUT), ("M", gate.IN)] )
        gate.module.__init__( self, name, portlist, mapping, parent)

        for name in [ 'EXD', 'CM' ]:
            for i in range(0, 4):
                n = "%s%d" % (name,i)
                self.netlist[n] = net.net(n, parent=self)   

        self.gatelist.extend([
                NMOS_XOR2("EXD0gate", dict([('OUT',self.netlist['EXD0']),('I0',self.port['E0'].netconn),('I1',self.port['D0'].netconn)]), self),
                NMOS_XOR2("EXD1gate", dict([('OUT',self.netlist['EXD1']),('I0',self.port['E1'].netconn),('I1',self.port['D1'].netconn)]), self),
                NMOS_XOR2("EXD2gate", dict([('OUT',self.netlist['EXD2']),('I0',self.port['E2'].netconn),('I1',self.port['D2'].netconn)]), self),
                NMOS_XOR2("EXD3gate", dict([('OUT',self.netlist['EXD3']),('I0',self.port['E3'].netconn),('I1',self.port['D3'].netconn)]), self),
                NMOS_XOR2("F0gate", dict([('OUT',self.port['F0'].netconn),('I0',self.netlist['EXD0']),('I1',self.netlist['CM0'])]), self),
                NMOS_XOR2("F1gate", dict([('OUT',self.port['F1'].netconn),('I0',self.netlist['EXD1']),('I1',self.netlist['CM1'])]), self),
                NMOS_XOR2("F2gate", dict([('OUT',self.port['F2'].netconn),('I0',self.netlist['EXD2']),('I1',self.netlist['CM2'])]), self),
                NMOS_XOR2("F3gate", dict([('OUT',self.port['F3'].netconn),('I0',self.netlist['EXD3']),('I1',self.netlist['CM3'])]), self),
                
                NMOS_OR2("CM0gate", dict([('OUT',self.netlist['CM0']),('I0',self.port['C0'].netconn),('I1',self.port['M'].netconn)]), self),
                NMOS_OR2("CM1gate", dict([('OUT',self.netlist['CM1']),('I0',self.port['C1'].netconn),('I1',self.port['M'].netconn)]), self),
                NMOS_OR2("CM2gate", dict([('OUT',self.netlist['CM2']),('I0',self.port['C2'].netconn),('I1',self.port['M'].netconn)]), self),
                NMOS_OR2("CM3gate", dict([('OUT',self.netlist['CM3']),('I0',self.port['C3'].netconn),('I1',self.port['M'].netconn)]), self),


                NMOS_AND4("AEBgate", dict([('OUT',self.port["AEB"].netconn),('I0',self.port["F0"].netconn), 
                                           ('I1',self.port["F1"].netconn), ('I2',self.port["F2"].netconn), 
                                           ('I3',self.port["F3"].netconn)]), self)])

