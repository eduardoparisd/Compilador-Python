from patrones import *
from ex_regulares import *
import re

class Nodo:
    def __init__(self, valor, tipo=None, hijos=None):
        self.valor = valor
        self.tipo = tipo
        self.hijos = hijos if hijos else []
    
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def parser(tokens):
    global variables
    actual = 0
    variables = {}
    
    def factor():
        nonlocal actual
        token_actual = tokens[actual]

        if re.search(NUMERICO, token_actual):
                nodo = Nodo(token_actual)
                actual += 1
                return nodo
            
        elif re.match(IDENTIFICADOR, token_actual):
                nodo = Nodo(token_actual)
                actual += 1
                return nodo
            
        elif token_actual == "(":
                actual += 1
                nodo_expr = expresion()

                if tokens[actual] == ")":
                    actual += 1
                    return nodo_expr
                else:
                    raise SyntaxError("Error de Sintaxis. Se esperaba ')'")
    
    def termino():
        nonlocal actual
        nodo = factor()
        
        while actual < len(tokens):
            token_actual = tokens[actual]
            
            if re.match(MUL_POT, token_actual):
                actual += 1
                nodo_op = Nodo(token_actual)
                nodo_op.agregar_hijo(nodo)
                nodo_op.agregar_hijo(factor())
                nodo = nodo_op

            elif re.match(DIVISION, token_actual):
                actual += 1
                nodo_op = Nodo(token_actual)
                nodo_op.agregar_hijo(nodo)
                nodo_op.agregar_hijo(factor())
                nodo = nodo_op
            else:
                break
        
        return nodo

    
    def expresion():
        nonlocal actual
        nodo = termino()


        while actual < len(tokens):
            token_actual = tokens[actual]

            if re.match(ADICION, token_actual):
                actual += 1
                nodo_op = Nodo(token_actual)
                nodo_op.agregar_hijo(nodo)
                nodo_op.agregar_hijo(termino())
                nodo = nodo_op

            elif re.match(SUSTRACCION, token_actual):
                actual += 1
                nodo_op = Nodo(token_actual)
                nodo_op.agregar_hijo(nodo)
                nodo_op.agregar_hijo(termino())
                nodo = nodo_op

            elif re.match(ASIGNACION, token_actual):
                actual += 1
                nodo_op = Nodo(token_actual)
                variable = nodo.valor
                nodo_op.agregar_hijo(nodo)
                nodo_op.agregar_hijo(termino())
                asignar_valor(variable, termino())
                nodo = nodo_op

            else:
                break
            
        return nodo

    def asignar_valor(variable, valor):
         global variables
         variables[variable] = valor.valor
         

    arbol_sintactico = [expresion()]

    if None in arbol_sintactico:
        return None

    return arbol_sintactico
    
    
   
'''
res_1 = 15 + 1.52*((15*4)/5)

          =
        /   \
     res_1    +
            /   \
          15   *
              /   \
            1.52   /
                   / \
                 *    5
                / \
              15   4

'''