"""from math import factorial

def numero_factorial(x):
    return factorial(x)

print(numero_factorial(1))
print(numero_factorial(2))
print(numero_factorial(4))
print(numero_factorial(7))
print(numero_factorial(3))
"""

def factorial(n):
    fact = 1
    for i in range(2, n + 1):             
        fact *= i
    return fact

#print(factorial(1))
#print(factorial(2))
#print(factorial(3))
#print(factorial(4))
#print(factorial(7))   