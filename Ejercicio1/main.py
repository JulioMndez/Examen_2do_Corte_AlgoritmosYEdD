# Definimos un nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Creamos una lista enlazada simple para manejar los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def como_lista(self):
        actual = self.cabeza
        resultado = []
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

# Función para invertir la frase usando nodos
def invertir_frase(frase):
    palabras = frase.split()  # Separa las palabras
    lista = ListaEnlazada()

    for palabra in palabras:
        lista.insertar_al_inicio(palabra)  # Inserta cada palabra al inicio

    palabras_invertidas = lista.como_lista()
    return ' '.join(palabras_invertidas)

# Ejemplo de uso
frase_original = "Hola mundo desde UAM"
frase_invertida = invertir_frase(frase_original)
print("Frase original:", frase_original)
print("Frase invertida:", frase_invertida)