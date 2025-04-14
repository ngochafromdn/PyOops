from antlr4 import *
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class SymbolTableVisitor(syntaxVisitor):
    def __init__(self):
        self.global_scope = {}
        self.scopes = [self.global_scope]  # Stack of scopes
        self.current_function = None

    def current_scope(self):
        return self.scopes[-1]

    def push_scope(self):
        self.scopes.append({})
    
    def pop_scope(self):
        self.scopes.pop()

    def define(self, name, value):
        if name in self.current_scope():
            print(f"[Warning] Redeclaration of '{name}' in current scope.")
        self.current_scope()[name] = value

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    # Visit entire program
    def visitProgram(self, ctx: syntaxParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.global_scope

    # Variable declaration
    def visitVarDeclStmt(self, ctx: syntaxParser.VarDeclStmtContext):
        var_decl = ctx.variable_declaration()
        data_type = var_decl.DATA_TYPE() or var_decl.ARR_TYPE().getText()
        identifier = var_decl.IDENTIFIER().getText()
        self.define(identifier, {'type': data_type.getText()})
        return self.visitChildren(ctx)

    # Assignment
    def visitAssignStmt(self, ctx: syntaxParser.AssignStmtContext):
        name = ctx.assignment().IDENTIFIER().getText()
        if not self.lookup(name):
            print(f"[Error] Variable '{name}' assigned before declaration.")
        return self.visitChildren(ctx)

    # New type definition (struct-like)
    def visitNewTypeDef(self, ctx: syntaxParser.NewTypeDefContext):
        typename = ctx.IDENTIFIER().getText()
        fields = {}
        for field in ctx.children:
            if hasattr(field, 'DATA_TYPE') or hasattr(field, 'ARR_TYPE'):
                type_token = field.DATA_TYPE() or field.ARR_TYPE()
                if type_token:
                    type_name = type_token.getText()
                    name = field.IDENTIFIER().getText()
                    fields[name] = type_name
        self.define(typename, {'type': 'struct', 'fields': fields})
        return self.visitChildren(ctx)

    # Function definition
    def visitFuncStmt(self, ctx: syntaxParser.FuncStmtContext):
        func_name = ctx.IDENTIFIER().getText()
        return_type = ctx.DATA_TYPE().getText() if ctx.DATA_TYPE() else 'void'
        params = []

        if ctx.param_list():
            for i in range(len(ctx.param_list().IDENTIFIER())):
                param_name = ctx.param_list().IDENTIFIER(i).getText()
                param_type = ctx.param_list().DATA_TYPE(i).getText()
                params.append({'name': param_name, 'type': param_type})

        self.define(func_name, {
            'type': 'function',
            'return_type': return_type,
            'params': params
        })

        # Enter function scope
        self.push_scope()
        for param in params:
            self.define(param['name'], {'type': param['type']})
        self.visit(ctx.block())
        self.pop_scope()
        return None

    # Block (new scope)
    def visitBlockStmt(self, ctx: syntaxParser.BlockStmtContext):
        self.push_scope()
        self.visit(ctx.block())
        self.pop_scope()
        return None

    # If, While, Try blocks all open new scopes
    def visitIfStmt(self, ctx: syntaxParser.IfStmtContext):
        self.visit(ctx.expression())
        self.visit(ctx.block(0))
        if ctx.ELSE():
            self.visit(ctx.block(-1))
        return None

    def visitWhileStmt(self, ctx: syntaxParser.WhileStmtContext):
        self.visit(ctx.expression())
        self.visit(ctx.block())
        return None

    def visitTryStmt(self, ctx: syntaxParser.TryStmtContext):
        self.visit(ctx.block(0))  # try block
        self.visit(ctx.except_clause().block())  # except block
        return None
