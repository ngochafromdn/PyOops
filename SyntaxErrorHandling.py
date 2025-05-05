from antlr4.error.ErrorListener import ErrorListener

# ANSI color codes
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

class SyntaxErrorHandling(ErrorListener):
    """Custom error listener for reporting syntax errors with colorized messages"""

    def __init__(self):
        super().__init__()
        self.error_count = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error_count += 1
        print(f"{RED}{BOLD}[Syntax Error]{RESET} Line {YELLOW}{line}{RESET}:{YELLOW}{column}{RESET} - {msg}")
        
        # Try to get the CharStream from recognizer's token source
        try:
            char_stream = recognizer._input.tokenSource.inputStream
            lines = char_stream.strdata.splitlines()
            if 0 <= line - 1 < len(lines):
                error_line = lines[line - 1]
                print(f"\n{CYAN}{error_line}{RESET}")
                pointer = ' ' * column + f"{RED}^{RESET}"
                print(f"{pointer}")
        except Exception as ex:
            print(f"{YELLOW}(Could not retrieve input stream: {ex}){RESET}")

        # Print offending symbol
        if offendingSymbol:
            print(f"{BOLD}Offending symbol:{RESET} '{offendingSymbol.text}'")

        # Print expected tokens
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
            print(f"{YELLOW}(Could not retrieve expected tokens: {ex}){RESET}")
