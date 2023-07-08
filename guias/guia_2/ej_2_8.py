from guia_1.ej_1_5 import factorial

CENTINELA = 0

def ingresar_valores():
    m = int(input("Por favor ingrese un número para calcular su factorial: "))
    while m != CENTINELA:
        fact = factorial(m)
        print("El factorial de " + str(m) + " es: ", fact)
        
        m = int(input("Por favor ingrese un número para calcular su factorial: "))
        

ingresar_valores()