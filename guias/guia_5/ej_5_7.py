def suma_divisores(n):
    contador = 1
    for i in range (2, n):
        if n % i == 0:
            contador += i
    return(contador)

#print(suma_divisores(5))
#print(suma_divisores(89))
#print(suma_divisores(98))
#print(suma_divisores(20))
#print(suma_divisores(8))
#print(suma_divisores(6))
