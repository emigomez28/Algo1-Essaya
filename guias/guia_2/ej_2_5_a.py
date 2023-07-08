def par_impar(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

assert(par_impar(2)) == 1
assert(par_impar(3)) == 0
assert(par_impar(4)) == 1
assert(par_impar(5)) == 0
assert(par_impar(6)) == 1
