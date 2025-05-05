# Generated from syntax.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,305,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,1,1,1,1,1,3,1,82,8,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,96,8,1,1,2,
        1,2,5,2,100,8,2,10,2,12,2,103,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,111,
        8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,5,6,122,8,6,10,6,12,6,125,
        9,6,1,7,1,7,1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,8,1,8,1,8,5,8,138,
        8,8,10,8,12,8,141,9,8,1,9,1,9,1,9,5,9,146,8,9,10,9,12,9,149,9,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,159,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        175,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,185,8,11,1,
        12,1,12,1,12,3,12,190,8,12,1,12,1,12,1,13,1,13,1,13,5,13,197,8,13,
        10,13,12,13,200,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,5,14,214,8,14,10,14,12,14,217,9,14,1,14,1,14,3,14,
        221,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,4,19,
        246,8,19,11,19,12,19,247,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,5,21,261,8,21,10,21,12,21,264,9,21,1,22,1,22,1,22,
        1,22,5,22,270,8,22,10,22,12,22,273,9,22,1,22,1,22,1,23,1,23,1,23,
        1,23,5,23,281,8,23,10,23,12,23,284,9,23,1,23,1,23,1,24,1,24,1,24,
        1,24,5,24,292,8,24,10,24,12,24,295,9,24,1,24,1,24,1,25,1,25,1,25,
        1,26,1,26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,0,5,1,0,13,14,1,0,30,31,1,
        0,19,24,1,0,26,27,1,0,28,29,321,0,57,1,0,0,0,2,95,1,0,0,0,4,97,1,
        0,0,0,6,106,1,0,0,0,8,112,1,0,0,0,10,116,1,0,0,0,12,118,1,0,0,0,
        14,126,1,0,0,0,16,134,1,0,0,0,18,142,1,0,0,0,20,158,1,0,0,0,22,184,
        1,0,0,0,24,186,1,0,0,0,26,193,1,0,0,0,28,201,1,0,0,0,30,222,1,0,
        0,0,32,228,1,0,0,0,34,233,1,0,0,0,36,236,1,0,0,0,38,241,1,0,0,0,
        40,251,1,0,0,0,42,255,1,0,0,0,44,265,1,0,0,0,46,276,1,0,0,0,48,287,
        1,0,0,0,50,298,1,0,0,0,52,301,1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,
        0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,
        1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,63,3,8,4,0,63,64,5,33,0,0,
        64,96,1,0,0,0,65,66,3,6,3,0,66,67,5,33,0,0,67,96,1,0,0,0,68,96,3,
        28,14,0,69,96,3,30,15,0,70,96,3,36,18,0,71,72,3,34,17,0,72,73,5,
        33,0,0,73,96,1,0,0,0,74,76,5,4,0,0,75,77,7,0,0,0,76,75,1,0,0,0,76,
        77,1,0,0,0,77,78,1,0,0,0,78,79,5,41,0,0,79,81,5,37,0,0,80,82,3,42,
        21,0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,5,38,0,0,84,
        96,3,4,2,0,85,96,3,4,2,0,86,96,3,38,19,0,87,88,3,32,16,0,88,89,5,
        33,0,0,89,96,1,0,0,0,90,96,3,50,25,0,91,96,3,52,26,0,92,93,3,24,
        12,0,93,94,5,33,0,0,94,96,1,0,0,0,95,62,1,0,0,0,95,65,1,0,0,0,95,
        68,1,0,0,0,95,69,1,0,0,0,95,70,1,0,0,0,95,71,1,0,0,0,95,74,1,0,0,
        0,95,85,1,0,0,0,95,86,1,0,0,0,95,87,1,0,0,0,95,90,1,0,0,0,95,91,
        1,0,0,0,95,92,1,0,0,0,96,3,1,0,0,0,97,101,5,35,0,0,98,100,3,2,1,
        0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,
        104,1,0,0,0,103,101,1,0,0,0,104,105,5,36,0,0,105,5,1,0,0,0,106,107,
        5,14,0,0,107,110,5,41,0,0,108,109,5,25,0,0,109,111,3,10,5,0,110,
        108,1,0,0,0,110,111,1,0,0,0,111,7,1,0,0,0,112,113,5,41,0,0,113,114,
        5,25,0,0,114,115,3,10,5,0,115,9,1,0,0,0,116,117,3,12,6,0,117,11,
        1,0,0,0,118,123,3,14,7,0,119,120,7,1,0,0,120,122,3,14,7,0,121,119,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,13,1,
        0,0,0,125,123,1,0,0,0,126,131,3,16,8,0,127,128,7,2,0,0,128,130,3,
        16,8,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,
        0,0,0,132,15,1,0,0,0,133,131,1,0,0,0,134,139,3,18,9,0,135,136,7,
        3,0,0,136,138,3,18,9,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,1,
        0,0,0,139,140,1,0,0,0,140,17,1,0,0,0,141,139,1,0,0,0,142,147,3,20,
        10,0,143,144,7,4,0,0,144,146,3,20,10,0,145,143,1,0,0,0,146,149,1,
        0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,19,1,0,0,0,149,147,1,0,
        0,0,150,151,5,27,0,0,151,159,3,20,10,0,152,153,5,32,0,0,153,154,
        5,37,0,0,154,155,3,10,5,0,155,156,5,38,0,0,156,159,1,0,0,0,157,159,
        3,22,11,0,158,150,1,0,0,0,158,152,1,0,0,0,158,157,1,0,0,0,159,21,
        1,0,0,0,160,161,5,37,0,0,161,162,3,10,5,0,162,163,5,38,0,0,163,185,
        1,0,0,0,164,185,5,9,0,0,165,185,5,10,0,0,166,167,5,41,0,0,167,168,
        5,39,0,0,168,169,3,10,5,0,169,170,5,40,0,0,170,185,1,0,0,0,171,172,
        5,41,0,0,172,174,5,37,0,0,173,175,3,26,13,0,174,173,1,0,0,0,174,
        175,1,0,0,0,175,176,1,0,0,0,176,185,5,38,0,0,177,185,5,41,0,0,178,
        185,5,18,0,0,179,185,5,17,0,0,180,185,5,16,0,0,181,185,3,44,22,0,
        182,185,3,46,23,0,183,185,3,48,24,0,184,160,1,0,0,0,184,164,1,0,
        0,0,184,165,1,0,0,0,184,166,1,0,0,0,184,171,1,0,0,0,184,177,1,0,
        0,0,184,178,1,0,0,0,184,179,1,0,0,0,184,180,1,0,0,0,184,181,1,0,
        0,0,184,182,1,0,0,0,184,183,1,0,0,0,185,23,1,0,0,0,186,187,5,41,
        0,0,187,189,5,37,0,0,188,190,3,26,13,0,189,188,1,0,0,0,189,190,1,
        0,0,0,190,191,1,0,0,0,191,192,5,38,0,0,192,25,1,0,0,0,193,198,3,
        10,5,0,194,195,5,34,0,0,195,197,3,10,5,0,196,194,1,0,0,0,197,200,
        1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,27,1,0,0,0,200,198,1,
        0,0,0,201,202,5,1,0,0,202,203,5,37,0,0,203,204,3,10,5,0,204,205,
        5,38,0,0,205,215,3,4,2,0,206,207,5,2,0,0,207,208,5,1,0,0,208,209,
        5,37,0,0,209,210,3,10,5,0,210,211,5,38,0,0,211,212,3,4,2,0,212,214,
        1,0,0,0,213,206,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,
        1,0,0,0,216,220,1,0,0,0,217,215,1,0,0,0,218,219,5,2,0,0,219,221,
        3,4,2,0,220,218,1,0,0,0,220,221,1,0,0,0,221,29,1,0,0,0,222,223,5,
        3,0,0,223,224,5,37,0,0,224,225,3,10,5,0,225,226,5,38,0,0,226,227,
        3,4,2,0,227,31,1,0,0,0,228,229,5,6,0,0,229,230,5,37,0,0,230,231,
        3,10,5,0,231,232,5,38,0,0,232,33,1,0,0,0,233,234,5,5,0,0,234,235,
        3,10,5,0,235,35,1,0,0,0,236,237,5,7,0,0,237,238,3,4,2,0,238,239,
        5,8,0,0,239,240,3,4,2,0,240,37,1,0,0,0,241,242,5,15,0,0,242,243,
        5,41,0,0,243,245,5,35,0,0,244,246,3,40,20,0,245,244,1,0,0,0,246,
        247,1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,
        250,5,36,0,0,250,39,1,0,0,0,251,252,5,14,0,0,252,253,5,41,0,0,253,
        254,5,33,0,0,254,41,1,0,0,0,255,256,5,14,0,0,256,262,5,41,0,0,257,
        258,5,34,0,0,258,259,5,14,0,0,259,261,5,41,0,0,260,257,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,43,1,0,0,0,264,262,
        1,0,0,0,265,266,5,39,0,0,266,271,5,18,0,0,267,268,5,34,0,0,268,270,
        5,18,0,0,269,267,1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,
        1,0,0,0,272,274,1,0,0,0,273,271,1,0,0,0,274,275,5,40,0,0,275,45,
        1,0,0,0,276,277,5,39,0,0,277,282,5,16,0,0,278,279,5,34,0,0,279,281,
        5,16,0,0,280,278,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,283,
        1,0,0,0,283,285,1,0,0,0,284,282,1,0,0,0,285,286,5,40,0,0,286,47,
        1,0,0,0,287,288,5,39,0,0,288,293,5,17,0,0,289,290,5,34,0,0,290,292,
        5,17,0,0,291,289,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,
        1,0,0,0,294,296,1,0,0,0,295,293,1,0,0,0,296,297,5,40,0,0,297,49,
        1,0,0,0,298,299,5,11,0,0,299,300,5,33,0,0,300,51,1,0,0,0,301,302,
        5,12,0,0,302,303,5,33,0,0,303,53,1,0,0,0,22,57,76,81,95,101,110,
        123,131,139,147,158,174,184,189,198,215,220,247,262,271,282,293
    ]

