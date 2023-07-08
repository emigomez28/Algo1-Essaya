from ej_5_6 import es_potencia_de_dos

def suma_de_potencias(n, m):
    contador = 0
    for i in range(n , m + 1):
        if es_potencia_de_dos(i):
            contador += i
    print(contador)
    
suma_de_potencias(2, 10)
suma_de_potencias(0, 1)
suma_de_potencias(0, 100)
        