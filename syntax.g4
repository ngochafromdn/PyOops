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

// ARRAY TYPES
ARR_INT : 'int[]';
ARR_CHAR : 'char[]';
ARR_STR : 'str[]';

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
    | variable_declaration SEMI         # VarDeclStmt
    | if_stmt                           # IfStmt
    | while_stmt                        # WhileStmt
    | try_stmt                          # TryStmt
    | return_stmt SEMI                  # ReturnStmt
    | func_def                          # FuncStmt
    | block                             # BlockStmt
    | type_defStatement                 # NewTypeDef
    | print_stmt SEMI                   # PrintStmt
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
type_defStatement
    : TYPE_DEF IDENTIFIER LBRACE (DATA_TYPE IDENTIFIER SEMI)* RBRACE;
    
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


