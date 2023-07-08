def duracion_segundos(horas1, min1, seg1, horas2, min2, seg2):

    if horas1 <= horas2 and min1 <= min2 and seg1 <= seg2:

        horas_seg = int((horas2 - horas1) * 3600)
        min_seg = int((min2 - min1) * 60)
        seg = int(seg2 - seg1)
        resultado = horas_seg + min_seg + seg
        print(resultado)
    else:
       print("El intervalo no es valido")

def intervalo(seg1, seg2):
    if seg2 >= seg1 and seg1 > 0 and seg2 > 0:
        segundos = float(seg2 - seg1)
        horas = segundos // 3600
        min = (segundos % 3600) / 60
        seg_sobrante = (segundos % 3600)% 60
        print(f"horas:  {horas} minutos: {min} segundos: {seg_sobrante}")

    else:
        print("El intervalo no es valido")

def suma_intervalos():
    horas_1 = float(input("Ingrese la cantidad de horas: "))
    min_1 = float(input("Ingrese la cantidad de minutos: "))
    seg_1 = float(input("Ingrese la cantidad de segundos: "))

    horas_2 = float(input("Ingrese otra cantidad de horas: "))
    min_2 = float(input("Ingrese otra cantidad de minutos: "))
    seg_2 = float(input("Ingrese otra cantidad de segundos: "))  
    
    intervalo_1 = [horas_1, min_1, seg_1]
    intervalo_2 = [horas_2, min_2, seg_2]

    suma = [intervalo_1[0] + intervalo_2[0], intervalo_1[1] + intervalo_2[1], intervalo_1[2] + intervalo_2[2]]
    print(suma)




def main():
    suma_intervalos()

main()

