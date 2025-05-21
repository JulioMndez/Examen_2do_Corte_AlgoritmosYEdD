"""Ejercicio #3: Simulación de una lista de reproducción de música. Implemente
una lista de reproducción de música utilizando una lista enlazada. El programa debe
permitir agregar canciones, eliminar canciones, reproducir la siguiente canción,
reproducir la canción anterior y mostrar la lista de reproducción actual."""

from lista_reproduccion import ListaReproduccion

def menu():
    lista = ListaReproduccion()

    while True:
        print("\n--- Menú de Reproducción ---")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente")
        print("4. Reproducir anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cancion = input("Ingresa el nombre de la canción: ")
            lista.agregar_cancion(cancion)
        elif opcion == "2":
            cancion = input("Ingresa la canción a eliminar: ")
            lista.eliminar_cancion(cancion)
        elif opcion == "3":
            lista.siguiente()
        elif opcion == "4":
            lista.anterior()
        elif opcion == "5":
            lista.mostrar_lista()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
