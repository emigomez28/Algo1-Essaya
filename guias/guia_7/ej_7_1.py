def tupla_ordenada(t):
    for i in range (1,len(t)):
        if t[i] < t[i - 1]:
            return False    
    return True


print(tupla_ordenada((1,2,3,4,5,6,7)))
print(tupla_ordenada((1,2,3,0,2)))