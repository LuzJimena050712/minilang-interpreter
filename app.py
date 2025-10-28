from flask import Flask, render_template, request
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor
import io
import sys

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.form["code"]
    
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
    
    return render_template("index.html", result=output, code=code)

if __name__ == "__main__":
    app.run(debug=True)