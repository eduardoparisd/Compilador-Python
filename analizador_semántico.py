class Nodo:
    def __init__(self, valor, tipo=None, hijos=None):
        self.valor = valor
        self.tipo = tipo  # Agregamos el atributo tipo para almacenar el tipo de la variable
        self.hijos = hijos if hijos else []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def semantic(arbol, resultados_asignaciones):
    if arbol is not None:
        resultado = evaluar_arbol(arbol[0])
        if resultado is not None:
            #print(resultado)
            return resultado
    else:
        print("Error en el número de sentencias.")


def errores():
    return SyntaxError("Error de Sintaxis.")


def evaluar_arbol(nodo):
    
    if not nodo:
        return None

    if not nodo.hijos:
        return convertir_tipo(nodo.valor)

    operador = nodo.valor

    hijo_izq = evaluar_arbol(nodo.hijos[0])
    hijo_der = evaluar_arbol(nodo.hijos[1])

    if operador == "+":
        return hijo_izq + hijo_der
    elif operador == "-":
        return hijo_izq - hijo_der
    elif operador == "*":
        return hijo_izq * hijo_der
    elif operador == "/":
        return hijo_izq / hijo_der

def convertir_tipo(valor):
    if '.' in valor:
        return float(valor)
    elif valor.isdigit():
        return int(valor)
    else:
        return variables.get(valor, None)

#Diccionario para almacenar las variablesy sus valores.
variables = {}