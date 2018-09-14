BASE ?= 0x8000

SHELL=/bin/tcsh -f

TESTSRCS   ?= $(shell ls -1 *as)
IHEXES     ?= $(patsubst %.as,%.ihex,$(TESTSRCS))

all: ${IHEXES}

clean:
	rm -f *.o *.lst *.srec *.bin *.ihex *.ram *~

%.o : %.as
	ca65 -l $< -D BASE=$(BASE) 

%.bin: %.o
	cl65 $< --target none --start-addr $(BASE) -o $@ -l

%.ihex: %.bin
	python2 ../../lib/hex2bin.py -i bin -o ihex -f $< -g $@ --input_start_adr ${BASE}
