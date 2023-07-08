def sucesion_naturales():
    cant_notas = 0
    suma_num = 0
    CENTINELA = -1

    i = int(input("Porfavor ingrese una nota, use -1 para salir: "))

    while i != CENTINELA:
    
        cant_notas += 1
        suma_num += i
        i = int(input("Porfavor ingrese una nota, use -1 para salir: "))    
        
    promedio = suma_num / cant_notas
    print(f"La cantidad de notas es {cant_notas}, la suma total de las notas es {suma_num} y el promedio es {promedio}")
            
    

sucesion_naturales()
