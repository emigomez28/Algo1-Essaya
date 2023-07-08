def num_par():
    num_1 = int(input("Por favor ingrese un número: "))
    num_2 = int(input("Por favor ingrese otro número: "))
    
    if num_1 < num_2:
        for i in range(num_1, num_2 + 1):
            if i % 2 == 0:
                    print(i)          
    else:
        if not num_1 < num_2:
            for j in range(num_2, num_1, -1):
                if j % 2 == 0:
                    print(j)
        else:
            print("No hay ningun numero divisible entre los dos números")    


num_par()


