def conv_fah():
    for celsius in range(0,121,10):
        grados_fah = int((9/5) * celsius + 32)
        print(celsius, grados_fah)

conv_fah()