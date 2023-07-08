from vectores import diferencia, producto_vectorial, norma

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    #Devuelve el area de un triangulo dados 3 vectores en el espacio R3
    
    ab_x, ab_y, ab_z = diferencia(x1, y1, z1, x2, y2, z2)
    ac_x, ac_y, ac_z = diferencia(x1, y1, z1, x3 ,y3, z3)

    res_x, res_y, res_z = producto_vectorial(ab_x, ab_y, ab_z, ac_x, ac_y, ac_z)
    
    norma_res = norma(res_x, res_y, res_z)
    
    area = norma_res / 2
    
    return float(area)

assert(area_triangulo(5,8,-1,-2,3,4,-3,3,0)) == 19.45507645834372
assert(area_triangulo(1,2,3,4,5,6,7,8,9,)) == 0.0
assert(area_triangulo(2,7,8,26,89,10,6,2,1)) == 370.7344062802912
assert(area_triangulo(1,7,8,9,0,4,21,70,698)) == 3630.868353438334
assert(area_triangulo(89,75,97,90,53,35,28,5,3)) == 2354.7348046011466

