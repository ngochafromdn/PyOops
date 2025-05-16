import sys
import os
import argparse
import readline  # Adds command history and editing capabilities
from antlr4 import *
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser
from SyntaxErrorHandling import SyntaxErrorHandling
from SymbolTableVisitor import SymbolTableVisitor
from StatementAnalyzer import StatementAnalyzer
from RuntimeVisitor import RuntimeVisitor

class LanguageCommander:
    def __init__(self):
        self.symbol_table = SymbolTableVisitor()
        self.symbol_table.define("get_error", {"type": "str"})
        
    def execute_string(self, code_string, show_output=True, debug=False):
        """Execute code from a string"""
        input_stream = InputStream(code_string)
        
        # Setup lexer and parser
        lexer = syntaxLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = syntaxParser(token_stream)
        
        # Add error listener
        error_listener = SyntaxErrorHandling()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        try:
            # Parse
            tree = parser.program()
            
            if error_listener.error_count > 0:
                if show_output:
                    print(f"Found {error_listener.error_count} syntax errors. Execution skipped.")
                return None
                
            # Semantic analysis
            analyzer = StatementAnalyzer(self.symbol_table)
            analyzer.visit(tree)
            
            if debug and show_output:
                print("\nSymbol Table:")
                self.symbol_table.printSymbols()
            
            # Execute
            executor = RuntimeVisitor(self.symbol_table)
            output = executor.visit(tree)
            
            if show_output:
                print(output)
                
            return output
            
        except Exception as e:
            if show_output:
                print(f"Execution error: {e}")
            return None
    
    def execute_file(self, filepath, debug=False):
        """Execute code from a file"""
        try:
            with open(filepath, 'r') as f:
                code = f.read()
                
            print(f"Executing file: {filepath}")
            print("=== Program Output ===")
            self.execute_string(code, debug=debug)
            print("=== End of Output ===")
            
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
        except Exception as e:
            print(f"Error: {e}")
            
    def start_repl(self, debug=False):
        """Start an interactive REPL (Read-Eval-Print Loop)"""
        print(f"Interactive Pyoops Language Mode - Type 'exit()' to quit, 'help()' for commands")
        
        # Setup readline with history file
        history_file = os.path.expanduser('~/.pi_language_history')
        try:
            readline.read_history_file(history_file)
            readline.set_history_length(1000)
        except FileNotFoundError:
            pass
            
        # Main REPL loop
        while True:
            try:
                user_input = input("pi> ")
                
                # Check if command is a run() command
                if user_input.startswith('run(') and user_input.endswith(')'):
                    # Extract filename between the parentheses
                    filename = user_input[4:-1].strip().strip('"\'')
                    if filename:
                        self.execute_file(filename, debug=debug)
                    else:
                        print("Error: Missing filename. Usage: run(\"filename.pi\")")
                    continue
                    
                # Check if command is a load() command (loads but doesn't execute)
                elif user_input.startswith('load(') and user_input.endswith(')'):
                    # Extract filename between the parentheses
                    filename = user_input[5:-1].strip().strip('"\'')
                    if filename:
                        try:
                            with open(filename, 'r') as f:
                                code = f.read()
                                print(f"Loaded file: {filename}")
                                print("Type 'run_loaded()' to execute the loaded code")
                                self._loaded_code = code
                        except FileNotFoundError:
                            print(f"Error: File '{filename}' not found.")
                        except Exception as e:
                            print(f"Error loading file: {e}")
                    else:
                        print("Error: Missing filename. Usage: load(\"filename.pi\")")
                    continue
                    
                # Execute loaded code
                elif user_input.strip() == 'run_loaded()':
                    if hasattr(self, '_loaded_code') and self._loaded_code:
                        print("=== Executing loaded code ===")
                        self.execute_string(self._loaded_code, debug=debug)
                        print("=== End of execution ===")
                    else:
                        print("No code has been loaded. Use load(\"filename.pi\") first.")
                    continue
                    
                # Handle other special commands
                elif user_input.lower() == 'exit()':
                    break
                elif user_input.lower() == 'help()':
                    self._print_help()
                    continue
                elif user_input.lower() == 'clear()':
                    self.symbol_table = SymbolTableVisitor()
                    self.symbol_table.define("get_error", {"type": "str"})
                    print("Symbol table cleared.")
                    continue
                elif user_input.lower() == 'symbols()':
                    self.symbol_table.printSymbols()
                    continue
                elif user_input.strip() == '':
                    continue
                    
                # Execute the code
                self.execute_string(user_input, debug=debug)
                
            except KeyboardInterrupt:
                print("\nPress Ctrl+D or type 'exit()' to exit")
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                
        # Save history on exit
        try:
            readline.write_history_file(history_file)
        except:
            pass
            
        print("Goodbye!")
        
    def _print_help(self):
        """Print help information for the REPL"""
        help_text = """
Available commands:
  exit()      - Exit the interactive mode
  help()      - Show this help message
  clear()     - Clear the symbol table (reset variables)
  symbols()   - Print current symbol table contents
  
You can also enter any valid Pi language code for immediate execution.
        """
        print(help_text)

def main():
    # Setup command line argument parser
    parser = argparse.ArgumentParser(description='Pi Language Commander and Interpreter')
    parser.add_argument('file', nargs='?', help='File to execute (.pi extension)')
    parser.add_argument('-i', '--interactive', action='store_true', help='Start interactive mode')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
    parser.add_argument('-v', '--version', action='store_true', help='Show version information')
    
    args = parser.parse_args()
    
    # Create commander instance
    commander = LanguageCommander()
    
    if args.version:
        print("Pyoops Language Commander v1.0.0")
        return
    
    # Kiểm tra file extension
    if args.file:
        if not args.file.endswith('.pi'):
            print(f"Warning: File {args.file} does not have the standard .pi extension")
            proceed = input("Do you want to proceed? (y/n): ")
            if proceed.lower() != 'y':
                return
        
        commander.execute_file(args.file, debug=args.debug)
        
        # Start interactive mode after file execution if requested
        if args.interactive:
            commander.start_repl(debug=args.debug)
    
    # Start interactive mode if no file or explicitly requested
    elif args.interactive or not args.file:
        commander.start_repl(debug=args.debug)
    
if __name__ == "__main__":
    main()