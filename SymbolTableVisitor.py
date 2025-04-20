from antlr4 import *
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class SymbolTableVisitor(syntaxVisitor):
    def __init__(self):
        # Initialize the global symbol table (top-level scope)
        self.global_scope = {}
        # Stack to keep track of nested scopes (functions, blocks, etc.)
        self.scopes = [self.global_scope]
        self.current_function = None

    # Utility: Get the current scope from top of stack
    def current_scope(self):
        return self.scopes[-1]

    # Utility: Enter a new scope by pushing an empty dictionary onto the stack
    def push_scope(self):
        self.scopes.append({})

    # Utility: Exit the current scope
    def pop_scope(self):
        self.scopes.pop()

    # Define a new symbol in the current scope
    def define(self, name, value):
        if name in self.current_scope():
            print(f"[Warning] Redeclaration of '{name}' in current scope.")
        self.current_scope()[name] = value

    # Lookup a symbol from the top scope down to the global
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    # Visit the entire program (entry point)
    def visitProgram(self, ctx: syntaxParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)  # Visit each top-level statement
        return self.global_scope

    # Visit a variable declaration statement
    def visitVarDeclStmt(self, ctx: syntaxParser.VarDeclStmtContext):
        var_decl = ctx.variable_declaration()
        data_type_token = var_decl.DATA_TYPE() 
        data_type = data_type_token.getText() if data_type_token else "unknown"
        identifier = var_decl.IDENTIFIER().getText()
        self.define(identifier, {'type': data_type})  # Record type info in symbol table
        return self.visitChildren(ctx)

    # Visit an assignment statement
    def visitAssignStmt(self, ctx: syntaxParser.AssignStmtContext):
        name = ctx.assignment().IDENTIFIER().getText()
        if not self.lookup(name):
            print(f"[Error] Variable '{name}' assigned before declaration.")
        return self.visitChildren(ctx)

    # Visit a new type definition (e.g., struct definition)
    def visitType_defStatement(self, ctx: syntaxParser.Type_defStatementContext):
        typename = ctx.IDENTIFIER().getText()
        fields = {}

        # Extract field types and names from the custom type block
        for field in ctx.type_def_list():
            type_token = field.DATA_TYPE()
            if type_token:
                type_name = type_token.getText()
                name = field.IDENTIFIER().getText()
                fields[name] = type_name

        # Define the new type in the global scope
        self.define(typename, {'type': 'struct', 'fields': fields})
        return self.visitChildren(ctx)

    # Visit a function definition
    def visitFuncStmt(self, ctx: syntaxParser.FuncStmtContext):
        func_name = ctx.IDENTIFIER().getText()
        return_type = ctx.DATA_TYPE().getText() if ctx.DATA_TYPE() else 'void'
        params = []

        # Extract parameters (name and type)
        if ctx.param_list():
            for i in range(len(ctx.param_list().IDENTIFIER())):
                param_name = ctx.param_list().IDENTIFIER(i).getText()
                param_type = ctx.param_list().DATA_TYPE(i).getText()
                params.append({'name': param_name, 'type': param_type})

        # Record function signature in the symbol table
        self.define(func_name, {
            'type': 'function',
            'return_type': return_type,
            'params': params
        })

        # Create new scope for function body
        self.push_scope()

        # Add parameters to the function scope
        for param in params:
            self.define(param['name'], {'type': param['type']})

        # Visit the function body block
        self.visit(ctx.block())

        # Exit function scope
        self.pop_scope()
        return None

    # Visit a block (surrounded by braces), which opens a new scope
    def visitBlockStmt(self, ctx: syntaxParser.BlockStmtContext):
        self.push_scope()
        self.visit(ctx.block())
        self.pop_scope()
        return None

    # Visit a conditional if-elseif-else structure
    def visitIf_stmt(self, ctx: syntaxParser.If_stmtContext):
        expressions = ctx.expression()
        blocks = ctx.block()

        # Visit 'if' condition and block
        self.visit(expressions[0])
        self.visit(blocks[0])

        # Visit any 'else-if' conditions and blocks
        for i in range(1, len(expressions)):
            self.visit(expressions[i])
            self.visit(blocks[i])

        # Visit optional 'else' block
        if len(blocks) > len(expressions):
            self.visit(blocks[-1])
        return None

    # Visit a while-loop
    def visitWhile_stmt(self, ctx: syntaxParser.While_stmtContext):
        self.visit(ctx.expression())  # Visit loop condition
        self.visit(ctx.block())       # Visit loop body
        return None

    # Visit a try-except block
    def visitTry_Stmt(self, ctx: syntaxParser.TryStmtContext):
        blocks = ctx.block()
        # try_block = ctx.block(0)
        # except_block = ctx.block(1)

        print("👉 Executing try block:")
        self.visit(blocks[0])  # Visit the try block

        print("👉 Exception caught, executing except block:")
        self.visit(blocks[1])  # Visit the except block

        return None

    # Print all defined symbols for debugging
    def printSymbols(self):
        print("Global Scope:")
        self.print_scope(self.global_scope)

        for idx, scope in enumerate(self.scopes[1:], 1):
            print(f"Scope {idx}:")
            self.print_scope(scope)

        print("Debugging scopes:")
        for idx, scope in enumerate(self.scopes):
            print(f"Scope {idx} contents: {scope}")

    # Helper: Print a single scope
    def print_scope(self, scope):
        if not scope:
            print("  (empty scope)")
        else:
            for name, value in scope.items():
                print(f"  {name}: {value}")
