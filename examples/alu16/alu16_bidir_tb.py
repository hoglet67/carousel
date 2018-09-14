import gate
import net
from testbench import testbench
from count16_bidir_nmos import count16_bidir_nmos
#from adder16 import adder16
from sn74181alu_bidir_nmos import sn74181alu_bidir_nmos


class alu16_tb(testbench):

    def __init__(self, options):
        testbench.__init__(self, options)


        self.netlist.update( gate.wire(['q%02d' %i for i in range(0,16)]))
        self.netlist.update( gate.wire(['qq%02d' %i for i in range(0,16)]))
        self.netlist.update( gate.wire(['f%02d' %i for i in range(0,16)]))
        self.netlist.update( gate.wire(['s%d' %i for i in range(0,4)]))
        self.netlist.update( gate.wire(['aeb%d' %i for i in range(0,4)]))
        self.netlist.update( gate.wire(['x%d' %i for i in range(0,4)]))
        self.netlist.update( gate.wire(['y%d' %i for i in range(0,4)]))
        self.netlist.update( gate.wire(['cn4%d' %i for i in range(0,4)]))
        self.netlist.update( gate.wire([ 'rstb', 'phi', 'mode', 'carryin']))


        dut0 = count16_bidir_nmos( "cout16_0_u", dict([ ('Q0', self.netlist['q00']),
                             ('Q1', self.netlist['q01']),
                             ('Q2', self.netlist['q02']),
                             ('Q3', self.netlist['q03']),
                             ('Q4', self.netlist['q04']),
                             ('Q5', self.netlist['q05']),
                             ('Q6', self.netlist['q06']),
                             ('Q7', self.netlist['q07']),
                             ('Q8', self.netlist['q08']),
                             ('Q9', self.netlist['q09']),
                             ('Q10', self.netlist['q10']),
                             ('Q11', self.netlist['q11']),
                             ('Q12', self.netlist['q12']),
                             ('Q13', self.netlist['q13']),
                             ('Q14', self.netlist['q14']),
                             ('Q15', self.netlist['q15']),
                             ('CIN', self.netlist['vdd']),                            
                             ('PHI', self.netlist['phi']),
                             ('RSTB', self.netlist['rstb'])]))
        dut1 = count16_bidir_nmos( "cout16_1_u", dict([ ('Q0', self.netlist['qq00']),
                             ('Q1', self.netlist['qq01']),
                             ('Q2', self.netlist['qq02']),
                             ('Q3', self.netlist['qq03']),
                             ('Q4', self.netlist['qq04']),
                             ('Q5', self.netlist['qq05']),
                             ('Q6', self.netlist['qq06']),
                             ('Q7', self.netlist['qq07']),
                             ('Q8', self.netlist['qq08']),
                             ('Q9', self.netlist['qq09']),
                             ('Q10', self.netlist['qq10']),
                             ('Q11', self.netlist['qq11']),
                             ('Q12', self.netlist['qq12']),
                             ('Q13', self.netlist['qq13']),
                             ('Q14', self.netlist['qq14']),
                             ('Q15', self.netlist['qq15']),
                             ('CIN', self.netlist['vdd']),                            
                             ('PHI', self.netlist['q08']),
                             ('RSTB', self.netlist['rstb'])]))
        dut2 = sn74181alu_bidir_nmos( "alu_0_u", dict([ ('A0', self.netlist['q00']),
                                      ('A1', self.netlist['q01']),
                                      ('A2', self.netlist['q02']),
                                      ('A3', self.netlist['q03']),
                                      ('B0', self.netlist['qq00']),
                                      ('B1', self.netlist['qq01']),
                                      ('B2', self.netlist['qq02']),
                                      ('B3', self.netlist['qq03']),
                                      ('S0', self.netlist['s0']),
                                      ('S1', self.netlist['s1']),
                                      ('S2', self.netlist['s2']),
                                      ('S3', self.netlist['s3']),
                                      ('CN', self.netlist['carryin']),
                                      ('M', self.netlist['mode']),
                                      ('F0', self.netlist['f00']),
                                      ('F1', self.netlist['f01']),
                                      ('F2', self.netlist['f02']),
                                      ('F3', self.netlist['f03']),
                                      ('AEB', self.netlist['aeb0']),
                                      ('X', self.netlist['x0']),
                                      ('Y', self.netlist['y0']),
                                      ('CN4', self.netlist['cn40'])]))
        dut3 = sn74181alu_bidir_nmos( "alu_1_u", dict([ ('A0', self.netlist['q04']),
                                      ('A1', self.netlist['q05']),
                                      ('A2', self.netlist['q06']),
                                      ('A3', self.netlist['q07']),
                                      ('B0', self.netlist['qq04']),
                                      ('B1', self.netlist['qq05']),
                                      ('B2', self.netlist['qq06']),
                                      ('B3', self.netlist['qq07']),
                                      ('S0', self.netlist['s0']),
                                      ('S1', self.netlist['s1']),
                                      ('S2', self.netlist['s2']),
                                      ('S3', self.netlist['s3']),
                                      ('CN', self.netlist['cn40']),
                                      ('M', self.netlist['mode']),
                                      ('F0', self.netlist['f04']),
                                      ('F1', self.netlist['f05']),
                                      ('F2', self.netlist['f06']),
                                      ('F3', self.netlist['f07']),
                                      ('AEB', self.netlist['aeb1']),
                                      ('X', self.netlist['x1']),
                                      ('Y', self.netlist['y1']),
                                      ('CN4', self.netlist['cn41'])]))
        dut4 = sn74181alu_bidir_nmos( "alu_2_u", dict([ ('A0', self.netlist['q08']),
                                      ('A1', self.netlist['q09']),
                                      ('A2', self.netlist['q10']),
                                      ('A3', self.netlist['q11']),
                                      ('B0', self.netlist['qq08']),
                                      ('B1', self.netlist['qq09']),
                                      ('B2', self.netlist['qq10']),
                                      ('B3', self.netlist['qq11']),
                                      ('S0', self.netlist['s0']),
                                      ('S1', self.netlist['s1']),
                                      ('S2', self.netlist['s2']),
                                      ('S3', self.netlist['s3']),
                                      ('CN', self.netlist['cn41']),
                                      ('M', self.netlist['mode']),
                                      ('F0', self.netlist['f08']),
                                      ('F1', self.netlist['f09']),
                                      ('F2', self.netlist['f10']),
                                      ('F3', self.netlist['f11']),
                                      ('AEB', self.netlist['aeb2']),
                                      ('X', self.netlist['x2']),
                                      ('Y', self.netlist['y2']),
                                      ('CN4', self.netlist['cn42'])]))
        dut5 = sn74181alu_bidir_nmos( "alu_3_u", dict([ ('A0', self.netlist['q12']),
                                      ('A1', self.netlist['q13']),
                                      ('A2', self.netlist['q14']),
                                      ('A3', self.netlist['q15']),
                                      ('B0', self.netlist['qq12']),
                                      ('B1', self.netlist['qq13']),
                                      ('B2', self.netlist['qq14']),
                                      ('B3', self.netlist['qq15']),
                                      ('S0', self.netlist['s0']),
                                      ('S1', self.netlist['s1']),
                                      ('S2', self.netlist['s2']),
                                      ('S3', self.netlist['s3']),
                                      ('CN', self.netlist['cn43']),
                                      ('M', self.netlist['mode']),
                                      ('F0', self.netlist['f12']),
                                      ('F1', self.netlist['f13']),
                                      ('F2', self.netlist['f14']),
                                      ('F3', self.netlist['f15']),
                                      ('AEB', self.netlist['aeb3']),
                                      ('X', self.netlist['x3']),
                                      ('Y', self.netlist['y3']),
                                      ('CN4', self.netlist['cn43'])]))

        self.gatelist = [dut0, dut1, dut2, dut3, dut4, dut5]

        vector_string = '''
PI rstb
PI phi
PI s0
PI s1
PI s2
PI s3
PI mode
PI carryin

  0 0 1000 00
  1 0 1000 00
'''
        
        vector_string += '\n'.join(['  1 0 1000 00\n  1 1 1000 00'] * 65535)

        self.events  = self.read_flex_string( vector_string)

