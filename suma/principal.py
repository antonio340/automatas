import sys
from antlr4 import *
from traductorPythonaJavaLexer import traductorPythonaJavaLexer
from traductorPythonaJavaParser import traductorPythonaJavaParser
from traductorListener import traductorListener

def main(argv):
    if len(argv) < 2:
        print("Uso: python main.py <archivo.txt>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = traductorPythonaJavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = traductorPythonaJavaParser(stream)
    tree = parser.prog()

    translator = traductorListener()
    walker = ParseTreeWalker()
    walker.walk(translator, tree)

    print(translator.getJavaCode())

if __name__ == '__main__':
    main(sys.argv)
