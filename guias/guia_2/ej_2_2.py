def tasa_interes():

    pesos = int(input("Cual es la cantidad de pesos a ingresar?: "))
    interes = int(input("Cuanto es el interes?: "))
    años = int(input("Cuantos años?: "))

    monto_final = int(pesos * (1 + interes/100) ** años)
    print("El monto final es:",monto_final)

tasa_interes()