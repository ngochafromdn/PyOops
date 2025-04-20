from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class SemanticAnalyzer(syntaxVisitor):
    def __init__(self):
        super().__init__()

    def visitAssignStmt(self, ctx: syntaxParser.AssignStmtContext):
        name = ctx.assignment().IDENTIFIER().getText()
        value_type = self.visit(ctx.assignment().expression())
        symbol = self.lookup(name)
        if symbol is None:
            print(f"[Error] Variable '{name}' not declared before assignment.")
        elif symbol['type'] != value_type:
            print(f"[Type Error] Cannot assign '{value_type}' to variable '{name}' of type '{symbol['type']}'")
        return value_type

    def visitVarDeclStmt(self, ctx: syntaxParser.VarDeclStmtContext):
        var_decl = ctx.variable_declaration()
        declared_type = var_decl.DATA_TYPE().getText()
        name = var_decl.IDENTIFIER().getText()
        self.define(name, {'type': declared_type})

        if var_decl.expression():
            value_type = self.visit(var_decl.expression())
            if value_type != declared_type:
                print(f"[Type Error] Mismatched types in declaration of '{name}': expected '{declared_type}', got '{value_type}'")

    def visitFuncStmt(self, ctx: syntaxParser.FuncStmtContext):
        func_name = ctx.IDENTIFIER().getText()
        return_type = ctx.DATA_TYPE().getText() if ctx.DATA_TYPE() else "void"
        params = []

        if ctx.param_list():
            for i in range(len(ctx.param_list().IDENTIFIER())):
                pname = ctx.param_list().IDENTIFIER(i).getText()
                ptype = ctx.param_list().DATA_TYPE(i).getText()
                params.append({'name': pname, 'type': ptype})

        self.define(func_name, {
            'type': 'function',
            'return_type': return_type,
            'params': params
        })

        self.push_scope()
        for param in params:
            self.define(param['name'], {'type': param['type']})
        self.visit(ctx.block())
        self.pop_scope()

    def visitReturnStmt(self, ctx: syntaxParser.ReturnStmtContext):
        expr_type = self.visit(ctx.expression())
        # You can store the expected return type in a stack if nested functions exist
        return expr_type

    def visitIf_stmt(self, ctx: syntaxParser.If_stmtContext):
        for expr in ctx.expression():
            condition_type = self.visit(expr)
            if condition_type != 'bool':
                self.errors.append(f"[Type Error] Condition in if/elif must be 'bool', got '{condition_type}'.")
        return self.visitChildren(ctx)

    def visitWhile_stmt(self, ctx: syntaxParser.While_stmtContext):
        condition_type = self.visit(ctx.expression())
        if condition_type != 'bool':
            self.errors.append(f"[Type Error] While-loop condition must be 'bool', got '{condition_type}'.")
        return self.visitChildren(ctx)
    
    def visitPrintStmt(self, ctx: syntaxParser.PrintStmtContext):
        self.visit(ctx.expression())  # No type requirement for print
        return None

    def visitReturnStmt(self, ctx: syntaxParser.ReturnStmtContext):
        self.visit(ctx.expression())  # You can add function return checks later
        return None

    def visitTryStmt(self, ctx: syntaxParser.TryStmtContext):
        self.visit(ctx.block(0))  # try block
        self.visit(ctx.block(1))  # except block
        return None
    
    # ---- Expression Visitors ----

    def visitIdExpr(self, ctx: syntaxParser.IdExprContext):
        name = ctx.IDENTIFIER().getText()
        symbol = self.lookup(name)
        if not symbol:
            print(f"[Error] Use of undeclared variable '{name}'")
            return "unknown"
        return symbol['type']

    def visitNumberExpr(self, ctx: syntaxParser.NumberExprContext):
        value = ctx.getText()
        return 'float' if '.' in value else 'int'

    def visitStringExpr(self, ctx: syntaxParser.StringExprContext):
        return 'str'

    def visitCharExpr(self, ctx: syntaxParser.CharExprContext):
        return 'char'

    def visitTrueExpr(self, ctx): return 'bool'
    def visitFalseExpr(self, ctx): return 'bool'

    def visitAddSubExpr(self, ctx: syntaxParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left == right and left in {'int', 'float'}:
            return left
        print(f"[Type Error] Cannot apply '+' or '-' to '{left}' and '{right}'")
        return "unknown"

    def visitMulDivExpr(self, ctx: syntaxParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left == right and left in {'int', 'float'}:
            return left
        print(f"[Type Error] Cannot apply '*' or '/' to '{left}' and '{right}'")
        return "unknown"

    def visitCompExpr(self, ctx: syntaxParser.CompExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != right:
            print(f"[Type Error] Comparison between '{left}' and '{right}'")
        return 'bool'

    def visitLogicExpr(self, ctx: syntaxParser.LogicExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != 'bool' or right != 'bool':
            print(f"[Type Error] Logical operation requires boolean operands, got '{left}' and '{right}'")
        return 'bool'

    def visitUnaryMinusExpr(self, ctx: syntaxParser.UnaryMinusExprContext):
        expr_type = self.visit(ctx.expression())
        if expr_type not in {'int', 'float'}:
            print(f"[Type Error] Unary '-' not applicable to type '{expr_type}'")
        return expr_type

    def visitParenExpr(self, ctx: syntaxParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitNotExpr(self, ctx: syntaxParser.NotExprContext):
        inner_type = self.visit(ctx.expression())
        if inner_type != 'bool':
            print(f"[Type Error] 'not' requires boolean expression, got '{inner_type}'")
        return 'bool'

    # Array literals
    def visitIntArray(self, ctx: syntaxParser.IntArrayContext):
        return 'int[]'

    def visitCharArray(self, ctx: syntaxParser.CharArrayContext):
        return 'char[]'

    def visitStringArray(self, ctx: syntaxParser.StringArrayContext):
        return 'str[]'