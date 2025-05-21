"""Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que
determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
Use una pila para realizar el seguimiento de los paréntesis abiertos."""

from verificador import esta_balanceada

# Función que muestra el menú interactivo
def menu():
    while True:
        print("\n--- Verificador de Paréntesis Balanceados ---")
        print("1. Verificar cadena")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Solicita al usuario una cadena de texto
            cadena = input("Ingresa una cadena con paréntesis: ")

            # Verifica si la cadena está balanceada o no
            resultado = esta_balanceada(cadena)

            if resultado == "sin parentesis":
                print("La cadena no contiene ningún paréntesis.")
            elif resultado is True:
                print("La cadena está balanceada.")
            else:
                print("La cadena NO está balanceada.")

        elif opcion == "2":
            # Finaliza el programa
            print("Saliendo del programa.")
            break
        else:
            # Mensaje en caso de que se elija una opción inválida
            print("Opción inválida. Intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
