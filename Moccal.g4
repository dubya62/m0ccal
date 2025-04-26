grammar Moccal;

////////////////////////////////////
// Parser rules
access_specifier: (PUBLIC | PRIVATE | PROTECTED) ;

moccal : NEWLINE* line* EOF ;

// TODO: fix this to not parse the contents (in the lexer)
c : C NEWLINE* scope ;

line : (expr | declaration | function | class | ctrl_block | continue | break | return | useas | for | while | directive | guarantee | assumption | scope | c) (SEMICOLON | NEWLINE)+ ;

guarantee : MUL MUL? MUL? NEWLINE* scope ;
assumption : NOT NOT? NOT? NEWLINE* scope ;

directive : imp | include ;
imp : HASHTAG IMPORT expr ;
include : HASHTAG INCLUDE expr ;

scope : LBRACE NEWLINE* line*? RBRACE ;

args : LPAREN NEWLINE* (expr expr (COMMA NEWLINE* expr expr)*)? NEWLINE* RPAREN ;

for : FOR NEWLINE* LPAREN NEWLINE* (declaration | expr)? NEWLINE* SEMICOLON NEWLINE* expr? NEWLINE* SEMICOLON NEWLINE* expr? NEWLINE* RPAREN NEWLINE* scope ;

while : WHILE NEWLINE* expr NEWLINE* scope ;

use : USE ~AS+ ;
as : AS ~NEWLINE+? ;
useas : use as ;

continue : CONTINUE ;
break : BREAK ;
return : RETURN NEWLINE* expr ;

ctrl_block : ifblock NEWLINE* (elifblock | NEWLINE)* elseblock? ;

ifblock : IF NEWLINE* expr NEWLINE* scope ; 
elifblock : ELIF NEWLINE* expr NEWLINE* scope ;
elseblock: ELSE NEWLINE* scope ;

class : (access_specifier)? NEWLINE* (CLASS | STRUCT) NEWLINE* ID NEWLINE* (EXTENDS expr)? scope ;

function : (access_specifier)? NEWLINE* (FUNCTION | API) NEWLINE* ID NEWLINE* args NEWLINE* (ARROW expr)? scope ;

declaration : LET NEWLINE* expr (COLON expr)?;

expr : 
    INT | FLOAT | STRING | THIS | SUPER | array_literal | ID
    | NEWLINE expr
    | expr NEWLINE
    | expr DOT expr
    | (LOGNOT | DOT | NOT | COPY) expr
    | expr args
    | LPAREN expr RPAREN
    | expr LBRACK expr RBRACK
    | expr (MUL | DIV | MOD) expr
    | expr (SUB | ADD) expr
    | SUB expr
    | expr (LT | LE | GT | GE) expr
    | expr (EQ | NE) expr
    | expr AND expr
    | expr XOR expr
    | expr OR expr
    | expr LOGAND expr
    | expr LOGOR expr
    | expr (SET | XOREQ | OREQ | MULEQ | SUBEQ | ADDEQ | DIVEQ | MODEQ) expr
    | expr COMMA expr
    ;

array_literal : LBRACK NEWLINE* expr? NEWLINE* RBRACK ;


////////////////////////////////////
// Lexer rules
fragment UPPERCASE : [A-Z] ;
fragment LOWERCASE : [a-z] ;
fragment DIGIT : [0-9] ;
fragment ALPHANUM : UPPERCASE | LOWERCASE | DIGIT ;

SINGLECOMMENT : ('//' ~[\r\n]*) -> skip;
MULTICOMMENT: ('/*' .*? '*/') -> skip;

FLOAT : DIGIT* DOT DIGIT+ ;
INT : DIGIT+ ;
STRING : '"' .*? '"' ;

EQ : '==' ;
LE : '<=' ;
GE : '>=' ;
NE : '!=' ;

XOREQ : '^=' ;
ANDEQ : '&=' ;
OREQ : '|=' ;
MULEQ : '*=' ;
SUBEQ : '-=' ;
ADDEQ : '+=' ;
DIVEQ : '/=' ;
MODEQ : '%=' ;

COMMA : ',' ;
DOT : '.' ;
LOGAND : 'and' ;
LOGOR : 'or' ;
LOGNOT : 'not' ;

NOT : '~' ;
MOD : '%' ;
XOR : '^' ;
AND : '&' ;
OR : '|' ;
SET : '=' ;
MUL : '*' ;
ADD : '+' ;
DIV : '/' ;
COPY : '!' ;
LT : '<' ;
GT : '>' ;
SUB : '-' ;
HASHTAG : '#' ;

LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
LBRACE : '{' ;
RBRACE : '}' ;

SEMICOLON : ';' ;
COLON : ':' ;

// keywords
C : 'C' ;
LET : 'let' ; 
THIS : 'this' ;
SUPER : 'super' ;

PUBLIC : 'public' ;
PRIVATE : 'private' ;
PROTECTED : 'protected' ;
FUNCTION : 'function' ;
API : 'api' ;
CLASS : 'class' ;
STRUCT : 'struct' ;
EXTENDS : 'extends' ;

IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;

CONTINUE : 'continue' ;
BREAK : 'break' ;
RETURN : 'return' ;

ARROW : '->' ;


USE : 'use' ;
AS : 'as' ;

FOR : 'for' ;
WHILE : 'while' ;

IMPORT : 'import' ;
INCLUDE : 'include' ;


ID : (LOWERCASE | UPPERCASE | '_') (ALPHANUM | '_')* ;

WHITESPACE : (' ' | '\t') -> skip ;
NEWLINE : ('\r'? '\n' | '\r')+ ;





