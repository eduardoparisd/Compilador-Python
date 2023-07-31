from analizador_sintáctico import *
from analizador_léxico import *
from analizador_semántico import *

def procesar_asignacion(asignacion, resultados_asignaciones):
    # Separar la variable y la expresión
    variable, expresion = asignacion.split("=")
    variable = variable.strip()
    expresion = expresion.strip()

    # Realizar el análisis léxico y sintáctico de la expresión
    a_lexico = lexer(expresion)
    a_sintáctico = parser(a_lexico)

    if a_sintáctico is None:
        print(f"Error en la sintaxis de la asignación: {asignacion}")
        return

    # Evaluar la expresión y almacenar el resultado en la variable correspondiente
    resultado = semantic(a_sintáctico,resultados_asignaciones)
    if resultado is not None:
        variables[variable] = resultado
        resultados_asignaciones[variable] = resultado

def main():
    run = True
    resultados_asignaciones = {} # Diccionario para almacenar los resultados de las asignaciones
    while run:        
        text = input("--> ")

        if not text:
            continue

        if "=" in text:
            procesar_asignacion(text, resultados_asignaciones)
        elif text.startswith("print(") and text.endswith(")"):
            variable = text[6:-1].strip()  # Obtenemos el nombre de la variable de la función print
            if variable in resultados_asignaciones:
                print(resultados_asignaciones[variable])
            else:
                print(f"Error: La variable '{variable}' no está definida.")
        else:
            a_lexico = lexer(text)
            a_sintáctico = parser(a_lexico)

            if a_sintáctico is None:
                print("Error en la sintaxis.")
                continue

            semantic(a_sintáctico, resultados_asignaciones)


if __name__ == "__main__":
    main()
            
