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

def p_exp(p):
  '''
  exp: t_exp OR exp
  	 | t_exp
  '''

def p_t_exp(p):
  '''
  t_exp: g_exp AND t_exp
  		 | g_exp
  '''

def p_g_exp(p):
  '''
  g_exp: m_exp
  		| LESSTHAN m_exp
      |	LESSEQUAL m_exp
      | GREATERTHAN m_exp
      | GREATEREQUAL m_exp
      | EQUAL m_exp
      | NOEQUAL m_exp
  '''

def p_m_exp(p):
  '''
  m_exp: t
  		| t PLUS m_exp
      | t MINUS m_exp
  '''

def p_t(p):
  '''
  	t: f
    	| f MULT t
      | f DIV t
      | f DETER t
      | f TRANS t
      | f INVER t
  '''

def p_f(p):
  '''
  f: LPAREN exp RPAREN
  	| CTE_I
    | CTE_F
    | CTE_C
    | variable
    | llamada
  '''

def p_condicion(p):
  '''
  condicion: SI LPAREN exp RPAREN bloque SINO bloque SEMICOLON
  					|SI LPAREN exp RPAREN bloque SEMICOLON
  '''

def p_ciclo_w(p):
  '''
  ciclo_w: MIENTRAS LPAREN exp RPAREN HAZ bloque
  '''


def p_ciclo_f(p):
  '''
  ciclo_f: DESDE asigna HASTA CTE_I HAZ bloque
  '''




def p_var_cte(p):
	'''
  var_cte: exp
  		|CTE_I
      |CTE_F
  '''



def p_retorno(p):
  '''
  retorno: REGRESA exp SEMICOLON
  '''


##seccion de VARIABLES ya sea globales o de funcion
def p_vars(p):
  '''
  vars: VAR vars_aux
  '''

  ## seccion de vars para definir varios varios tipos de  id con o sin  brackets
def p_vars_aux(p):
  '''
  vars_aux: tipo_simple vars_aux1
  		| tipo_simple vars_aux1 vars_aux
  '''

  ##seccion de vars para ciclo de varias id con brackets
def p_vars_aux1(p):
  '''
  vars_aux1: vars_aux2 SEMICOLON
  		| vars_aux2 COMA vars_aux1
  '''

## seccion de vars para id con brackets
def p_vars_aux2(p):
  '''
    vars_aux2: id
    		| id LSQUARE CTE_I RSQUARE
        | id LSQUARE CTE_I RSQUARE LSQUARE CTE_I RSQUARE
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
