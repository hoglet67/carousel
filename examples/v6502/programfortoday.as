   ; Generate PI as ASCII characters, from the 6502.org thread 'program for today'
   ;     http://forum.6502.org/viewtopic.php?t=1878
   ;
   ; Modified to produce a shorter result faster for use in the carousel regression test:
   ;
   ;    you can get results from the pi generator a bit faster, if you only look for a few digits:
   ; LDX#31  becomes LDX#4
   ;   and
   ; LDX#104 becomes LDX#11
   ;   likewise
   ; LDX#103 becomes LDX#10
   ; CPX#31  becomes CPX#4
   ; 
   ; 

   ; reserve some space in zero page for the program
   ; P DS 104 
   .DEFINE P $80 
   ; Q DS 1 
   .DEFINE Q 0 
   ; R DS 1 
   .DEFINE R 1 

   .DEFINE CURPOS 2 
   .DEFINE CHRTMP 3  
   .DEFINE STROUT $10  

   .ORG     $8000
   LDA #STROUT
   STA CURPOS  

   CLD 
   JSR INIT 
;   LDX #31 
   LDX #4
L1: TXA 
   PHA 
   LDA #0 
   STA Q 
;   LDX #104 
   LDX #11 
L2: TXA 
   JSR MUL 
   PHA 
   LDA Q 
   PHA 
   LDA #10 
   STA Q 
   LDA P-1,X 
   JSR MUL 
   STA R 
   PLA 
   ADC Q 
   STA Q 
   PLA 
   ADC R 
   STX R 
   ASL R 
   DEC R 
   JSR DIV 
   STA P-1,X 
   DEX 
   BNE L2 
   LDA #10 
   STA R 
   LDA #0 
   JSR DIV 
   STA P 
   LDA Q 
   EOR #48 
   JSR OUTPUT 
   PLA 
   TAX 
;   CPX #31 
   CPX #4
   BNE L3 
   LDA #46 
   JSR OUTPUT 
L3: DEX 
   BNE L1 
   RTS 

INIT: 
   LDA #2 
;   LDX #103 
   LDX #10 
I1: STA P,X 
   DEX 
   BPL I1 
   RTS 

MUL: 
   STA R 
   LDA #0 
   LDY #8 
   LSR Q 
M1: BCC M2 
   CLC 
   ADC R 
M2: ROR 
   ROR Q 
   DEY 
   BNE M1 
   RTS 

DIV: 
   LDY #8 
   ASL Q 
D1: ROL 
   BCS D2 
   CMP R 
   BCC D3 
D2: SBC R 
   SEC 
D3: ROL Q 
   DEY 
   BNE D1 
   RTS 

OUTPUT:
        STA CHRTMP
        PHA
        TXA
        PHA
        LDX CURPOS
        LDA CHRTMP
        STA 0,X
        INC CURPOS
        PLA
        TAX
        PLA
        RTS