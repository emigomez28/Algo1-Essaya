def tuplas_a_diccionario(lista):
    res = {}
    for k, v in lista:
        if not k in res:
            values = res.get(k,[])
            values.append(v)
            res[k] = values
        else:
            res[k].append(v)
    return res

l = [ ("Hola", "don Pepito"), ("Hola", "don Jose"), ("Buenos", "dias"), ("Hola", "Emi"), ("Buenas", "Tardes") ]
print(tuplas_a_diccionario(l))