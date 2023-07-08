def primera_coincidencia(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

l = [1,2,34,1,2,45,1,6,0,90,1,1]
e = 1

print(primera_coincidencia(l,e))
