def password():
    PASSWORD = "hipopotamo"
    i = input("Contraseña: ")
    
    while i != PASSWORD:
        i = input("Contraseña: ")
    print("Pasaste")


password()