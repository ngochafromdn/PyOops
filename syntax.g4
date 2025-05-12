grammar syntax;

options {
    language = Python3;
}

// LEXER
// Keywords
IF : 'if';
ELSE : 'else';
WHILE : 'while';
FUNC: 'func';
RETURN: 'return';
PRINT: 'print';
TRY: 'try';
EXCEPT: 'except';
TRUE : 'true';
FALSE : 'false';
CONTINUE: 'continue';
BREAK: 'break';


// Identifiers and literals
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER : [0-9]+('.'[0-9]+)?;

// DATA TYPES
// Primitive
INT : 'int';
FLOAT : 'float';
STR : 'str';
CHAR : 'char';
TYPE_DEF: 'type';

DATA_TYPE
    : INT
    | FLOAT
    | STR
    | CHAR
    | TYPE_DEF
    ;

<<<<<<< Updated upstream
// ARRAY TYPES
ARR_INT : 'int[]';
ARR_CHAR : 'char[]';
ARR_STR : 'str[]';
=======
// 3. Newtype (Struct)
TYPE_DEF : 'type';
DOT : '.';
>>>>>>> Stashed changes

ARR_TYPE
    : ARR_INT 
    | ARR_CHAR 
    | ARR_STR 
    ;

// Char & String with escape sequences
CHARACTER : '\'' ( ~['\\\r\n] | '\\' . ) '\'' ;
STRING : '"' ( ~["\\\r\n] | '\\' . )* '"';

// Delimiters
SEMI : ';';
COMMA : ',';
LBRACE : '{';
RBRACE : '}';
LPAREN : '(';
RPAREN : ')';
LBRACKET : '[';
RBRACKET : ']';

// Operators    
ASSIGN : '=';
MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';
LT : '<';
LE : '<=';
GT : '>';
GE : '>=';
EQ : '==';
NE : '!=';
AND : 'and';
OR : 'or';
NOT : '!';

// Whitespace
WS : [ \t\r\n]+ -> skip;
    
// Comment
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '---' ( . | '\r' | '\n' )*? '---' -> skip ;

// PARSER
program
    : statement* EOF
    ;

// Statement 
statement 
    : assignment SEMI                   # AssignStmt
<<<<<<< Updated upstream
    | variable_declaration SEMI         # VarDeclStmt
    | if_stmt                           # IfStmt
    | while_stmt                        # WhileStmt
    | try_stmt                          # TryStmt
    | return_stmt SEMI                  # ReturnStmt
    | func_def                          # FuncStmt
    | block                             # BlockStmt
    | type_defStatement                 # NewTypeDef
    | print_stmt SEMI                   # PrintStmt
=======
    | variable_declaration SEMI        # VarDeclStmt
    | if_stmt                          # IfStmt
    | while_stmt                       # WhileStmt
    | try_stmt                         # TryStmt
    | return_stmt SEMI                 # ReturnStmt
    | FUNC (DATA_TYPE | VOID)? IDENTIFIER LPAREN param_list? RPAREN block # FuncStmt
    | block                            # BlockStmt
    | type_defStatement                # TypeDef
    | print_stmt SEMI                  # PrintStmt
    | continue_stmt                    # Continue
    | break_stmt                       # Break
    | function_call SEMI               # FuncCallStmt
    | type_defDeclaration SEMI         # TypeDefDeclStmt
>>>>>>> Stashed changes
    ;

// Block
block
    : LBRACE statement* RBRACE
    ;

// Variable Declaration
variable_declaration
    : DATA_TYPE IDENTIFIER (ASSIGN expression)?
    | ARR_INT IDENTIFIER (ASSIGN int_Array)?
    | ARR_CHAR IDENTIFIER (ASSIGN char_Array)?
    | ARR_STR IDENTIFIER (ASSIGN strArray)?
    ;  

// Assignment
assignment
<<<<<<< Updated upstream
    : IDENTIFIER ASSIGN (expression | int_Array | char_Array | strArray)
    ;
     
// Expressions
expression
    : expression (MUL | DIV) expression                 # MulDivExpr
    | expression (ADD | SUB) expression                 # AddSubExpr
    | expression (LT | LE | GT | GE | EQ | NE) expression       # CompExpr
    | expression (AND | OR) expression                  # LogicExpr
    | NOT LPAREN  expression RPAREN                     # NotExpr
    | LPAREN expression RPAREN                          # ParenExpr
    | TRUE                                                      # TrueExpr
    | FALSE                                                     # FalseExpr
    | IDENTIFIER                                                # IdExpr
    | NUMBER                                                    # NumberExpr
    | STRING                                                    # StringExpr
    | CHARACTER                                         # CharExpr
=======
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
    | type_defVar                                     # VarTypeDef
    ;

// Function call
function_call
    : IDENTIFIER LPAREN arg_list? RPAREN
    ;

arg_list
    : expression (COMMA expression)*
>>>>>>> Stashed changes
    ;

// If / While
if_stmt
    : IF LPAREN expression RPAREN block (ELSE IF LPAREN expression RPAREN block)* (ELSE block)?
    ;   
    
while_stmt
    : WHILE LPAREN expression RPAREN block (continue_stmt | break_stmt)*
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
    : TRY block (except_clause)
    ;
    
except_clause
    : EXCEPT block
    ;
     
// New type (Struct)
type_defDeclaration
    : IDENTIFIER IDENTIFIER  // e.g., newtype sth;
    ;

type_defVar
    : IDENTIFIER DOT IDENTIFIER
    ;

type_defStatement
    : TYPE_DEF IDENTIFIER LBRACE ((DATA_TYPE | ARR_TYPE) IDENTIFIER SEMI)* RBRACE;
    
// Function
func_def
    : FUNC (DATA_TYPE)? IDENTIFIER LPAREN param_list? RPAREN block
    ;
     
param_list
    : DATA_TYPE IDENTIFIER (COMMA DATA_TYPE IDENTIFIER)*
    ;
    
     
// Array Definition
int_Array 
    : LBRACKET (NUMBER (COMMA NUMBER)*)? RBRACKET		    # IntArray
    ;

char_Array
    : LBRACKET (CHARACTER (COMMA CHARACTER)*)? RBRACKET	    # CharArray
    ;

strArray
    : LBRACKET (STRING (COMMA STRING)*)? RBRACKET			# StringArray
    ;


// Continue / Break
continue_stmt
    : CONTINUE SEMI
    ;
    
break_stmt
    : BREAK SEMI
    ;


