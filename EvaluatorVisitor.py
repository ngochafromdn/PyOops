from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class EvaluatorVisitor(syntaxVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def visitPrint_stmt(self, ctx: syntaxParser.Print_stmtContext):
        value = self.visit(ctx.expression())
        print(f"🖨️ Output: {value}")
        return value

    # Example handlers below. You need one for each expression rule.
    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())

    def visitStringExpr(self, ctx: syntaxParser.StringExprContext):
        return bytes(ctx.STRING().getText()[1:-1], "utf-8").decode("unicode_escape")

    def visitIdExpr(self, ctx: syntaxParser.IdExprContext):
        name = ctx.IDENTIFIER().getText()
        value = self.symbol_table.get(name)
        if value is None:
            print(f"[Error] Undefined variable '{name}'")
        return value

    def visitAddSubExpr(self, ctx: syntaxParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return left + right if op == '+' else left - right

    def visitLogicExpr(self, ctx: syntaxParser.LogicExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return left and right if op == 'and' else left or right

    def visitCompExpr(self, ctx: syntaxParser.CompExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return eval(f"{left} {op} {right}")

    def visitNotExpr(self, ctx: syntaxParser.NotExprContext):
        return not self.visit(ctx.expression())

    def visitParenExpr(self, ctx: syntaxParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitTrueExpr(self, ctx: syntaxParser.TrueExprContext):
        return True

    def visitFalseExpr(self, ctx: syntaxParser.FalseExprContext):
        return False

