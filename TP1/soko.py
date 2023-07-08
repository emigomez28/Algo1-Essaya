import copy

PARED = "#"
ESPACIO = " "
CAJA = "$"
OBJETIVO_JUGADOR = "+"
OBJETIVO_CAJA = "*"
JUGADOR = "@"
OBJETIVO = "."
CARACTERES_VALIDOS = [PARED, ESPACIO, CAJA, OBJETIVO_JUGADOR, OBJETIVO_CAJA, JUGADOR, OBJETIVO]

def crear_grilla(lista):
    '''En base a una lista de strings crea una matriz representada como una lista de listas'''
    grilla = []
    for fila in lista:
        filas = []
        for char in fila:
            if char not in CARACTERES_VALIDOS:
                return
            filas.append(char) 
        grilla.append(list(filas))
        filas.clear()
    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    cantidad_de_filas = len(grilla) 
    cantidad_de_columnas = len(grilla[0]) 

    dimensiones = (cantidad_de_columnas, cantidad_de_filas) 
    return dimensiones

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == PARED

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return hay_objetivo_caja(grilla, c, f) or hay_objetivo_jugador(grilla, c, f) or hay_solo_objetivo(grilla, c, f)

def hay_objetivo_caja(grilla, c, f):
    '''Devuelve True si hay un objetivo y una caja en la columna y fila (c, f)'''
    return grilla[f][c] == OBJETIVO_CAJA

def hay_objetivo_jugador(grilla, c, f):
    '''Devuelve True si hay un objetivo y un jugador en la columna y fila (c, f)'''
    return grilla[f][c] == OBJETIVO_JUGADOR

def hay_solo_objetivo(grilla, c, f):
    '''Devuelve True si hay solo un objetivo en la columna y fila (c, f)'''
    return grilla[f][c] == OBJETIVO

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return hay_solo_caja(grilla, c, f) or hay_objetivo_caja(grilla, c, f)

def hay_solo_caja(grilla, c, f):
    '''Devuelve True si hay solo una caja en la columna y fila (c, f)'''
    return grilla[f][c] == CAJA

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return hay_solo_jugador(grilla, c, f) or hay_objetivo_jugador(grilla, c, f)

def hay_solo_jugador(grilla, c, f):
    '''Devuelve True si hay solo un jugador en la columna y fila (c, f)'''
    return grilla[f][c] == JUGADOR

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for c in grilla:
        for i in range(len(c)):
            if c[i] == CAJA or c[i] == OBJETIVO:
                return False
    return True
              
def en_rango(dir1, dir2, mapa):
    '''Devuelve True si la direccion obtenida se encuentra dentro del largo de la matriz'''
    return dir1 < len(mapa) and dir2 < len(mapa)

def objeto_en_posicion_siguiente(mapa, fila_actual, columna_actual, direccion, distancia = 1): 
    '''Devuelve lo que hay en la posicion siguiente en la direccion indicada'''
    dx, dy = direccion
    if hay_solo_caja(mapa, columna_actual + dx * distancia, fila_actual + dy * distancia):
        return CAJA
    elif hay_objetivo_caja(mapa, columna_actual + dx * distancia, fila_actual + dy * distancia):
        return OBJETIVO_CAJA
    elif hay_solo_objetivo(mapa, columna_actual + dx * distancia, fila_actual + dy * distancia):
        return OBJETIVO
    elif hay_pared(mapa, columna_actual + dx * distancia, fila_actual + dy * distancia):
        return PARED
    else:
        return ESPACIO

def objeto_en_posicion_subsiguiente(mapa, fila_actual, columna_actual, direccion):
    '''Devuelve el objeto que esta a 2 posiciones de distancia del jugador'''
    return objeto_en_posicion_siguiente(mapa, fila_actual, columna_actual, direccion, 2)

def movimiento_valido(mapa, fila_actual, columna_actual, direccion):
    '''Devuelve True si un movimiento es valido o no'''
    if objeto_en_posicion_siguiente(mapa, fila_actual, columna_actual, direccion) == ESPACIO or objeto_en_posicion_siguiente(mapa, fila_actual, columna_actual, direccion) == OBJETIVO:
        return True
    elif objeto_en_posicion_siguiente(mapa, fila_actual, columna_actual, direccion) == CAJA or objeto_en_posicion_siguiente(mapa, fila_actual, columna_actual, direccion) == OBJETIVO_CAJA:
        obj_2 = objeto_en_posicion_subsiguiente(mapa, fila_actual, columna_actual, direccion)
        if obj_2 == OBJETIVO or obj_2 == ESPACIO:
            return True
    return False

