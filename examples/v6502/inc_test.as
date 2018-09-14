
        ;; Simple test ROM
        .ORG $8000
RSTVECTOR:      
        LDY #1
        LDA #1
        STA $00

TOP:
        INC $00
        LDA $00
        STA $00,Y
        INY

        JMP TOP

        ;; Reset vector      
        .ORG $FFFC
        .WORD RSTVECTOR
