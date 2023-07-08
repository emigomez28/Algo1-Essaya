from math import pi

def VolumenEsfera(radio):
    volumen = (4/3) * pi * (radio ** 3)
    return volumen

print(VolumenEsfera(1))
print(VolumenEsfera(3))
print(VolumenEsfera(7))
print(VolumenEsfera(pi))

