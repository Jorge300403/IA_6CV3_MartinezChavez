import numpy as np

# Función objetivo: Una función simple para minimizar (por ejemplo, una parabólica)
def objective_function(x, y):
    return x**2 + y**2

# Inicialización de parámetros
def initialize_population(pop_size, bounds):
    X = np.random.uniform(bounds[0], bounds[1], pop_size)
    Y = np.random.uniform(bounds[0], bounds[1], pop_size)
    return X, Y

# Fase de construcción de caminos
def compute_distances_and_smells(X, Y):
    distances = np.sqrt(X**2 + Y**2)
    smells = 1 / distances
    return distances, smells

# Fase de cálculo de aptitud
def evaluate_fitness(smells, X, Y):
    best_smell_index = np.argmax(smells)
    best_X = X[best_smell_index]
    best_Y = Y[best_smell_index]
    return best_X, best_Y

# Algoritmo FFOA principal
def fruit_fly_optimization(objective_function, bounds, pop_size=20, iterations=100):
    # Inicialización
    X, Y = initialize_population(pop_size, bounds)
    best_solution = None
    best_score = float('inf')

    for iter in range(iterations):
        # Construcción de caminos
        distances, smells = compute_distances_and_smells(X, Y)
        
        # Evaluación de aptitud
        best_X, best_Y = evaluate_fitness(smells, X, Y)
        best_fitness = objective_function(best_X, best_Y)

        # Guardar mejor solución
        if best_fitness < best_score:
            best_solution = (best_X, best_Y)
            best_score = best_fitness
        
        # Movimiento hacia la mejor solución
        X = best_X + np.random.uniform(-1, 1, pop_size)
        Y = best_Y + np.random.uniform(-1, 1, pop_size)

        print(f"Iteración {iter + 1}: Mejor solución = {best_solution}, Mejor aptitud = {best_score}")

    return best_solution, best_score

# Configuración y ejecución
bounds = [-10, 10]  # Límites para x e y
best_solution, best_score = fruit_fly_optimization(objective_function, bounds)

print(f"\nResultado final: Mejor solución = {best_solution}, Mejor aptitud = {best_score}")
