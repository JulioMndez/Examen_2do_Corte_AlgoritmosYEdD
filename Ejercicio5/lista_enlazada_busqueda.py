"""
Implementación de una lista enlazada con función de búsqueda.
"""

class Nodo:
    """Clase que representa un nodo en la lista enlazada."""
    
    def __init__(self, dato):
        """Inicializa un nodo con un dato y sin referencia al siguiente."""
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Implementación de una lista enlazada simple."""
    
    def __init__(self):
        """Inicializa una lista enlazada vacía."""
        self.cabeza = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None
    
    def agregar(self, dato):
        """Agrega un elemento al final de la lista."""
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
        self.tamanio += 1
    
    def buscar(self, valor):
        """
        Busca un valor específico en la lista enlazada.
        
        Args:
            valor: El valor a buscar en la lista.
            
        Returns:
            Si se encuentra el valor, devuelve una tupla (True, posición).
            Si no se encuentra, devuelve (False, None).
        """
        if self.esta_vacia():
            return False, None
        
        actual = self.cabeza
        posicion = 0
        
        while actual:
            if actual.dato == valor:
                return True, posicion
            actual = actual.siguiente
            posicion += 1
        
        return False, None
    
    def __str__(self):
        """Representación en cadena de la lista enlazada."""
        if self.esta_vacia():
            return "Lista vacía"
        
        resultado = "Lista: "
        actual = self.cabeza
        
        while actual:
            resultado += str(actual.dato)
            if actual.siguiente:
                resultado += " -> "
            actual = actual.siguiente
            
        return resultado


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una nueva lista enlazada
    mi_lista = ListaEnlazada()
    
    # Agregar elementos
    elementos = [10, 20, 30, 40, 50]
    print("Agregando elementos a la lista:")
    for elemento in elementos:
        mi_lista.agregar(elemento)
        print(f"  Agregado: {elemento}")
    
    # Mostrar la lista
    print("\nLista completa:")
    print(mi_lista)
    
    # Realizar búsquedas
    valores_a_buscar = [30, 25, 50, 10, 60]
    
    print("\nRealizando búsquedas:")
    for valor in valores_a_buscar:
        encontrado, posicion = mi_lista.buscar(valor)
        
        if encontrado:
            print(f"  El valor {valor} se encuentra en la posición {posicion}")
        else:
            print(f"  El valor {valor} no se encuentra en la lista")
    
    # Ejemplo interactivo
    print("\n--- Búsqueda interactiva ---")
    while True:
        entrada = input("\nIngrese un valor a buscar (o 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            break
        
        try:
            valor = int(entrada)
            encontrado, posicion = mi_lista.buscar(valor)
            
            if encontrado:
                print(f"El valor {valor} se encuentra en la posición {posicion}")
            else:
                print(f"El valor {valor} no se encuentra en la lista")
                
        except ValueError:
            print("Por favor, ingrese un número entero válido")
    
    print("\n¡Gracias por usar el programa de búsqueda en lista enlazada!")