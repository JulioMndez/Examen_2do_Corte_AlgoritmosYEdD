"""
Implementación de una cola de prioridad-
Los elementos se desencolan según su prioridad (número menor indica mayor prioridad).
"""
import time

class ColaPrioridadError(Exception):
    """Clase para manejar errores específicos de la cola de prioridad."""
    pass


class ElementoPrioridad:
    """Clase que representa un elemento con nombre y prioridad."""
    
    def __init__(self, nombre, prioridad):
        """Inicializa un elemento con nombre y prioridad."""
        if not isinstance(prioridad, int):
            raise ColaPrioridadError("La prioridad debe ser un número entero")
        
        self.nombre = nombre
        self.prioridad = prioridad
    
    def __str__(self):
        """Representación en cadena del elemento."""
        return f"{self.nombre} (prioridad: {self.prioridad})"


class Nodo:
    """Clase que representa un nodo en la cola de prioridad."""
    
    def __init__(self, elemento):
        """Inicializa un nodo con un elemento y sin referencia al siguiente."""
        self.elemento = elemento
        self.siguiente = None


class ColaPrioridad:
    """Implementación de una cola de prioridad usando nodos enlazados."""
    
    def __init__(self):
        """Inicializa una cola de prioridad vacía."""
        self.primero = None  # Frente de la cola
        self.tamanio = 0     # Contador de elementos
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return self.primero is None
    
    def encolar(self, nombre, prioridad):
        """
        Agrega un elemento a la cola según su prioridad.
        Los elementos con menor valor de prioridad se colocan más cerca del frente.
        """
        if nombre is None:
            raise ColaPrioridadError("El nombre no puede ser nulo")
            
        try:
            print("\n>>> Procesando: Agregando elemento a la cola...")
            time.sleep(2)
            
            # Crear el nuevo elemento y nodo
            nuevo_elemento = ElementoPrioridad(nombre, prioridad)
            nuevo_nodo = Nodo(nuevo_elemento)
            
            # Caso especial: cola vacía o el nuevo elemento tiene mayor prioridad que el primero
            if self.esta_vacia() or prioridad < self.primero.elemento.prioridad:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
                print(f">>> Elemento '{nombre}' agregado al frente de la cola con prioridad {prioridad}")
            else:
                # Buscar la posición correcta según la prioridad
                actual = self.primero
                while actual.siguiente and actual.siguiente.elemento.prioridad <= prioridad:
                    actual = actual.siguiente
                
                # Insertar el nuevo nodo en la posición correcta
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                print(f">>> Elemento '{nombre}' insertado en la cola con prioridad {prioridad}")
            
            self.tamanio += 1
            time.sleep(2)
            print(">>> Operación completada.")
        except Exception as e:
            raise ColaPrioridadError(f"Error al encolar: {str(e)}")
    
    def desencolar(self):
        """Elimina y devuelve el elemento con mayor prioridad (menor valor)."""
        if self.esta_vacia():
            raise ColaPrioridadError("No se puede desencolar de una cola vacía")
        
        try:
            print("\n>>> Procesando: Removiendo elemento con mayor prioridad...")
            time.sleep(2)
            
            # El elemento con mayor prioridad siempre está al frente
            elemento = self.primero.elemento
            
            # El segundo elemento pasa a ser el primero
            self.primero = self.primero.siguiente
            
            self.tamanio -= 1
            
            print(f">>> Elemento removido: {elemento}")
            time.sleep(2)
            print(">>> Operación completada.")
            return elemento
        except Exception as e:
            raise ColaPrioridadError(f"Error al desencolar: {str(e)}")
    
    def ver_frente(self):
        """Devuelve el elemento con mayor prioridad sin eliminarlo."""
        if self.esta_vacia():
            raise ColaPrioridadError("La cola está vacía")
            
        print("\n>>> Consultando elemento con mayor prioridad...")
        time.sleep(2)
        print(f">>> Elemento encontrado: {self.primero.elemento}")
        return self.primero.elemento
    
    def tamano(self):
        """Devuelve la cantidad de elementos en la cola."""
        print(f"\n>>> La cola contiene {self.tamanio} elementos.")
        return self.tamanio
    
    def vaciar(self):
        """Vacía la cola completamente."""
        print("\n>>> Procesando: Vaciando la cola...")
        time.sleep(2)
        
        self.primero = None
        self.tamanio = 0
        
        print(">>> La cola ha sido vaciada completamente.")
    
    def __str__(self):
        """Representación en cadena de la cola de prioridad."""
        if self.esta_vacia():
            return "Cola de prioridad vacía"
        
        try:
            print("\n>>> Generando representación de la cola...")
            time.sleep(2)
            
            resultado = "Cola de prioridad: "
            actual = self.primero
            
            while actual:
                resultado += str(actual.elemento)
                if actual.siguiente:
                    resultado += " -> "
                actual = actual.siguiente
            
            print(">>> Representación generada.")
            return resultado
        except Exception as e:
            return f"Error al representar la cola: {str(e)}"


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n===== COLA DE PRIORIDAD =====")
    print("1. Agregar elemento")
    print("2. Remover elemento con mayor prioridad")
    print("3. Ver elemento con mayor prioridad")
    print("4. Verificar si la cola está vacía")
    print("5. Ver tamaño de la cola")
    print("6. Mostrar toda la cola")
    print("7. Vaciar la cola")
    print("8. Salir")
    print("============================")


