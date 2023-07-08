def abreviar(s):
    iniciales = ""
    ESPACIO = " "
    for i in range(0, len(s)):
        if i == 0:
            iniciales += s[i]
        elif s[i] == ESPACIO:
            iniciales +=s [i+1]
        else:
            pass
    print(iniciales)

abreviar("Universal Serial Bus") # USB
