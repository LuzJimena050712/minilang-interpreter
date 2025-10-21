import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor

def main():
    
    print("Ingrese la operación:")

    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.program()

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()

