import heapq
import time 

# Laberinto
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

# Nodo
class Nodo:
    def __init__(self, posicion, padre=None, g=0, h=0):
        self.posicion = posicion  
        self.padre = padre 
        self.g = g 
        self.h = h  
    
    @property
    def f(self):
        return self.g + self.h 

# Función para imprimir el laberinto
def imprimir_laberinto(laberinto, solucion=[]):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if (i, j) in solucion:
                print("P", end=" ")  
            else:
                print(laberinto[i][j], end=" ")
        print()
    print()

# Heurística
def heuristica(posicion_actual, posicion_final):
    return abs(posicion_actual[0] - posicion_final[0]) + abs(posicion_actual[1] - posicion_final[1])

# Reconstrucción del camino final
def reconstruir_camino(nodo):
    camino = []
    actual = nodo
    while actual is not None:
        camino.append(actual.posicion)
        actual = actual.padre
    camino.reverse()
    return camino

# Movimiento válido
def es_movimiento_valido(laberinto, posicion):
    fila, columna = posicion
    if 0 <= fila < len(laberinto) and 0 <= columna < len(laberinto[0]) and laberinto[fila][columna] == 0:
        return True
    return False

# Algoritmo A* 
def resolver_laberinto_A_star(laberinto, inicio, fin):
    nodo_inicio = Nodo(inicio, None, 0, heuristica(inicio, fin))
    nodo_fin = Nodo(fin)

    cola = []
    heapq.heappush(cola, (nodo_inicio.f, nodo_inicio))
    
    visitados = set()

    while cola:
        _, nodo_actual = heapq.heappop(cola)

        imprimir_laberinto(laberinto, reconstruir_camino(nodo_actual))

        if nodo_actual.posicion == nodo_fin.posicion:
            print("¡Laberinto resuelto!")
            return reconstruir_camino(nodo_actual)

        visitados.add(nodo_actual.posicion)

        fila, columna = nodo_actual.posicion
        movimientos = [(fila-1, columna), (fila+1, columna), (fila, columna-1), (fila, columna+1)]

        for movimiento in movimientos:
            if es_movimiento_valido(laberinto, movimiento) and movimiento not in visitados:
                nuevo_nodo = Nodo(movimiento, nodo_actual, nodo_actual.g + 1, heuristica(movimiento, fin))

                heapq.heappush(cola, (nuevo_nodo.f, nuevo_nodo))

    print("No se encontró solución.")
    return None

t_inicio = time.time()
# Llamar a la función para resolver el laberinto
camino_solucion = resolver_laberinto_A_star(laberinto, inicio, fin)
t_fin = time.time()

# Imprimir la solución final
if camino_solucion:
    print("Se encontró un camino. El laberinto resuelto es:")
    imprimir_laberinto(laberinto, camino_solucion)
    print("\n\n\nEl tiempo de ejecución fue: ", (t_fin-t_inicio))
else:
    print("No se encontró ninguna solución para el laberinto.")
