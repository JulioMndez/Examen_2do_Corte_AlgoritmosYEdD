class Nodo:
    def __init__(self, cancion):
        # Canción actual
        self.cancion = cancion
        # Apunta a la siguiente canción
        self.siguiente = None
        # Apunta a la canción anterior (doblemente enlazada)
        self.anterior = None
