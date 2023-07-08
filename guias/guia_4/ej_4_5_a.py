def es_biciesto(n):
    if n % 4 == 0 and n % 400 == 0:
        return True
    else:
        return False

print(es_biciesto(400)) #True
print(es_biciesto(100)) #False
print(es_biciesto(4)) #False    
print(es_biciesto(800)) #True
print(es_biciesto(-10)) #False