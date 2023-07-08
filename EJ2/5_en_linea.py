import gamelib

COLUMNAS = 10
FILAS = 10
ANCHO_VENTANA = 300
ALTO_VENTANA = 300
VACIO = "-"
CIRCULO = 'O'
CRUZ = 'X'
MARGEN_Y = 30
MARGEN_X = 0  
POS_TEXTO = 20 
CENTRO_TABLERO = ANCHO_VENTANA / 2

def juego_crear():
    """
    Inicializa el estado del juego creando una matriz represenatada
    como una lista de filas (lista de listas)
    """
    tablero = []
    filas = []
    for i in range(FILAS):
        for j in range(COLUMNAS):
            filas.append(VACIO)   
        tablero.append([VACIO]*COLUMNAS)
    return tablero

def obtener_diferencial(ancho, alto, filas, columnas, margen_x, margen_y):
    dx = int((alto - margen_x)/filas)
    dy = int((ancho - margen_y )/columnas)
    return (dx, dy)

def en_rango(x,y):
    '''
    Devuelve True si la posicion donde hizo click el jugador esta dentro del tablero
    '''
    return x >= 0 and x < COLUMNAS and y >= 0 and y < FILAS

def escribir_turno(turno):
    '''
    Muestra por pantalla de quien es el turno
    '''
    if turno % 2 == 0:
        gamelib.draw_text('Turno X', CENTRO_TABLERO, POS_TEXTO)
    elif turno % 2 != 0:
        gamelib.draw_text('Turno O', CENTRO_TABLERO, POS_TEXTO)

def es_valido(x, y, juego):
   return en_rango(x,y) and juego[x][y] == VACIO  

def juego_actualizar(juego, px, py, turno):
    '''
    Actualiza el estado del juego
    '''

    dx , dy = obtener_diferencial(ANCHO_VENTANA, ALTO_VENTANA, FILAS, COLUMNAS, MARGEN_X, MARGEN_Y)
    if py < dy:
        return juego
    else:
        x = int(px / dx) 
        y = int((py - MARGEN_Y) / dy) 
        if es_valido(x, y, juego):
            if turno % 2 == 0:
                juego[x][y] = CRUZ
            else:
                juego[x][y] = CIRCULO
    return juego
    
def turno_actualizar(juego, px, py, turno):
    '''
    Actualiza el estado del juego
    '''
    
    dx , dy = obtener_diferencial(ANCHO_VENTANA, ALTO_VENTANA, FILAS, COLUMNAS, MARGEN_X, MARGEN_Y)

    x = int(px / dx) 
    y = int((py - MARGEN_Y) / dy) 
    if es_valido(x, y, juego):
        turno+=1
    return turno
    
def juego_mostrar(juego):
    '''
    Muestra el tablero por pantalla
    '''
    x0= 0
    y0 = 30
    dx , dy = obtener_diferencial(ANCHO_VENTANA, ALTO_VENTANA, FILAS, COLUMNAS, MARGEN_X, MARGEN_Y)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            x1 = dx * i + x0
            y1 = dy * j + y0
            x2 = x1 + dx
            y2 = y1 + dy
            x_texto = (x1 + x2) / 2
            y_texto = (y1 + y2) / 2
            if juego[i][j] == CRUZ:
                gamelib.draw_text(CRUZ, x_texto, y_texto)
                gamelib.draw_rectangle(x1, y1, x2, y2,outline = 'white', fill = '')
            elif juego[i][j] == CIRCULO:
                gamelib.draw_text(CIRCULO, x_texto, y_texto)
                gamelib.draw_rectangle(x1, y1, x2, y2,outline = 'white', fill = '')
            else:
                gamelib.draw_rectangle(x1, y1, x2, y2, outline = 'white', fill = '', )
                                
def main():
    juego = juego_crear()
    turno = 0
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    while gamelib.is_alive():
        gamelib.draw_begin()
        juego_mostrar(juego)
        escribir_turno(turno)
        gamelib.draw_end()
        ev = gamelib.wait()
        if not ev:
            break
        elif ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break
        elif ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y
            turno = turno_actualizar(juego, x, y, turno)
            juego = juego_actualizar(juego, x, y, turno)
gamelib.init(main)


