def reemplazar(s):
    ESPACIO = " "
    aux = ""
    for i in range (0,len(s)):
        if s[i] == ESPACIO:
            aux += "_"
        else:
            aux +=s[i]
    print(aux[:len(aux)])


