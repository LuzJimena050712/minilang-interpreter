from django.shortcuts import render
from antlr4 import *
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .EvalVisitor import EvalVisitor
import io
import sys

def index(request):
    context = {}
    
    if request.method == "POST":
        code = request.POST.get("code", "")
        
        # Captura la salida de print()
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        try:
            input_stream = InputStream(code)
            lexer = MiniLangLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = MiniLangParser(stream)
            tree = parser.program()
            
            visitor = EvalVisitor()
            visitor.visit(tree)
            
            output = buffer.getvalue()
        except Exception as e:
            output = f"Error: {str(e)}"
        finally:
            sys.stdout = old_stdout
        
        context['result'] = output
        context['code'] = code
    
    return render(request, 'interpreter/index.html', context)