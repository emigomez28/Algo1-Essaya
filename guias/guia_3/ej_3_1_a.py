def duracion_segundos(horas1, min1, seg1, horas2, min2, seg2):

    if horas1 <= horas2 and min1 <= min2 and seg1 <= seg2:

        horas_seg = int((horas2 - horas1) * 3600)
        min_seg = int((min2 - min1) * 60)
        seg = int(seg2 - seg1)
        resultado = horas_seg + min_seg + seg
        print(resultado)
    else:
       print("El intervalo no es valido")
                
def main():       
    duracion_segundos(1,2,3,4,5,6)
    duracion_segundos(1,3,4,5,9,6) 
    duracion_segundos(7,2,1,5,2,1)
    duracion_segundos(1,2,3,4,1,5)
main()

