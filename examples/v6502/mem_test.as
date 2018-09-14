        .ORG $8000

        ;; Fill first 256 bytes of memory with the number of each byte

MEM_TEST:
        LDA #$00
        TAY
        LDA #$00
        TAX
        STA $00
        
LOOP:   
        INY
        INX
        STY $0000,X
        BNE LOOP


END:    NOP
        JMP END

   