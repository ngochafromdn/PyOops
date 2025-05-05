# ExpressionAnalyzer.py
import logging
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ExpressionAnalyzer(syntaxVisitor):
    def __init__(self, symbol_table):
        super().__init__()
        self.symbol_table = symbol_table
        self.errors = []

    def visitStringArray(self, ctx: syntaxParser.StringArrayContext):
        if ctx is None:
            return None
        return "str[]"
    
    def visitCharArray(self, ctx: syntaxParser.CharArrayContext):
        if ctx is None:
            return None
        return "char[]"
    
    def visitIntArray(self, ctx: syntaxParser.IntArrayContext):
        if ctx is None:
            return None
        return "int[]"
            
    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        if ctx is None or ctx.NUMBER() is None:
            return None
            
        text = ctx.NUMBER().getText()

        if '.' in text:
            return "float"
        else:
            return "int"

    def visitStringExpr(self, ctx: syntaxParser.StringExprContext):
        if ctx is None or ctx.STRING() is None:
            return None
            
        return "str"

    def visitCharExpr(self, ctx: syntaxParser.CharExprContext):
        if ctx is None or ctx.CHARACTER() is None:
            return None
            
        return "char"

    def visitIdExpr(self, ctx: syntaxParser.IdExprContext):
        if ctx is None or ctx.IDENTIFIER() is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        name = ctx.IDENTIFIER().getText()
        value = self.symbol_table.lookup(name)
        
        if value is None:
            error = f"[Error] Line {line}, Column {column}: Undefined variable '{name}'"
            self.errors.append(error)
            logger.error(error)
            return None
            
        return value['type']

    def visitArrayAccessExpr(self, ctx: syntaxParser.ArrayAccessExprContext):
        if ctx is None or ctx.IDENTIFIER() is None or ctx.expression() is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        array_name = ctx.IDENTIFIER().getText()
        index_type = self.visit(ctx.expression())

        array_info = self.symbol_table.lookup(array_name)
        if not array_info:
            error = f"[Error] Line {line}, Column {column}: Undefined variable '{array_name}'"
            self.errors.append(error)
            logger.error(error)
            return None

        array_type = array_info.get('type', '')
        
        # Check if the variable is an array type
        if not array_type.endswith('[]'):
            error = f"[Error] Line {line}, Column {column}: Variable '{array_name}' is not an array"
            self.errors.append(error)
            logger.error(error)
            return None
            
        # Check if the index is an integer
        if index_type != "int":
            error = f"[Type Error] Line {line}, Column {column}: Array index must be an integer, got {index_type}"
            self.errors.append(error)
            logger.error(error)
            return None
            
        # Return the element type (remove the [] suffix)
        element_type = array_type[:-2]
        return element_type

    def visitCompExpr(self, ctx: syntaxParser.CompExprContext):
        if ctx is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        
        # Check if there are any add_expr children
        if not ctx.add_expr() or len(ctx.add_expr()) < 2:
            return self.visit(ctx.add_expr(0)) if ctx.add_expr() else None
        
        left_type = self.visit(ctx.add_expr(0))
        right_type = self.visit(ctx.add_expr(1))
        
        # If either operand is invalid, bail out
        if left_type is None or right_type is None:
            return None
            
        op = ctx.getChild(1).getText()

        # Check operand types
        if left_type != right_type:
            error = f"[Type Error] Line {line}, Column {column}: Cannot compare '{left_type}' with '{right_type}'"
            self.errors.append(error)
            logger.error(error)
            return None

        # Return bool type for comparison expressions
        return 'bool'

    def visitLogicExpr(self, ctx: syntaxParser.LogicExprContext):
        if ctx is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        
        # Check if there are any comp_expr children
        if not ctx.comp_expr() or len(ctx.comp_expr()) < 2:
            return self.visit(ctx.comp_expr(0)) if ctx.comp_expr() else None
        
        left_type = self.visit(ctx.comp_expr(0))
        right_type = self.visit(ctx.comp_expr(1))
        
        # If either operand is invalid, bail out
        if left_type is None or right_type is None:
            return None
            
        if left_type != 'bool' or right_type != 'bool':
            error = f"[Type Error] Line {line}, Column {column}: Logical operations require boolean operands, got '{left_type}' and '{right_type}'"
            self.errors.append(error)
            logger.error(error)
            return None
        
        return 'bool'
    
    def visitMulDivExpr(self, ctx: syntaxParser.MulDivExprContext):
        if ctx is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        
        # Check if there are any unary_expr children
        if not ctx.unary_expr() or len(ctx.unary_expr()) < 2:
            return self.visit(ctx.unary_expr(0)) if ctx.unary_expr() else None
        
        left_type = self.visit(ctx.unary_expr(0))
        right_type = self.visit(ctx.unary_expr(1))
        
        # If either operand is invalid, bail out
        if left_type is None or right_type is None:
            return None
            
        if left_type not in ('int', 'float') or right_type not in ('int', 'float'):
            error = f"[Type Error] Line {line}, Column {column}: Arithmetic operations require numeric operands, got '{left_type}' and '{right_type}'"
            self.errors.append(error)
            logger.error(error)
            return None
        
        # If one operand is float, result is float
        if left_type == 'float' or right_type == 'float':
            return 'float'
        return 'int'
    
    def visitAddSubExpr(self, ctx: syntaxParser.AddSubExprContext):
        if ctx is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        
        # Check if there are any mul_expr children
        if not ctx.mul_expr() or len(ctx.mul_expr()) < 2:
            return self.visit(ctx.mul_expr(0)) if ctx.mul_expr() else None
        
        left_type = self.visit(ctx.mul_expr(0))
        right_type = self.visit(ctx.mul_expr(1))
        
        # If either operand is invalid, bail out
        if left_type is None or right_type is None:
            return None
            
        op = ctx.getChild(1).getText()
        
        # Handle string concatenation
        if op == '+' and (left_type == 'str' or right_type == 'str'):
            if left_type != 'str' or right_type != 'str':
                error = f"[Type Error] Line {line}, Column {column}: Cannot concatenate '{left_type}' with '{right_type}'"
                self.errors.append(error)
                logger.error(error)
                return None
            return 'str'
            
        if left_type not in ('int', 'float') or right_type not in ('int', 'float'):
            error = f"[Type Error] Line {line}, Column {column}: Arithmetic operations require numeric operands, got '{left_type}' and '{right_type}'"
            self.errors.append(error)
            logger.error(error)
            return None
        
        # If one operand is float, result is float
        if left_type == 'float' or right_type == 'float':
            return 'float'
        return 'int'
    
    def visitParenExpr(self, ctx: syntaxParser.ParenExprContext):
        if ctx is None or ctx.expression() is None:
            return None
        return self.visit(ctx.expression())
    
    def visitTrueExpr(self, ctx: syntaxParser.TrueExprContext):
        if ctx is None:
            return None
        return 'bool'
    
    def visitFalseExpr(self, ctx: syntaxParser.FalseExprContext):
        if ctx is None:
            return None
        return 'bool'
    
    def visitUnaryMinusExpr(self, ctx: syntaxParser.UnaryMinusExprContext):
        if ctx is None or ctx.unary_expr() is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        expr_type = self.visit(ctx.unary_expr())
        
        if expr_type is None:
            return None
            
        if expr_type not in ('int', 'float'):
            error = f"[Type Error] Line {line}, Column {column}: Unary minus requires numeric operand, got '{expr_type}'"
            self.errors.append(error)
            logger.error(error)
            return None
        return expr_type
    
    def visitNotExpr(self, ctx: syntaxParser.NotExprContext):
        if ctx is None or ctx.expression() is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        expr_type = self.visit(ctx.expression())
        
        if expr_type is None:
            return None
            
        if expr_type != 'bool':
            error = f"[Type Error] Line {line}, Column {column}: Logical NOT requires boolean operand, got '{expr_type}'"
            self.errors.append(error)
            logger.error(error)
            return None
        return 'bool'
        
    def visitFuncCallExpr(self, ctx: syntaxParser.FuncCallExprContext):
        if ctx is None or ctx.IDENTIFIER() is None:
            return None
            
        line = ctx.start.line
        column = ctx.start.column
        func_name = ctx.IDENTIFIER().getText()
        func_info = self.symbol_table.lookup(func_name)
        
        if not func_info or func_info.get('type') != 'function':
            error = f"[Error] Line {line}, Column {column}: Undefined function '{func_name}'"
            self.errors.append(error)
            logger.error(error)
            return None
            
        # Check parameters
        args = []
        if ctx.arg_list():
            for expr_ctx in ctx.arg_list().expression():
                if expr_ctx is not None:
                    arg_type = self.visit(expr_ctx)
                    if arg_type:
                        args.append(arg_type)
                    
        params = func_info.get('params', [])
        if len(args) != len(params):
            error = f"[Error] Line {line}, Column {column}: Function '{func_name}' expects {len(params)} arguments, got {len(args)}"
            self.errors.append(error)
            logger.error(error)
            return None
            
        for i, (arg_type, param) in enumerate(zip(args, params)):
            if arg_type != param['type']:
                error = f"[Type Error] Line {line}, Column {column}: Argument {i+1} of function '{func_name}' expects type '{param['type']}', got '{arg_type}'"
                self.errors.append(error)
                logger.error(error)
                return None
                
        # Return function return type
        return func_info.get('return_type')
    
    # Default method to handle any missing visitor methods
    def defaultResult(self):
        return None