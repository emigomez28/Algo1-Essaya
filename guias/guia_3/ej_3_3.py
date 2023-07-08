def mayor_producto(num1, num2, num3, num4):
    tupla = [num1, num2, num3, num4]
    maximo = 0
    for i in tupla:   # Recorren los numeros de la tupla
        for j in tupla:  
            producto = i * j
            if producto > maximo and i != j:
                maximo = producto
    print(maximo)
mayor_producto(1,-2,4,-8)