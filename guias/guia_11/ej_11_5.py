def rot13(origen, destino):
    with open(origen, 'r') as o, open(destino, 'w') as d:
        line = o.readline().rstrip()
        for line in o:
            for char in line:
                conv = chr((ord(char) + 13) // 26)
                d.writelines(conv)


rot13('practica.txt', 'destino.txt')