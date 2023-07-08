def coincidencias(lista, elemento):
    contador = 0
    for i in range (len(lista)):
        if lista[i] == elemento:
            contador += 1
    return contador

l = [1,2,34,1,2,45,1,6,0,90,1,1]
e = 0

print(coincidencias(l,e))