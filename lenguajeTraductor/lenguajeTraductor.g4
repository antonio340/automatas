grammar lenguajeTraductor;

program: statement+ ;

statement
    : assignment
    | printStatement
    | ifStatement
    | elseBlock
    | functionDeclaration
    | functionCall
    | inputStatement
    | repeatStatement
    | whileStatement
    | returnVariable
    ;

assignment: ID '=' expression ;
printStatement: 'mostrar' (STRING | expression) ( '+' (STRING | expression) )* ;
ifStatement: 'si' condition 'entonces' block ( elseBlock )? ;
elseBlock: 'sino' block ; 
functionDeclaration: 'funcion' ID '(' parameters? ')' block ;
returnVariable: 'devolver' ID | expression ;
functionCall: 'activar' ID '(' arguments? ')' ;
inputStatement: 'guardar entrada en' ID ;
repeatStatement: 'repetir' ID 'hasta el valor de' ID block ;
whileStatement: 'mientras' condition block ;

block: '{' statement* '}' ;
condition: expression ( '>' expression | '<' expression | '==' expression | conditionBoolean) ;
conditionBoolean: (' es verdadero ' | ' es falso '); 
expression: (term ( ('+' | '-') term )* ) | ID ;
term: factor ( ('*' | '/') factor )* ;
factor: NUMBER | ID | '(' expression ')' ;

parameters: ID ( ',' ID )* ;
arguments: expression ( ',' expression )* ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
STRING: '"' .*? '"' ;
WS: [ \t\r\n]+ -> skip ;
