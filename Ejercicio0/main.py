from infix_to_postfix import infix_to_postfix
from evaluate_postfix import evaluate_postfix

def main():
    """
    Función principal que ejecuta la conversión y evaluación de expresiones.
    """
    infix_expression = "3 + 5 * ( 2 - 8 )"
    print("Expresión infija:", infix_expression)

    postfix_expression = infix_to_postfix(infix_expression)
    print("Expresión en postfijo:", postfix_expression)

    result = evaluate_postfix(postfix_expression)
    print("Resultado de la evaluación:", result)

if __name__ == "__main__":
    main()