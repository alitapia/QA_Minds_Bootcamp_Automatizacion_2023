#tabla = int(input("Ingresa un numero del 1 al 10"))
#MIN = 1
#MAX = 11
#BASE = 1

#for number in range(MIN,MAX,BASE):
#    print(f"{tabla} * {number} = {tabla * number}")




import random
MIN = 1
MAX = 10
numero = random.randint(MIN, MAX)
print(numero)

INICIO = 1
FIN = numero

for number in range(INICIO,FIN):
    print("*"* number)
