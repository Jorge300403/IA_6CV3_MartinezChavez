from collections import deque
import time

laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Posición de inicio y salida
inicio = (0, 1) 
fin = (3, 4)    

# Clase para definir un nodo del laberinto
class Nodo:
    def __init__(self, posicion, padre=None):
        self.posicion = posicion  
        self.padre = padre        

# Imprimir el laberinto con el camino actual
def imprimir_laberinto(laberinto, camino_actual=[]):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if (i, j) in camino_actual:
                print("P", end=" ")  
            else:
                print(laberinto[i][j], end=" ")
        print()
    print()

# Verificar si el movimiento es válido
def es_movimiento_valido(laberinto, posicion):
    fila, columna = posicion
    if 0 <= fila < len(laberinto) and 0 <= columna < len(laberinto[0]) and laberinto[fila][columna] == 0:
        return True
    return False

# Función para realizar la búsqueda en anchura 
def resolver_laberinto():
    nodo_inicial = Nodo(inicio)
    cola = deque([nodo_inicial])
    visitados = set()  
    visitados.add(nodo_inicial.posicion)

    while cola:
        nodo_actual = cola.popleft()  
        posicion_actual = nodo_actual.posicion
        
        camino_actual = reconstruir_camino(nodo_actual)
        imprimir_laberinto(laberinto, camino_actual)
        print(f"Visitando: {posicion_actual}")

        if posicion_actual == fin:
            print("¡Se encontró la solución!")
            return reconstruir_camino(nodo_actual)

        fila, columna = posicion_actual
        movimientos = [(fila - 1, columna), (fila + 1, columna), (fila, columna - 1), (fila, columna + 1)]

        for movimiento in movimientos:
            if es_movimiento_valido(laberinto, movimiento) and movimiento not in visitados:
                visitados.add(movimiento)
                nuevo_nodo = Nodo(movimiento, nodo_actual)
                cola.append(nuevo_nodo)

    print("No se encontró una solución para el laberinto.")
    return None

# Función para reconstruir el camino desde el nodo solución hasta el nodo inicial
def reconstruir_camino(nodo):
    camino = []
    while nodo is not None:
        camino.append(nodo.posicion)
        nodo = nodo.padre
    camino.reverse()
    return camino

# Función principal para ejecutar la resolución del laberinto
def ejecutar_resolucion():
    camino_solucion = resolver_laberinto()

    if camino_solucion:
        print("\nCamino final para resolver el laberinto:")
        imprimir_laberinto(laberinto, camino_solucion)
        print(f"El camino encontrado es: {camino_solucion}")
    else:
        print("No se encontró ninguna solución para el laberinto.")

# Ejecutar la solución
ejecutar_resolucion()
