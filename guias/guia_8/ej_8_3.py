def agenda(string, lista):
    res = []
    aux = ""
    
    for i in range(len(lista)):
            aux += lista[i][0]
            if aux == string:
                res.append(lista[i][0])
    return res


