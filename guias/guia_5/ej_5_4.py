import random

def get_randint():
    random_int = random.randrange(0, 21)
    return random_int

def num_rand():
  num_secreto = get_randint()
  num_user = int(input("Porfavor ingrese un nro: "))
  condicion = True
  while condicion:
    if num_user < num_secreto:
        num_user = int(input(("El numero ingresado es menor, porfavor ingrese un nro nuevamente: ")))
    elif num_user > num_secreto:
        num_user = int(input(("El numero ingresado es mayor, porfavor ingrese un nro nuevamente: ")))
    else:
        num_user == num_secreto
        condicion = False
        print("Encontraste el nro!")
    
        
num_rand()