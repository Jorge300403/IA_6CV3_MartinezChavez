import random

#ESTRUCTURA DEL NODO
class Nodo:
    def __init__(self, estado, padre=None, accion=None):
        self.estado = estado      # es el tablero
        self.padre = padre        # nodo padre para ver el camino
        self.accion = accion      # que movimiento se hizo

    def obtener_camino(self):
        #Reconstruir el camino desde el nodo raíz hasta el nodo actual
        camino = []
        nodo_actual = self
        while nodo_actual.padre is not None:
            camino.append(nodo_actual.accion)
            nodo_actual = nodo_actual.padre
        camino.reverse()  # Invertimos el camino para que sea desde el inicio
        return camino

#PILA
class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0

#CREAMOS LOS POSIBLES MOVIMIENTOS DE LA FICHA
def mover_ficha(estado, direccion):
    # Encontramos la posición del espacio vacío (0)
    index_espacio = estado.index(0)
    nuevo_estado = estado[:]

    # Definimos las posibles direcciones y los movimientos válidos
    if direccion == 'arriba' and index_espacio > 1:  # Solo podemos mover hacia arriba si no estamos en la primera fila
        nuevo_estado[index_espacio], nuevo_estado[index_espacio - 2] = nuevo_estado[index_espacio - 2], nuevo_estado[index_espacio]
    elif direccion == 'abajo' and index_espacio < 2:  # Solo podemos mover hacia abajo si no estamos en la última fila
        nuevo_estado[index_espacio], nuevo_estado[index_espacio + 2] = nuevo_estado[index_espacio + 2], nuevo_estado[index_espacio]
    elif direccion == 'izquierda' and index_espacio % 2 != 0:  # Solo podemos mover hacia la izquierda si no estamos en la primera columna
        nuevo_estado[index_espacio], nuevo_estado[index_espacio - 1] = nuevo_estado[index_espacio - 1], nuevo_estado[index_espacio]
    elif direccion == 'derecha' and index_espacio % 2 != 1:  # Solo podemos mover hacia la derecha si no estamos en la segunda columna
        nuevo_estado[index_espacio], nuevo_estado[index_espacio + 1] = nuevo_estado[index_espacio + 1], nuevo_estado[index_espacio]

    return nuevo_estado

#IMPRIMIR EL TABLERO
def imprimir_tablero(estado):
    print(f"{estado[0]} {estado[1]}")
    print(f"{estado[2]} {estado[3]}")
    print()

#GENERAMOS UN ESTADO INICIAL DEL JUEGO
def generar_estado_aleatorio():
    estado = [0, 1, 2, 3]
    random.shuffle(estado)
    return estado

#HACEMOS LA BUSQUEDA DE LA SOLUCIÓN
def puzzle4(estado_inicial, estado_objetivo):
    # Cremaos la lista que son los nodo frontera ( nodos hijos ) y le asignamos una nueva pila
    frontera = Pila()
    nodo_inicial = Nodo(estado_inicial)
    frontera.push(nodo_inicial)

    # Usamos un conjunto para los nodos visitados
    visitados = set()

    # Bucle para poder crear a los hijos
    while not frontera.esta_vacia():
        nodo_actual = frontera.pop()
        estado_actual = nodo_actual.estado

        # Si encontramos la solución, regresamos el camino
        if estado_actual == estado_objetivo:
            return nodo_actual.obtener_camino()

        # Añadimos el estado actual a los visitados
        visitados.add(tuple(estado_actual))

        # Creamos a los nodos hijos
        for direccion in ['arriba', 'abajo', 'izquierda', 'derecha']:
            nuevo_estado = mover_ficha(estado_actual, direccion)
            #Verificamos que no hayamos ya creado ese estado
            if tuple(nuevo_estado) not in visitados:
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, direccion)
                frontera.push(nuevo_nodo)

    # Si no se encuentra solución
    return None

#EJECUTAMOS EL PROBLEMA
def resolver_puzzle():
    estado_inicial = generar_estado_aleatorio()  # Estado inicial aleatorio
    estado_objetivo = [1, 2, 3, 0]  # Estado objetivo (solución)

    print("Estado inicial del 4-puzzle:")
    imprimir_tablero(estado_inicial)

    # Ejecutamos DFS para resolver el puzzle
    solucion = puzzle4(estado_inicial, estado_objetivo)

    # Mostramos el resultado paso a paso
    if solucion:
        print("Se encontró una solución. Movimientos a realizar:")
        estado_actual = estado_inicial
        for i, movimiento in enumerate(solucion):
            print(f"Movimiento {i+1}: {movimiento}")
            estado_actual = mover_ficha(estado_actual, movimiento)
            imprimir_tablero(estado_actual)
    else:
        print("No se encontró ninguna solución.")

#MANDAMOS LLAMAR LA SOLUCIÓN
resolver_puzzle()