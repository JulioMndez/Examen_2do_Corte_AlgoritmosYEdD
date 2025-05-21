from nodo import Nodo

class ListaReproduccion:
    def __init__(self):
        # Inicio de la lista (primera canción)
        self.inicio = None
        # Canción actual que se está reproduciendo
        self.actual = None

    def agregar_cancion(self, cancion):
        # Crea un nuevo nodo con la canción
        nuevo = Nodo(cancion)

        if self.inicio is None:
            # Si la lista está vacía, el nuevo nodo es el inicio y el actual
            self.inicio = nuevo
            self.actual = nuevo
        else:
            # Agrega al final de la lista
            temp = self.inicio
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp

    def eliminar_cancion(self, cancion):
        if self.inicio is None:
            print("La lista está vacía.")
            return

        temp = self.inicio
        while temp:
            if temp.cancion == cancion:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.inicio = temp.siguiente

                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior

                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior

                print(f"Canción '{cancion}' eliminada.")
                return
            temp = temp.siguiente

        print(f"Canción '{cancion}' no encontrada.")

    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print("Reproduciendo:", self.actual.cancion)
        else:
            print("No hay siguiente canción.")

    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print("Reproduciendo:", self.actual.cancion)
        else:
            print("No hay canción anterior.")

    def mostrar_lista(self):
        if self.inicio is None:
            print("Lista vacía.")
            return
        temp = self.inicio
        print("\nLista de reproducción:")
        while temp:
            indicador = " <-- [Reproduciendo]" if temp == self.actual else ""
            print(f"• {temp.cancion}{indicador}")
            temp = temp.siguiente
