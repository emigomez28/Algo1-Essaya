def euclides(m, n):
    r = m % n
    if r == 0:
        print(f"El MCD de {m} es {n}")
    else:
        while r > 0:
            m = n
            n = r
            r = m % n
        print(f"El MCD de {m} es {n}")
euclides(15, 9)    
euclides(9, 15)
euclides(10, 8)
euclides(12, 6)

