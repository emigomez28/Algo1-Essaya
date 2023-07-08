import gamelib
import soko

IMG_PISO = 'img/ground.gif'
IMG_PARED = 'img/wall.gif'
IMG_JUGADOR = 'img/player.gif'
IMG_OBJETIVO = 'img/goal.gif'
IMG_CAJA = 'img/box.gif'

def mostrar_grilla(nivel, nro_nivel_actual, nivel_max):
    try:
        if nro_nivel_actual > nivel_max:
            gamelib.resize(300, 300)
            gamelib.draw_text('Felicidades, ganaste el juego!!!', 150, 150)
        else:
            cant_columnas = len(nivel)
            cant_filas = len(nivel[0])
            gamelib.resize(cant_filas * 64, cant_columnas * 64)
            for i in range(cant_filas):
                for j in range(cant_columnas):
                    x = 64 * i
                    y = 64 * j
                    gamelib.draw_image(IMG_PISO, x, y)
                    if soko.hay_pared(nivel, i, j):
                        gamelib.draw_image(IMG_PARED, x, y)
                    elif soko.hay_solo_jugador(nivel, i, j):
                        gamelib.draw_image(IMG_JUGADOR , x, y)
                    elif soko.hay_solo_objetivo(nivel, i, j):
                        gamelib.draw_image(IMG_OBJETIVO, x, y)
                    elif soko.hay_solo_caja(nivel, i, j):
                        gamelib.draw_image(IMG_CAJA, x, y)
                    elif soko.hay_objetivo_caja(nivel, i, j):
                        gamelib.draw_image(IMG_CAJA, x, y)
                        gamelib.draw_image(IMG_OBJETIVO, x, y)
                    elif soko.hay_objetivo_jugador(nivel, i, j):
                        gamelib.draw_image(IMG_JUGADOR, x, y)
                        gamelib.draw_image(IMG_OBJETIVO, x, y)
    except TypeError:
        return

def mostrar_soluciones(sol_encontrada):
    if sol_encontrada == None:
        gamelib.draw_text(f'Presione "h" para una pista', 100, 25)
    elif sol_encontrada:
        gamelib.draw_text('Pistas disponibles', 75, 25)
    else:
        gamelib.draw_text('No se puede ganar el nivel, presione "r" para reiniciar', 195, 25)
    