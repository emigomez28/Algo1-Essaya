def domino(ficha1, ficha2):
    for i in range(0,len(ficha1) - 1):
        sep1 = ficha1.split("-")
        sep2 = ficha2.split("-")
        if sep1[i] == sep2[i] or sep1[0] == sep2[i]:
                return True
    return False

print(domino("3-4","5-4")) #True
print(domino("1-2","2-1")) #True
print(domino("3-4","6-1")) #False
print(domino("3-4","5-3")) #True
print(domino("5-6","2-1")) #False