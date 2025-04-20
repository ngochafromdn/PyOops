from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class ExpressionAnalyzer(syntaxVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        text = ctx.NUMBER().getText()
        return float(text) if '.' in text else int(text)

    def visitStringExpr(self, ctx: syntaxParser.StringExprContext):
        return bytes(ctx.STRING().getText()[1:-1], "utf-8").decode("unicode_escape")

    def visitCharExpr(self, ctx: syntaxParser.CharExprContext):
        return bytes(ctx.getText()[1:-1], "utf-8").decode("unicode_escape")

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

    def visitMulDivExpr(self, ctx: syntaxParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '/' and right == 0:
            print("I have error: Division by zero error!")
            return None
        return left * right if op == '*' else left / right

    def visitLogicExpr(self, ctx: syntaxParser.LogicExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return left and right if op == 'and' else left or right

    def visitCompExpr(self, ctx: syntaxParser.CompExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        return eval(f"{repr(left)} {op} {repr(right)}")

    def visitNotExpr(self, ctx: syntaxParser.NotExprContext):
        return not self.visit(ctx.expression())

    def visitParenExpr(self, ctx: syntaxParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitTrueExpr(self, ctx: syntaxParser.TrueExprContext):
        return True

    def visitFalseExpr(self, ctx: syntaxParser.FalseExprContext):
        return False

    def visitUnaryMinusExpr(self, ctx: syntaxParser.UnaryMinusExprContext):
        return -self.visit(ctx.expression())

    def visitIntArray(self, ctx: syntaxParser.IntArrayContext):
        return [int(num.getText()) for num in ctx.NUMBER()]

    def visitCharArray(self, ctx: syntaxParser.CharArrayContext):
        return [bytes(char.getText()[1:-1], "utf-8").decode("unicode_escape") for char in ctx.CHARACTER()]

    def visitStringArray(self, ctx: syntaxParser.StringArrayContext):
        return [bytes(string.getText()[1:-1], "utf-8").decode("unicode_escape") for string in ctx.STRING()]

