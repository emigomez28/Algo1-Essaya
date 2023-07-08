def modulo(n):
    if n < 0:
        return -n
    return n

def main():
    print(modulo(2)) 
    print(modulo(3)) 
    print(modulo(89)) 
    print(modulo(-56)) 
    print(modulo(-90)) 
    print(modulo(0)) 
main()