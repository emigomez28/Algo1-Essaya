def pedir_entero(mensaje, min, maximo):
    condicion = True
    while condicion:
        z = input(f"{mensaje} [{min}..{maximo}]: ")

        if z.isdecimal():
            conversion = float(z)
            if conversion in range(min, maximo+1):
                condicion = False
                print(z)
            else:
                print(f"Porfavor ingrese un nro entre {min} y {maximo}")
        else:
            print(f"Porfavor ingrese un nro entre {min} y {maximo}")

pedir_entero("Cual es tu nro favorito?", -50, 50)