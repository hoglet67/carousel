import gate
import net
from hex2bin import Hex2Bin

ADRSIZE = 32768
DRVSTR = net.SUPPLY_STR

class rom32k(gate.gate) :
    def __init__ ( self, name, mapping, parent=None, filename="", adr_lo=0 ) :
        portlist = dict( [("adr%02d"%i, gate.IN) for i in range (0,15)] +
                         [("data%d"%i, gate.OUT) for i in range (0,8)] +
                         [("csb", gate.IN)] +
                         [("oeb", gate.IN)] )
        gate.gate.__init__( self, name, portlist, mapping, parent, is_a_primitive=True)

        self.adr_lo=adr_lo
        # initialize a 32K ROM array
        self.mem_array = ["00000000"] * ADRSIZE 

        self.mem_array[0x7FFC] = "00000000"   # reset vector for 6502 (little endian)
        self.mem_array[0x7FFD] = "10000000"
        self.mem_array[0x7FFE] = "10000000"   # reset vector for 6800 (big endian)
        self.mem_array[0x7FFF] = "00000000"

        if filename == "":
            # Initialize the ROM with hard coded values initially - will use ROMBO's hex2bin.py
            # class for this once I remember how it works
            self.mem_array[0] = "10100000" #LDY
            self.mem_array[1] = "00000000" # #0
            self.mem_array[2] = "10100010" #LDX
            self.mem_array[3] = "00000000" # #0
            self.mem_array[4] = "10101001" #LDA
            self.mem_array[5] = "00000001" # #1
            self.mem_array[6] = "10011001" #STA 00,Y
            self.mem_array[7] = "00000000" #
            self.mem_array[8] = "00000000" #
            self.mem_array[9] = "11001000" #INY
            self.mem_array[10] = "11100110" #INC
            self.mem_array[11] = "00000000" #00
            self.mem_array[12] = "01001100" #JMP
            self.mem_array[13] = "00000110" #06
            self.mem_array[14] = "10000000" #80
        else:
            h = Hex2Bin(memory_image_start=self.adr_lo, memory_image_size=ADRSIZE)
            rslt = h.read_file( filename, ignore_checksum=False)
            # Copy image from hex2bin object into mem_array
            localadr = 0
            for i in range (0,ADRSIZE):
                (data, valid) = h.read_byte(i)
                if valid:
                    # remember to pad the leading zeros and lose the 0b prefix
                    self.mem_array[localadr]= bin(data)[2:].zfill(8)
                    #print "Adr", i, "Data ", self.mem_array[i & 0x7FFF] 
                    localadr +=1

        # Save the last address and use this (optimistically) in place of bad addresses
        self.lastadr = 0

        # some shorthand and busses
        self.oeb  = self.port['oeb'].netconn
        self.databus = [ self.port["data%d" % n].netconn for n in range(7,-1, -1)]
        self.adrbus = [ self.port["adr%02d" % n].netconn for n in range(14,-1, -1)]
        self.csb  = self.port['csb'].netconn        
        self.driverpins = [ self.outputpins["data%d" % n] for n in range(7,-1, -1)]

    def simulate(self):

        result = []
        if self.oeb.value == '1' or self.csb.value == '1':
            # if not selected or writing the outputs will be tristated
            for (d,pin) in zip(self.databus, self.driverpins):
                if ( pin.state !=  ('Z',0) ):
                    result.append( (d, ('Z',0), pin) )
        elif self.oeb.value == '0' and self.csb.value == '0':
            adrvalstr = ''.join([ n.value for n in self.adrbus ])
            try:
                adrint = int(adrvalstr,2)
                self.lastadr = adrint
            except:
                # print "Bad address %s", adrvalstr
                adrint = self.lastadr
            for (d,pin,bit) in zip(self.databus, self.driverpins, self.mem_array[adrint]):
                if ( pin.state !=  (bit,DRVSTR) ):
                    result.append( (d, (bit,DRVSTR), pin))
        else:
            for (d,pin) in zip(self.databus, self.driverpins):
                if (pin.state !=  ('X',DRVSTR) ):
                    result.append((d, ('X',DRVSTR), pin))

            
        return result



