def conv_fah(celsius):
    grados_fah = int((9/5) * celsius + 32)
    return grados_fah

def main():
    conv_fah(45)
    conv_fah(70)
    conv_fah(89)
    conv_fah(400)
    conv_fah(23)
main()