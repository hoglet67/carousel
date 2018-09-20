import gate
import net
from testbench import testbench
from primitive import NMOS, UNMOS

## Full nMOS implementation of a 4x4 SRAM array
##
##     +-----------------+---------+-----------------+---------+-----------------+---------+-----------------+------< word0
##    _|_  q03    q03_b _|_       _|_  q02    q02_b _|_       _|_  q01    q01_b _|_       _|_  q00    q00_b _|_     
## +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+  
## |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        |  
## |   +-----------------+---------+-----------------+---------+-----------------+---------+-----------------+------< word1
## |  _|_  q13    q13_b _|_  | |  _|_  q12    q12_b _|_  | |  _|_  q11    q11_b _|_  | |  _|_  q10    q10_b _|_  |  
## +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+  
## |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        |  
## |   +-----------------+---------+-----------------+---------+-----------------+---------+-----------------+------< word2
## |  _|_  q23    q23_b _|_  | |  _|_  q22    q22_b _|_  | |  _|_  q21    q21_b _|_  | |  _|_  q20    q20_b _|_  |  
## +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+  
## |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        |  
## |   +-----------------+---------+-----------------+---------+-----------------+---------+-----------------+------< word3
## |  _|_  q33    q33_b _|_  | |  _|_  q32    q32_b _|_  | |  _|_  q31    q31_b _|_  | |  _|_  q30    q30_b _|_  |  
## +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+ +-'   '-+--|>o---+--'   '-+  
## |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        | |       +--o<|---+        |  
## |   +-----------------+---------+-----------------+---------+-----------------+---------+-----------------+------< write
## |  _|_               _|_  | |  _|_               _|_  | |  _|_               _|_  | |  _|_               _|_  |  
## +-'   '--o<|-+------'   '-+ +-'   '--o<|-+------'   '-+ +-'   '--o<|-+------'   '-+ +-'   '--o<|-+------'   '-+  
## |    n23     | n13        | |    n22     | n12        | |    n21     | n11        | |    n20     | n10        |  
## |            o            | |            o            | |            o            | |            o            |  
## |           /_\           | |           /_\           | |           /_\           | |           /_\           |  
## v            |            v v            |            v v            |            v v            |            v  
## bit3      data3_in   bit3_b bit2      data2_in   bit2_b bit1      data1_in   bit1_b bit0      data0_in   bit0_b 

