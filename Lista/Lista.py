from Lista.Nodo import Nodo

class ListaCircular:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertar(self,id,nombre,precio):
        if self.vacia():
            self.primero = self.ultimo = Nodo(nombre,id,nombre,precio)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(nombre,id,nombre,precio)
            self.ultimo.siguiente  = self.primero

    def recorrer(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.id, aux.nombre, aux.precio)
            aux = aux.siguiente
        print(aux.nombre)

    def buscar(self,buscar):
        aux = self.primero
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.primero:
                
                if aux.nombre == buscar:
                    return aux.precio
                    break 

                aux = aux.siguiente