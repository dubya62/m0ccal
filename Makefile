

.PHONY: antlr

antlr: Moccal.g4
	antlr4 -Dlanguage=Python3 $<
	