# Programa principal
if __name__ == "__main__":
    # Crear una nueva cola de prioridad
    mi_cola = ColaPrioridad()
    
    try:
        opcion = 0
        
        print("Bienvenido al programa de Cola de Prioridad")
        print("Los elementos con menor número de prioridad serán atendidos primero")
        
        while opcion != 8:
            mostrar_menu()
            
            try:
                opcion = int(input("\nSeleccione una opción (1-8): "))
                
                if opcion == 1:  # Agregar elemento
                    nombre = input("Ingrese el nombre del elemento: ")
                    prioridad = int(input("Ingrese la prioridad (número entero, menor = mayor prioridad): "))
                    mi_cola.encolar(nombre, prioridad)
                    
                elif opcion == 2:  # Remover elemento
                    if mi_cola.esta_vacia():
                        print("\n>>> La cola está vacía. No hay elementos para remover.")
                    else:
                        elemento = mi_cola.desencolar()
                        input("\nPresione Enter para continuar...")
                    
                elif opcion == 3:  # Ver frente
                    if mi_cola.esta_vacia():
                        print("\n>>> La cola está vacía. No hay elementos para mostrar.")
                    else:
                        mi_cola.ver_frente()
                        input("\nPresione Enter para continuar...")
                    
                elif opcion == 4:  # Verificar si está vacía
                    if mi_cola.esta_vacia():
                        print("\n>>> La cola está vacía.")
                    else:
                        print("\n>>> La cola NO está vacía.")
                    input("\nPresione Enter para continuar...")
                    
                elif opcion == 5:  # Ver tamaño
                    mi_cola.tamano()
                    input("\nPresione Enter para continuar...")
                    
                elif opcion == 6:  # Mostrar toda la cola
                    print("\n" + str(mi_cola))
                    input("\nPresione Enter para continuar...")
                    
                elif opcion == 7:  # Vaciar la cola
                    mi_cola.vaciar()
                    input("\nPresione Enter para continuar...")
                    
                elif opcion == 8:  # Salir
                    print("\n¡Gracias por usar el programa de Cola de Prioridad!")
                    
                else:
                    print("\n>>> Opción no válida. Por favor, seleccione una opción del 1 al 8.")
                    input("\nPresione Enter para continuar...")
                    
            except ValueError:
                print("\n>>> Error: Debe ingresar un número entero.")
                input("\nPresione Enter para continuar...")
        
    except ColaPrioridadError as e:
        print(f"\n>>> Error en la cola de prioridad: {e}")
        input("\nPresione Enter para continuar...")
    except Exception as e:
        print(f"\n>>> Error inesperado: {e}")
        input("\nPresione Enter para continuar...")