import antlr4
from antlr4 import *
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser
from syntaxListener import syntaxListener  # Import syntaxListener (generated from ANTLR)

# Hỏi tên file trong thư mục tests/
file_name = input("Nhập tên file trong thư mục tests/ (vd: function.txt): ")
file_path = f"tests/{file_name}"

class TreePrinter(syntaxListener):
    def enterProgram(self, ctx):
        print("Program:")
        
    def enterStatement(self, ctx):
        print(f"  Statement: {ctx.getText()}")

    def enterFuncDef(self, ctx):
        print(f"  Function definition: {ctx.IDENTIFIER().getText()}")

    def enterAssignment(self, ctx):
        print(f"  Assignment: {ctx.IDENTIFIER().getText()}")

    def enterReturnStmt(self, ctx):
        print(f"  Return statement: {ctx.getText()}")
        
    # Bạn có thể thêm các hàm `enterX` tùy theo loại node trong cây bạn muốn in chi tiết hơn

try:
    # Mở file và tạo input stream
    input_stream = FileStream(file_path, encoding='utf-8')

    # Khởi tạo lexer & parser
    lexer = syntaxLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = syntaxParser(stream)

    # Bắt đầu parse từ rule 'program'
    tree = parser.program()

    # Tạo và dùng TreePrinter để in cây
    printer = TreePrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    print("✅ Parse thành công!")

except FileNotFoundError:
    print("❌ Không tìm thấy file.")
except Exception as e:
    print(f"❌ Lỗi khi parse: {e}")

