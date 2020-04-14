import ply.lex as lex
import sys


##Declaration of tokens
tokens = [
    'ID',           ## variable
    'LPAREN',       ## (
    'RPAREN',       ## )
    'LBRACKET',     ## {
    'RBRACKET',     ## }
    'LSQUARE',      ## [
    'RSQUARE',      ## ]
    'COLON',        ## :
    'COMMA',        ## ,
    'SEMICOLON',    ## ;
    'COMMENT',      ## %%
    'CTE_I',        ## 123
    'CTE_F',        ## 123.123
    'CTE_C',        ## a
    'EQUAL',        ## =
    'LESSTHAN',     ## <
    'GREATERTHAN',  ## >
    'NOEQUAL',      ## <>
    'PLUS',         ## +
    'MINUS',        ## -
    'MULT',         ## *
    'DIV',          ## /
    'AND',          ## &
    'OR',           ## |
    'SAME',        ## ==
    'DETER',        ## $
    'TRANS',        ## ¡
    'INVER',        ## ?
    ]

##Reserved words
reserverd = {
    'programa' : 'PROGRAMA',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'void' : 'VOID',
    'principal' : 'PRINCIPAL',
    'funcion' : 'FUNCION',
    'regreso' : 'REGRESO',
    'lee' : 'LEE',
    'escribe' : 'ESCRIBE',
    'si' : 'SI',
    'entonces' : 'ENTONCES',
    'sino' : 'SINO',
    'mientras' : 'MIENTRAS',
    'haz' : 'HAZ',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'hacer' : 'HACER'
}



##tokens symbols
t_ignore = ' \t\n'

# Symbols
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COLON = r'\:'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_COMMENT = r'\%%'

# Comparison
t_EQUAL = r'\='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_NOEQUAL = r'\<>'
t_SAME = r'\=='

# Logic Operators
t_AND = r'\&'
t_OR = r'\|'

# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

# Matrix Operators
t_DETER = r'\$'
t_TRANS = r'\¡'
t_INVER = r'\?'

# Constants
t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_C = r'(\'[^\']*\')'

tokens = tokens + list(reserverd.values())

##declaration for letters with words ex hola93
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserverd.get(t.value,'ID')
    return t

##Lexer error function
def t_error(t):
    global success
    success = False
    print ("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()
