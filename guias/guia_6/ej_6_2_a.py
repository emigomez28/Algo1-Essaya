def separar(cadena, caracter):
    aux = ""
    
    for i in range (0, len(cadena)):

        aux += cadena[i]
        aux+= caracter

    print(aux[:len(aux)-1])


separar("separar", ",")