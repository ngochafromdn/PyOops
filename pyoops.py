"""
Main entry point for the language interpreter.
This script orchestrates the compilation and execution pipeline:
1. Lexical analysis (tokenization)
2. Parsing (syntax analysis)
3. Semantic analysis
4. Runtime execution
"""
import sys
from antlr4 import *
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser
from SyntaxErrorHandling import SyntaxErrorHandling
from SymbolTableVisitor import SymbolTableVisitor
from StatementAnalyzer import StatementAnalyzer
from RuntimeVisitor import RuntimeVisitor

def main(input_file):
    """
    Main function to run the interpreter on the given input file.
    
    Args:
        input_file: Path to the source code file to interpret
    """
    print(f"Running interpreter on file: {input_file}")
    
    # Step 1: Read the input file
    try:
        with open(input_file, 'r') as f:
            input_stream = InputStream(f.read())
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    # Step 2: Setup lexer and token stream for parsing
    lexer = syntaxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = syntaxParser(token_stream)

    # Step 3: Configure custom error handling for syntax errors
    error_listener = SyntaxErrorHandling()
    parser.removeErrorListeners()  # Remove default error listeners
    parser.addErrorListener(error_listener)  # Add our custom error handler

    # Step 4: Parse the input to create the syntax tree
    try:
        tree = parser.program()  # Start parsing at the 'program' rule
    except Exception as e:
        print(f"Parsing failed: {e}")
        return

    # Step 5: If syntax is valid, continue with semantic analysis and execution
    if error_listener.error_count == 0:
        # Step 5.1: Initialize symbol table for variable tracking
        symbol_table = SymbolTableVisitor()
        # Add built-in functions to the symbol table
        symbol_table.define("get_error", {"type": "str"})
        
        # Step 5.2: Perform semantic analysis (type checking, scope validation)
        try:
            analyzer = StatementAnalyzer(symbol_table)
            analyzer.visit(tree)
            # Uncomment to debug symbol table contents:
            # print("\nSymbol Table after semantic analysis:")
            # symbol_table.printSymbols()
        except Exception as e:
            print(f"Semantic analysis failed: {e}")
            return

        # Step 5.3: Execute the program by visiting the parse tree
        try:
            executor = RuntimeVisitor(symbol_table)
            output = executor.visit(tree)
            
            # Display program output
            print("\n=== Program Output ===")
            print(output)
            print("=== End of Output ===")
        except Exception as e:
            print(f"Runtime execution failed: {e}")
            return
    else:
        # Skip execution if syntax errors were found
        print(f"Found {error_listener.error_count} syntax errors. Execution skipped.")

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python runner.py <input_file>")
        sys.exit(1)
    
    # Run the interpreter with the provided input file
    main(sys.argv[1])