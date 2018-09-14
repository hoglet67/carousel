BASE ?= 0x8000

SHELL=/bin/tcsh -f

TESTSRCS   ?= $(shell ls -1 *as)
IHEXES     ?= $(patsubst %.as,%.ihex,$(TESTSRCS))

all: ${IHEXES}

clean:
	rm -f *.o *.lst *.srec *.bin *.ihex *.ram *~ *.s19

%.hex : %.as
	as0 $< -h 

%.ihex: %.hex
	mv -f $< $@

