from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorHandling(ErrorListener):
    def __init__(self):
        super().__init__()
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        syntax_err = f"[Syntax Error] Line {line}, column {column}: {msg}"
        print(syntax_err)    