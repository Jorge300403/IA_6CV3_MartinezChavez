import random

# PRIMERO DEFINIMOS LA FUNCIÓN
def f(x, y):
    return ((1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2)

# DEFINIMOS LOS RANGOS DE x E y
x_minimo, x_maximo = -4.5, 4.5
y_minimo, y_maximo = -4.5, 4.5

# Número de iteraciones
n_iteraciones = 10000

# CREAMOS NUESTRAS VARIABLES SOLUCIÓN U ÓPTIMAS
valor_minimo = float('inf')
mejor_x = None
mejor_y = None

# REALIZAMOS LAS ITERACIONES
for iteracion in range(1, n_iteraciones + 1):
    # EN CADA ITERACIÓN GENERAMOS VALORES ALEATORIOS DENTRO DE LOS RANGOS DEFINIDOS
    x = random.uniform(x_minimo, x_maximo)
    y = random.uniform(y_minimo, y_maximo)
    
    # EVALUAMOS LA FUNCIÓN CON ESTOS VALORES
    valor_actual = f(x, y)
    
    # SI EL RESULTADO ES MENOR AL VALOR MÍNIMO GUARDADO, LO ACTUALIZAMOS
    if valor_actual < valor_minimo:
        valor_minimo = valor_actual
        mejor_x = x
        mejor_y = y
        
        # IMPRIMIMOS CADA VEZ QUE ENCONTRAMOS UN NUEVO MÍNIMO
        print(f'Iteración: {iteracion}, Nuevo mínimo encontrado: {valor_minimo}')
        print(f'Valores: x = {mejor_x}, y = {mejor_y}\n')

# IMPRIMIMOS EL RESULTADO FINAL
print(f'\nEl valor mínimo encontrado en {n_iteraciones} iteraciones es: {valor_minimo}')
print(f'Valores de x e y que minimizan la función: x = {mejor_x}, y = {mejor_y}')
