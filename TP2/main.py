import soko
import gamelib
import interfaz

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
NIVELES = 'niveles.txt'
TECLAS = 'teclas.txt'

def obtener_nivel_en_juego(nro_nivel, dict_niveles, nivel_max):
    if nro_nivel <= nivel_max:
        nivel_actual = f"Level_{nro_nivel}"
        nivel_en_juego = dict_niveles[nivel_actual]
        return nivel_en_juego
    else:
        return

def main():
    niveles = soko.obtener_niveles(NIVELES)
    nivel_max = len(niveles.keys())
    config = soko.cargar_config(TECLAS)
    nro_nivel_actual = 155
    nivel_en_juego = obtener_nivel_en_juego(nro_nivel_actual, niveles, nivel_max)

    while gamelib.is_alive():
        gamelib.draw_begin()
        interfaz.mostrar_grilla(nivel_en_juego, nro_nivel_actual, nivel_max)
        gamelib.draw_end()
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        tecla = ev.key
        direccion_string  = config.get(tecla)
        if direccion_string == 'SALIR':
            break
        if direccion_string == 'REINICIAR':
            nivel_en_juego = obtener_nivel_en_juego(nro_nivel_actual, niveles, nivel_max)   
        else:
            direccion_tupla = soko.DIRECCIONES.get(direccion_string)
            nivel_en_juego = soko.mover(nivel_en_juego, direccion_tupla)
        if soko.juego_ganado(nivel_en_juego):
            nro_nivel_actual += 1
            nivel_en_juego = obtener_nivel_en_juego(nro_nivel_actual, niveles, nivel_max)   
gamelib.init(main)
