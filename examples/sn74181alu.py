#
#
# Based on code created from ISCAS benchmark set:
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
from primitive import AND, OR, NOR, XOR, INV, BUF, NAND


class sn74181alu( gate.module ):
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
                INV("Cinv", [self.netlist['CNb'], self.port['CN'].netconn], self), 

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
                INV("Bb0gate",[self.port["Bb0"].netconn, self.port["B0"].netconn], self),
                INV("Bb1gate",[self.port["Bb1"].netconn, self.port["B1"].netconn], self),
                INV("Bb2gate",[self.port["Bb2"].netconn, self.port["B2"].netconn], self),
                INV("Bb3gate",[self.port["Bb3"].netconn, self.port["B3"].netconn], self),
                
                AND("ABS30gate",[self.netlist["ABS30"], self.port["A0"].netconn, self.port["B0"].netconn, self.port["S3"].netconn], self),
                AND("ABS31gate",[self.netlist["ABS31"], self.port["A1"].netconn, self.port["B1"].netconn, self.port["S3"].netconn], self),
                AND("ABS32gate",[self.netlist["ABS32"], self.port["A2"].netconn, self.port["B2"].netconn, self.port["S3"].netconn], self),
                AND("ABS33gate",[self.netlist["ABS33"], self.port["A3"].netconn, self.port["B3"].netconn, self.port["S3"].netconn], self),
                
                AND("ABbS20gate", [self.netlist["ABbS20"], self.port["A0"].netconn, self.port["Bb0"].netconn, self.port["S2"].netconn], self),
                AND("ABbS21gate", [self.netlist["ABbS21"], self.port["A1"].netconn, self.port["Bb1"].netconn, self.port["S2"].netconn], self),
                AND("ABbS22gate", [self.netlist["ABbS22"], self.port["A2"].netconn, self.port["Bb2"].netconn, self.port["S2"].netconn], self),
                AND("ABbS23gate", [self.netlist["ABbS23"], self.port["A3"].netconn, self.port["Bb3"].netconn, self.port["S2"].netconn], self),
                
                NOR("E0gate", [self.port["E0"].netconn, self.netlist["ABS30"], self.netlist["ABbS20"]], self),
                NOR("E1gate", [self.port["E1"].netconn, self.netlist["ABS31"], self.netlist["ABbS21"]], self),
                NOR("E2gate", [self.port["E2"].netconn, self.netlist["ABS32"], self.netlist["ABbS22"]], self),
                NOR("E3gate", [self.port["E3"].netconn, self.netlist["ABS33"], self.netlist["ABbS23"]], self)]

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
                AND("BbS10gate", [self.netlist["BbS10"], self.port["Bb0"].netconn, self.port["S1"].netconn], self),
                AND("BbS11gate", [self.netlist["BbS11"], self.port["Bb1"].netconn, self.port["S1"].netconn], self),
                AND("BbS12gate", [self.netlist["BbS12"], self.port["Bb2"].netconn, self.port["S1"].netconn], self),
                AND("BbS13gate", [self.netlist["BbS13"], self.port["Bb3"].netconn, self.port["S1"].netconn], self),

                AND("BS00gate", [self.netlist["BS00"], self.port["B0"].netconn, self.port["S0"].netconn], self),
                AND("BS01gate", [self.netlist["BS01"], self.port["B1"].netconn, self.port["S0"].netconn], self),
                AND("BS02gate", [self.netlist["BS02"], self.port["B2"].netconn, self.port["S0"].netconn], self),
                AND("BS03gate", [self.netlist["BS03"], self.port["B3"].netconn, self.port["S0"].netconn], self),

                NOR("D0gate", [self.port["D0"].netconn, self.netlist["BbS10"], self.netlist["BS00"], self.port["A0"].netconn], self),
                NOR("D1gate", [self.port["D1"].netconn, self.netlist["BbS11"], self.netlist["BS01"], self.port["A1"].netconn], self),
                NOR("D2gate", [self.port["D2"].netconn, self.netlist["BbS12"], self.netlist["BS02"], self.port["A2"].netconn], self),
                NOR("D3gate", [self.port["D3"].netconn, self.netlist["BbS13"], self.netlist["BS03"], self.port["A3"].netconn], self)])


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
                INV("C0gate", [self.port["C0"].netconn, self.port["CNb"].netconn], self),

                BUF("Pb0gate", [self.netlist['Pbuf0'], self.port["Pb0"].netconn], self),
                AND("CNbGb0gate", [self.netlist["CNbGb0"], self.port["CNb"].netconn, self.port["Gb0"].netconn], self),

                BUF("Pb1gate", [self.netlist['Pbuf1'], self.port["Pb1"].netconn], self),
                AND("Pb0Gb1gate", [self.netlist["Pb0Gb1"], self.port["Pb0"].netconn, self.port["Gb1"].netconn], self),
                AND("CNbGb01gate", [self.netlist["CNbGb01"], self.port["CNb"].netconn, self.port["Gb0"].netconn, self.port["Gb1"].netconn], self),

                BUF("Pb2gate", [self.netlist['Pbuf2'], self.port["Pb2"].netconn], self),
                AND("Pb1Gb2gate", [self.netlist["Pb1Gb2"], self.port["Pb1"].netconn, self.port["Gb2"].netconn], self),
                AND("Pb0Gb12gate", [self.netlist["Pb0Gb12"], self.port["Pb0"].netconn, self.port["Gb1"].netconn, self.port["Gb2"].netconn], self),
                AND("CNbGb012gate", [self.netlist["CNbGb012"], self.port["CNb"].netconn, self.port["Gb0"].netconn, self.port["Gb1"].netconn, self.port["Gb2"].netconn], self),

                BUF("Pb3gate", [self.netlist['Pbuf3'], self.port["Pb3"].netconn], self),
                AND("Pb2Gb3gate", [self.netlist["Pb2Gb3"], self.port["Pb2"].netconn, self.port["Gb3"].netconn], self),
                AND("Pb1Gb23gate", [self.netlist["Pb1Gb23"], self.port["Pb1"].netconn, self.port["Gb2"].netconn, self.port["Gb3"].netconn], self),
                AND("Pb0Gb123gate", [self.netlist["Pb0Gb123"], self.port["Pb0"].netconn, self.port["Gb1"].netconn, self.port["Gb2"].netconn, self.port["Gb3"].netconn], self),


                NAND("Xgate", [self.port["X"].netconn, self.port["Gb0"].netconn, self.port["Gb1"].netconn, self.port["Gb2"].netconn, self.port["Gb3"].netconn], self),

                NOR("Ygate", [ self.port["Y"].netconn, self.netlist["Pbuf3"],self.netlist["Pb2Gb3"],self.netlist["Pb1Gb23"],self.netlist["Pb0Gb123"]], self),

                NAND("XCNbgate", [self.netlist["XCNb"], self.port["Gb0"].netconn, self.port["Gb1"].netconn, self.port["Gb2"].netconn, self.port["Gb3"].netconn, self.port["CNb"].netconn], self),

                AND("CN4gate", [self.port["CN4"].netconn, self.port["Y"].netconn, self.netlist["XCNb"]], self),

                NOR("C3gate", [self.port["C3"].netconn, self.netlist["Pbuf2"], self.netlist["Pb1Gb2"], self.netlist["Pb0Gb12"], self.netlist["CNbGb012"]], self),

                NOR("C2gate", [self.port["C2"].netconn, self.netlist["Pbuf1"], self.netlist["Pb0Gb1"], self.netlist["CNbGb01"]], self),

                NOR("C1gate", [self.port["C1"].netconn, self.netlist["Pbuf0"], self.netlist["CNbGb0"]], self)])



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
                XOR("EXD0gate", [self.netlist['EXD0'], self.port['E0'].netconn, self.port['D0'].netconn], self),
                XOR("EXD1gate", [self.netlist['EXD1'], self.port['E1'].netconn, self.port['D1'].netconn], self),
                XOR("EXD2gate", [self.netlist['EXD2'], self.port['E2'].netconn, self.port['D2'].netconn], self),
                XOR("EXD3gate", [self.netlist['EXD3'], self.port['E3'].netconn, self.port['D3'].netconn], self),
                
                OR("CM0gate", [self.netlist['CM0'], self.port['C0'].netconn, self.port['M'].netconn], self),
                OR("CM1gate", [self.netlist['CM1'], self.port['C1'].netconn, self.port['M'].netconn], self),
                OR("CM2gate", [self.netlist['CM2'], self.port['C2'].netconn, self.port['M'].netconn], self),
                OR("CM3gate", [self.netlist['CM3'], self.port['C3'].netconn, self.port['M'].netconn], self),

                XOR("F0gate", [self.port['F0'].netconn, self.netlist['EXD0'], self.netlist['CM0']], self),
                XOR("F1gate", [self.port['F1'].netconn, self.netlist['EXD1'], self.netlist['CM1']], self),
                XOR("F2gate", [self.port['F2'].netconn, self.netlist['EXD2'], self.netlist['CM2']], self),
                XOR("F3gate", [self.port['F3'].netconn, self.netlist['EXD3'], self.netlist['CM3']], self),

                AND("AEBgate", [self.port["AEB"].netconn, self.port["F0"].netconn, self.port["F1"].netconn, self.port["F2"].netconn, self.port["F3"].netconn], self)])

