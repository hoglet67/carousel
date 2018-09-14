       .ORG $8000
TOP:                    
        LDA #$00
        SEC                      
        STA $0000
        ROL
        STA $0001
        ROL
        STA $0002
        ROL
        STA $0003
        ROL
        STA $0004
        ROL
        STA $0005
        ROL
        STA $0006
        ROL
        STA $0007
        ROL
        STA $0008
        ROL
        STA $0009
        CLC
        LDA #$FF
        STA $000A
        ROL
        STA $000B
        ROL
        STA $000C
        ROL
        STA $000D
        ROL
        STA $000E
        ROL
        STA $000F
        ROL
        STA $0010
        ROL
        STA $0011
        ROL
        STA $0012
        ROL
        STA $0013
rotr:
        LDA #$00
        SEC                      
        STA $0014
        ROR
        STA $0015
        ROR
        STA $0016
        ROR
        STA $0017
        ROR
        STA $0018
        ROR
        STA $0019
        ROR
        STA $001A
        ROR
        STA $001B
        ROR
        STA $001C
        ROR
        STA $001D
        CLC
        LDA #$FF
        STA $001E
        ROR
        STA $001F
        ROR
        STA $0020
        ROR
        STA $0021
        ROR
        STA $0022
        ROR
        STA $0023
        ROR
        STA $0024
        ROR
        STA $0025
        ROR
        STA $0026
        ROR
        STA $0027

WAIT:   
        NOP
        JMP WAIT




