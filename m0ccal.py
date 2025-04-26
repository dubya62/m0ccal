from antlr4 import *
from MoccalLexer import MoccalLexer
from MoccalListener import MoccalListener
from MoccalParser import MoccalParser
import sys


class MoccalPrintListener(MoccalListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = MoccalLexer(FileStream("test7.ccal"))
    stream = CommonTokenStream(lexer)
    parser = MoccalParser(stream)

    tree = parser.moccal()

    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
