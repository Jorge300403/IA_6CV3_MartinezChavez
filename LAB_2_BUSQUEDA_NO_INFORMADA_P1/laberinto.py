# Representación del laberinto
# 0 = camino, 1 = pared
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Posición de inicio y salida
inicio = (0, 1)  # Coordenadas (fila, columna) de inicio
fin = (3, 4)     # Coordenadas (fila, columna) de salida

#NODO
class Nodo:
    def __init__(self, posicion, anterior=None):
        self.posicion = posicion 
        self.anterior = anterior 

#MOSTRAR EL LABERINTO
def imprimir_laberinto(laberinto, posicion_actual):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if (i, j) == posicion_actual:
                print("P", end=" ") 
            else:
                print(laberinto[i][j], end=" ")
        print()
    print()

# MOVIMIENTO VALIDO
def es_movimiento_valido(laberinto, fila, columna, visitados):
    if 0 <= fila < len(laberinto) and 0 <= columna < len(laberinto[0]):
        if laberinto[fila][columna] == 0 and (fila, columna) not in visitados:
            return True
    return False

# OBTENER CAMINO
def obtener_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.posicion)
        nodo = nodo.anterior
    camino.reverse()  
    return camino

#FUNCION QUE CREA LOS NODOS HIJOS
def resolver_laberinto(laberinto, inicio, fin):
    pila = [Nodo(inicio)]  
    visitados = set() 

    while pila:
        nodo_actual = pila.pop()
        fila_actual, columna_actual = nodo_actual.posicion

        # Imprimir el laberinto con la posición actual
        imprimir_laberinto(laberinto, nodo_actual.posicion)

        # Si llegamos a la posición final, se reconstruye el camino y se imprime
        if nodo_actual.posicion == fin:
            print("¡Has llegado a la salida!")
            return obtener_camino(nodo_actual)

        # Marcar la posición actual como visitada
        visitados.add(nodo_actual.posicion)

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        movimientos = [
            (fila_actual - 1, columna_actual),  # Arriba
            (fila_actual + 1, columna_actual),  # Abajo
            (fila_actual, columna_actual - 1),  # Izquierda
            (fila_actual, columna_actual + 1)   # Derecha
        ]

        # Agregar los movimientos válidos a la pila, creando un nuevo nodo para cada movimiento
        for movimiento in movimientos:
            fila, columna = movimiento
            if es_movimiento_valido(laberinto, fila, columna, visitados):
                nuevo_nodo = Nodo(movimiento, nodo_actual)  # Crear un nuevo nodo enlazado al nodo actual
                pila.append(nuevo_nodo)

    print("No se encontró solución.")
    return None

# Llamada a la función principal para resolver el laberinto
def solucion_laberinto():
    camino_solucion = resolver_laberinto(laberinto, inicio, fin)

    # Imprimir el resultado
    if camino_solucion:
        print("Se encontró un camino. El laberinto resuelto es:")
    else:
        print("No se pudo resolver el laberinto.")

solucion_laberinto()
