def numero_triangular(n):
    if n == 0:
        return 0
    else:
        return n + numero_triangular(n-1)
print(numero_triangular(6))