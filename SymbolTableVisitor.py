from antlr4 import *
from syntaxVisitor import syntaxVisitor
from syntaxParser import syntaxParser

class SymbolTableVisitor(syntaxVisitor):
    def __init__(self):
        self.global_scope = {}
        self.scopes = [self.global_scope]
        self.all_scopes = [{'name': 'Global', 'symbols': self.global_scope}]
        self.current_function = None

    @property
    def current_scope(self):
        return self.scopes[-1]

    def push_scope(self, scope_name="Anonymous"):
        new_scope = {}
        self.scopes.append(new_scope)
        self.all_scopes.append({'name': scope_name, 'symbols': new_scope})

    def pop_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def reset_to_global(self):
        while len(self.scopes) > 1:
            self.pop_scope()

    def define(self, name, value, line=None, column=None):
        if name in self.current_scope:
            raise ValueError(f"[Error] Line {line}, Column {column}: Redeclaration of '{name}' in current scope.")
        self.current_scope[name] = value

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def update(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                if isinstance(scope[name], dict):
                    if isinstance(value, dict):
                        scope[name].update(value)
                    else:
                        scope[name]['value'] = value
                else:
                    scope[name] = value
                return True
        return False

    def updateField_typedef(self, instance_name, field_name, value):
        for scope in reversed(self.scopes):
            if instance_name in scope:
                instance = scope[instance_name]
                if isinstance(instance, dict) and 'fields' in instance:
                    if field_name in instance['fields']:
                        instance['fields'][field_name]['value'] = value
                        return True
        return False
    
    def printSymbols(self):
        print("=== Symbol Table ===")
        for scope in self.all_scopes:
            print(f"{scope['name']} Scope:")
            if not scope['symbols']:
                print("  (empty scope)")
            else:
                for name, value in scope['symbols'].items():
                    print(f"  {name}: {value}")

    def define_function(self, name, return_type, param_list, body_ctx):
        if name in self.global_scope:
            raise ValueError(f"Function '{name}' already defined.")

        self.global_scope[name] = {
            "type": "function",
            "return_type": return_type,
            "params": [{"type": t, "name": n} for t, n in param_list],
            "body": body_ctx
        }

