def multiplo_10(num):
    mult_10 = (num // 10) * 10
    return(mult_10) 

assert(multiplo_10(153)) == 150
assert(multiplo_10(147)) == 140
assert(multiplo_10(15)) == 10
assert(multiplo_10(567)) == 560
assert(multiplo_10(458)) == 450