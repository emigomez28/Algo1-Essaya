def intervalo(seg1, seg2):
    if seg2 >= seg1 and seg1 > 0 and seg2 > 0:
        segundos = float(seg2 - seg1)
        horas = segundos // 3600
        min = (segundos % 3600) / 60
        seg_sobrante = (segundos % 3600)% 60
        print(f"horas:  {horas} minutos: {min} segundos: {seg_sobrante}")

    else:
        print("El intervalo no es valido")







def main():
    intervalo(0,3600)
    intervalo(0, 60)
    intervalo(500, 800)
    intervalo(700, 600)
    intervalo(15, 78)
    #intervalo("asd",80)
    intervalo(-8000, 9000)


main()