def password():
    PASSWORD = "hipopotamo"
    i = input("Contraseña: ")
    intentos = 0
    
    while i != PASSWORD and intentos < 4:
        intentos += 1
        i = input("Contraseña: ")

    if intentos > 4 or i != PASSWORD:
        return False
    else:
        return True
        

password()
