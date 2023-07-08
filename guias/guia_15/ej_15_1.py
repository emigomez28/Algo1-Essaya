def cantidad_de_numeros(num):
    string = str(num)
    if string == "":
        return 0
    return 1 + cantidad_de_numeros(string[1:])

print(cantidad_de_numeros(1234567))