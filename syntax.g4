grammar syntax;

options {
    language = Python3;
}

// —--------------LEXER—-------------------------------

// 1. Keywords
IF : 'if';
ELSE : 'else';
WHILE : 'while';
FUNC : 'func';
RETURN : 'return';
PRINT : 'print';
TRY : 'try';
EXCEPT : 'except';
TRUE : 'true';
FALSE : 'false';
CONTINUE : 'continue';
BREAK : 'break';
VOID : 'void';

DATA_TYPE
    : 'int[]'
    | 'float[]'
    | 'str[]'
    | 'char[]'
    | 'int'
    | 'float'
    | 'str'
    | 'char'
    ;

// 3. Newtype (Struct)
TYPE_DEF : 'type';
DOT : '.';

// 4. Literals
CHARACTER : '\'' ( ~['\\\r\n] | '\\' . ) '\'' ;
STRING : '"' ( ~["\\\r\n] | '\\' . )* '"' ;
NUMBER : '-'? [0-9]+ ('.' [0-9]+)? ;

// 5. Operators
LE : '<=';
GE : '>=';
EQ : '==';
NE : '!=';
LT : '<';
GT : '>';
ASSIGN : '=';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
AND : 'and';
OR : 'or';
NOT : '!';

// 6. Delimiters
SEMI : ';';
COMMA : ',';
LBRACE : '{';
RBRACE : '}';
LPAREN : '(';
RPAREN : ')';
LBRACKET : '[';
RBRACKET : ']';

// 7. Identifiers
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

// 8. Comments
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '---' .*? '---' -> skip ;

// 9. Whitespace
WS : [ \t\r\n]+ -> skip ;

// —--------------PARSER—-------------------------------

program
    : statement* EOF
    ;

// Statement
statement
    : assignment SEMI                   # AssignStmt
    | variable_declaration SEMI        # VarDeclStmt
    | if_stmt                          # IfStmt
    | while_stmt                       # WhileStmt
    | try_stmt                         # TryStmt
    | return_stmt SEMI                 # ReturnStmt
    | FUNC (DATA_TYPE | VOID)? IDENTIFIER LPAREN param_list? RPAREN block # FuncStmt
    | block                            # BlockStmt
    | type_defStatement                # NewTypeDef
    | print_stmt SEMI                  # PrintStmt
    | continue_stmt                    # Continue
    | break_stmt                       # Break
    | function_call SEMI               # FuncCallStmt
    | type_defDeclaration SEMI         # TypeDefDeclStmt
    ;

// Block
block
    : LBRACE statement* RBRACE
    ;

// Variable Declaration
variable_declaration
    : DATA_TYPE IDENTIFIER (ASSIGN expression)?
    ;

// Assignment
assignment
    : (IDENTIFIER | type_defVar) ASSIGN expression
    ;

// Tách tầng biểu thức (Expression Precedence)

expression
    : logic_expr
    ;

logic_expr
    : comp_expr ( (AND | OR) comp_expr )*           # LogicExpr
    ;

comp_expr
    : add_expr ( (LT | LE | GT | GE | EQ | NE) add_expr )*   # CompExpr
    ;

add_expr
    : mul_expr ( (ADD | SUB) mul_expr )*             # AddSubExpr
    ;

mul_expr
    : unary_expr ( (MUL | DIV) unary_expr )*         # MulDivExpr
    ;

unary_expr
    : SUB unary_expr                          # UnaryMinusExpr
    | NOT LPAREN expression RPAREN            # NotExpr
    | primary_expr                            # PrimaryExpr
    ;


primary_expr
    : LPAREN expression RPAREN                       # ParenExpr
    | TRUE                                            # TrueExpr
    | FALSE                                           # FalseExpr
    | IDENTIFIER LBRACKET expression RBRACKET        # ArrayAccessExpr
    | IDENTIFIER LPAREN arg_list? RPAREN             # FuncCallExpr
    | IDENTIFIER                                      # IdExpr
    | NUMBER                                          # NumberExpr
    | STRING                                          # StringExpr
    | CHARACTER                                       # CharExpr
    | int_Array                                       # IntArray
    | char_Array                                      # CharArray
    | strArray                                        # StringArray
    ;

// Function call
function_call
    : IDENTIFIER LPAREN arg_list? RPAREN
    ;

arg_list
    : expression (COMMA expression)*
    ;

// If / While
if_stmt
    : IF LPAREN expression RPAREN block (ELSE IF LPAREN expression RPAREN block)* (ELSE block)?
    ;

while_stmt
    : WHILE LPAREN expression RPAREN block
    ;

// Print
print_stmt
    : PRINT LPAREN expression RPAREN
    ;

// Return statement
return_stmt
    : RETURN expression
    ;

// Try / Except
try_stmt
    : TRY block (EXCEPT block)
    ;

// New type (Struct)
type_defDeclaration
    : IDENTIFIER IDENTIFIER  // e.g., newtype sth
    ;

type_defVar
    : IDENTIFIER DOT IDENTIFIER
    ;

type_defStatement
    : TYPE_DEF IDENTIFIER LBRACE type_def_list+ RBRACE
    ;

type_def_list
    : DATA_TYPE IDENTIFIER SEMI
    ;

// Function parameters
param_list
    : DATA_TYPE IDENTIFIER (COMMA DATA_TYPE IDENTIFIER)*
    ;

// Array Definition
int_Array
    : LBRACKET (NUMBER (COMMA NUMBER)*) RBRACKET
    ;

char_Array
    : LBRACKET (CHARACTER (COMMA CHARACTER)*) RBRACKET
    ;

strArray
    : LBRACKET (STRING (COMMA STRING)*) RBRACKET
    ;

// Continue / Break
continue_stmt
    : CONTINUE SEMI
    ;

break_stmt
    : BREAK SEMI
    ;
