from syntaxParser import syntaxParser
from syntaxVisitor import syntaxVisitor
from SymbolTableVisitor import SymbolTableVisitor
from ExpressionAnalyzer import ExpressionAnalyzer

class StatementAnalyzer(syntaxVisitor):
    def __init__(self, symbol_table, expr_analyzer):
        self.symbol_table = symbol_table
        self.expr_analyzer = ExpressionAnalyzer(symbol_table)

    def visitAssignStmt(self, ctx: syntaxParser.AssignStmtContext):
        print(6)
        name = ctx.assignment().IDENTIFIER().getText()
        value_type = self.visit(ctx.assignment().expression())
        symbol = self.symbol_table.lookup(name)
        
        if symbol is None:
            print(f"[Error] Variable '{name}' not declared before assignment.")
        elif symbol['type'] != value_type:
            print(f"[Type Error] Cannot assign '{value_type}' to variable '{name}' of type '{symbol['type']}'")
        return value_type

    def visitVarDeclStmt(self, ctx: syntaxParser.VarDeclStmtContext):
        var_decl = ctx.variable_declaration()
        declared_type = var_decl.DATA_TYPE().getText()
        identifier = var_decl.IDENTIFIER().getText()
        self.symbol_table.define(identifier, {'type': declared_type})  # Record type info in symbol table
        
        if var_decl.expression():
            value_type = self.expr_analyzer.visit(var_decl.expression())
            print("Value:", var_decl.expression().getText(), "Type:", value_type)

            if value_type != declared_type:
                print(f"[Type Error] Mismatched types in declaration of '{identifier}': expected '{declared_type}', got '{value_type}'")

        # return self.visitChildren(ctx) 

    # def visitFuncStmt(self, ctx: syntaxParser.FuncStmtContext):
    #     func_name = ctx.IDENTIFIER().getText()
    #     return_type = ctx.DATA_TYPE().getText() if ctx.DATA_TYPE() else "void"
    #     params = []

    #     if ctx.param_list():
    #         for i in range(len(ctx.param_list().IDENTIFIER())):
    #             pname = ctx.param_list().IDENTIFIER(i).getText()
    #             ptype = ctx.param_list().DATA_TYPE(i).getText()
    #             params.append({'name': pname, 'type': ptype})

    #     self.define(func_name, {
    #         'type': 'function',
    #         'return_type': return_type,
    #         'params': params
    #     })

    #     self.push_scope()
    #     for param in params:
    #         self.symbol_table.define(param['name'], {'type': param['type']})
    #     self.visit(ctx.block())
    #     self.pop_scope()
    #     return None
    
    # def visitReturnStmt(self, ctx: syntaxParser.ReturnStmtContext):
    #     expr_type = self.visit(ctx.expression())
    #     # You can store the expected return type in a stack if nested functions exist
    #     return expr_type

    # def visitType_defStatement(self, ctx: syntaxParser.Type_defStatementContext):
    #     typename = ctx.IDENTIFIER().getText()
    #     fields = {}
    #     # Extract field types and names from the custom type block
    #     for field in ctx.type_def_list():
    #         type_token = field.DATA_TYPE()
    #         if type_token:
    #             type_name = type_token.getText()
    #             name = field.IDENTIFIER().getText()
    #             fields[name] = type_name

    #     # Define the new type in the global scope
    #     self.symbol_table.define(typename, {'type': 'struct', 'fields': fields})
    #     return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx: syntaxParser.If_stmtContext):
        for expr in ctx.expression():
            condition_type = self.expr_analyzer.visit(expr)
            if condition_type != 'bool' or condition_type != syntaxParser.CompExprContext:
                print(f"[Type Error] Condition in if/elif must be 'bool' or comparison expression.")
        # return self.visitChildren(ctx)

    def visitWhile_stmt(self, ctx: syntaxParser.While_stmtContext):
        condition_type = self.expr_analyzer.visit(ctx.expression())
        if condition_type != 'bool' or condition_type != syntaxParser.CompExprContext:
            print(f"[Type Error] While-loop condition must be 'bool' or comparison expression.")
    
    def visitPrintStmt(self, ctx: syntaxParser.PrintStmtContext):
        self.visit(ctx.expression())  # No type requirement for print
        return None

    def visitTryStmt(self, ctx: syntaxParser.TryStmtContext):
        self.visit(ctx.block(0))  # try block
        self.visit(ctx.block(1))  # except block
        return None
