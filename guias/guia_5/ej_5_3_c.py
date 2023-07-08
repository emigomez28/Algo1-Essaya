import time

def password():
    PASSWORD = "hipopotamo"
    i = input("Contraseña: ")
    intentos = 0

    while i != PASSWORD and intentos < 4:
        intentos += 1
        delay = 5 ** intentos 
        time.sleep(delay)
        
        i = input("Contraseña: ")
    if intentos > 4 or i != PASSWORD:
        print("Te quedaste sin intentos")

    else:
        print("Pasaste")


password()