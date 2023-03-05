#Imprime todos los números del 0 al 99, de dos en dos y que no sean múltiplos del 3



for num in range(0, 100, 2):
    if num %3 == 0:
        continue
    else:
        print(f"{num}")
print("*"*10)


#2. Dado un número aleatorio del 1 al 20 multiplicado por 2, imprime el valor del mismo. Itera los números del 1 al 99,
# y en cuanto el número sea igual al número aleatorio rompemos la iteración y muestre la suma de todos los
# números iterados hasta el momento.

import random
MIN = 1
MAX = 20
numero = (random.randint(MIN,MAX))*2
numero = int(numero)
suma = 0

for num in range(1, 100, 1 ):
    if num == numero:
        print(numero)
        break
    suma += num
print(f"suma es: {suma}")
print("*"*10)



list = ["México" , "Venezuela","Argentina","Brasil","Colombia","Panama"]
list.append("Chile")
print(list)
list.sort()
print(list)


def is_country_present(countries: list , target : str):
    for country in countries:
        if country == target:
            return True
        return False

print(is_country_present(list, "Venezuela"))




list = ["México" , "Venezuela","Argentina","Brasil","Colombia","Panama"]
pretty = ",".join(list)
print(pretty)

split_result = "México,Venezuela,Argentina,Brasil,Colombia,Panama".split(",")
print(split_result)