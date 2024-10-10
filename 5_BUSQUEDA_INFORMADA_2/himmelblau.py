import numpy as np
import queue

# Definimos la función de Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Definimos la búsqueda con cola (BFS)
def bfs_search_himmelblau(start_x, start_y, x_range=(-5, 5), y_range=(-5, 5), step=0.1):
    visited = set()
    q = queue.Queue()
    q.put((start_x, start_y))
    min_value = float('inf')
    best_coords = (start_x, start_y)

    while not q.empty():
        x, y = q.get()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Calculamos el valor de la función en el punto actual
        f_value = himmelblau(x, y)
        
        # Actualizamos el mínimo si encontramos un valor menor
        if f_value < min_value:
            min_value = f_value
            best_coords = (x, y)

        # Generamos los vecinos (nodos) en el espacio de búsqueda
        neighbors = [
            (x + step, y),
            (x - step, y),
            (x, y + step),
            (x, y - step)
        ]

        for nx, ny in neighbors:
            # Solo añadimos vecinos que estén dentro del rango permitido
            if x_range[0] <= nx <= x_range[1] and y_range[0] <= ny <= y_range[1]:
                q.put((nx, ny))

    return best_coords, min_value

# Comenzamos la búsqueda desde un punto inicial
start_x = 0
start_y = 0
result = bfs_search_himmelblau(start_x, start_y)

print(f"Las coordenadas (x, y) que minimizan la función son: {result[0]}")
print(f"El valor mínimo de la función es: {result[1]}")
