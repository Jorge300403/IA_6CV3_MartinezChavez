#DEFINIMOS UN NODO EL CUAL SERA EL QUE IMPLEMENTAREMOS EN LAS ESTRUCTURAS
#EN DONDE COMO FUNCIONES TIENE UN VALOR Y UN APUNTADOR A SIGUIENTE
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

#PILA
class Pila:
    def __init__(self):
        self.cima = None

    def esta_vacia(self):
        return self.cima is None

    def push(self, objeto):
        nuevo_nodo = Nodo(objeto)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def pop(self):
        if self.esta_vacia():
            return None
        nodo_removido = self.cima
        self.cima = self.cima.siguiente
        return nodo_removido.valor

    def ver_cima(self):
        if self.esta_vacia():
            return None
        return self.cima.valor

    def mostrar_pila(self):
        actual = self.cima
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

#COLA
class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None

    def esta_vacia(self):
        return self.frente is None

    def insertar(self, objeto):
        nuevo_nodo = Nodo(objeto)
        if self.esta_vacia():
            self.frente = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def quitar(self):
        if self.esta_vacia():
            return None
        nodo_removido = self.frente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.ultimo = None
        return nodo_removido.valor

    def recorrer(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def buscar(self, objeto):
        actual = self.frente
        while actual:
            if actual.valor == objeto:
                return True
            actual = actual.siguiente
        return False

#LISTA
class ListaGenerica:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def insertar(self, objeto):
        nuevo_nodo = Nodo(objeto)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, objeto):
        if self.esta_vacia():
            return False

        if self.primero.valor == objeto:
            self.primero = self.primero.siguiente
            return True

        actual = self.primero
        anterior = None
        while actual:
            if actual.valor == objeto:
                anterior.siguiente = actual.siguiente  
                return True
            anterior = actual
            actual = actual.siguiente
            
        return False

    def recorrer(self):
        actual = self.primero
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
    


# Creando una pila
pila = Pila()
pila.push("objeto 1")
pila.push("objeto 2")
pila.push("objeto 3")
print("Pila:", pila.mostrar_pila()) 
print("Pop:", pila.pop())  
print("Pila:", pila.mostrar_pila()) 

# Creando una cola
cola = Cola()
cola.insertar("objeto A")
cola.insertar("objeto B")
cola.insertar("objeto C")
print("Cola:", cola.recorrer())  
print("Quitar:", cola.quitar()) 
print("Cola:", cola.recorrer())  

# Creando una lista genérica
lista = ListaGenerica()
lista.insertar("elemento 1")
lista.insertar("elemento 2")
lista.insertar("elemento 3")
print("Lista:", lista.recorrer())  
print("Eliminar 'elemento 2':", lista.eliminar("elemento 2")) 
print("Lista:", lista.recorrer())  

