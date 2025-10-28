from MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.vars = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[name] = value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print(value)

    def visitExpr(self, ctx):
        
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.ID():
            name = ctx.ID().getText()
            return self.vars[name]
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.expr(0))
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            if op == '-':
                return left - right
            if op == '*':
                return left * right
            if op == '/':
                return left / right
        return 0