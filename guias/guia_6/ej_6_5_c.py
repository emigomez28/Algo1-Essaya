def palabras_a(s):
    aux = ""
    A = "A"
    ESPACIO = " "
    for i in range(0, len(s)+1):
        if s[i] == ESPACIO and s[i + 1] == A or s[i + 1] == A.lower():
            aux += s[i]
        elif s[i + 1] != A or s[i + 1] != A.lower() and s[i] == ESPACIO:
            pass
        else:
            aux += s[i]
    print(aux)

palabras_a("Antes de ayer") # Antes ayer