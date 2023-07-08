def sin_consonantes(s):
    VOCALES = ["a","e","i","o","u"]
    aux = ""
    ESPACIO = " "
    for i in range(0, len(s)):
        if s[i] in VOCALES or s[i] == ESPACIO:
            aux += s[i]
        else:
            pass
    print(aux)
    

sin_consonantes("sin consonantes")