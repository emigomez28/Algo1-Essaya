def es_valida(d, m, n):
    
    if d > 0 and d <= 31:
        if m > 0 and m <=12:
            if n > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
    
            
    
        
    

print(es_valida(0,2,6)) #False
print(es_valida(1,0,14)) #False
print(es_valida(0,0,0)) #False
print(es_valida(-6,0,89)) #False
print(es_valida(14,9,2022)) #True