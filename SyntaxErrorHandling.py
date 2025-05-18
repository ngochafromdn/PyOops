import sys
from antlr4.error.ErrorListener import ErrorListener


RED = "\033[91m"
BLUE = "\033[34m"     
BOLD = "\033[1m"
RESET = "\033[0m"

class SyntaxErrorHandling(ErrorListener):
    """Custom error listener for reporting syntax errors with colorized messages"""

    def __init__(self):
        super().__init__()
        self.error_count = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg):
        self.error_count += 1
        print(f"{RED}{BOLD}[Syntax Error]{RESET}{RED} Line {line}:{column} - {msg}{RESET}")
        
        try:
            char_stream = recognizer._input.tokenSource.inputStream
            lines = char_stream.strdata.splitlines()
            if 0 <= line - 1 < len(lines):
                error_line = lines[line - 1]
                print(f"\n{RED}{error_line}{RESET}")
                pointer = ' ' * column + f"{RED}^{RESET}"
                print(f"{pointer}")
        except Exception as ex:
            print(f"{BLUE}(Could not retrieve input stream: {ex}){RESET}\n")

        if offendingSymbol:
            print(f"{BOLD}{RED}Offending symbol: '{offendingSymbol.text}'{RESET}")

        try:
            expected_tokens = recognizer.getExpectedTokens()
            if expected_tokens:
                expected = []
                for interval in expected_tokens.intervals:
                    for t in range(interval.a, interval.b + 1):
                        if 0 <= t < len(recognizer.literalNames):
                            token_name = recognizer.literalNames[t] or recognizer.symbolicNames[t]
                            expected.append(token_name)
                expected_clean = ', '.join(filter(None, expected))
                print(f"{BOLD}Expected one of:{RESET} {expected_clean}\n")
        except Exception as ex:
            print(f"{BLUE}(Could not retrieve expected tokens: {ex}){RESET}")
    
        # Exit program
        sys.exit(1)
