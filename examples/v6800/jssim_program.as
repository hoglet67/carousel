        ORG $8000

TOP:        
        LDAA #0
        STAA $0F
        LDX #$4321
        TXS
LOOP:
        LDAB #$FB
        JSR L2
        JMP LOOP
        NOP
        NOP
        NOP
        NOP
L2:
        INX
        DECA
        INC $0F
        SEC
        ADCB #$02
        RTS

