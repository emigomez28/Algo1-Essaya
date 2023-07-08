def consonantes(s):
    VOCALES = ["a","e","i","o","u"]
    aux = ""
    for i in range(0, len(s)):
        if s[i] in VOCALES:
            pass
        else:
            aux += s[i]
    print(aux)

consonantes("algoritmos")
consonantes("logaritmos")
