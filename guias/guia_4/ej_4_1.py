from math import sqrt

def es_par(n):
    return n % 2 == 0 
        

def es_primo(n):
    
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def main():
    print(es_par(4))
    print(es_par(3))
    print(es_par(5))
    print(es_par(56))
    print(es_par(89))
    print(es_primo(2)) #True
    print(es_primo(3)) #True
    print(es_primo(4)) #False
    print(es_primo(17)) #True
    print(es_primo(11)) #True
main()