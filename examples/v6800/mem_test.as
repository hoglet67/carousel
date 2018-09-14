        ORG $8000


MEM_TEST
        LDS #$01FF
        LDX #$20
        LDAA #$00
LOOP
        STAA $00,X
        INX
        INCA
        BNE LOOP

END:    NOP
        JMP END

   