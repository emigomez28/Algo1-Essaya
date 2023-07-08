def tasa_interes(pesos, interes, años):
    monto_final = pesos * (1 + interes/100) ** años
    return monto_final

def main():
    int(tasa_interes(10000,50,10))
    int(tasa_interes(100,10,1))
    int(tasa_interes(3450,20,5))
    int(tasa_interes(300,1,15))
    int(tasa_interes(3000,1,30))
main()