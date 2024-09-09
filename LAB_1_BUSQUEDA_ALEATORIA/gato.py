import random

# FUNCIÓN PARA CREAR EL TABLERO DE 4 FILAS X 4 COLUMNAS
def crear_tablero():
    return [[' ' for _ in range(4)] for _ in range(4)]

# FUNCIÓN PARA IMPRIMIR EL TABLERO AL INICIO Y DESPUÉS DE CADA TIRADA
def imprimir_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 7)

# VERIFICAMOS SI HAY UN GANADOR, ES UNA FUNCIÓN BOOLEANA
def verificar_ganador(tablero, jugador):
    for i in range(4):
        # PRIMERO VERIFICAMOS SI TODAS LAS FILAS Y TODAS LAS COLUMNAS TIENEN ALGÚN GANADOR
        # UN GANADOR SE DA SI EN TODAS LAS POSICIONES [i][j] ESTÁ SU FIGURA
        if all([tablero[i][j] == jugador for j in range(4)]) or all([tablero[j][i] == jugador for j in range(4)]):
            return True
    # AHORA VERIFICAMOS LAS 2 DIAGONALES
    if all([tablero[i][i] == jugador for i in range(4)]) or all([tablero[i][3-i] == jugador for i in range(4)]):
        return True
    return False

# COMPROBAMOS SI EL TABLERO ESTÁ LLENO
# ESTO SE DARÁ CUANDO NO HAY UN GANADOR, ENTONCES SERÁ UN EMPATE
def tablero_lleno(tablero):
    return all([tablero[i][j] != ' ' for i in range(4) for j in range(4)])

# HACEMOS LA TIRADA DEL USUARIO
def movimiento_jugador(tablero):
    # HACEMOS UN BUCLE PARA PODER VERIFICAR QUE SE INGRESÓ UNA POSICIÓN CORRECTA
    while True:
        try:
            # PRIMERO LE SOLICITAMOS LA FILA EN UN RANGO DEL 0 AL 3
            fila = int(input("Ingresa la fila (0-3): "))
            # DESPUÉS LE SOLICITAMOS LA COLUMNA EN UN RANGO DEL 0 AL 3
            columna = int(input("Ingresa la columna (0-3): "))
            # COMPROBAMOS LA LEGALIDAD DEL TIRO, PRIMERO QUE LA FILA Y COLUMNA INGRESADA ESTÉN DENTRO DEL RANGO
            # DESPUÉS QUE LA POSICIÓN DONDE SE DESEA TIRAR ESTÉ VACÍA
            if 0 <= fila < 4 and 0 <= columna < 4 and tablero[fila][columna] == ' ':
                # SI LA LEGALIDAD DEL TIRO ES CORRECTA, SE AGREGA UNA X QUE ES LA FICHA DEL JUGADOR
                tablero[fila][columna] = 'X'
                break
            else:
                # EN CASO DE QUE NO SEA VÁLIDO, DEBERÁ VOLVER A PEDIR QUE EL USUARIO INGRESE LAS POSICIONES
                print("Movimiento no válido. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingresa números entre 0 y 3.")

# AHORA HAREMOS LA TIRADA DE LA COMPUTADORA
def movimiento_computadora(tablero):
    # HAREMOS UN BUCLE PARA PODER ENCONTRAR UNA POSICIÓN VACÍA
    while True:
        # PRIMERO ELIGE UN NÚMERO ALEATORIO ENTRE 0 Y 3 PARA LA FILA
        fila = random.randint(0, 3)
        # DESPUÉS ELIGE UN NÚMERO ALEATORIO ENTRE 0 Y 3 PARA LA COLUMNA
        columna = random.randint(0, 3)
        # COMPRUEBA SI LA POSICIÓN ESTÁ VACÍA
        if tablero[fila][columna] == ' ':
            # EN CASO DE QUE SÍ, AGREGA UNA O QUE ES LA FICHA DE LA COMPUTADORA
            tablero[fila][columna] = 'O'
            break

# FUNCIÓN DEL JUEGO
def juego_gato():
    # PRIMERO CREAMOS LA MATRIZ DE 4 X 4 Y LA GUARDAMOS EN LA VARIABLE TABLERO
    tablero = crear_tablero()
    # IMPRIMIMOS EL TABLERO
    imprimir_tablero(tablero)

    # INICIAMOS EL BUCLE DEL JUEGO
    while True:
        # PRIMERO HACEMOS LA TIRADA DEL JUGADOR
        # DESPUÉS IMPRIMIMOS EL TABLERO
        # COMPROBAMOS SI GANA EL USUARIO
        movimiento_jugador(tablero)
        imprimir_tablero(tablero)
        if verificar_ganador(tablero, 'X'):
            print("¡Felicidades! Has ganado.")
            break
        if tablero_lleno(tablero):
            print("¡Es un empate!")
            break

        # DESPUÉS HACEMOS LA TIRADA DE LA COMPUTADORA
        # IMPRIMIMOS EL TABLERO
        # COMPROBAMOS SI HA GANADO LA COMPUTADORA
        print("Turno de la computadora...")
        movimiento_computadora(tablero)
        imprimir_tablero(tablero)
        if verificar_ganador(tablero, 'O'):
            print("La computadora ha ganado.")
            break
        if tablero_lleno(tablero):
            print("¡Es un empate!")
            break

    # DADO QUE ES UN BUCLE, LO ROMPEREMOS CUANDO HAYA UN GANADOR O HAYA UN EMPATE

# INICIALIZAMOS EL JUEGO
juego_gato()
