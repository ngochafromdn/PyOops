grammar syntax;

// LEXER
// Keywords
IF : 'if';
ELSE : 'else';
WHILE : 'while';

// Identifiers and literals
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER : [0-9]+;

// DATA TYPES
// Boolean
TRUE : 'True';
FALSE : 'False';
NOT : '!';

// Char & String
CHAR : '\'' . '\'' ;
STRING : '"' (~["\\] | '\\' .)* '"' ;

// Delimiters
SEMI : ';';
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
AND : '&&';
OR : '||';

// Whitespace
WS : [ \t\r\n]+ -> skip;


// PARSER
program : statement* EOF;

statement
    : assignment ';'      # AssignStmt
    | ifStatement         # IfStmt
    | whileStatement      # WhileStmt
    | block               # BlockStmt
    ;

array 
    : '[' (INT (',' INT)*)? ']' 
    | '[' (CHAR (',' CHAR)*)? ']'
    | '[' (STRING (',' STRING)*)? ']';

assignment : IDENTIFIER '=' (expression | intArray );

ifStatement : 'if' '(' logicalExpression ')' statement ('else' statement)?;

whileStatement : 'while' '(' logicalExpression ')' statement;

block : '{' statement* '}';

logicalExpression
    : expression ('<' | '<=' | '>' | '>=' | '==' | '!=') expression  # CompExpr
    | logicalExpression ('&&' | '||') logicalExpression  # LogicExpr
    | '(' logicalExpression ')'            # ParenLogicExpr
    | NOT '(' logicalExpression ')'
    | TRUE
    | FALSE
    ;

expression
    : expression ('*' | '/' ) expression   # MulDivExpr
    | expression ('+' | '-' ) expression   # AddSubExpr
    | '(' expression ')'                    # ParenExpr
    | IDENTIFIER                            # IdExpr
    | NUMBER                                # Number
    | NOT '(' expression ')'
    | TRUE
    | FALSE
    ;