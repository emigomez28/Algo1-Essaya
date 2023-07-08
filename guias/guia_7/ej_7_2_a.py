def domino(ficha1, ficha2):
    for i in range(0, len(ficha1)):
        if ficha1[i] == ficha2[i] or ficha1[i-1] == ficha2[i]:
            return True
    return False

print(domino((3,4),(5,4))) #True
print(domino((1,2),(2,1))) #True
print(domino((3,4),(6,1))) #False
print(domino((3,4),(5,3))) #True
print(domino((5,6),(2,1))) #False