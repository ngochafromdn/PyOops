grammar syntax;

options {
    language = Python3;
}

// —--------------LEXER—-------------------------------

// 1. Keywords - placed before identifiers to prioritize correct keyword recognition
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
VOID : 'void';

// Data types
DATA_TYPE
    : 'int'
    | 'float'
    | 'str'
    | 'char'
    | 'int[]'
    | 'char[]'
    | 'str[]'
    ;

// 4. Newtype - Same as Struct
TYPE_DEF : 'type';

// 5. Literals
CHARACTER : '\'' ( ~['\\\r\n] | '\\' . ) '\'' ;
STRING : '"' ( ~["\\\r\n] | '\\' . )* '"' ;
NUMBER : [0-9]+('.'[0-9]+)?;

// 6. Operators - place 2-character operators before 1-character ones
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

// 7. Delimiters
SEMI : ';';
COMMA : ',';
LBRACE : '{';
RBRACE : '}';
LPAREN : '(';
RPAREN : ')';
LBRACKET : '[';
RBRACKET : ']';

// 8. Identifiers - placed near the end to avoid mistaking keywords as identifiers
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

// 9. Comments
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '---' ( . | '\r' | '\n' )*? '---' -> skip ;

// 10. Whitespace
WS : [ \t\r\n]+ -> skip;

// —--------------PARSER—-------------------------------

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
    | FUNC (DATA_TYPE | VOID )? IDENTIFIER LPAREN param_list? RPAREN block    # FuncStmt          
    | block                             # BlockStmt
    | type_defStatement                 # NewTypeDef
    | print_stmt SEMI                   # PrintStmt
    | continue_stmt                     # Continue
    | break_stmt                        # Break
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
    : IDENTIFIER ASSIGN (expression | int_Array | char_Array | strArray)
    ;
     
// Expressions
expression
    : '-' expression                                  # UnaryMinusExpr
    | expression (MUL | DIV) expression                 # MulDivExpr
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
    : IF LPAREN expression RPAREN block (ELSE IF LPAREN expression RPAREN block)*? (ELSE block)?
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
    : 'try' block ('except' block)  
    ;
    
// New type (Struct)
type_defStatement
    : TYPE_DEF IDENTIFIER LBRACE type_def_list+ RBRACE
    ;

type_def_list
    : DATA_TYPE IDENTIFIER SEMI
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



