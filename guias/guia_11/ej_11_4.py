def grep(cadena, archivo):
    with open(archivo) as f:
        for linea in archivo:
            if cadena == linea:
                print(linea)

grep('Hola', 'practica.txt')