import random
import copy
from collections import deque

# Clase para definir un nodo del puzzle
class Nodo:
    def __init__(self, estado, padre=None, movimiento=None):
        self.estado = estado      
        self.padre = padre    
        self.movimiento = movimiento 

# Generar un tablero 2x2 aleatorio y con un espacio vacío representado por 0
def generar_estado_inicial():
    estado = [1, 2, 3, 0]
    random.shuffle(estado)
    return [estado[:2], estado[2:]]

# Imprimir el tablero 2x2
def imprimir_tablero(estado):
    for fila in estado:
        print(fila)
    print()

# Obtener la posición (fila, columna) del espacio vacío (0)
def obtener_posicion_vacia(estado):
    for i in range(2):
        for j in range(2):
            if estado[i][j] == 0:
                return (i, j)

# Obtener los posibles movimientos del espacio vacío (0)
def obtener_movimientos_validos(posicion_vacia):
    fila, columna = posicion_vacia
    movimientos = []
    
    if fila > 0:
        movimientos.append("arriba")
    if fila < 1:
        movimientos.append("abajo")
    if columna > 0:
        movimientos.append("izquierda")
    if columna < 1:
        movimientos.append("derecha")
    
    return movimientos

# Mover el espacio vacío (0) en la dirección especificada
def mover(estado, posicion_vacia, direccion):
    nueva_estado = copy.deepcopy(estado)
    fila, columna = posicion_vacia
    
    if direccion == "arriba":
        nueva_estado[fila][columna], nueva_estado[fila - 1][columna] = nueva_estado[fila - 1][columna], nueva_estado[fila][columna]
    elif direccion == "abajo":
        nueva_estado[fila][columna], nueva_estado[fila + 1][columna] = nueva_estado[fila + 1][columna], nueva_estado[fila][columna]
    elif direccion == "izquierda":
        nueva_estado[fila][columna], nueva_estado[fila][columna - 1] = nueva_estado[fila][columna - 1], nueva_estado[fila][columna]
    elif direccion == "derecha":
        nueva_estado[fila][columna], nueva_estado[fila][columna + 1] = nueva_estado[fila][columna + 1], nueva_estado[fila][columna]
    
    return nueva_estado

# Verificar si se ha alcanzado el estado objetivo
def es_estado_objetivo(estado):
    return estado == [[1, 2], [3, 0]]

# Función para realizar la regresión y reconstruir el camino desde el nodo solución hasta el inicio
def reconstruir_camino(nodo):
    camino = []
    while nodo.padre is not None:
        camino.append((nodo.movimiento, nodo.estado))
        nodo = nodo.padre
    camino.reverse()
    return camino

# Implementación de la búsqueda en anchura (BFS) para resolver el 4-puzzle
def resolver_4_puzzle():
    estado_inicial = generar_estado_inicial()
    print("Estado inicial:")
    imprimir_tablero(estado_inicial)

    nodo_inicial = Nodo(estado_inicial)
    cola = deque([nodo_inicial])
    visitados = set() 

    while cola:
        nodo_actual = cola.popleft()  
        estado_actual = nodo_actual.estado
        
        if es_estado_objetivo(estado_actual):
            print("¡Se encontró la solución!")
            camino_solucion = reconstruir_camino(nodo_actual)
            return camino_solucion

        posicion_vacia = obtener_posicion_vacia(estado_actual)
        movimientos_validos = obtener_movimientos_validos(posicion_vacia)

        for movimiento in movimientos_validos:
            nuevo_estado = mover(estado_actual, posicion_vacia, movimiento)
            estado_tupla = tuple(tuple(fila) for fila in nuevo_estado)

            if estado_tupla not in visitados:
                visitados.add(estado_tupla)
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, movimiento)
                cola.append(nuevo_nodo)

    return None

# Función principal para ejecutar la solución del 4-puzzle
def ejecutar_resolucion():
    camino_solucion = resolver_4_puzzle()

    if camino_solucion:
        print("\nCamino para resolver el puzzle:")
        for movimiento, estado in camino_solucion:
            print(f"Movimiento: {movimiento}")
            imprimir_tablero(estado)
    else:
        print("No se encontró una solución para el puzzle.")

# Ejecutar la solución
ejecutar_resolucion()
