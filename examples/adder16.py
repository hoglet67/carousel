import gate
import net


class adder16( gate.module ) :
    def __init__ ( self, name, mapping, parent=None ) :
        portlist = dict( [("S%02d"%i, gate.OUT) for i in range (0,16)] +
                         [("A%02d"%i, gate.IN) for i in range (0,16)] +
                         [("B%02d"%i, gate.IN) for i in range (0,16)] )
        gate.module.__init__( self, name, portlist, mapping, parent)
        

    def simulate( self ) :
        carry = 0
        valida = True
        validb = True
        result = []
        for i in range(0, 16):
            a = gate.BUF[self.port["A%02d"%i][0].value[0]]
            b = gate.BUF[self.port["B%02d"%i][0].value[0]]
            outputnet = self.port["S%02d"%i][0]
            if (a != 'X' and b != 'X' and carry != 'X'):
                a = 1 if a == '1' else 0
                b = 1 if b == '1' else 0                
                s = (a + b + carry) & 0x01
                carry = (a + b + carry) & 0x10 >> 1                
                s = '1' if s == 1 else '0'            
            else :
                s = 'X'
            if s != outputnet.value:
                result.append( (outputnet, s) )


        return (result, self.strength) 
