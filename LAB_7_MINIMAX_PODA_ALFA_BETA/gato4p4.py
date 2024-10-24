import math

# Representación de jugadores
HUMANO = 'X'
IA = 'O'
VACIO = '-'

# Tamaño del tablero
TAMANO_TABLERO = 4

# Inicialización del tablero 4x4
def inicializar_tablero():
    return [[VACIO for _ in range(TAMANO_TABLERO)] for _ in range(TAMANO_TABLERO)]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()

# Verificación si hay un ganador
def hay_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(TAMANO_TABLERO):
        if all(tablero[i][j] == jugador for j in range(TAMANO_TABLERO)) or all(tablero[j][i] == jugador for j in range(TAMANO_TABLERO)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(TAMANO_TABLERO)) or all(tablero[i][TAMANO_TABLERO - i - 1] == jugador for i in range(TAMANO_TABLERO)):
        return True

    return False

# Verificar si hay empate
def hay_empate(tablero):
    return all(tablero[i][j] != VACIO for i in range(TAMANO_TABLERO) for j in range(TAMANO_TABLERO))

# Función de evaluación para el estado actual del tablero
def evaluar_tablero(tablero):
    if hay_ganador(tablero, IA):
        return 10  # Victoria de la IA
    elif hay_ganador(tablero, HUMANO):
        return -10  # Victoria del Humano
    else:
        return 0  # Empate o sin ganador

# Implementación del algoritmo Minimax con poda Alfa-Beta y límite de profundidad
def minimax(tablero, profundidad, alfa, beta, es_maximizador, limite_profundidad=4):
    puntaje = evaluar_tablero(tablero)

    # Si el juego termina o se alcanza el límite de profundidad, devolver el puntaje
    if puntaje == 10 or puntaje == -10 or profundidad == limite_profundidad:
        return puntaje

    if hay_empate(tablero):
        return 0

    # Maximizar la IA
    if es_maximizador:
        mejor_puntaje = -math.inf

        for i in range(TAMANO_TABLERO):
            for j in range(TAMANO_TABLERO):
                if tablero[i][j] == VACIO:
                    tablero[i][j] = IA
                    puntaje_actual = minimax(tablero, profundidad + 1, alfa, beta, False, limite_profundidad)
                    mejor_puntaje = max(mejor_puntaje, puntaje_actual)
                    alfa = max(alfa, mejor_puntaje)
                    tablero[i][j] = VACIO

                    if beta <= alfa:
                        break
        return mejor_puntaje

    # Minimizar el jugador humano   
    else:
        mejor_puntaje = math.inf

        for i in range(TAMANO_TABLERO):
            for j in range(TAMANO_TABLERO):
                if tablero[i][j] == VACIO:
                    tablero[i][j] = HUMANO
                    puntaje_actual = minimax(tablero, profundidad + 1, alfa, beta, True, limite_profundidad)
                    mejor_puntaje = min(mejor_puntaje, puntaje_actual)
                    beta = min(beta, mejor_puntaje)
                    tablero[i][j] = VACIO

                    if beta <= alfa:
                        break
        return mejor_puntaje

# Función para que la IA haga su movimiento óptimo con impresión de diagnóstico
def movimiento_ia(tablero):
    print("IA está pensando...")
    mejor_puntaje = -math.inf
    mejor_movimiento = (-1, -1)

    for i in range(TAMANO_TABLERO):
        for j in range(TAMANO_TABLERO):
            if tablero[i][j] == VACIO:
                # La IA realiza un movimiento temporal
                tablero[i][j] = IA
                # Calcula el puntaje del movimiento con Minimax
                puntaje_actual = minimax(tablero, 0, -math.inf, math.inf, False, limite_profundidad=4)
                # Deshace el movimiento temporal
                tablero[i][j] = VACIO

                # Actualiza el mejor puntaje y movimiento si es necesario
                if puntaje_actual > mejor_puntaje:
                    mejor_puntaje = puntaje_actual
                    mejor_movimiento = (i, j)

    print(f"IA elige la posición: {mejor_movimiento}")
    return mejor_movimiento


# Función para validar la entrada del usuario
def validar_entrada(tablero):
    while True:
        try:
            fila = int(input("Ingresa la fila (0-3): "))
            columna = int(input("Ingresa la columna (0-3): "))
            if 0 <= fila < TAMANO_TABLERO and 0 <= columna < TAMANO_TABLERO:
                if tablero[fila][columna] == VACIO:
                    return fila, columna
                else:
                    print("La posición ya está ocupada. Intenta de nuevo.")
            else:
                print("Posición fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entre 0 y 3.")     


# Modalidad del juego (corregida con límites de profundidad)
def jugar():
    print("Elige una modalidad:")
    print("1. Humano vs Humano")
    print("2. Humano vs IA")
    print("3. IA vs IA")
    opcion = int(input("Ingresa el número de la modalidad: "))

    tablero = inicializar_tablero()
    imprimir_tablero(tablero)

    if opcion == 1:
        # Modalidad Humano vs Humano
        turno = HUMANO
        while not hay_ganador(tablero, HUMANO) and not hay_ganador(tablero, IA) and not hay_empate(tablero):
            print(f"Turno de {turno}")
            fila, columna = validar_entrada(tablero)
            tablero[fila][columna] = turno
            turno = IA if turno == HUMANO else HUMANO
            imprimir_tablero(tablero)

    elif opcion == 2:
        # Modalidad Humano vs IA
        turno = HUMANO
        while not hay_ganador(tablero, HUMANO) and not hay_ganador(tablero, IA) and not hay_empate(tablero):
            if turno == HUMANO:
                print("Turno del Humano")
                fila, columna = validar_entrada(tablero)
                tablero[fila][columna] = HUMANO
                turno = IA
            else:
                print("Turno de la IA")
                fila, columna = movimiento_ia(tablero)
                if fila != -1 and columna != -1:
                    tablero[fila][columna] = IA
                turno = HUMANO
            imprimir_tablero(tablero)

    elif opcion == 3:
        # Modalidad IA vs IA
        turno = IA
        while not hay_ganador(tablero, HUMANO) and not hay_ganador(tablero, IA) and not hay_empate(tablero):
            print(f"Turno de la IA ({turno})")
            fila, columna = movimiento_ia(tablero)
            if fila != -1 and columna != -1:
                tablero[fila][columna] = turno
            turno = IA if turno == HUMANO else HUMANO
            imprimir_tablero(tablero)

    # Resultado del juego
    if hay_ganador(tablero, HUMANO):
        print("¡El Humano ganó!")
    elif hay_ganador(tablero, IA):
        print("¡La IA ganó!")
    else:
        print("¡Empate!")

# Ejecutar el juego (para probar en entorno local)
jugar()  # Descomenta esta línea para ejecutar en tu entorno local