grammar Oper;
root : expr EOF ;
expr : expr MAS expr
     | expr MENOS expr
     | expr MULT expr
     | expr DIV expr
     | <assoc=right> expr POT expr 
     | NUM
     ;

NUM : [0-9]+ ;
MAS : '+' ;
MENOS : '-' ;
MULT : '*' ;
DIV : '/' ;
POT : '^' ; 
WS : [ \n]+ -> skip ;