class syntaxParser ( Parser ):

    grammarFileName = "syntax.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'func'", 
                     "'return'", "'print'", "'try'", "'except'", "'true'", 
                     "'false'", "'continue'", "'break'", "'void'", "<INVALID>", 
                     "'type'", "<INVALID>", "<INVALID>", "<INVALID>", "'<='", 
                     "'>='", "'=='", "'!='", "'<'", "'>'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'and'", "'or'", "'!'", "';'", 
                     "','", "'{'", "'}'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FUNC", "RETURN", 
                      "PRINT", "TRY", "EXCEPT", "TRUE", "FALSE", "CONTINUE", 
                      "BREAK", "VOID", "DATA_TYPE", "TYPE_DEF", "CHARACTER", 
                      "STRING", "NUMBER", "LE", "GE", "EQ", "NE", "LT", 
                      "GT", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "AND", 
                      "OR", "NOT", "SEMI", "COMMA", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "IDENTIFIER", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_variable_declaration = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_logic_expr = 6
    RULE_comp_expr = 7
    RULE_add_expr = 8
    RULE_mul_expr = 9
    RULE_unary_expr = 10
    RULE_primary_expr = 11
    RULE_function_call = 12
    RULE_arg_list = 13
    RULE_if_stmt = 14
    RULE_while_stmt = 15
    RULE_print_stmt = 16
    RULE_return_stmt = 17
    RULE_try_stmt = 18
    RULE_type_defStatement = 19
    RULE_type_def_list = 20
    RULE_param_list = 21
    RULE_int_Array = 22
    RULE_char_Array = 23
    RULE_strArray = 24
    RULE_continue_stmt = 25
    RULE_break_stmt = 26

    ruleNames =  [ "program", "statement", "block", "variable_declaration", 
                   "assignment", "expression", "logic_expr", "comp_expr", 
                   "add_expr", "mul_expr", "unary_expr", "primary_expr", 
                   "function_call", "arg_list", "if_stmt", "while_stmt", 
                   "print_stmt", "return_stmt", "try_stmt", "type_defStatement", 
                   "type_def_list", "param_list", "int_Array", "char_Array", 
                   "strArray", "continue_stmt", "break_stmt" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FUNC=4
    RETURN=5
    PRINT=6
    TRY=7
    EXCEPT=8
    TRUE=9
    FALSE=10
    CONTINUE=11
    BREAK=12
    VOID=13
    DATA_TYPE=14
    TYPE_DEF=15
    CHARACTER=16
    STRING=17
    NUMBER=18
    LE=19
    GE=20
    EQ=21
    NE=22
    LT=23
    GT=24
    ASSIGN=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    AND=30
    OR=31
    NOT=32
    SEMI=33
    COMMA=34
    LBRACE=35
    RBRACE=36
    LPAREN=37
    RPAREN=38
    LBRACKET=39
    RBRACKET=40
    IDENTIFIER=41
    LINE_COMMENT=42
    BLOCK_COMMENT=43
    WS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(syntaxParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.StatementContext)
            else:
                return self.getTypedRuleContext(syntaxParser.StatementContext,i)


        def getRuleIndex(self):
            return syntaxParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = syntaxParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2233383049466) != 0):
                self.state = 54
                self.statement()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(syntaxParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NewTypeDefContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_defStatement(self):
            return self.getTypedRuleContext(syntaxParser.Type_defStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewTypeDef" ):
                listener.enterNewTypeDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewTypeDef" ):
                listener.exitNewTypeDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewTypeDef" ):
                return visitor.visitNewTypeDef(self)
            else:
                return visitor.visitChildren(self)


    class PrintStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def print_stmt(self):
            return self.getTypedRuleContext(syntaxParser.Print_stmtContext,0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call(self):
            return self.getTypedRuleContext(syntaxParser.Function_callContext,0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallStmt" ):
                listener.enterFuncCallStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallStmt" ):
                listener.exitFuncCallStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallStmt" ):
                return visitor.visitFuncCallStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(syntaxParser.AssignmentContext,0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class TryStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def try_stmt(self):
            return self.getTypedRuleContext(syntaxParser.Try_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStmt" ):
                listener.enterTryStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStmt" ):
                listener.exitTryStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryStmt" ):
                return visitor.visitTryStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(syntaxParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class BreakContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def break_stmt(self):
            return self.getTypedRuleContext(syntaxParser.Break_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)


    class ContinueContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def continue_stmt(self):
            return self.getTypedRuleContext(syntaxParser.Continue_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_stmt(self):
            return self.getTypedRuleContext(syntaxParser.If_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def while_stmt(self):
            return self.getTypedRuleContext(syntaxParser.While_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable_declaration(self):
            return self.getTypedRuleContext(syntaxParser.Variable_declarationContext,0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclStmt" ):
                listener.enterVarDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclStmt" ):
                listener.exitVarDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStmt" ):
                return visitor.visitVarDeclStmt(self)
            else:
                return visitor.visitChildren(self)


    class FuncStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(syntaxParser.FUNC, 0)
        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)
        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)
        def block(self):
            return self.getTypedRuleContext(syntaxParser.BlockContext,0)

        def param_list(self):
            return self.getTypedRuleContext(syntaxParser.Param_listContext,0)

        def DATA_TYPE(self):
            return self.getToken(syntaxParser.DATA_TYPE, 0)
        def VOID(self):
            return self.getToken(syntaxParser.VOID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncStmt" ):
                listener.enterFuncStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncStmt" ):
                listener.exitFuncStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncStmt" ):
                return visitor.visitFuncStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def return_stmt(self):
            return self.getTypedRuleContext(syntaxParser.Return_stmtContext,0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = syntaxParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = syntaxParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.assignment()
                self.state = 63
                self.match(syntaxParser.SEMI)
                pass

            elif la_ == 2:
                localctx = syntaxParser.VarDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.variable_declaration()
                self.state = 66
                self.match(syntaxParser.SEMI)
                pass

            elif la_ == 3:
                localctx = syntaxParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.if_stmt()
                pass

            elif la_ == 4:
                localctx = syntaxParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.while_stmt()
                pass

            elif la_ == 5:
                localctx = syntaxParser.TryStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.try_stmt()
                pass

            elif la_ == 6:
                localctx = syntaxParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.return_stmt()
                self.state = 72
                self.match(syntaxParser.SEMI)
                pass

            elif la_ == 7:
                localctx = syntaxParser.FuncStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.match(syntaxParser.FUNC)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13 or _la==14:
                    self.state = 75
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 78
                self.match(syntaxParser.IDENTIFIER)
                self.state = 79
                self.match(syntaxParser.LPAREN)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 80
                    self.param_list()


                self.state = 83
                self.match(syntaxParser.RPAREN)
                self.state = 84
                self.block()
                pass

            elif la_ == 8:
                localctx = syntaxParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 85
                self.block()
                pass

            elif la_ == 9:
                localctx = syntaxParser.NewTypeDefContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 86
                self.type_defStatement()
                pass

            elif la_ == 10:
                localctx = syntaxParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 87
                self.print_stmt()
                self.state = 88
                self.match(syntaxParser.SEMI)
                pass

            elif la_ == 11:
                localctx = syntaxParser.ContinueContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 90
                self.continue_stmt()
                pass

            elif la_ == 12:
                localctx = syntaxParser.BreakContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 91
                self.break_stmt()
                pass

            elif la_ == 13:
                localctx = syntaxParser.FuncCallStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 92
                self.function_call()
                self.state = 93
                self.match(syntaxParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(syntaxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(syntaxParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.StatementContext)
            else:
                return self.getTypedRuleContext(syntaxParser.StatementContext,i)


        def getRuleIndex(self):
            return syntaxParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = syntaxParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(syntaxParser.LBRACE)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2233383049466) != 0):
                self.state = 98
                self.statement()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(syntaxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(syntaxParser.DATA_TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(syntaxParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)


        def getRuleIndex(self):
            return syntaxParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = syntaxParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(syntaxParser.DATA_TYPE)
            self.state = 107
            self.match(syntaxParser.IDENTIFIER)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 108
                self.match(syntaxParser.ASSIGN)
                self.state = 109
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(syntaxParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)


        def getRuleIndex(self):
            return syntaxParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = syntaxParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(syntaxParser.IDENTIFIER)
            self.state = 113
            self.match(syntaxParser.ASSIGN)
            self.state = 114
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_expr(self):
            return self.getTypedRuleContext(syntaxParser.Logic_exprContext,0)


        def getRuleIndex(self):
            return syntaxParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = syntaxParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.logic_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_logic_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicExprContext(Logic_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Logic_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comp_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.Comp_exprContext)
            else:
                return self.getTypedRuleContext(syntaxParser.Comp_exprContext,i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.AND)
            else:
                return self.getToken(syntaxParser.AND, i)
        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.OR)
            else:
                return self.getToken(syntaxParser.OR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)



    def logic_expr(self):

        localctx = syntaxParser.Logic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_logic_expr)
        self._la = 0 # Token type
        try:
            localctx = syntaxParser.LogicExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.comp_expr()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.comp_expr()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_comp_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompExprContext(Comp_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Comp_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def add_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.Add_exprContext)
            else:
                return self.getTypedRuleContext(syntaxParser.Add_exprContext,i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.LT)
            else:
                return self.getToken(syntaxParser.LT, i)
        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.LE)
            else:
                return self.getToken(syntaxParser.LE, i)
        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.GT)
            else:
                return self.getToken(syntaxParser.GT, i)
        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.GE)
            else:
                return self.getToken(syntaxParser.GE, i)
        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.EQ)
            else:
                return self.getToken(syntaxParser.EQ, i)
        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.NE)
            else:
                return self.getToken(syntaxParser.NE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompExpr" ):
                listener.enterCompExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompExpr" ):
                listener.exitCompExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompExpr" ):
                return visitor.visitCompExpr(self)
            else:
                return visitor.visitChildren(self)



    def comp_expr(self):

        localctx = syntaxParser.Comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comp_expr)
        self._la = 0 # Token type
        try:
            localctx = syntaxParser.CompExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.add_expr()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0):
                self.state = 127
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self.add_expr()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_add_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddSubExprContext(Add_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Add_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mul_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.Mul_exprContext)
            else:
                return self.getTypedRuleContext(syntaxParser.Mul_exprContext,i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.ADD)
            else:
                return self.getToken(syntaxParser.ADD, i)
        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.SUB)
            else:
                return self.getToken(syntaxParser.SUB, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self):

        localctx = syntaxParser.Add_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_add_expr)
        self._la = 0 # Token type
        try:
            localctx = syntaxParser.AddSubExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.mul_expr()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 135
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.mul_expr()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_mul_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulDivExprContext(Mul_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Mul_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.Unary_exprContext)
            else:
                return self.getTypedRuleContext(syntaxParser.Unary_exprContext,i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.MUL)
            else:
                return self.getToken(syntaxParser.MUL, i)
        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.DIV)
            else:
                return self.getToken(syntaxParser.DIV, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self):

        localctx = syntaxParser.Mul_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mul_expr)
        self._la = 0 # Token type
        try:
            localctx = syntaxParser.MulDivExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.unary_expr()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28 or _la==29:
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.unary_expr()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_unary_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimaryExprContext(Unary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Unary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_expr(self):
            return self.getTypedRuleContext(syntaxParser.Primary_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(Unary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Unary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(syntaxParser.NOT, 0)
        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(Unary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Unary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(syntaxParser.SUB, 0)
        def unary_expr(self):
            return self.getTypedRuleContext(syntaxParser.Unary_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)



    def unary_expr(self):

        localctx = syntaxParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unary_expr)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = syntaxParser.UnaryMinusExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(syntaxParser.SUB)
                self.state = 151
                self.unary_expr()
                pass
            elif token in [32]:
                localctx = syntaxParser.NotExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(syntaxParser.NOT)
                self.state = 153
                self.match(syntaxParser.LPAREN)
                self.state = 154
                self.expression()
                self.state = 155
                self.match(syntaxParser.RPAREN)
                pass
            elif token in [9, 10, 16, 17, 18, 37, 39, 41]:
                localctx = syntaxParser.PrimaryExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.primary_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return syntaxParser.RULE_primary_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(syntaxParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class CharArrayContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def char_Array(self):
            return self.getTypedRuleContext(syntaxParser.Char_ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharArray" ):
                listener.enterCharArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharArray" ):
                listener.exitCharArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharArray" ):
                return visitor.visitCharArray(self)
            else:
                return visitor.visitChildren(self)


    class TrueExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(syntaxParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueExpr" ):
                listener.enterTrueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueExpr" ):
                listener.exitTrueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueExpr" ):
                return visitor.visitTrueExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntArrayContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_Array(self):
            return self.getTypedRuleContext(syntaxParser.Int_ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntArray" ):
                listener.enterIntArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntArray" ):
                listener.exitIntArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntArray" ):
                return visitor.visitIntArray(self)
            else:
                return visitor.visitChildren(self)


    class StringArrayContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def strArray(self):
            return self.getTypedRuleContext(syntaxParser.StrArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringArray" ):
                listener.enterStringArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringArray" ):
                listener.exitStringArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringArray" ):
                return visitor.visitStringArray(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(syntaxParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)
        def LBRACKET(self):
            return self.getToken(syntaxParser.LBRACKET, 0)
        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)

        def RBRACKET(self):
            return self.getToken(syntaxParser.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccessExpr" ):
                listener.enterArrayAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccessExpr" ):
                listener.exitArrayAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessExpr" ):
                return visitor.visitArrayAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class FalseExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(syntaxParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseExpr" ):
                listener.enterFalseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseExpr" ):
                listener.exitFalseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseExpr" ):
                return visitor.visitFalseExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)
        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)
        def arg_list(self):
            return self.getTypedRuleContext(syntaxParser.Arg_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class CharExprContext(Primary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a syntaxParser.Primary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(syntaxParser.CHARACTER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharExpr" ):
                listener.enterCharExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharExpr" ):
                listener.exitCharExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharExpr" ):
                return visitor.visitCharExpr(self)
            else:
                return visitor.visitChildren(self)



    def primary_expr(self):

        localctx = syntaxParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primary_expr)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = syntaxParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(syntaxParser.LPAREN)
                self.state = 161
                self.expression()
                self.state = 162
                self.match(syntaxParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = syntaxParser.TrueExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(syntaxParser.TRUE)
                pass

            elif la_ == 3:
                localctx = syntaxParser.FalseExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(syntaxParser.FALSE)
                pass

            elif la_ == 4:
                localctx = syntaxParser.ArrayAccessExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(syntaxParser.IDENTIFIER)
                self.state = 167
                self.match(syntaxParser.LBRACKET)
                self.state = 168
                self.expression()
                self.state = 169
                self.match(syntaxParser.RBRACKET)
                pass

            elif la_ == 5:
                localctx = syntaxParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.match(syntaxParser.IDENTIFIER)
                self.state = 172
                self.match(syntaxParser.LPAREN)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2890647668224) != 0):
                    self.state = 173
                    self.arg_list()


                self.state = 176
                self.match(syntaxParser.RPAREN)
                pass

            elif la_ == 6:
                localctx = syntaxParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                self.match(syntaxParser.IDENTIFIER)
                pass

            elif la_ == 7:
                localctx = syntaxParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 178
                self.match(syntaxParser.NUMBER)
                pass

            elif la_ == 8:
                localctx = syntaxParser.StringExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 179
                self.match(syntaxParser.STRING)
                pass

            elif la_ == 9:
                localctx = syntaxParser.CharExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 180
                self.match(syntaxParser.CHARACTER)
                pass

            elif la_ == 10:
                localctx = syntaxParser.IntArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 181
                self.int_Array()
                pass

            elif la_ == 11:
                localctx = syntaxParser.CharArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 182
                self.char_Array()
                pass

            elif la_ == 12:
                localctx = syntaxParser.StringArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 183
                self.strArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(syntaxParser.Arg_listContext,0)


        def getRuleIndex(self):
            return syntaxParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = syntaxParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(syntaxParser.IDENTIFIER)
            self.state = 187
            self.match(syntaxParser.LPAREN)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2890647668224) != 0):
                self.state = 188
                self.arg_list()


            self.state = 191
            self.match(syntaxParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(syntaxParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.COMMA)
            else:
                return self.getToken(syntaxParser.COMMA, i)

        def getRuleIndex(self):
            return syntaxParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = syntaxParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expression()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 194
                self.match(syntaxParser.COMMA)
                self.state = 195
                self.expression()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.IF)
            else:
                return self.getToken(syntaxParser.IF, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.LPAREN)
            else:
                return self.getToken(syntaxParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(syntaxParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.RPAREN)
            else:
                return self.getToken(syntaxParser.RPAREN, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.BlockContext)
            else:
                return self.getTypedRuleContext(syntaxParser.BlockContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.ELSE)
            else:
                return self.getToken(syntaxParser.ELSE, i)

        def getRuleIndex(self):
            return syntaxParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = syntaxParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(syntaxParser.IF)
            self.state = 202
            self.match(syntaxParser.LPAREN)
            self.state = 203
            self.expression()
            self.state = 204
            self.match(syntaxParser.RPAREN)
            self.state = 205
            self.block()
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self.match(syntaxParser.ELSE)
                    self.state = 207
                    self.match(syntaxParser.IF)
                    self.state = 208
                    self.match(syntaxParser.LPAREN)
                    self.state = 209
                    self.expression()
                    self.state = 210
                    self.match(syntaxParser.RPAREN)
                    self.state = 211
                    self.block() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 218
                self.match(syntaxParser.ELSE)
                self.state = 219
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(syntaxParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(syntaxParser.BlockContext,0)


        def getRuleIndex(self):
            return syntaxParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = syntaxParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(syntaxParser.WHILE)
            self.state = 223
            self.match(syntaxParser.LPAREN)
            self.state = 224
            self.expression()
            self.state = 225
            self.match(syntaxParser.RPAREN)
            self.state = 226
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(syntaxParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(syntaxParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(syntaxParser.RPAREN, 0)

        def getRuleIndex(self):
            return syntaxParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = syntaxParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(syntaxParser.PRINT)
            self.state = 229
            self.match(syntaxParser.LPAREN)
            self.state = 230
            self.expression()
            self.state = 231
            self.match(syntaxParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(syntaxParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(syntaxParser.ExpressionContext,0)


        def getRuleIndex(self):
            return syntaxParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = syntaxParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(syntaxParser.RETURN)
            self.state = 234
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Try_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(syntaxParser.TRY, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.BlockContext)
            else:
                return self.getTypedRuleContext(syntaxParser.BlockContext,i)


        def EXCEPT(self):
            return self.getToken(syntaxParser.EXCEPT, 0)

        def getRuleIndex(self):
            return syntaxParser.RULE_try_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTry_stmt" ):
                listener.enterTry_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTry_stmt" ):
                listener.exitTry_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTry_stmt" ):
                return visitor.visitTry_stmt(self)
            else:
                return visitor.visitChildren(self)




    def try_stmt(self):

        localctx = syntaxParser.Try_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_try_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(syntaxParser.TRY)
            self.state = 237
            self.block()

            self.state = 238
            self.match(syntaxParser.EXCEPT)
            self.state = 239
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_defStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_DEF(self):
            return self.getToken(syntaxParser.TYPE_DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(syntaxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(syntaxParser.RBRACE, 0)

        def type_def_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(syntaxParser.Type_def_listContext)
            else:
                return self.getTypedRuleContext(syntaxParser.Type_def_listContext,i)


        def getRuleIndex(self):
            return syntaxParser.RULE_type_defStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_defStatement" ):
                listener.enterType_defStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_defStatement" ):
                listener.exitType_defStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_defStatement" ):
                return visitor.visitType_defStatement(self)
            else:
                return visitor.visitChildren(self)




    def type_defStatement(self):

        localctx = syntaxParser.Type_defStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type_defStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(syntaxParser.TYPE_DEF)
            self.state = 242
            self.match(syntaxParser.IDENTIFIER)
            self.state = 243
            self.match(syntaxParser.LBRACE)
            self.state = 245 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 244
                self.type_def_list()
                self.state = 247 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 249
            self.match(syntaxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_def_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(syntaxParser.DATA_TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(syntaxParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def getRuleIndex(self):
            return syntaxParser.RULE_type_def_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_def_list" ):
                listener.enterType_def_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_def_list" ):
                listener.exitType_def_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_def_list" ):
                return visitor.visitType_def_list(self)
            else:
                return visitor.visitChildren(self)




    def type_def_list(self):

        localctx = syntaxParser.Type_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_type_def_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(syntaxParser.DATA_TYPE)
            self.state = 252
            self.match(syntaxParser.IDENTIFIER)
            self.state = 253
            self.match(syntaxParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.DATA_TYPE)
            else:
                return self.getToken(syntaxParser.DATA_TYPE, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.IDENTIFIER)
            else:
                return self.getToken(syntaxParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.COMMA)
            else:
                return self.getToken(syntaxParser.COMMA, i)

        def getRuleIndex(self):
            return syntaxParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = syntaxParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(syntaxParser.DATA_TYPE)
            self.state = 256
            self.match(syntaxParser.IDENTIFIER)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 257
                self.match(syntaxParser.COMMA)
                self.state = 258
                self.match(syntaxParser.DATA_TYPE)
                self.state = 259
                self.match(syntaxParser.IDENTIFIER)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(syntaxParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(syntaxParser.RBRACKET, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.NUMBER)
            else:
                return self.getToken(syntaxParser.NUMBER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.COMMA)
            else:
                return self.getToken(syntaxParser.COMMA, i)

        def getRuleIndex(self):
            return syntaxParser.RULE_int_Array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_Array" ):
                listener.enterInt_Array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_Array" ):
                listener.exitInt_Array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_Array" ):
                return visitor.visitInt_Array(self)
            else:
                return visitor.visitChildren(self)




    def int_Array(self):

        localctx = syntaxParser.Int_ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_int_Array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(syntaxParser.LBRACKET)

            self.state = 266
            self.match(syntaxParser.NUMBER)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 267
                self.match(syntaxParser.COMMA)
                self.state = 268
                self.match(syntaxParser.NUMBER)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 274
            self.match(syntaxParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Char_ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(syntaxParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(syntaxParser.RBRACKET, 0)

        def CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.CHARACTER)
            else:
                return self.getToken(syntaxParser.CHARACTER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.COMMA)
            else:
                return self.getToken(syntaxParser.COMMA, i)

        def getRuleIndex(self):
            return syntaxParser.RULE_char_Array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_Array" ):
                listener.enterChar_Array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_Array" ):
                listener.exitChar_Array(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar_Array" ):
                return visitor.visitChar_Array(self)
            else:
                return visitor.visitChildren(self)




    def char_Array(self):

        localctx = syntaxParser.Char_ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_char_Array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(syntaxParser.LBRACKET)

            self.state = 277
            self.match(syntaxParser.CHARACTER)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 278
                self.match(syntaxParser.COMMA)
                self.state = 279
                self.match(syntaxParser.CHARACTER)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
            self.match(syntaxParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(syntaxParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(syntaxParser.RBRACKET, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.STRING)
            else:
                return self.getToken(syntaxParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(syntaxParser.COMMA)
            else:
                return self.getToken(syntaxParser.COMMA, i)

        def getRuleIndex(self):
            return syntaxParser.RULE_strArray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrArray" ):
                listener.enterStrArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrArray" ):
                listener.exitStrArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrArray" ):
                return visitor.visitStrArray(self)
            else:
                return visitor.visitChildren(self)




    def strArray(self):

        localctx = syntaxParser.StrArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_strArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(syntaxParser.LBRACKET)

            self.state = 288
            self.match(syntaxParser.STRING)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 289
                self.match(syntaxParser.COMMA)
                self.state = 290
                self.match(syntaxParser.STRING)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self.match(syntaxParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(syntaxParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def getRuleIndex(self):
            return syntaxParser.RULE_continue_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_stmt" ):
                listener.enterContinue_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_stmt" ):
                listener.exitContinue_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = syntaxParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(syntaxParser.CONTINUE)
            self.state = 299
            self.match(syntaxParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(syntaxParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(syntaxParser.SEMI, 0)

        def getRuleIndex(self):
            return syntaxParser.RULE_break_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = syntaxParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(syntaxParser.BREAK)
            self.state = 302
            self.match(syntaxParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





