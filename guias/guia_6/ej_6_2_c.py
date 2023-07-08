def password(cadena, caracter):
    aux = ""
    for i in range(0, len(cadena)):
        aux += caracter
    print(f"Su clave es: {aux}")

password("Emi", "*") #***
password("1234567", "X") #XXXXXXX