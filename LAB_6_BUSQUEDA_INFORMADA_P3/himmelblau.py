import numpy as np
import random
import math

# Definimos la función de Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Función de recocido simulado
def simulated_annealing(func, x0, y0, max_iters=10000, T=1000.0, cooling_rate=0.003):
    # Inicializamos las variables
    current_x = x0
    current_y = y0
    current_value = func(current_x, current_y)
    best_x, best_y = current_x, current_y
    best_value = current_value
    
    for i in range(max_iters):
        # Enfriamos la temperatura
        T = T * (1 - cooling_rate)
        
        # Generamos nuevos valores de x, y cercanos
        new_x = current_x + random.uniform(-1, 1)
        new_y = current_y + random.uniform(-1, 1)
        
        # Aseguramos que estén dentro de los límites [-5, 5]
        new_x = max(min(new_x, 5), -5)
        new_y = max(min(new_y, 5), -5)
        
        new_value = func(new_x, new_y)
        
        # Calculamos la diferencia entre las funciones
        delta_value = new_value - current_value
        
        # Aceptamos el nuevo punto con probabilidad
        if delta_value < 0 or random.uniform(0, 1) < math.exp(-delta_value / T):
            current_x, current_y = new_x, new_y
            current_value = new_value
            
        # Actualizamos el mejor valor encontrado
        if current_value < best_value:
            best_x, best_y = current_x, current_y
            best_value = current_value
    
    return best_x, best_y, best_value

# Punto inicial aleatorio dentro del rango [-5, 5]
initial_x = random.uniform(-5, 5)
initial_y = random.uniform(-5, 5)

# Ejecutamos el recocido simulado
best_x, best_y, best_value = simulated_annealing(himmelblau, initial_x, initial_y)

print(f'Los valores de x, y que minimizan la función de Himmelblau 
      son: x = {best_x}, y = {best_y}, con un valor mínimo de {best_value}')
