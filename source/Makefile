
v6800.py: source_ed_6800/transdefs.js source_ed_6800/segdefs.js source_6800/nodenames.js padlist_6800 
	#python2 trans2gates.py source_6800/transdefs.js source_6800/segdefs.js source_6800/nodenames.js padlist_6800 v6800
	python2 trans2gates.py source_ed_6800/transdefs.js source_ed_6800/segdefs.js source_6800/nodenames.js padlist_6800 v6800

v6502.py:
	python2 trans2gates.py source_6502/transdefs.js source_6502/segdefs.js source_6502/nodenames.js padlist_6502 v6502

v80.py:
	python2 trans2gates.py source_z80/transdefs.js source_z80/segdefs.js source_z80/nodenames.js padlist_z80 v80

all: v6800.py v6502.py v80.py

clean:
	rm v*py *~




