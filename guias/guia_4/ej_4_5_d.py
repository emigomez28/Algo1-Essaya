from ej_4_5_c import es_valida

def fin_de_mes(d , m, n):
    if es_valida(d, m, n):
        dias_hasta_finde = 0
        for i in range(d, 31):
            dias_hasta_finde += 1
        return dias_hasta_finde
    else:
        return False


print(fin_de_mes(0,2,6)) 
print(fin_de_mes(1,0,14)) 
print(fin_de_mes(0,0,0)) 
print(fin_de_mes(-6,0,89))
print(fin_de_mes(14,9,2022)) 
