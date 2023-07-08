def vote_por_mi(t,p,n):
    for i in range(p, n + 1):
        if t[i][1] == "Hombre":
            print(f"Estimado {t[i][0]}, vote por mi")
        else:
            print(f"Estimada {t[i][0]}, vote por mi")


vote_por_mi((("Emiliano", "Hombre"), ("Pepito", "Hombre"), ("Jorge", "Hombre"), ("Eva","Mujer")),1, 3)