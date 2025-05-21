# stack.py

class Node:
    """
    Clase para representar un nodo en la pila enlazada.
    Cada nodo contiene un dato y una referencia al siguiente nodo.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        """
        Inicializa una pila vacía con la cima apuntando a None.
        """
        self.top = None  # Nodo superior de la pila

    def is_empty(self):
        """
        Verifica si la pila está vacía.

        Returns:
            bool: True si la pila está vacía, False si contiene elementos.
        """
        return self.top is None

    def push(self, item):
        """
        Inserta un nuevo elemento en la cima de la pila.

        Args:
            item: El dato a almacenar en el nuevo nodo de la pila.
        """
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Elimina y devuelve el elemento en la cima de la pila.

        Returns:
            El dato almacenado en el nodo superior de la pila.

        Raises:
            IndexError: Si se intenta desapilar de una pila vacía.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        """
        Devuelve el elemento en la cima de la pila sin eliminarlo.

        Returns:
            El dato almacenado en el nodo superior de la pila.

        Raises:
            IndexError: Si la pila está vacía.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def size(self):
        """
        Calcula el número de elementos en la pila.

        Returns:
            int: La cantidad de nodos en la pila.
        """
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count