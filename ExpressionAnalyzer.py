import logging
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ExpressionAnalyzer(syntaxVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def visitStringArray(self, ctx: syntaxParser.StringArrayContext):
        if ctx.strArray().getText():
            return "str[]"
    
    def visitCharArray(self, ctx: syntaxParser.CharArrayContext):
        if ctx.char_Array().getText():
            return "char[]"
    
    def visitIntArray(self, ctx: syntaxParser.IntArrayContext):
        if ctx.int_Array().getText():
            return "int[]"
            
    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        text = ctx.NUMBER().getText()

        if '.' in text:
            return "float"
        else:
            return "int"

        # try:
        #     return float(text) if '.' in text else int(text)
        # except ValueError:
        #     logger.error(f"Invalid number: {text}")
        #     return None

    def visitStringExpr(self, ctx: syntaxParser.StringExprContext):
        if ctx.STRING().getText():
            return "str"
    #     raw = ctx.STRING().getText()
    #     return bytes(raw[1:-1], "utf-8").decode("unicode_escape")

    def visitCharExpr(self, ctx: syntaxParser.CharExprContext):
        if ctx.CHARACTER().getText():
            return "char"
    #     raw = ctx.getText()
    #     return bytes(raw[1:-1], "utf-8").decode("unicode_escape")

    

    # def visitIdExpr(self, ctx: syntaxParser.IdExprContext):
    #     name = ctx.IDENTIFIER().getText()
    #     value = self.symbol_table.get(name)
    #     if value is None:
    #         logger.error(f"[Error] Undefined variable '{name}'")
    #         return None
    #     return value

    # def visitAddSubExpr(self, ctx: syntaxParser.AddSubExprContext):
    #     left = self.visit(ctx.expression(0))
    #     right = self.visit(ctx.expression(1))
    #     op = ctx.getChild(1).getText()

    #     if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
    #         logger.error("Addition/Subtraction requires numeric operands")
    #         return None

    #     return left + right if op == '+' else left - right

    # def visitMulDivExpr(self, ctx: syntaxParser.MulDivExprContext):
    #     left = self.visit(ctx.expression(0))
    #     right = self.visit(ctx.expression(1))
    #     op = ctx.getChild(1).getText()

    #     if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
    #         logger.error("Multiplication/Division requires numeric operands")
    #         return None

    #     if op == '/' and right == 0:
    #         logger.error("Division by zero error!")
    #         return None

    #     return left * right if op == '*' else left / right

    # def visitLogicExpr(self, ctx: syntaxParser.LogicExprContext):
    #     left = self.visit(ctx.expression(0))
    #     right = self.visit(ctx.expression(1))
    #     op = ctx.getChild(1).getText()

    #     if not isinstance(left, bool) or not isinstance(right, bool):
    #         logger.error("Logical operations require boolean operands")
    #         return None

    #     return left and right if op == 'and' else left or right

    # def visitCompExpr(self, ctx: syntaxParser.CompExprContext):
    #     left = self.visit(ctx.expression(0))
    #     right = self.visit(ctx.expression(1))
    #     op = ctx.getChild(1).getText()

    #     allowed_ops = {'==', '!=', '<', '<=', '>', '>='}
    #     if op not in allowed_ops:
    #         logger.error(f"Unsupported comparison operator: {op}")
    #         return None

    #     try:
    #         return eval(f"{repr(left)} {op} {repr(right)}")
    #     except Exception as e:
    #         logger.error(f"Comparison error: {e}")
    #         return None

    # def visitNotExpr(self, ctx: syntaxParser.NotExprContext):
    #     value = self.visit(ctx.expression())
    #     if not isinstance(value, bool):
    #         logger.error("Logical NOT requires a boolean operand")
    #         return None
    #     return not value

    # def visitParenExpr(self, ctx: syntaxParser.ParenExprContext):
    #     return self.visit(ctx.expression())

    # def visitTrueExpr(self, ctx: syntaxParser.TrueExprContext):
    #     return True

    # def visitFalseExpr(self, ctx: syntaxParser.FalseExprContext):
    #     return False

    # def visitUnaryMinusExpr(self, ctx: syntaxParser.UnaryMinusExprContext):
    #     value = self.visit(ctx.expression())
    #     if not isinstance(value, (int, float)):
    #         logger.error("Unary minus requires a numeric operand")
    #         return None
    #     return -value

    # def visitIntArray(self, ctx: syntaxParser.IntArrayContext):
    #     result = []
    #     for num in ctx.NUMBER():
    #         try:
    #             result.append(int(num.getText()))
    #         except ValueError:
    #             logger.warning(f"Invalid integer: {num.getText()}")
    #     return result

    # def visitCharArray(self, ctx: syntaxParser.CharArrayContext):
    #     result = []
    #     for char in ctx.CHARACTER():
    #         try:
    #             decoded = bytes(char.getText()[1:-1], "utf-8").decode("unicode_escape")
    #             result.append(decoded)
    #         except Exception as e:
    #             logger.warning(f"Invalid character: {char.getText()} ({e})")
    #     return result

    # def visitStringArray(self, ctx: syntaxParser.StringArrayContext):
    #     result = []
    #     for string in ctx.STRING():
    #         try:
    #             decoded = bytes(string.getText()[1:-1], "utf-8").decode("unicode_escape")
    #             result.append(decoded)
    #         except Exception as e:
    #             logger.warning(f"Invalid string: {string.getText()} ({e})")
    #     return result

    # # Optional: if you want to support null
    # def visitNullExpr(self, ctx):
    #     return None