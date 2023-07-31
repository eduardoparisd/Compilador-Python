palabras_reservadas = (
    'func',#0
    'return',#1
    'print',#2
    #Tipos de datos
    'float',#3
    'str',#4
    'int',#5
    'null',#6
    #Booleanos
    'True',#7
    'False',#8
    #Condicionales
    'if',#9
    'else',#10
    #Bucles
    'while',#11
    'for',#12
    #Operadores Lógicos
    'AND',#13
    'OR',#14
    'NOT'#15
)

tokenzz = palabras_reservadas + (
    'IDENTIFICADOR',#16

    #NUMERICOS
    'ENTERO',#17
    'DECIMAL',#18

    #ARITMÉTICOS
    'ADICION',#19
    'SUSTRACCION',#20
    'MULTIPLICACION',#21
    'DIVISION',#22
    'MODULO',#23
    'POTENCIA',#24

    #COMPARADORES
    'MENORQ',#25
    'MAYORQ',#26
    'MAIGUALQ',#27
    'MEIGUALQ',#28
    'DESIGUALDAD',#29
    'ASIGNACION',#30

    #DELIMITADORES
    'PUNTOCOMA',#31
    'COMA',#32
    'PARAIZQ',#33
    'PARDER',#34
    'CORIZQ',#35
    'CORDER',#36
    'LLAIZQ',#37
    'LLADER',#38
    'ESPACIO',#39
    'PUNTO',#40

    'PALABRA RESERVADA',#41
    'COMILLAS'#42
)

