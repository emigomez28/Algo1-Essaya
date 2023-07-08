def mayusc(s):
    aux = ""
    ESPACIO = " "
    for i in range(0, len(s)):
        if i == 0:
            aux += s[i].upper()

        elif s[i] == ESPACIO:
            aux += ESPACIO
            aux += s[i+1].upper()
        
        elif s[i - 1] == ESPACIO and s[i].lower():
            pass
        else:
            aux += s[i]
    print(aux)

mayusc("republica argentina") #Republica Argentina
mayusc("estados unidos de america") #Estados Unidos De America
