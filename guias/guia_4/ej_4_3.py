def matriz_identidad(n):
    matriz = "" 
    for i in range(0, n):
        for j in range (0,n):
            if i == j:
                matriz += "1"
            else:
                matriz += "0"
        matriz += "\n"
    print(matriz)

matriz_identidad(3)
matriz_identidad(4)
#matriz_identidad(90)
#matriz_identidad(59)