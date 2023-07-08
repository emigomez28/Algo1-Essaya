def es_potencia_de_dos(n):

    i = 2
    while True:
        i *= 2
        if i == n:
            return True
        if i > n:
            return False  


#print(es_potencia_de_dos(1024)) #True
#print(es_potencia_de_dos(2)) #True
#print(es_potencia_de_dos(89)) #False
#print(es_potencia_de_dos(0)) #False
#print(es_potencia_de_dos(64)) #True
#print(es_potencia_de_dos(6)) #False

