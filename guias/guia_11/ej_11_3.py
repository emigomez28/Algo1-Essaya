def wc(archivo):
    cant_lineas = 0
    cant_carac = 0
    cant_pal = 0
    with open(archivo) as file:
        for line in file:
            for word in line:
                if word == " " or word == "\n":
                    print(line)
                    cant_pal += 1
                cant_carac += 1
            cant_lineas += 1
    print(f"Cantidad de lineas: {cant_lineas} Cantidad de caracteres: {cant_carac} Cantidad de palabras: {cant_pal}", end =" ")
wc('practica.txt')