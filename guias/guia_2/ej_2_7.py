def numeros_triangulares():
    n = int(input("Por favor ingrese un número: "))
    print("Los números triangulares son: ")
    for i in range(1,n+1):
        res = int(i * (i+1)/2)
        print(i,res)

numeros_triangulares()