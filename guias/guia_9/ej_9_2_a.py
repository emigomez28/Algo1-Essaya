def cant_de_apariciones(cadena):
    cant = dict()
    palabras = cadena.lower().split()
    for p in palabras:
        if p in cant:
            cant[p] += 1
        else:
            cant[p] = 1
    return cant

s = "Que lindo dia hace hoy"
print(cant_de_apariciones(s))