Lista = []
def cargarContenido(dato):
    Lista.append(dato)

def imprimirLista():
    print(Lista)

def quitarDeLista(dato):
    Lista.remove(dato)

if __name__ == "__main__":
    cargarContenido("MILIII")
    cargarContenido("DURE")
    imprimirLista()
    quitarDeLista("MILIII")
    imprimirLista()
