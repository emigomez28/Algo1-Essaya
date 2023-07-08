def facturacion(lista1, lista2):
    res = []
    suma = 0
    for i in range(len(lista1)):
        if lista1[i][0] == lista2[i][0]:
            precio_total = lista1[i][2] * lista2[i][1]
            cant = lista2[i][1]
            desc = lista1[i][1]
            p_uni = lista1[i][2]
            res.append((cant, desc, p_uni, precio_total))
    for j in range(len(res)): 
        suma += res[j][3]
    print(f"La suma total es: {suma}")

