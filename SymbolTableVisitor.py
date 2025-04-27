from antlr4 import *
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class SymbolTableVisitor(syntaxVisitor):
    def __init__(self):
        self.global_scope = {}
        self.scopes = [self.global_scope]

    # Get the current scope from top of stack
    def current_scope(self):
        return self.scopes[-1]

    # Enter a new scope by pushing an empty dictionary onto the stack
    def push_scope(self):
        self.scopes.append({})

    # Exit the current scope
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
