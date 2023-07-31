#ENTERO = r'\d+'
"""
Significados de los caracteres dentro de las expresiones
* indica que el elemento precedente puede repetirse cero o más veces. 
$ se utiliza para denotar el final de una línea o cadena.
? indica que el elemento precedente es opcional, es decir, puede aparecer cero o una vez. 
"""
IDENTIFICADOR = r'[_a-zA-Z][_a-zA-Z0-9]*'
ESPACIO = r' '
NUMERICO = r'\d+(\.\d+)?'

#OPERACIONES ARITMETICAS
ordn_precedencia = r'[*/%]'
ADICION = r'\+'
SUSTRACCION = r'-'
MUL_POT = r'\*'
DIVISION = r'/'
MODULO = r'%'
POTENCIA = r'\^'

#OPERACIONES LÓGICAS
AND = r'&'
OR = r'\|'
NOT = r'!'

#OPERACIONES COMPARATIVAS
ASIGNACION = r'='
MENORQ = r'<'
MAYORQ = r'>'
#MAIGUALQ = r'>='
#MEIGUALQ = r'<='
#DESIGUALDAD = r'<>'

#DELIMITADORES
PUNTO = r'\.'
PUNTOCOMA = r';'
COMA = r','
#PARIZQ = r'\('
#PARDER = r')'
#CORIZQ = r'['
#CORDER = r']'
#LLAIZQ = r'\{'
#LLADER = r'}'
PARENTESIS = r'\(|\)'
CORCHETES = r'\[|\]'
LLAVES = r'\{|\}'
COMILLAS = r'"'

#DISMINUCION = r'\-\-'
#AUMENTO = r'\+\+'
