"""
Interactive command-line interface for the language interpreter.

This script provides a more advanced interface for the language, including:
1. A REPL (Read-Eval-Print Loop) for interactive coding
2. File execution capabilities
3. Command history and special commands
4. Debug output options
"""
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

# Terminal colors for better output formatting
CYAN_BOLD = "\033[1;36m"  
RESET = "\033[0m"         

class LanguageCommander:
    """
    Main class that handles executing code, both from files and interactively.
    Maintains a persistent symbol table across executions in the same session.
    """
    def __init__(self):
        """Initialize the commander with a fresh symbol table."""
        self.symbol_table = SymbolTableVisitor()
        # Register built-in functions
        self.symbol_table.define("get_error", {"type": "str"})
        
    def execute_string(self, code_string, show_output=True, debug=False):
        """
        Execute code from a string input.
        
        Args:
            code_string: Source code as a string
            show_output: Whether to print execution output
            debug: Whether to show debug information
            
        Returns:
            The output of the program, or None if execution failed
        """
        input_stream = InputStream(code_string)
        
        # Step 1: Setup lexer and parser
        lexer = syntaxLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = syntaxParser(token_stream)
        
        # Step 2: Configure error handling
        error_listener = SyntaxErrorHandling()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        try:
            # Step 3: Parse the input
            tree = parser.program()
            
            # Check for syntax errors
            if error_listener.error_count > 0:
                if show_output:
                    print(f"Found {error_listener.error_count} syntax errors. Execution skipped.")
                return None
                
            # Step 4: Perform semantic analysis
            analyzer = StatementAnalyzer(self.symbol_table)
            analyzer.visit(tree)
            
            # Show symbol table in debug mode
            if debug and show_output:
                print("\nSymbol Table:")
                self.symbol_table.printSymbols()
            
            # Step 5: Execute the code
            executor = RuntimeVisitor(self.symbol_table)
            output = executor.visit(tree)
            
            # Display output if requested
            if show_output:
                print(output)
                
            return output
            
        except Exception as e:
            if show_output:
                print(f"Execution error: {e}")
            return None
    
    def execute_file(self, filepath, debug=False):
        """
        Execute code from a file.
        
        Args:
            filepath: Path to the source code file
            debug: Whether to show debug information
        """
        try:
            # Read the entire file content
            with open(filepath, 'r') as f:
                code = f.read()
                
            print(f"Executing file: {filepath}")
            print(f"{CYAN_BOLD}=== Program Output ==={RESET}")
            self.execute_string(code, debug=debug)
            print(f"{CYAN_BOLD}=== End of Output ==={RESET}")
            
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
        except Exception as e:
            print(f"Error: {e}")
            
    def start_repl(self, debug=False):
        """
        Start an interactive REPL (Read-Eval-Print Loop) session.
        
        Args:
            debug: Whether to show debug information
        """
        print(f"Interactive Pyoops Language Mode - Type 'exit()' to quit, 'help()' for commands")
        
        # Setup readline with history file for command history
        history_file = os.path.expanduser('~/.bibi_language_history')
        try:
            readline.read_history_file(history_file)
            readline.set_history_length(1000)  # Limit history to 1000 entries
        except FileNotFoundError:
            # No existing history file, will create one on exit
            pass
            
        # Main REPL loop
        while True:
            try:
                # Get user input with a prompt
                user_input = input("bibi> ")
                
                # --- Special commands handling ---
                
                # Execute a file: run("filename.bibi")
                if user_input.startswith('run(') and user_input.endswith(')'):
                    # Extract filename between the parentheses
                    filename = user_input[4:-1].strip().strip('"\'')
                    if filename:
                        self.execute_file(filename, debug=debug)
                    else:
                        print("Error: Missing filename. Usage: run(\"filename.bibi\")")
                    continue
                    
                # Load a file without executing: load("filename.bibi")
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
                        print("Error: Missing filename. Usage: load(\"filename.bibi\")")
                    continue
                    
                # Execute previously loaded code
                elif user_input.strip() == 'run_loaded()':
                    if hasattr(self, '_loaded_code') and self._loaded_code:
                        print("=== Executing loaded code ===")
                        self.execute_string(self._loaded_code, debug=debug)
                        print("=== End of execution ===")
                    else:
                        print("No code has been loaded. Use load(\"filename.bibi\") first.")
                    continue
                    
                # Other REPL commands
                elif user_input.lower() == 'exit()':
                    # Exit the REPL
                    break
                elif user_input.lower() == 'help()':
                    # Show available commands
                    self._print_help()
                    continue
                elif user_input.lower() == 'clear()':
                    # Reset the symbol table (clear all variables)
                    self.symbol_table = SymbolTableVisitor()
                    self.symbol_table.define("get_error", {"type": "str"})
                    print("Symbol table cleared.")
                    continue
                elif user_input.lower() == 'symbols()':
                    # Display current symbol table contents
                    self.symbol_table.printSymbols()
                    continue
                elif user_input.strip() == '':
                    # Skip empty input
                    continue
                    
                # If not a special command, execute as code
                self.execute_string(user_input, debug=debug)
                
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\nPress Ctrl+D or type 'exit()' to exit")
            except EOFError:
                # Handle Ctrl+D (EOF) by exiting
                break
            except Exception as e:
                # Catch any other exceptions to keep the REPL running
                print(f"Error: {e}")
                
        # Save command history on exit
        try:
            readline.write_history_file(history_file)
        except:
            # Failed to save history, but not critical
            pass
            
        print("Goodbye!")
        
    def _print_help(self):
        """Print help information for the REPL's special commands."""
        help_text = """
Available commands:
  exit()      - Exit the interactive mode
  help()      - Show this help message
  clear()     - Clear the symbol table (reset variables)
  symbols()   - Print current symbol table contents
  run("file") - Execute code from a file
  load("file")- Load code from a file without executing
  run_loaded()- Execute previously loaded code
  
You can also enter any valid bibi language code for immediate execution.
        """
        print(help_text)

def main():
    """
    Main entry point: Parse command-line arguments and start
    the appropriate mode (file execution or interactive REPL).
    """
    # Setup command line argument parser
    parser = argparse.ArgumentParser(description='Bibi Language Commander and Interpreter')
    parser.add_argument('file', nargs='?', help='File to execute (.bibi extension)')
    parser.add_argument('-i', '--interactive', action='store_true', help='Start interactive mode')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
    parser.add_argument('-v', '--version', action='store_true', help='Show version information')
    
    args = parser.parse_args()
    
    # Create commander instance
    commander = LanguageCommander()
    
    # Display version information if requested
    if args.version:
        print("Pyoops Language Commander v1.0.0")
        return
    
    # Check file extension if a file is specified
    if args.file:
        if not args.file.endswith('.bibi'):
            print(f"Warning: File {args.file} does not have the standard .bibi extension")
            proceed = input("Do you want to proceed? (y/n): ")
            if proceed.lower() != 'y':
                return
        
        # Execute the specified file
        commander.execute_file(args.file, debug=args.debug)
        
        # Start interactive mode after file execution if requested
        if args.interactive:
            commander.start_repl(debug=args.debug)
    
    # Start interactive mode if no file or explicitly requested
    elif args.interactive or not args.file:
        commander.start_repl(debug=args.debug)
    
if __name__ == "__main__":
    main()