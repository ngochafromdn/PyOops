import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser
from SymbolTableVisitor import SymbolTableVisitor

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
        print("  " * indent + f"{rule_name}:{indent}")
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

    # Bắt đầu parse từ rule 'program'
    tree = parser.program()

    # In cây cú pháp theo dạng cây thụ
    print("Parse Tree:")
    print_tree(tree, parser)

    print("✅ Parse thành công!")

    # Assume `tree` is the parse tree from syntaxParser
    visitor = SymbolTableVisitor()
    visitor.visit(tree)
    visitor.printSymbols()

except FileNotFoundError:
    print("❌ Không tìm thấy file.")
except Exception as e:
    print(f"❌ Lỗi khi parse: {e}")
