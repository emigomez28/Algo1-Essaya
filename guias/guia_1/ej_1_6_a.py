from audioop import mul


def operaciones_mat(num_1, num_2):
    suma = num_1 + num_2
    resta = num_1 - num_2
    dividir = num_1 / num_2
    multiplicar = num_1 * num_2
    return(suma, resta, dividir, multiplicar)

print(operaciones_mat(2,3))
print(operaciones_mat(2,4))
print(operaciones_mat(6,3))
print(operaciones_mat(4,7))
