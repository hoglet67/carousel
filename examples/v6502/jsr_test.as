        .ORG $8000

        LDA $00
        TAX

TOP:    
        NOP
        JSR SUB1
        JSR SUB2
        JSR SUB3
        NOP
        JMP TOP
        
        .WORD 00,00,00,00
        .WORD 00,00,00,00
        
SUB1:
        LDA #'6'
        STA $0000,X
        RTS

SUB2:
        LDA #'5'
        INX
        STA $0000,X
        RTS

SUB3:
        JSR SUB4
        LDA #'2'
        INX
        STA $0000,X
        INX
        RTS

SUB4:
        LDA #'0'
        INX
        STA $0000,X
        RTS




