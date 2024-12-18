import sys
from antlr4 import *
from lenguajeTraductorLexer import lenguajeTraductorLexer
from lenguajeTraductorParser import lenguajeTraductorParser
from listener import listener

def main(argv):
    if len(argv) < 2:
        print("Uso: python main.py <archivo.txt>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file)
    lexer = lenguajeTraductorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = lenguajeTraductorParser(stream)
    tree = parser.program()

    translator = listener()
    walker = ParseTreeWalker()
    walker.walk(translator, tree)

    print(translator.getPythonCode())

if __name__ == '__main__':
    main(sys.argv)
