from Lista.Nodo import Nodo

class ListaCircular:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertar(self,id,nombre,precio):
        if self.vacia():
            self.primero = self.ultimo = Nodo(id,nombre,precio)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(id,nombre,precio)
            self.ultimo.siguiente  = self.primero

    def verificar(self):
        if self.vacia():
            return ("No hay elementos en la lista")

    def recorrer(self):
        aux = self.primero
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.primero:
                print(aux.id,aux.precio)
                aux = aux.siguiente
            print(aux.id,aux.precio)
            
    def buscar(self,buscar):
        aux = self.primero
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.primero:
                
                if aux.id == buscar:
                    return aux.precio

                aux = aux.siguiente
            
            return "No existe"

    def buscarNombre(self,buscar):
        aux = self.primero
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.primero:
                
                if aux.id == buscar:
                    return aux.nombre

                aux = aux.siguiente
            
            return "No existe"