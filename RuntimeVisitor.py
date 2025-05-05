# Fixed RuntimeVisitor.py - with improved array handling
from syntaxParser import syntaxParser
from syntaxVisitor import syntaxVisitor
import sys

class RuntimeVisitor(syntaxVisitor):
    def __init__(self, symbol_table):
        super().__init__()
        self.symbol_table = symbol_table
        self.output = []
        self.in_function = None
        self.return_value = None
        self.function_definitions = {}
        self.collect_function_definitions()
        self.break_flag = False
        self.continue_flag = False
    
    def collect_function_definitions(self):
        """Find and store all function definitions from the symbol table"""
        for scope in self.symbol_table.all_scopes:
            for name, info in scope['symbols'].items():
                if isinstance(info, dict) and info.get('type') == 'function':
                    # Store function definition from global scope
                    self.function_definitions[name] = info
    
    def visitProgram(self, ctx:syntaxParser.ProgramContext):
        # Ensure we're in global scope
        self.symbol_table.reset_to_global()
        
        # Execute each statement at program level
        for stmt in ctx.statement():
            # Skip function definitions during execution
            if isinstance(stmt, syntaxParser.FuncStmtContext):
                continue
                
            if stmt is not None:
                self.visit(stmt)
            
            # Check for flags that might affect execution
            if self.return_value is not None or self.break_flag or self.continue_flag:
                break
            
        return "\n".join(self.output)
    
    def visitVarDeclStmt(self, ctx:syntaxParser.VarDeclStmtContext):
        if ctx is None or ctx.variable_declaration() is None:
            return None
            
        var_decl = ctx.variable_declaration()
        identifier = var_decl.IDENTIFIER().getText()
        data_type = var_decl.DATA_TYPE().getText()
        
        if var_decl.expression():
            value = self.visit(var_decl.expression())
            
            # Handle array types
            if data_type.endswith('[]'):
                if not isinstance(value, list):
                    # Convert single values to a list if assigning to array
                    value = [value]
            
            self.symbol_table.update(identifier, {'type': data_type, 'value': value})
        else:
            # Initialize with default values
            default_value = None
            if data_type == 'int':
                default_value = 0
            elif data_type == 'float':
                default_value = 0.0
            elif data_type == 'str':
                default_value = ""
            elif data_type == 'char':
                default_value = ''
            elif data_type.endswith('[]'):
                default_value = []
            
            self.symbol_table.update(identifier, {'type': data_type, 'value': default_value})
        
        return None
    
    def visitAssignStmt(self, ctx:syntaxParser.AssignStmtContext):
        if ctx is None or ctx.assignment() is None:
            return None
            
        assign = ctx.assignment()
        name = assign.IDENTIFIER().getText()
        
        # Find the variable in the symbol table
        symbol = self.symbol_table.lookup(name)
        if not symbol:
            self.output.append(f"[Runtime Error] Variable '{name}' not defined.")
            return None
        
        # Evaluate expression and update variable
        if assign.expression():
            value = self.visit(assign.expression())
            self.symbol_table.update(name, {'value': value})
        
        return None
    
    def visitPrintStmt(self, ctx:syntaxParser.PrintStmtContext):
        # Get the expression directly
        expr = None
        if ctx.print_stmt() and ctx.print_stmt().expression():
            expr = ctx.print_stmt().expression()
        elif hasattr(ctx, 'expression') and ctx.expression():
            expr = ctx.expression()
        
        if expr:
            # Execute the expression and print the result
            expr_value = self.visit(expr)
            self.output.append(str(expr_value))
        
        return None
    
    def visitFuncStmt(self, ctx:syntaxParser.FuncStmtContext):
        # Just store function definition - this is already done in semantics phase
        return None
    
    # Fixed function call and return handling in RuntimeVisitor
    def visitFuncCallExpr(self, ctx:syntaxParser.FuncCallExprContext):
        if ctx is None or ctx.IDENTIFIER() is None:
            return None
            
        func_name = ctx.IDENTIFIER().getText()
        
        # Lookup function definition
        func_def = self.function_definitions.get(func_name)
        if not func_def:
            self.output.append(f"[Runtime Error] Function '{func_name}' not defined.")
            return None
        
        # Evaluate arguments
        args = []
        if ctx.arg_list():
            for expr_ctx in ctx.arg_list().expression():
                if expr_ctx is not None:
                    arg_value = self.visit(expr_ctx)
                    args.append(arg_value)
        
        # Execute the function and return its value
        return_value = self.execute_function(func_name, args)
        return return_value

    def execute_function(self, func_name, args):
        # Get function info
        func_info = self.function_definitions.get(func_name)
        if not func_info:
            func_info = self.symbol_table.lookup(func_name)
            
        if not func_info or func_info.get("type") != "function":
            self.output.append(f"[Runtime Error] Function '{func_name}' not defined.")
            return None

        # Save current state
        prev_function = self.in_function
        prev_return = self.return_value
        prev_break = self.break_flag
        prev_continue = self.continue_flag
        
        # Set up new function scope
        self.symbol_table.push_scope(f"Call_{func_name}")
        self.in_function = func_name
        self.return_value = None
        self.break_flag = False
        self.continue_flag = False
        
        # Bind arguments to parameters
        params = func_info.get('params', [])
        for i, param in enumerate(params):
            if i < len(args):
                self.symbol_table.define(param['name'], {
                    'type': param['type'],
                    'value': args[i]
                })
            else:
                self.symbol_table.define(param['name'], {
                    'type': param['type'],
                    'value': None
                })
        
        # Execute function body
        if 'body' in func_info:
            self.visit(func_info['body'])
        
        # Get return value and restore state
        return_val = self.return_value
        self.symbol_table.pop_scope()
        self.in_function = prev_function
        self.return_value = prev_return
        self.break_flag = prev_break
        self.continue_flag = prev_continue
        
        return return_val

    def visitReturnStmt(self, ctx:syntaxParser.ReturnStmtContext):
        # Check if inside a function
        if not self.in_function:
            self.output.append("[Runtime Error] Return statement outside function.")
            return None
        
        # Get the expression directly
        expr = None
        if ctx.return_stmt() and ctx.return_stmt().expression():
            expr = ctx.return_stmt().expression()
        elif hasattr(ctx, 'expression') and ctx.expression():
            expr = ctx.expression()
        
        # Set return value
        if expr:
            self.return_value = self.visit(expr)
        else:
            self.return_value = None
            
        return None

    # Make sure the if statement visitor correctly handles conditions and blocks
    def visitIfStmt(self, ctx:syntaxParser.IfStmtContext):
        if ctx is None:
            return None
            
        # Get the if_stmt context
        if_stmt_ctx = ctx.if_stmt()
        if not if_stmt_ctx:
            return None
        
        # Find all expressions (conditions) and blocks
        expressions = []
        blocks = []
        
        for i in range(if_stmt_ctx.getChildCount()):
            child = if_stmt_ctx.getChild(i)
            if isinstance(child, syntaxParser.ExpressionContext):
                expressions.append(child)
            elif isinstance(child, syntaxParser.BlockContext):
                blocks.append(child)
        
        # Evaluate conditions and execute appropriate block
        for i in range(len(expressions)):
            condition = self.visit(expressions[i])
            if condition:
                self.visit(blocks[i])
                return None
        
        # If no conditions matched and there's an else block
        if len(blocks) > len(expressions):
            self.visit(blocks[-1])
        
        return None

    # Add this comprehensive method for handling blocks
    def visitBlock(self, ctx:syntaxParser.BlockContext):
        if ctx is None:
            return None
            
        # Execute each statement in the block
        for stmt in ctx.statement():
            # Skip if the statement is null
            if stmt is None:
                continue
                
            # Visit the statement
            self.visit(stmt)
            
            # Stop execution if we hit a return, break, or continue
            if self.return_value is not None or self.break_flag or self.continue_flag:
                break
                
        return None
    
    def visitWhileStmt(self, ctx:syntaxParser.WhileStmtContext):
        if ctx is None or ctx.while_stmt() is None:
            return None
            
        # Access the while_stmt rule
        while_stmt = ctx.while_stmt()
        
        # Save flags state
        prev_break = self.break_flag
        prev_continue = self.continue_flag
        self.break_flag = False
        self.continue_flag = False
        
        # Execute the while loop
        while True:
            # Evaluate condition
            condition = self.visit(while_stmt.expression())
            if not condition or self.break_flag:
                break
            
            # Execute the body
            self.visit(while_stmt.block())
            
            # Handle continue
            if self.continue_flag:
                self.continue_flag = False
                continue
                
            # Handle return in loop body
            if self.in_function and self.return_value is not None:
                break
        
        # Restore flags
        self.break_flag = prev_break
        self.continue_flag = prev_continue
        
        return None
    
    def visitContinue(self, ctx:syntaxParser.ContinueContext):
        if ctx is None:
            return None
            
        # Set continue flag
        self.continue_flag = True
        return None
    
    def visitBreak(self, ctx:syntaxParser.BreakContext):
        if ctx is None:
            return None
            
        # Set break flag
        self.break_flag = True
        return None
    
    # Improved array handling methods
    
    # Fix for int arrays
    def visitIntArray(self, ctx:syntaxParser.IntArrayContext):
        if ctx is None:
            return None
            
        result = []
        # Get all NUMBER tokens - make sure ctx.NUMBER() is available
        if hasattr(ctx, 'NUMBER') and callable(getattr(ctx, 'NUMBER')):
            number_tokens = ctx.NUMBER()
            for number_token in number_tokens:
                text = number_token.getText()
                # Convert to appropriate numeric type
                if '.' in text:
                    value = float(text)
                else:
                    value = int(text)
                result.append(value)
        else:
            # Alternative approach - parse the array from text directly
            text = ctx.getText()
            if text.startswith('[') and text.endswith(']'):
                content = text[1:-1].strip()
                if content:
                    items = content.split(',')
                    for item in items:
                        num_str = item.strip()
                        if '.' in num_str:
                            result.append(float(num_str))
                        else:
                            result.append(int(num_str))
                            
        return result
    
    # Fix for char arrays
    def visitCharArray(self, ctx:syntaxParser.CharArrayContext):
        if ctx is None:
            return None
                
        # Process character array literals
        result = []
        
        # Get all CHARACTER tokens
        if hasattr(ctx, 'CHARACTER') and callable(getattr(ctx, 'CHARACTER')):
            character_tokens = ctx.CHARACTER()
            for char_token in character_tokens:
                text = char_token.getText()
                # Remove quotes from character literal
                value = text[1:-1]  # Remove the surrounding quotes
                result.append(value)
        else:
            # Alternative approach - parse from text directly
            full_text = ctx.getText()
            # Strip the outer brackets
            if full_text.startswith('[') and full_text.endswith(']'):
                content = full_text[1:-1].strip()
                # Split by commas but respect quoted strings
                if content:
                    parts = []
                    in_quotes = False
                    current = ""
                    for char in content:
                        if char == "'" and (len(current) == 0 or current[-1] != '\\'):
                            in_quotes = not in_quotes
                            if not in_quotes:  # Just exited a quote
                                parts.append(current)
                                current = ""
                            continue
                        elif char == ',' and not in_quotes:
                            # End of an item
                            if current.strip():
                                parts.append(current.strip())
                            current = ""
                        else:
                            current += char
                    
                    # Add the last item if there is one
                    if current.strip():
                        parts.append(current.strip())
                    
                    # Process the parts
                    for part in parts:
                        if part.startswith("'") and part.endswith("'"):
                            result.append(part[1:-1])  # Remove quotes
                        else:
                            result.append(part)
        
        return result
    
    # Fix for string arrays
    def visitStringArray(self, ctx:syntaxParser.StringArrayContext):
        if ctx is None:
            return None
            
        # Process string array literals
        result = []
        
        # Get all STRING tokens
        if hasattr(ctx, 'STRING') and callable(getattr(ctx, 'STRING')):
            string_tokens = ctx.STRING()
            for string_token in string_tokens:
                text = string_token.getText()
                # Remove quotes
                value = text[1:-1]
                result.append(value)
        else:
            # Alternative approach - parse from text directly
            text = ctx.getText()
            if text.startswith('[') and text.endswith(']'):
                content = text[1:-1].strip()
                # Need to handle quoted strings properly
                if content:
                    parts = []
                    in_quotes = False
                    current = ""
                    for char in content:
                        if char == '"' and (len(current) == 0 or current[-1] != '\\'):
                            in_quotes = not in_quotes
                            if not in_quotes:  # Just exited a quote
                                parts.append(current)
                                current = ""
                            continue
                        elif char == ',' and not in_quotes:
                            # End of an item
                            if current.strip():
                                parts.append(current.strip())
                            current = ""
                        else:
                            current += char
                    
                    # Add the last item if there is one
                    if current.strip():
                        parts.append(current.strip())
                    
                    # Process the parts
                    for part in parts:
                        if part.startswith('"') and part.endswith('"'):
                            result.append(part[1:-1])  # Remove quotes
                        else:
                            result.append(part)
                
        return result
        
    def visitArrayAccessExpr(self, ctx:syntaxParser.ArrayAccessExprContext):
        if ctx is None or ctx.IDENTIFIER() is None or ctx.expression() is None:
            return None
            
        # Get array name and index
        array_name = ctx.IDENTIFIER().getText()
        
        # Find the array in symbol table
        symbol = self.symbol_table.lookup(array_name)
        if not symbol:
            self.output.append(f"[Runtime Error] Array '{array_name}' not defined.")
            return None
            
        # Get the array value
        array_value = symbol.get('value', None)
        
        # If it's a string representation of a list, convert it to a proper list
        if isinstance(array_value, str) and array_value.startswith('[') and array_value.endswith(']'):
            try:
                # Parse string format to actual list
                content = array_value[1:-1].strip()
                if not content:  # Empty array
                    array_value = []
                else:
                    # Split by comma and convert elements based on array type
                    items = content.split(',')
                    array_value = []
                    for item in items:
                        item = item.strip()
                        # Try to determine the type
                        if item.startswith("'") and item.endswith("'"):
                            # Char type
                            array_value.append(item[1:-1])
                        elif item.startswith('"') and item.endswith('"'):
                            # String type
                            array_value.append(item[1:-1])
                        else:
                            # Number type
                            try:
                                if '.' in item:
                                    array_value.append(float(item))
                                else:
                                    array_value.append(int(item))
                            except ValueError:
                                # If can't convert to number, keep as is
                                array_value.append(item)
                
                # Update the symbol table
                self.symbol_table.update(array_name, {'value': array_value})
            except Exception as e:
                self.output.append(f"[Runtime Error] Failed to parse array: {str(e)}")
                return None
        
        # Ensure the value is a list
        if not isinstance(array_value, list):
            self.output.append(f"[Runtime Error] Variable '{array_name}' is not an array.")
            return None
            
        # Calculate the index
        index_value = self.visit(ctx.expression())
        if not isinstance(index_value, int):
            self.output.append(f"[Runtime Error] Array index must be an integer, got '{type(index_value).__name__}'.")
            return None
            
        # Check for index out of bounds
        if index_value < 0 or index_value >= len(array_value):
            self.output.append(f"[Runtime Error] Index {index_value} out of bounds for array '{array_name}'.")
            return None
            
        # Return the element at the index
        return array_value[index_value]
    
    def visitIdExpr(self, ctx:syntaxParser.IdExprContext):
        if ctx is None or ctx.IDENTIFIER() is None:
            return None
            
        name = ctx.IDENTIFIER().getText()
        symbol = self.symbol_table.lookup(name)
        
        if not symbol:
            self.output.append(f"[Runtime Error] Variable '{name}' not defined.")
            return None
        
        return symbol.get('value', None)
    
    def visitNumberExpr(self, ctx:syntaxParser.NumberExprContext):
        if ctx is None or ctx.NUMBER() is None:
            return None
            
        text = ctx.NUMBER().getText()
        if '.' in text:
            return float(text)
        else:
            return int(text)
    
    def visitStringExpr(self, ctx:syntaxParser.StringExprContext):
        if ctx is None or ctx.STRING() is None:
            return None
            
        # Remove quotes and handle escape sequences
        text = ctx.STRING().getText()
        return text[1:-1]  # Remove quotes
    
    def visitCharExpr(self, ctx:syntaxParser.CharExprContext):
        if ctx is None or ctx.CHARACTER() is None:
            return None
            
        # Remove quotes and handle escape sequences
        text = ctx.CHARACTER().getText()
        return text[1:-1]  # Remove quotes
    
    def visitTrueExpr(self, ctx:syntaxParser.TrueExprContext):
        if ctx is None:
            return None
        return True
    
    def visitFalseExpr(self, ctx:syntaxParser.FalseExprContext):
        if ctx is None:
            return None
        return False
    
    def visitParenExpr(self, ctx:syntaxParser.ParenExprContext):
        if ctx is None or ctx.expression() is None:
            return None
        return self.visit(ctx.expression())
    
    def visitUnaryMinusExpr(self, ctx:syntaxParser.UnaryMinusExprContext):
        if ctx is None or ctx.unary_expr() is None:
            return None
            
        value = self.visit(ctx.unary_expr())
        if isinstance(value, (int, float)):
            return -value
        else:
            self.output.append("[Runtime Error] Cannot apply unary minus to non-numeric value.")
            return None
    
    def visitNotExpr(self, ctx:syntaxParser.NotExprContext):
        if ctx is None or ctx.expression() is None:
            return None
            
        value = self.visit(ctx.expression())
        return not bool(value)
    
    def visitAddSubExpr(self, ctx:syntaxParser.AddSubExprContext):
        if ctx is None:
            return None
            
        # Handle simple case with just one mul_expr
        if len(ctx.mul_expr()) == 1:
            return self.visit(ctx.mul_expr(0))
            
        left = self.visit(ctx.mul_expr(0))
        right = self.visit(ctx.mul_expr(1))
        op = ctx.getChild(1).getText()
        
        if op == '+':
            # String concatenation
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            # Numeric addition
            elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            else:
                self.output.append("[Runtime Error] Invalid operands for addition.")
                return None
        else:  # op == '-'
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left - right
            else:
                self.output.append("[Runtime Error] Invalid operands for subtraction.")
                return None
    
    def visitMulDivExpr(self, ctx:syntaxParser.MulDivExprContext):
        if ctx is None:
            return None
            
        # Handle simple case with just one unary_expr
        if len(ctx.unary_expr()) == 1:
            return self.visit(ctx.unary_expr(0))
            
        left = self.visit(ctx.unary_expr(0))
        right = self.visit(ctx.unary_expr(1))
        op = ctx.getChild(1).getText()
        
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            self.output.append("[Runtime Error] Invalid operands for multiplication/division.")
            return None
        
        if op == '*':
            return left * right
        else:  # op == '/'
            if right == 0:
                self.output.append("[Runtime Error] Division by zero.")
                return None
            return left / right
    
    def visitCompExpr(self, ctx:syntaxParser.CompExprContext):
        if ctx is None:
            return None
            
        # Get all add_expr children
        add_expressions = ctx.add_expr()
        if not add_expressions or len(add_expressions) == 0:
            return None
            
        # If only one add_expr, just visit it
        if len(add_expressions) == 1:
            return self.visit(add_expressions[0])
        
        # Get comparison operators
        operators = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() in ['<', '<=', '>', '>=', '==', '!=']:
                operators.append(child.getText())
        
        # Evaluate the first expression
        left = self.visit(add_expressions[0])
        
        # Apply operators
        for i in range(len(operators)):
            op = operators[i]
            right = self.visit(add_expressions[i+1])
            
            if op == '<':
                result = left < right
            elif op == '<=':
                result = left <= right
            elif op == '>':
                result = left > right
            elif op == '>=':
                result = left >= right
            elif op == '==':
                result = left == right
            elif op == '!=':
                result = left != right
            else:
                self.output.append(f"[Runtime Error] Unknown comparison operator: {op}")
                return None
                
            # Combine results for chained comparisons
            if i < len(operators) - 1:
                if not result:
                    return False
                left = right
            else:
                return result
                
        return result

    def visitLogicExpr(self, ctx:syntaxParser.LogicExprContext):
        if ctx is None:
            return None
            
        # Get all comp_expr children
        comp_expressions = ctx.comp_expr()
        if not comp_expressions or len(comp_expressions) == 0:
            return None
            
        # If only one comp_expr, just visit it
        if len(comp_expressions) == 1:
            return self.visit(comp_expressions[0])
        
        # Get operators (AND/OR)
        operators = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() in ['and', 'or']:
                operators.append(child.getText())
        
        # Evaluate the first expression
        result = self.visit(comp_expressions[0])
        
        # Apply operators with short-circuit evaluation
        for i in range(len(operators)):
            op = operators[i]
            if op == 'and':
                if not result:
                    return False  # Short-circuit AND
                right = self.visit(comp_expressions[i+1])
                result = result and right
            elif op == 'or':
                if result:
                    return True   # Short-circuit OR
                right = self.visit(comp_expressions[i+1])
                result = result or right
        
        return result
    
    # Default method for any unimplemented visitor methods
    def defaultResult(self):
        return None