class sram4x4_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)

        self.netlist.update(gate.wire( ['write']))
        self.netlist.update(gate.wire( ['data0_in', 'n10', 'n20', 'bit0', 'bit0_b', 'word0']))
        self.netlist.update(gate.wire( ['data1_in', 'n11', 'n21', 'bit1', 'bit1_b', 'word1']))
        self.netlist.update(gate.wire( ['data2_in', 'n12', 'n22', 'bit2', 'bit2_b', 'word2']))
        self.netlist.update(gate.wire( ['data3_in', 'n13', 'n23', 'bit3', 'bit3_b', 'word3']))

        for j in range (0,4):
            for i in range (0,4):
                self.netlist.update(gate.wire( ['word%d%d' % (i,j), 'q%d%d' % (i,j), 'q%d%d_b' % (i,j)]))
                self.netlist['q%d%d' % (i,j)].pullup_str = net.DEPL_STR
                self.netlist['q%d%d_b' % (i,j)].pullup_str = net.DEPL_STR

            self.netlist['n1%d' %j].pullup_str = net.DEPL_STR
            self.netlist['n2%d' %j].pullup_str = net.DEPL_STR
        
        self.gatelist = []

        for j in range (0,4):
            for i in range (0,4):
                self.gatelist.extend( [
                    NMOS( "ram%d%d_0_u" % (j,i),
                          [ self.netlist['q%d%d' % (j,i)],
                            self.netlist['vss'], 
                            self.netlist['q%d%d_b' % (j,i)]],
                          parent=self),
                    NMOS( "ram%d%d_1_u" % (j,i), 
                          [ self.netlist['q%d%d_b' % (j,i)], 
                            self.netlist['vss'], 
                            self.netlist['q%d%d' % (j,i)]],
                          parent = self),
                    NMOS( "ram%d%d_2_u" % (j,i), 
                          [ self.netlist['bit%d' % i], 
                            self.netlist['q%d%d' % (j,i)], 
                            self.netlist['word%d' % j]],
                          parent = self),
                    NMOS( "ram%d%d_3_u" % (i,j), 
                          [ self.netlist['bit%d_b' % i ], 
                            self.netlist['q%d%d_b' % (j,i)], 
                            self.netlist['word%d' % j]],
                          parent = self)])
            self.gatelist.extend( [            
                    NMOS( "ctrl_0%d_u" % j, 
                          [ self.netlist['bit%d' %j ], 
                            self.netlist['n2%d' %j], 
                            self.netlist['write']], self),
                    NMOS( "ctrl_1%d_u" %j, 
                          [ self.netlist['bit%d_b' %j], 
                            self.netlist['n1%d' %j ], 
                            self.netlist['write']], self),
                    NMOS( "ctrl_2%d_u" %j, 
                          [ self.netlist['n1%d' %j], 
                            self.netlist['vss'], 
                            self.netlist['data%d_in' % j ]], self),
                    NMOS( "ctrl_4%d_u" %j, 
                          [ self.netlist['n2%d' %j], 
                            self.netlist['vss'], 
                            self.netlist['n1%d' %j]], self)])
        
        vector_string = '''
PI data3_in
PI data2_in
PI data1_in
PI data0_in

PI write

PI word3
PI word2
PI word1
PI word0

PO q33
PO q32
PO q31
PO q30

PO q23
PO q22
PO q21
PO q20

PO q13
PO q12
PO q11
PO q10

PO q03
PO q02
PO q01
PO q00

PO bit3
PO bit2
PO bit1
PO bit0

PO bit3_b
PO bit2_b
PO bit1_b
PO bit0_b

#  dddd                 
#  aaaa                       
#  tttt w wwww                             bbbb
#  aaaa r oooo                             iiii
#  1010                               bbbb tttt  
#  ____ i rrrr  qqqq qqqq qqqq qqqq   iiii 3210
#  iiii t dddd  3333 2222 1111 0000   tttt ____
#  nnnn e 3210  3210 3210 3210 3210   3210 bbbb
# ----------------------------------------------
   0000 0 0000  XXXX XXXX XXXX XXXX   XXXX XXXX
   0000 1 0001  XXXX XXXX XXXX LLLL   XXXX XXXX
   0000 1 0010  XXXX XXXX LLLL LLLL   XXXX XXXX
   0000 1 0100  XXXX LLLL LLLL LLLL   XXXX XXXX
   0000 1 1000  LLLL LLLL LLLL LLLL   XXXX XXXX
   0000 0 0000  LLLL LLLL LLLL LLLL   XXXX XXXX
                                               
   1111 0 0000  LLLL LLLL LLLL LLLL   XXXX XXXX
   1111 0 0001  LLLL LLLL LLLL LLLL   LLLL HHHH
   1111 0 0010  LLLL LLLL LLLL LLLL   LLLL HHHH
   1111 0 0100  LLLL LLLL LLLL LLLL   LLLL HHHH
   1111 0 1000  LLLL LLLL LLLL LLLL   LLLL HHHH
   1111 0 0000  LLLL LLLL LLLL LLLL   XXXX XXXX
                                               
   1111 0 0000  LLLL LLLL LLLL LLLL   XXXX XXXX
   1111 1 0001  LLLL LLLL LLLL HHHH   XXXX XXXX
   1111 1 0010  LLLL LLLL HHHH HHHH   XXXX XXXX
   1111 1 0100  LLLL HHHH HHHH HHHH   XXXX XXXX
   1111 1 1000  HHHH HHHH HHHH HHHH   XXXX XXXX
   1111 0 0000  HHHH HHHH HHHH HHHH   XXXX XXXX
                                               
   0000 0 0000  HHHH HHHH HHHH HHHH   XXXX XXXX
   0000 0 0001  HHHH HHHH HHHH HHHH   HHHH LLLL
   0000 0 0010  HHHH HHHH HHHH HHHH   HHHH LLLL
   0000 0 0100  HHHH HHHH HHHH HHHH   HHHH LLLL
   0000 0 1000  HHHH HHHH HHHH HHHH   HHHH LLLL
   0000 0 0000  HHHH HHHH HHHH HHHH   XXXX XXXX
                                               
   0000 0 0000  HHHH HHHH HHHH HHHH   XXXX XXXX
   0000 0 0001  HHHH HHHH HHHH LLLL   XXXX XXXX
   0000 0 0000  HHHH HHHH HHHH LLLL   XXXX XXXX
   0000 0 0100  HHHH LLLL HHHH LLLL   XXXX XXXX
   0000 0 0000  HHHH LLLL HHHH LLLL   XXXX XXXX
                                               
   1111 0 0000  HHHH LLLL HHHH LLLL   XXXX XXXX
   1111 0 0001  HHHH LLLL HHHH LLLL   LLLL HHHH
   1111 0 0010  HHHH LLLL HHHH LLLL   HHHH LLLL
   1111 0 0100  HHHH LLLL HHHH LLLL   LLLL HHHH
   1111 0 1000  HHHH LLLL HHHH LLLL   HHHH LLLL
   1111 0 0000  HHHH LLLL HHHH LLLL   XXXX XXXX

'''

        self.events  = self.read_flex_string( vector_string)