def actualizar_posicion_siguiente_anterior(mapa, fila, columna, valor_anterior):
    '''Actualiza el valor de la posicion desde la cual el jugador se mueve'''
    if valor_anterior == OBJETIVO_JUGADOR:
        mapa[fila][columna] = OBJETIVO
    else:
        mapa[fila][columna] = ESPACIO

def actualizar_posicion_siguiente(mapa, fila, columna, direccion, valor_siguiente, distancia = 1):
    '''Actualiza el valor de la posicion a la cual llega el jugador'''
    dx, dy = direccion
    mapa[fila + dy * distancia][columna + dx * distancia] = valor_siguiente

def actualizar_posicion_subsiguiente(mapa, fila, columna, direccion, valor_siguiente):
    '''Actualiza la posicion que esta a 2 posiciones de distancia del jugador'''
    actualizar_posicion_siguiente(mapa, fila, columna, direccion, valor_siguiente, 2)

def mover_jugador(mapa, fila, columna, direccion):
    '''Funcion axuliar que se utiliza para mover al jugador'''
    if objeto_en_posicion_siguiente(mapa, fila, columna, direccion) == OBJETIVO:
        actualizar_posicion_siguiente(mapa, fila, columna, direccion, OBJETIVO_JUGADOR)
        
    elif objeto_en_posicion_siguiente(mapa, fila, columna, direccion) == ESPACIO:
        actualizar_posicion_siguiente(mapa, fila, columna, direccion, JUGADOR)

    else:
        mover_caja(mapa, fila, columna, direccion)
        if objeto_en_posicion_siguiente(mapa, fila, columna, direccion) == OBJETIVO_CAJA:
            actualizar_posicion_siguiente(mapa, fila, columna, direccion, OBJETIVO_JUGADOR)
        elif objeto_en_posicion_siguiente(mapa, fila, columna, direccion) == CAJA:
            actualizar_posicion_siguiente(mapa, fila, columna, direccion, JUGADOR)
        
def mover_caja(mapa, fila, columna, direccion):
    '''Funcion auxiliar que se utiliza para mover a la caja'''
    if objeto_en_posicion_subsiguiente(mapa, fila, columna, direccion) == ESPACIO:
            actualizar_posicion_subsiguiente(mapa, fila, columna, direccion, CAJA)
            
    elif objeto_en_posicion_subsiguiente(mapa, fila, columna, direccion) == OBJETIVO:
            actualizar_posicion_subsiguiente(mapa, fila, columna, direccion, OBJETIVO_CAJA)
            
    elif objeto_en_posicion_siguiente(mapa, fila, columna, direccion) == OBJETIVO_CAJA:
        if objeto_en_posicion_subsiguiente(mapa, fila, columna, direccion) == ESPACIO:
            actualizar_posicion_subsiguiente(mapa, fila, columna, direccion, CAJA)
            
        elif objeto_en_posicion_subsiguiente(mapa, fila, columna, direccion) == OBJETIVO:
            actualizar_posicion_subsiguiente(mapa, fila, columna, direccion, OBJETIVO_CAJA)
            actualizar_posicion_siguiente(mapa, fila, columna, direccion, OBJETIVO_JUGADOR)
            
def buscar_jugador(mapa):
    '''Busca la posicion del jugador en la grilla'''
    for f in range(len(mapa)):
        for c in range(len(mapa[f])):
            if hay_jugador(mapa, c, f):
                return (f, c)
        
def mover(grilla,direccion):
    '''Ejecuta el movimiento siempre y cuando este sea valido'''
    # Realizo una copia de la grilla para no modificar la original, luego busco la posicion del jugador y si
    # el movimiento es valido, ejecuto el movimiento en la copia.
    mapa = copy.deepcopy(grilla)
    fila, columna = buscar_jugador(mapa)
    
    if movimiento_valido(mapa, fila, columna, direccion):
        valor_anterior = mapa[fila][columna]
        actualizar_posicion_siguiente_anterior(mapa, fila, columna, valor_anterior)
        mover_jugador(mapa, fila, columna, direccion)   
        return mapa
    return mapa
