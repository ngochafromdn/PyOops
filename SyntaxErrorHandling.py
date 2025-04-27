from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorHandling(ErrorListener):
    def __init__(self):
        super().__init__()
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "token recognition error" in msg:
            syntax_err = f"[Lexer Error] Line {line}, Column {column}: {msg}"
        else:
            syntax_err = f"[Syntax Error] Line {line}, Column {column}: {msg}"
        print(syntax_err)
