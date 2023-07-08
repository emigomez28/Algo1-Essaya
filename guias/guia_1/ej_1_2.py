def numero_producto(num_1,num_2):
    return num_1 * num_2

def usuario():
    num_1 = int(input("Por favor ingrese un número: "))
    num_2 = int(input("Por favor ingrese otro número: "))
    multiplicar = numero_producto(num_1,num_2)
    print(multiplicar)

usuario()
