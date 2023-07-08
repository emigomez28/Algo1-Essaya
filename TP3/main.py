import soko
import gamelib
import interfaz
import pila
import acciones

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
NIVELES = 'niveles.txt'
TECLAS = 'teclas.txt'

def inicializar():
    niveles = soko.obtener_niveles(NIVELES)
    nivel_max  = len(niveles.keys())
    config = soko.cargar_config(TECLAS)
    nro_nivel_actual = 1
    nivel_en_juego = acciones.obtener_nivel_en_juego(nro_nivel_actual, niveles, nivel_max)
    pila_deshacer, pila_rehacer = pila.Pila(), pila.Pila()
    pila_deshacer.apilar(nivel_en_juego)
    return nivel_en_juego, niveles, nivel_max, nro_nivel_actual, pila_deshacer, pila_rehacer, config

def main():
    nivel_en_juego, niveles, nivel_max, nro_nivel_actual, pila_deshacer, pila_rehacer, config = inicializar()
    sol_encontrada = None
    movimientos = pila.Pila()
    while gamelib.is_alive():
        gamelib.draw_begin()
        interfaz.mostrar_grilla(nivel_en_juego, nro_nivel_actual, nivel_max)
        interfaz.mostrar_soluciones(sol_encontrada)
        gamelib.draw_end()
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        tecla = ev.key
        direccion_string  = config.get(tecla)
        if direccion_string == 'SALIR':
            break
        
        nivel_en_juego, sol_encontrada, movimientos = acciones.realizar_accion(direccion_string, nivel_en_juego, nro_nivel_actual, niveles, nivel_max, pila_deshacer, pila_rehacer, sol_encontrada, movimientos)
        
        if soko.juego_ganado(nivel_en_juego):
            nivel_en_juego, nro_nivel_actual = acciones.pasar_nivel(nro_nivel_actual, niveles, nivel_max)
            pila_deshacer, pila_rehacer = acciones.reiniciar_pilas()
            sol_encontrada = None
gamelib.init(main)