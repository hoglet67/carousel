        .ORG $8000

        LDA #$00
TOP:
        JSR $0010
        JMP TOP 
        BRK
        BRK
        BRK
        BRK
        BRK
        BRK
        BRK
        NOP
        INX
        DEY
        INC $0F
        SEC
        ADC #$02