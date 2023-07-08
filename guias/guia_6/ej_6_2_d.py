
def insertar_cada_3(s, c):
    aux = ""
    for i in range(0, len(s)):
        if i % 3 == 0 and i != 0:
            aux += c
            aux += s[i]
        else:
            aux += s[i]
    print(aux)

insertar_cada_3("2552552550", ".")
insertar_cada_3("Emiliano", "-") #Emi-lia-no



