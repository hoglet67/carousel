import gate
import net
from hex2bin import Hex2Bin

ADRSIZE = 32768
DRVSTR = net.SUPPLY_STR

class ram32k(gate.gate) :
    def __init__ ( self, name, mapping, parent=None, verbose = False, adr_lo = 0 ) :
        portlist = dict( [("adr%02d"%i, gate.IN) for i in range (0,15)] +
                         [("data%d"%i, gate.INOUT) for i in range (0,8)] +
                         [("csb", gate.IN)] +
                         [("web", gate.IN)] +
                         [("oeb", gate.IN)] )
        gate.gate.__init__( self, name, portlist, mapping, parent, is_a_primitive=True)
        self.verbose = verbose
        self.adr_lo = adr_lo
  
        # initialize a 32K ROM array
        self.mem_array = ["XXXXXXXX"] * ADRSIZE 

        # Save the last address and use this (optimistically) in place of bad addresses
        self.lastadr = 0

        # some shorthand and busses
        self.oeb  = self.port['oeb'].netconn
        self.databus = [ self.port["data%d" % n].netconn for n in range(7,-1, -1)]
        self.adrbus = [ self.port["adr%02d" % n].netconn for n in range(14,-1, -1)]
        self.csb  = self.port['csb'].netconn        
        self.web  = self.port['web'].netconn        
        self.driverpins = [ self.outputpins["data%d" % n] for n in range(7,-1, -1)]
 
        # Handle writes first at the very end of a write cycle ie on the rising edge
        # of web or csb, so need to store the previous data and address ready to
        # use.
        self.writeenable = False
        self.writedata = '00000000'
        self.writeaddress = []


    def message(self, msg ) :
        print "%s : %s" % (self.fullname(), msg)

    def simulate(self):

        result = []
        
        #
        # First handle writes to memory on the rising edge of the web or csb following
        # a valid write condition state. Using this edge prevents multiple writes of
        # different data (possibly to different addresses) takeing place during the
        # event wheel iterations.
        #
        if self.csb.value == '1' or self.web.value == '1':
            if self.writeenable:            
                try:
                    adrint = int(self.writeaddress,2)
                    self.lastadr = adrint
                except:
                    if self.verbose:
                        self.message( "Bad address %s" % self.writeaddress)
                    adrint = self.lastadr

                # Do the write
                self.mem_array[adrint] = self.writedata
                if self.verbose:
                    self.message( "Writing %s to address %d" %( self.writedata, adrint))
                    self.message( self.mem_array[0:10])

            # Completing a write or csb/web being in this state invalidates any write prep
            self.writeenable = False
        elif self.csb.value == '0' and self.web.value == '0':
            # if self.verbose:
            #     self.message( "Detected write preparation", self.writeaddress, self.writedata
            self.writeenable = True
            self.writedata = ''.join( [ d.value for d in self.databus ])
            self.writeaddress = ''.join([ n.value for n in self.adrbus ])


        #
        # Now handle reads similar to the ROM except that the web signal is also
        # able to act as a tristate enable/disable. No attempt to use edges here
        # assume that fully async reads are ok even it it means temporarily reading
        # the wrong address before the address bus stabilizes or just reading the
        # same address 2 or more times.
        #
        if self.oeb.value == '1' or self.csb.value == '1' or self.web.value == '0':
            # if not selected or writing the outputs will be tristated
            for (d,pin) in zip(self.databus, self.driverpins):
                if ( pin.state !=  ('Z',0) ):
                    result.append( (d, ('Z',0), pin) )
        elif self.oeb.value == '0' and self.csb.value == '0' and self.web.value == '1':
            adrvalstr = ''.join([ n.value for n in self.adrbus ])
            try:
                adrint = int(adrvalstr,2)
                self.lastadr = adrint
            except:
                if self.verbose:
                    self.message( "Bad address %s" % adrvalstr)
                adrint = self.lastadr
            for (d,pin,bit) in zip(self.databus, self.driverpins, self.mem_array[adrint]):
                if ( pin.state !=  (bit,DRVSTR) ):
                    result.append( (d, (bit,DRVSTR), pin))
            if self.verbose:
                self.message( "reading %s from adr %d" % (self.mem_array[adrint], adrint))
        else:
            for (d,pin) in zip(self.databus, self.driverpins):
                if (pin.state !=  ('X',DRVSTR) ):
                    result.append((d, ('X',DRVSTR), pin))

            
        return result



    def finish_simulation ( self, options ) :
        '''
        Optional dump of memory contents to screen or file at the end of simulation.
        
        When dumping to files, any locations with 'X' are written as 0xFF
        '''
        if "ramdump" in options:
            ramopts = options["ramdump"]

            if "lo" in ramopts:
                first_adr = int(ramopts["lo"])
            else:
                first_adr = self.adr_lo

            if "hi" in ramopts:
                num_bytes = int(ramopts["hi"]) - first_adr
            elif "numbytes" in options ["ramdump"]:
                num_bytes = int(ramopts["numbytes"])
            else:
                num_bytes = ADRSIZE

            if "filename" in ramopts:
                filename = ramopts["filename"]
            else:
                filename = None

                
            hexl = []
            ascl = []
            line = []
            for adr in range ( first_adr, first_adr + num_bytes ) :
                if not (adr - first_adr) % 16 :
                    hexl.append("%s  %s" % (''.join(line), ''.join(ascl)))
                    line = ["%04x: " % adr]
                    ascl = []

                byte = self.mem_array[adr]
                if byte == 'XXXXXXXX':
                    byte = "11111111"
                i = int(byte,2)
                line.append("%02x " % i)
                ascl.append( chr(i) if i > 31 and i <128 else '.')

            hexl.append("%s  %s" % (''.join(line), ''.join(ascl)))

            if not filename:
                print "RAM Dump from memory ", self.fullname()
                print '\n'.join(hexl)
            else:
                f = open(filename, "w")
                for l in hexl:
                    f.write("%s\n" % l)
                f.close()

        return 
