def prod_escalar(vec1, vec2):
    prod_escalar = 0
    for i in range(0, len(vec1)):
        for j in range(0, len(vec2)):
            prod_escalar =+ vec1[i] * vec2[j]
    print(prod_escalar)

prod_escalar((1,0),(0,1)) #0
prod_escalar((2,0),(1,1)) #2
prod_escalar((0,0),(10,5)) #0
prod_escalar((2,5),(1,3)) #17
prod_escalar((5,8),(10,11))#138