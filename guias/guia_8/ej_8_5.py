def f(lista, elemento):
    max = len(lista) - 1
    min = 0
    mid = 0

    while min <= max:
        mid = (max + min) // 2
        if lista[mid] < elemento:
            min = mid + 1
        elif lista[mid] > elemento:
            max = mid - 1
        else:
            return mid
    lista.insert(min, elemento)
    return min
    
        

l =[1,2,3,4,6,7,8,9,10]
e = 5
print(f(l,e))
print(l)