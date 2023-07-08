import pila
import soko

def realizar_accion(direccion_string, nivel_en_juego, nro_nivel_actual, niveles, nivel_max, pila_deshacer, pila_rehacer, sol_encontrada, movimientos):
    if direccion_string == 'PISTAS':
            if sol_encontrada:
                tablero, movimientos = ejecutar_pistas(movimientos, nivel_en_juego, pila_deshacer)
            else:
                tablero, sol_encontrada, movimientos = calcular_pistas(nivel_en_juego)
                if movimientos is None:
                    sol_encontrada = False
    elif direccion_string == 'REINICIAR':
        pila_deshacer, pila_rehacer = reiniciar()
        tablero = obtener_nivel_en_juego(nro_nivel_actual, niveles, nivel_max)
    elif direccion_string == 'DESHACER' and not pila_deshacer.esta_vacia():
        tablero = deshacer(pila_deshacer, pila_rehacer)  
    elif direccion_string == 'REHACER' and not pila_rehacer.esta_vacia():
        tablero = rehacer(pila_deshacer, pila_rehacer)   
    else:
        tablero = realizar_movimiento(direccion_string, pila_deshacer, nivel_en_juego)
        sol_encontrada = None
    return tablero, sol_encontrada, movimientos

def ejecutar_pistas(movimientos, nivel_en_juego, pila_deshacer):
    mov = movimientos.desapilar() 
    tablero_pista = soko.mover(nivel_en_juego, mov)
    pila_deshacer.apilar(tablero_pista)
    tablero = tablero_pista
    return tablero, movimientos

def calcular_pistas(nivel_en_juego):
    sol_encontrada, movimientos = encontrar_solucion(nivel_en_juego)
    tablero = nivel_en_juego 
    return tablero, sol_encontrada, movimientos

def encontrar_solucion(estado_inicial):
    visitados = dict()
    pila_acciones = pila.Pila()
    return backtracking(estado_inicial, visitados, pila_acciones)

def backtracking(estado, visitados, pila_acciones):
    visitados[soko.estado_a_string(estado)] = estado
    if soko.juego_ganado(estado):
        return True, []
    for dir in soko.LISTA_DIR:
        nuevo_estado2 = soko.mover(estado, dir)
        if soko.estado_a_string(nuevo_estado2) not in visitados.keys():
            nuevo_estado = soko.mover(estado, dir)
            sol_encontrada, acciones = backtracking(nuevo_estado, visitados, pila_acciones)
            if sol_encontrada:
                pila_acciones.apilar(dir)
                return True, pila_acciones
    return False, None

def reiniciar():
    deshacer, rehacer = reiniciar_pilas()
    return deshacer , rehacer

def reiniciar_pilas():
    deshacer, rehacer = pila.Pila(), pila.Pila()
    return deshacer, rehacer

def obtener_nivel_en_juego(nro_nivel, dict_niveles, nivel_max):
    if nro_nivel <= nivel_max:
        nivel_actual = f"Level_{nro_nivel}"
        nivel_en_juego = dict_niveles[nivel_actual]
        return nivel_en_juego
    else:
        return

def deshacer(deshacer, rehacer):
    estado_anterior = deshacer.ver_tope()
    ultimo_movimiento = deshacer.desapilar()
    rehacer.apilar(ultimo_movimiento)
    nivel_en_juego = estado_anterior
    return nivel_en_juego

def rehacer(deshacer, rehacer):
    tope_rehacer = rehacer.desapilar()
    deshacer.apilar(tope_rehacer)
    nivel_en_juego = tope_rehacer
    return nivel_en_juego

def realizar_movimiento(direccion_string, deshacer, tablero):
    direccion_tupla = soko.DIRECCIONES.get(direccion_string)
    nivel_en_juego = soko.mover(tablero, direccion_tupla)
    deshacer.apilar(nivel_en_juego)
    return nivel_en_juego

def pasar_nivel(nro_nivel_actual, niveles, nivel_max):
    nro_nivel_actual += 1
    nivel_en_juego = obtener_nivel_en_juego(nro_nivel_actual, niveles, nivel_max)   
    return nivel_en_juego, nro_nivel_actual



