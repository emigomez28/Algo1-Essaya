def agenda():
    CENTINELA = "*"
    SALIDA = "Gracias, vuelva prontos!"
    agenda = dict()
    add_name = input(f"Porfavor ingrese un nombre, utilice {CENTINELA} para salir: ")
    while add_name != CENTINELA:
    
        if add_name in agenda:
            cond = input("Desea cambiar el numero? si/no: ")
            if cond.lower() == "si":
                add_num = input("Porfavor ingrese el nro. correspondiente: ")    
                agenda[add_name] = add_num
            else:
                add_name = input(f"Porfavor ingrese un nombre, utilice {CENTINELA} para salir: ")
        else:
            add_num = input("Porfavor ingrese el nro. correspondiente: ")
            agenda[add_name] = add_num
    print(SALIDA)     
    print(agenda)
    return agenda

agenda()