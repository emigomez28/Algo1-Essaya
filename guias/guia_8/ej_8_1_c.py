def todas_coincidencias(lista, elemento):
    res = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            res.append(i)
    return res

l = [1,2,34,1,2,45,1,6,0,90,1,1]
e = 1

print(todas_coincidencias(l,e))