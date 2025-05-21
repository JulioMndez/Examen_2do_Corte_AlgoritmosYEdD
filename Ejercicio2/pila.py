class Nodo:
    def __init__(self, dato):
        # Almacena el valor del nodo
        self.dato = dato
        # Apunta al siguiente nodo (el que está debajo en la pila)
        self.siguiente = None

class Pila:
    def __init__(self):
        # El tope de la pila inicia vacío
        self.tope = None

    def esta_vacia(self):
        # Retorna True si no hay elementos en la pila
        return self.tope is None

    def apilar(self, valor):
        # Crea un nuevo nodo con el valor recibido
        nuevo_nodo = Nodo(valor)
        # El nuevo nodo apunta al antiguo tope
        nuevo_nodo.siguiente = self.tope
        # Ahora el nuevo nodo es el tope de la pila
        self.tope = nuevo_nodo

    def desapilar(self):
        # Si la pila está vacía, no se puede desapilar
        if self.esta_vacia():
            return None
        # Guarda el valor actual del tope
        valor = self.tope.dato
        # El nuevo tope será el siguiente nodo
        self.tope = self.tope.siguiente
        return valor

    def ver_tope(self):
        # Devuelve el valor del nodo en el tope sin quitarlo
        if self.esta_vacia():
            return None
        return self.tope.dato
