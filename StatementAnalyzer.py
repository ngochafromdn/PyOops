from syntaxParser import syntaxParser
from syntaxVisitor import syntaxVisitor
from ExpressionAnalyzer import ExpressionAnalyzer
import logging
import sys

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s')) 
logger.addHandler(handler)
logger.propagate = False

# ANSI color codes
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Helper function for colorized error reporting
def report_error(line, column, message, error_type="Error"):
    formatted_error = f"{RED}{BOLD}[{error_type}]{RESET}{RED} Line {line}:{column} - {message}{RESET}"
    print(formatted_error)
    sys.exit(1)

class StatementAnalyzer(syntaxVisitor):
    def __init__(self, symbol_table):
        super().__init__()
        self.symbol_table = symbol_table
        self.expr_analyzer = ExpressionAnalyzer(symbol_table)
        self.current_function = None
        self.in_loop = False

    def visitProgram(self, ctx:syntaxParser.ProgramContext):
        self.symbol_table.reset_to_global()
        for stmt in ctx.statement():
            self.visit(stmt)
        return None
    
    def visitBlockStmt(self, ctx:syntaxParser.BlockStmtContext):
        # Create a new scope for block
        self.symbol_table.push_scope("Block")
        for stmt in ctx.block().statement():
            self.visit(stmt)
        self.symbol_table.pop_scope()
        return None
    
    def visitAssignStmt(self, ctx:syntaxParser.AssignStmtContext):
        line = ctx.start.line
        column = ctx.start.column
        
        assign = ctx.assignment()
        
        # Variable assignment
        if assign.IDENTIFIER():
            name = assign.IDENTIFIER().getText()
            symbol = self.symbol_table.lookup(name)
            
            if symbol is None:
                message = f"Variable '{name}' not declared before assignment."
                report_error(line, column, message)
            
            if assign.expression():
                value_type = self.expr_analyzer.visit(assign.expression())
                if value_type != symbol['type'] and value_type is not None:
                    message = f"Mismatched types in assignment of '{name}': expected '{symbol['type']}', got '{value_type}'"
                    report_error(line, column, message, "Type Error")
                else:
                    self.symbol_table.update(name, {'value': assign.expression().getText()})
        
        # Typedef assignment
        elif assign.type_defVar():
            newtype_name = assign.type_defVar().IDENTIFIER(0).getText()
            field_name = assign.type_defVar().IDENTIFIER(1).getText()

            newtype = self.symbol_table.lookup(newtype_name)
            if not newtype or newtype.get('kind') != 'newtype_instance':
                message = f"'{newtype_name}' is not a declared new-type instance."
                report_error(line, column, message)

            if field_name not in newtype['fields']:
                message = f"Field '{field_name}' not found in new-type instance '{newtype_name}'."
                report_error(line, column, message)

            expected_type = newtype['fields'][field_name]['type']
            value_type = self.expr_analyzer.visit(assign.expression())
            
            if expected_type != value_type:
                message = f"Mismatched types in field assignment '{newtype_name}.{field_name}': expected '{expected_type}', got '{value_type}'"
                report_error(line, column, message, "Type Error")
            else:
                self.symbol_table.updateField_typedef(newtype_name, field_name, assign.expression().getText())
        
        return None

    def visitVarDeclStmt(self, ctx: syntaxParser.VarDeclStmtContext):
        line = ctx.start.line
        column = ctx.start.column
        var_decl = ctx.variable_declaration()
        declared_type = var_decl.DATA_TYPE().getText()
        identifier = var_decl.IDENTIFIER().getText()

        try:
            self.symbol_table.define(identifier, {'type': declared_type, 'value': None}, line, column)
        except ValueError as e:
            # Extract the error message from the exception
            message = str(e)
            if "[Error]" in message:
                # Remove the prefix if it exists
                message = message.split(": ", 1)[1] if ": " in message else message
            report_error(line, column, message)
            return None
        
        if var_decl.expression():
            evaluated_type = self.expr_analyzer.visit(var_decl.expression())
            if evaluated_type is not None:
                if evaluated_type == declared_type or (declared_type.endswith('[]') and evaluated_type == declared_type[:-2]):
                    self.symbol_table.update(identifier, {'value': var_decl.expression().getText()})
                else:
                    message = f"Mismatched types in declaration of '{identifier}': expected '{declared_type}', got '{evaluated_type}'"
                    report_error(line, column, message, "Type Error")
            else:
                message = f"Invalid expression in variable declaration."
                report_error(line, column, message)
        return None

    def visitFuncStmt(self, ctx: syntaxParser.FuncStmtContext):
        line = ctx.start.line
        column = ctx.start.column
        
        func_name = ctx.IDENTIFIER().getText()
        return_type = ctx.DATA_TYPE().getText() if ctx.DATA_TYPE() else 'void'
        
        if self.symbol_table.lookup(func_name):
            message = f"Function '{func_name}' already defined."
            report_error(line, column, message)
            return None
        
        # Rest of the method remains unchanged
        params = []
        if ctx.param_list():
            param_types = ctx.param_list().DATA_TYPE()
            param_names = ctx.param_list().IDENTIFIER()
            
            for i in range(len(param_types)):
                param_type = param_types[i].getText()
                param_name = param_names[i].getText()
                params.append({'type': param_type, 'name': param_name})
        
        self.symbol_table.reset_to_global()
        self.symbol_table.define(func_name, {
            'type': 'function',
            'return_type': return_type,
            'params': params,
            'body': ctx.block()
        }, line, column)
        
        old_function = self.current_function
        self.current_function = func_name
        
        self.symbol_table.push_scope(f"Function {func_name}")
        for param in params:
            self.symbol_table.define(param['name'], {'type': param['type'], 'value': None})
        
        self.visit(ctx.block())
        
        self.symbol_table.pop_scope()
        self.current_function = old_function
        
        return None

    def visitType_defDeclaration(self, ctx: syntaxParser.Type_defDeclarationContext):
        line = ctx.start.line
        column = ctx.start.column

        newtype_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()

        newtypedef = self.symbol_table.lookup(newtype_name)

        if (not newtypedef) or (newtypedef.get('type') != 'typedef') :
            message = f"New type {newtype_name} is not declared."
            report_error(line, column, message)

        if self.symbol_table.lookup(var_name):
            message = f"New-type field '{var_name}' is redeclared."
            report_error(line, column, message)

        instance_fields = {}
        for field_name, field_type in newtypedef['fields'].items():
            instance_fields[field_name] = {'type': field_type, 'value': None}

        self.symbol_table.define(var_name, {
            'type': newtype_name,
            'kind': 'newtype_instance',
            'fields': instance_fields
        })
        
        return None

    def visitType_defStatement(self, ctx:syntaxParser.Type_defStatementContext):
        line = ctx.start.line
        column = ctx.start.column

        newtype_name = ctx.IDENTIFIER().getText()
        newtype_fields = {}

        if self.symbol_table.lookup(newtype_name):
            message = f"New type '{newtype_name}' has been already declared."
            report_error(line, column, message)

        for field in ctx.type_def_list():
            datatype_field = field.DATA_TYPE()
            if datatype_field:
                data_type = datatype_field.getText()
                name = field.IDENTIFIER().getText()

                if name in newtype_fields:
                    message = f"Field '{name}' is redeclared in new type '{newtype_name}'."
                    report_error(field.IDENTIFIER().symbol.line, field.IDENTIFIER().symbol.column, message)

                newtype_fields[name] = data_type

        self.symbol_table.define(newtype_name, {'type': 'typedef', 'fields': newtype_fields})

        return None
    
    def visitPrintStmt(self, ctx: syntaxParser.PrintStmtContext):
        line = ctx.start.line
        column = ctx.start.column
        
        # Direct access the expression
        expr = ctx.print_stmt().expression()
        
        if not expr:
            message = f"Print statement requires an expression."
            report_error(line, column, message)
            return None

        expr_type = self.expr_analyzer.visit(expr)
        if expr_type is None:
            message = f"Invalid expression in print statement."
            report_error(line, column, message, "Type Error")
        return None

    def visitReturnStmt(self, ctx: syntaxParser.ReturnStmtContext):
        line = ctx.start.line
        column = ctx.start.column
        
        if not self.current_function:
            message = f"Return statement outside of function."
            report_error(line, column, message)
            return None
        
        func_info = self.symbol_table.lookup(self.current_function)
        if not func_info:
            message = f"Cannot find function '{self.current_function}'."
            report_error(line, column, message)
            return None
        
        return_type = func_info.get('return_type', 'void')
        
        # Access the expression
        expr = ctx.return_stmt().expression() if hasattr(ctx, 'return_stmt') and ctx.return_stmt() else None
        if not expr:
            # If no expression but non-void function
            if return_type != 'void':
                message = f"Missing return value for non-void function '{self.current_function}'."
                report_error(line, column, message, "Type Error")
            return None
            
        # Check expression type
        expr_type = self.expr_analyzer.visit(expr)
        if return_type == 'void':
            message = f"Cannot return a value from a void function."
            report_error(line, column, message, "Type Error")
        elif expr_type != return_type:
            message = f"Return type mismatch: expected '{return_type}', got '{expr_type}'."
            report_error(line, column, message, "Type Error")            
        return None

    def visitIfStmt(self, ctx: syntaxParser.IfStmtContext):
        # Extract and analyze condition from if_stmt rule
        if_stmt_ctx = ctx.if_stmt()
        if not if_stmt_ctx:
            return None
            
        # Check all expressions in the if-else chain
        for i in range(if_stmt_ctx.getChildCount()):
            child = if_stmt_ctx.getChild(i)
            if isinstance(child, syntaxParser.ExpressionContext):
                condition_type = self.expr_analyzer.visit(child)
                if condition_type != 'bool':
                    line = child.start.line
                    column = child.start.column
                    message = f"If condition must be boolean, got '{condition_type}'"
                    report_error(line, column, message, "Type Error")

        # Visit all blocks
        for i in range(if_stmt_ctx.getChildCount()):
            child = if_stmt_ctx.getChild(i)
            if isinstance(child, syntaxParser.BlockContext):
                self.symbol_table.push_scope("If Block")
                self.visit(child)
                self.symbol_table.pop_scope()
                
        return None

    def visitWhileStmt(self, ctx: syntaxParser.WhileStmtContext):
        if not ctx.while_stmt():
            return None
            
        while_stmt_ctx = ctx.while_stmt()
        line = ctx.start.line
        column = ctx.start.column
        
        # Check the condition directly
        expr = while_stmt_ctx.expression()
        if expr:
            condition_type = self.expr_analyzer.visit(expr)
            if condition_type != 'bool':
                message = f"While condition must be boolean, got '{condition_type}'"
                report_error(line, column, message, "Type Error")
                
        # Set loop flag and visit the block
        old_in_loop = self.in_loop
        self.in_loop = True
        
        block = while_stmt_ctx.block()
        if block:
            self.symbol_table.push_scope("While Loop")
            self.visit(block)
            self.symbol_table.pop_scope()
        
        self.in_loop = old_in_loop
        return None
    
    def visitContinue(self, ctx: syntaxParser.ContinueContext):
        line = ctx.start.line
        column = ctx.start.column
        
        if not self.in_loop:
            message = f"Continue statement outside of loop."
            report_error(line, column, message)
        return None

    def visitBreak(self, ctx: syntaxParser.BreakContext):
        line = ctx.start.line
        column = ctx.start.column
        
        if not self.in_loop:
            message = f"Break statement outside of loop."
            report_error(line, column, message)
        return None
    
    def visitArrayAccessExpr(self, ctx: syntaxParser.ArrayAccessExprContext):
        line = ctx.start.line
        column = ctx.start.column
        
        array_name = ctx.IDENTIFIER().getText()
        array_info = self.symbol_table.lookup(array_name)
        
        if not array_info:
            message = f"Undefined array '{array_name}'"
            report_error(line, column, message)
            return None
            
        array_type = array_info.get('type', '')
        if not array_type.endswith('[]'):
            message = f"Variable '{array_name}' is not an array"
            report_error(line, column, message)
            return None
            
        # Check the index expression
        index_type = self.expr_analyzer.visit(ctx.expression())
        if index_type != 'int':
            message = f"Array index must be an integer, got '{index_type}'"
            report_error(line, column, message, "Type Error")
            return None
            
        # Return the element type
        return array_type[:-2]  # Remove the [] suffix