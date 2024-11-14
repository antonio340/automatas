grammar traductorPythonaJava;

prog: stat+ ;
stat: funcDef | printStat ;
funcDef: DEF ID LPAREN params? RPAREN COLON body ;
params: ID (COMMA ID)* ;
body: (assignmentStat | returnStat)* ;
assignmentStat: ID EQ expr  ;
returnStat: RETURN expr ;
printStat: PRINT LPAREN exprList RPAREN  ;
exprList: expr (COMMA expr)* ;
expr: expr PLUS expr | ID | INT | funcCall ;
funcCall: ID LPAREN args? RPAREN ;
args: expr (COMMA expr)* ;

// Reglas léxicas
DEF: 'def' ;
RETURN: 'return' ;
PRINT: 'print' ;
EQ: '=' ;
PLUS: '+' ;
LPAREN: '(' ;
RPAREN: ')' ;
COLON: ':' ;
COMMA: ',' ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
INT: [0-9]+ ;
WS:[ \t\r\n]+ ->skip;

