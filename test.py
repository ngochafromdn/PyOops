import antlr4
from antlr4 import *
from syntaxLexer import syntaxLexer
from syntaxParser import syntaxParser

# Hỏi tên file trong thư mục tests/
file_name = input("Nhập tên file trong thư mục tests/ (vd: function.txt): ")
file_path = f"tests/{file_name}"

try:
    # Mở file và tạo input stream
    input_stream = FileStream(file_path, encoding='utf-8')

    # Khởi tạo lexer & parser
    lexer = syntaxLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = syntaxParser(stream)

    # Bắt đầu parse từ rule 'program'
    tree = parser.program()
# In cây cú pháp ra màn hìn
    print(tree.toStringTree(recog=parser))


    print("✅ Parse thành công!")

except FileNotFoundError:
    print("❌ Không tìm thấy file.")
except Exception as e:
    print(f"❌ Lỗi khi parse: {e}")

