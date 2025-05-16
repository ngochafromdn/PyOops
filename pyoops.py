import sys
from antlr4 import *
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser
from SyntaxErrorHandling import SyntaxErrorHandling
from SymbolTableVisitor import SymbolTableVisitor
from StatementAnalyzer import StatementAnalyzer
from RuntimeVisitor import RuntimeVisitor

def main(input_file):
    print(f"Running interpreter on file: {input_file}")
    
    try:
        # Đọc nội dung tệp
        with open(input_file, 'r') as f:
            input_stream = InputStream(f.read())
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    # Tạo lexer và parser
    lexer = syntaxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = syntaxParser(token_stream)

    # Gắn trình xử lý lỗi cú pháp
    error_listener = SyntaxErrorHandling()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Phân tích cú pháp
    try:
        tree = parser.program()
    except Exception as e:
        print(f"Parsing failed: {e}")
        return

    # Nếu không có lỗi cú pháp, tiếp tục với phân tích ngữ nghĩa
    if error_listener.error_count == 0:
        # Tạo bảng ký hiệu
        symbol_table = SymbolTableVisitor()
        symbol_table.define("get_error", {"type": "str"})
        
        # Phân tích ngữ nghĩa
        try:
            analyzer = StatementAnalyzer(symbol_table)
            analyzer.visit(tree)
            # print("\nSymbol Table after semantic analysis:")
            # symbol_table.printSymbols()
        except Exception as e:
            print(f"Semantic analysis failed: {e}")
            return

        # Chạy trình thông dịch
        try:
            executor = RuntimeVisitor(symbol_table)
            output = executor.visit(tree)
            
            print("\n=== Program Output ===")
            print(output)
            print("=== End of Output ===")
        except Exception as e:
            print(f"Runtime execution failed: {e}")
            return
    else:
        print(f"Found {error_listener.error_count} syntax errors. Execution skipped.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python runner.py <input_file>")
        sys.exit(1)
    
    main(sys.argv[1])