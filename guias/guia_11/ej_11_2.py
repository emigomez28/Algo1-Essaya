def cp(archivo):
    with open(archivo, 'r') as f, open('new.txt', 'a') as new:
        line = f.read(800)
        new.write(line)

cp('practica.txt')