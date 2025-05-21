from stack import Stack

def evaluate_postfix(expression):
    """
    Evalúa una expresión matemática en notación postfija.

    Args:
        expression (str): Expresión postfija con tokens separados por espacios,
                          p. ej. "3 5 2 8 - * +".

    Returns:
        int or float: Resultado numérico de la evaluación.
    """
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            # Si el token es un número, apilarlo
            stack.push(int(token))
        else:
            # Operador: desapilar dos operandos y aplicar la operación
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                resultado = left + right
            elif token == '-':
                resultado = left - right
            elif token == '*':
                resultado = left * right
            elif token == '/':
                resultado = left / right
            else:
                raise ValueError(f"Operador desconocido: {token}")
            stack.push(resultado)

    # El resultado final es el último elemento en la pila
    return stack.pop()