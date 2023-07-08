def es_potencia(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * es_potencia(a, b - 1)

print(es_potencia(2,3))