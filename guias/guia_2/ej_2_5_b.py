def par_impar(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

assert(par_impar(2)) == 0
assert(par_impar(3)) == 1
assert(par_impar(4)) == 0
assert(par_impar(5)) == 1
assert(par_impar(6)) == 0