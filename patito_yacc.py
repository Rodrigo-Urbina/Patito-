import ply.yacc as yacc
import sys

success = True

from patito_lex import tokens

##gramatic rules
def p_program(p):
    '''
    program : PROGRAM ID COLON vars bloque
            | PROGRAM ID COLON bloque
    '''

def p_vars(p):
    '''
    vars : VAR varAUX2
    '''

def p_varAUX(p):
    '''
    varAUX : ID
           | ID COMA varAUX
    '''


def p_varAUX2(p):
    '''
    varAUX2 : varAUX COLON tipo SEMICOLON
            | varAUX COLON tipo SEMICOLON varAUX2
    '''

def p_tipo(p):
    '''
    tipo : INT
        | FLOAT
    '''

def p_bloque(p):
    '''
    bloque : LBRACKET RBRACKET
            | LBRACKET bloqueAUX RBRACKET
    '''

def p_bloqueAUX(p):
    '''
    bloqueAUX : estatuto
                 | estatuto bloqueAUX
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
            | condicion
            | escritura
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUAL expresion SEMICOLON
    '''


def p_escritura(p):
    '''
    escritura : PRINT LPARENT escrituraAUX RPARENT SEMICOLON
    '''

def p_escrituraAUX(p):
    '''
    escrituraAUX : expresion
                 | CTE_STRING
                 | expresion COMA escrituraAUX
                 | CTE_STRING COMA escrituraAUX
    '''

def p_expresion(p):
    '''
    expresion : exp
             | exp GREATERTHAN exp
             | exp LESSTHAN exp
             | exp NOEQUAL exp
    '''

def p_condicion(p):
    '''
    condicion : IF LPARENT expresion RPARENT bloque SEMICOLON
              | IF LPARENT expresion RPARENT bloque ELSE bloque SEMICOLON
    '''

def p_exp(p):
    '''
    exp : termino
        | termino PLUS exp
        | termino MINUS exp
    '''
def p_termino(p):
    '''
    termino : factor
            | factor MULT termino
            | factor DIV termino
    '''

def p_factor(p):
    '''
    factor : LPARENT expresion RPARENT
           | factorAUX
    '''

def p_factorAUX(p):
    '''
    factorAUX : PLUS varCte
              | MINUS varCte
              | varCte
    '''

def p_varCte(p):
    '''
    varCte : ID
           | CTE_I
           | CTE_F
    '''

##error function for parser
def p_error(p):
    global success
    success = False
    print("Error de sintaxis en '%s'" % p.value)


parser = yacc.yacc()


data = "testFile.txt"
f = open(data,'r')
s = f.read()

parser.parse(s)

if success == True:
    print("El archivo se ha aceptado")
    sys.exit()
else:
    print("El archivo tiene errores")
    sys.exit()
