from stack import Stack

def precedence(op):
    """
    Devuelve la precedencia del operador.

    Args:
        op (str): Operador matemático ('+', '-', '*', '/').

    Returns:
        int: Valor de precedencia (mayor valor = mayor precedencia).
    """
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    """
    Convierte una expresión matemática en notación infija a notación postfija.

    Args:
        expression (str): Expresión infija con tokens separados por espacios,
                          p. ej. "3 + 5 * ( 2 - 8 )".

    Returns:
        str: Expresión en notación postfija (tokens separados por espacios).
    """
    output = []
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            # Si el token es un operando, añadirlo a la salida
            output.append(token)
        elif token == '(':
            # Apilar paréntesis izquierdo
            stack.push(token)
        elif token == ')':
            # Desapilar hasta encontrar el paréntesis izquierdo
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Eliminar '(' de la pila
        else:
            # Operador encontrado: desapilar operadores con mayor o igual precedencia
            while (not stack.is_empty() and
                   precedence(stack.peek()) >= precedence(token)):
                output.append(stack.pop())
            stack.push(token)

    # Desapilar todos los operadores restantes
    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)