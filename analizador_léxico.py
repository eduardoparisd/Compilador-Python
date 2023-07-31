from ex_regulares import *
from patrones import *
import re

# ANALIZADOR LÉXICO

class Nodo:
    def __init__(self, valor, tipo=None, hijos=None):
        self.valor = valor
        self.tipo = tipo  # Agregamos el atributo tipo para almacenar el tipo de la variable
        self.hijos = hijos if hijos else []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

"""
Primeramente creo una función llamada lexer que tomará el código fuente como entrada.
Gracias a esta función podremos analizar el código fuente y poder generar tokens.
"""
def lexer(d_entrada):
    #Se crea una lista vacía para almacenar estos tokens que seran retornados al final.
    tokens = []
    #Esta otra variable es solo para mostrar en pantalla como estaría funcionando.
    tokens_demos = []
    #Tendremos un valor actual para rastrear nuestra posición en el ciclo.
    actual = 0
    """
    Comenzaremos creando un bucle while donde estaremos configurando nuestro valor actual que
    estaremos incrementando tanto como sea posible dentro del bucle para poder recorrer el código
    fuente carácter por carácter.

    Incrementamos nuestro valor actual, esto gracias a que es posible que nuestros tokens puedan tener cualquier longitud.
    """
    while actual < len(d_entrada):
        encontrado = False
        caracter = d_entrada[actual]  

        for palabra in tokenzz:
            """
            Por ejemplo, si d_entrada es igual a "Hola mundo" y actual tiene un valor de 4, 
            entonces d_entrada[actual:] devolverá la subcadena "mundo" 
            (los caracteres desde el índice 4 hasta el final de la cadena).
            """
            if re.search(r'\b'+palabra+r'\b', d_entrada[actual:]):
                tokens_demos.append({'c.lexica': tokenzz[41], 'lexema': palabra})
                tokens.append(palabra)
                actual += len(palabra)
                encontrado = True
                break

        if not encontrado:
            #####################################################
            #                   IDENTIFICADOR                   #
            #####################################################
            if re.match(IDENTIFICADOR, d_entrada[actual:]):
                identificador_match = re.match(IDENTIFICADOR, d_entrada[actual:])
                identificador = identificador_match.group()
                tokens_demos.append({'c.lexica': tokenzz[16], 'lexema': identificador})
                tokens.append(identificador)
                actual += len(identificador)
                continue
 
            #####################################################
            #                     NÚMEROS                       #
            #####################################################
            #Almacenamos la coincidencia en numero_match
            if re.match(NUMERICO, d_entrada[actual:]):
                numero_match = re.match(NUMERICO, d_entrada[actual:])
                numero = numero_match.group()
                
                if re.search(PUNTO, numero):
                #if "." in numero: Hace exactamente lo mismo
                    tokens_demos.append({'c.lexica': tokenzz[18], 'lexema': numero})
                else:
                    tokens_demos.append({'c.lexica': tokenzz[17], 'lexema': numero})
                    
                tokens.append(numero)
                actual += len(numero)
                continue

            #####################################################
            #              OPERADORES ARITMÉTICOS               #
            #####################################################
                
            #---------------------ADICIÓN---------------------
            elif re.match(ADICION, caracter):
            #if re.match(r'[\(\)\{\}\[\]]', caracter):
            #if caracter == "+":
            #if caracter == r'[\(\)\{\}\[\]]':
                tokens_demos.append({'c.lexica': tokenzz[19], 'lexema': caracter})
                tokens.append(caracter)
                #Incrementamos nuestra variable actual, para que recorra el siguiente valor de nuestros datos de entrada.
                actual += 1
                continue
                
            #---------------------SUSTRACCIÓN---------------------
            elif re.match(SUSTRACCION,caracter):
                tokens_demos.append({'c.lexica': tokenzz[20], 'lexema': caracter})
                tokens.append(caracter)
                actual +=1
                continue

            #---------------------MULTIPLICACIÓN y POTENCIA---------------------
            elif re.match(MUL_POT,caracter):
                if actual+1 < len(d_entrada) and d_entrada[actual+1] == caracter:
                    tokens_demos.append({'c.lexica': tokenzz[24], 'lexema': caracter+caracter})
                    tokens.append(caracter+caracter)
                    actual +=2
                    continue
                else:
                    tokens_demos.append({'c.lexica': tokenzz[21], 'lexema': caracter})
                    tokens.append(caracter)
                    actual +=1
                    continue

            elif re.match(POTENCIA, caracter):
                    tokens_demos.append({'c.lexica': tokenzz[24], 'lexema': caracter})
                    tokens.append(caracter)
                    actual +=1
                    continue

            #---------------------DIVISIÓN---------------------
            elif re.match(DIVISION,caracter):
                tokens_demos.append({'c.lexica': tokenzz[22], 'lexema': caracter})
                tokens.append(caracter)
                actual +=1
                continue
            #---------------------MÓDULO----------------------
            elif re.match(MODULO,caracter):
                tokens_demos.append({'c.lexica': tokenzz[23], 'lexema': caracter})
                tokens.append(caracter)
                actual +=1
                continue

            #####################################################
            #              OPERADORES LÓGICOS                   #
            #####################################################

            #---------------------AND------------------------- 
            elif re.match(AND, caracter):
                if actual+1 < len(d_entrada) and d_entrada[actual+1] == caracter:
                    tokens_demos.append({'c.lexica': tokenzz[13], 'lexema': caracter+caracter})
                    tokens.append(caracter+caracter)
                    actual += 2
                    continue
                else:
                    raise ValueError(f"({caracter}) No es un caracter único. Quisiste decir: {caracter+caracter}")
                
            #---------------------OR--------------------------     
            elif re.match(OR, caracter):
                if actual+1 < len(d_entrada) and d_entrada[actual+1] == caracter:
                    tokens_demos.append({'c.lexica': tokenzz[14], 'lexema': caracter+caracter})
                    tokens.append(caracter+caracter)
                    actual += 2
                    continue
                else:
                    raise ValueError(f"({caracter}) No es un caracter único. Quisiste decir: {caracter+caracter}")
            
            #---------------------NOT--------------------- 
            elif re.match(NOT,caracter):    
                tokens_demos.append({'c.lexica': tokenzz[15], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue

            #####################################################
            #              OPERACIONES COMPARATIVAS             #
            #####################################################

            #---------------------ASIGNACIÓN--------------------- 
            elif re.match(ASIGNACION,caracter): 
                tokens_demos.append({'c.lexica': tokenzz[30], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue
            
            #---------------------MENORQ--------------------- 
            elif re.match(MENORQ,caracter):   
                tokens_demos.append({'c.lexica': tokenzz[25], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue
            #---------------------MAYORQ--------------------- 
            elif re.match(MAYORQ,caracter):                  
                tokens_demos.append({'c.lexica': tokenzz[26], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue

            #####################################################
            #                   DELIMITADORES                   #
            #####################################################

            #---------------------PUNTOCOMA---------------------
            elif re.match(PUNTOCOMA,caracter): 
                tokens_demos.append({'c.lexica': tokenzz[31], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue

            #---------------------COMA---------------------
            elif re.match(COMA,caracter):
                tokens_demos.append({'c.lexica': tokenzz[32], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue

            #---------------------PARENTESIS---------------------
            elif re.match(PARENTESIS,caracter):
                if caracter == "(":  
                    tokens_demos.append({'c.lexica': tokenzz[33], 'lexema': caracter})
                    tokens.append(caracter)
                    actual += 1
                    continue
                else: 
                    tokens_demos.append({'c.lexica': tokenzz[34], 'lexema': caracter})
                    tokens.append(caracter)
                    actual += 1
                    continue
                
            #---------------------CORCHETES---------------------
            elif re.match(CORCHETES,caracter):
                if caracter == "[":    
                    tokens_demos.append({'c.lexica': tokenzz[35], 'lexema': caracter})
                    tokens.append(caracter)
                    actual += 1
                    continue

                else:
                    tokens_demos.append({'c.lexica': tokenzz[36], 'lexema': caracter})
                    tokens.append(caracter)
                    actual += 1
                    continue
                
            #---------------------LLAVES---------------------
            elif re.match(LLAVES,caracter):
                if caracter == "{":    
                    tokens_demos.append({'c.lexica': tokenzz[37], 'lexema': caracter})
                    tokens.append(caracter)
                    actual += 1
                    continue
                else:  
                    tokens_demos.append({'c.lexica': tokenzz[38], 'lexema': caracter})
                    tokens.append(caracter)
                    actual += 1
                    continue

            #---------------------ESPACIO--------------------- 
            elif re.match(ESPACIO,caracter):                    
                #SI ENCUENTRA UN ESPACI SIMPLEMENTE NO LO TOMA EN CUENTA
                actual += 1
                continue
                
            #---------------------PUNTO---------------------
            elif re.match(PUNTO,caracter):
                tokens_demos.append({'c.lexica': tokenzz[40], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue
            
            #---------------------COMILLAS---------------------
            #elif re.match(COMILLAS,caracter):
            elif caracter == COMILLAS:
                tokens_demos.append({'c.lexica': tokenzz[42], 'lexema': caracter})
                tokens.append(caracter)
                actual += 1
                continue

            else:    
                raise ValueError(f"No se pudo reconocer el token: {caracter}")
        
    
    #print(tokens_demos)
    #print(tokens)
    return tokens
