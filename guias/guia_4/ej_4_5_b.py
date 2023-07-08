def cant_dias(m, n):
    if m >= 0 and n >= 0:
        dias = m * 30 + n * 365
        return dias
    else:
        return "Los parametros no son validos" 

print(cant_dias(1, 1)) #395
print(cant_dias(2, 6)) #2250
print(cant_dias(-1,43 )) #Los parametros no son validos
print(cant_dias(8, 7))  #2795
print(cant_dias(19, 0)) #570