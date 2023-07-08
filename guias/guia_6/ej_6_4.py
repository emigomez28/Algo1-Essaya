

def separar_miles(s):
    aux = ""
    separacion = s[:: 3]
    for i in range(len(s)-1, -1, -1):
        if s[i] in separacion and i != 0:
            aux += "."
            aux += s[i]
        else:
            aux += s[i]
    print(aux)

separar_miles("1234567890")