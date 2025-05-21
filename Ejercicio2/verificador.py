
from pila import Pila

def esta_balanceada(cadena):
    # Verifica si la cadena contiene algún paréntesis
    if not any(c in '()[]{}' for c in cadena):
        return "sin parentesis"

    # Crea una pila vacía para manejar los paréntesis abiertos
    pila = Pila()

    # Diccionario que asocia cada cierre con su apertura correspondiente
    pares = {')': '(', ']': '[', '}': '{'}

    # Recorre cada carácter de la cadena
    for caracter in cadena:
        if caracter in '([{':
            # Si es un paréntesis de apertura, se apila
            pila.apilar(caracter)
        elif caracter in ')]}':
            # Si es un paréntesis de cierre, se desapila y compara
            tope = pila.desapilar()
            if tope != pares[caracter]:
                # Si no coincide, los paréntesis no están balanceados
                return False

    # Si la pila quedó vacía, los paréntesis están correctamente balanceados
    return pila.esta_vacia()
