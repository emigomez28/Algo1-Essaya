def head(ruta, n):
    with open(ruta) as f:
        for i in range(n):
            line = f.readline().rstrip()
            print(line)
head('asd.txt', 10)