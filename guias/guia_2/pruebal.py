#from guia_1.ej_1_5 import factorial

def factorial(n):
    fact = 1
    for i in range(2, n + 1):             
        fact *= i
    return fact


def calcular_factoriales():
    m = int(input("Por favor ingrese la cantidad de valores a los cuales desea calcular su factorial: "))

    for m in range(0, m):
        n = int(input("Por favor ingrese el número al cual quiere calcular su factorial: "))
        fact_n = factorial(n)
        print("El factorial de " + str(n) + " es ", fact_n)

calcular_factoriales()