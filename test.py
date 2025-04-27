from antlr4 import *
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser
from SymbolTableVisitor import SymbolTableVisitor
from StatementAnalyzer import StatementAnalyzer
from ExpressionAnalyzer import ExpressionAnalyzer
from SemanticAnalyzer import SemanticAnalyzer
from SyntaxErrorHandling import SyntaxErrorHandling

# Hỏi tên file trong thư mục tests/
file_name = input("Nhập tên file trong thư mục tests/ (vd: function.txt): ")
file_path = f"tests/{file_name}"

# Hàm đệ quy in cây cú pháp
def print_tree(node, parser, indent=0):
    if isinstance(node, TerminalNode):
        text = node.getText().replace("\n", "\\n")  # Hiển thị xuống dòng cho đẹp
        print("  " * indent + text)
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print("  " * indent + f"{rule_name}:")
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            print_tree(child, parser, indent + 1)

try:
    # Mở file và tạo input stream
    input_stream = FileStream(file_path, encoding='utf-8')

     # Khởi tạo lexer & parser
    lexer = syntaxLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = syntaxParser(stream)

    # Remove all default error listeners
    custom_listener = SyntaxErrorHandling()

    lexer.removeErrorListeners()
    lexer.addErrorListener(custom_listener)

    parser.removeErrorListeners()
    parser.addErrorListener(custom_listener)

    # Bắt đầu parse từ rule 'program'
    tree = parser.program()

    # In cây cú pháp theo dạng cây thụ
    # print("Parse Tree:")
    # print_tree(tree, parser)

    print("\n✅ Parse thành công!")

    # *Kiểm tra Symbol Table* (Xây dựng bảng ký hiệu)
    symbol_table_visitor = SymbolTableVisitor()
    symbol_table_visitor.visit(tree)
    print("\n✅ Xây dựng bảng ký hiệu thành công!")

    # *Kiểm tra ngữ nghĩa*
    # semantic_analyzer = SemanticAnalyzer()
    # semantic_analyzer.visit(tree)
    # print("\n✅ Phân tích ngữ nghĩa thành công!")
    expr = ExpressionAnalyzer(symbol_table_visitor)
    expr.visit(tree)
    statement = StatementAnalyzer(symbol_table_visitor, expr)
    statement.visit(tree)

except FileNotFoundError:
    print("❌ Không tìm thấy file.")
except Exception as e:
    print(f"❌ Error: {e}")
