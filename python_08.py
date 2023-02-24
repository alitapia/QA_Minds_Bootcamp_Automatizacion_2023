# Escribe un script que dado un número permita calcular la sumatoria de todos los números que lo
# preceden desde cero. Ejemplo:
# número = 5
# resultado = 1+2+3+4+5

limite = int(input("Ingresa un numero"))
suma = 0
numero = 0

while numero <= limite:
    suma += numero
    numero +=1
print(suma)
print("*"*10)

# Escribe un script que dado dos números permita mostrar todos los números que existen entre ambos. Ejemplo:
# numero_a = 8
# numero_b = 5
# Resultado: 6,7

#NUMERO_A = 8
#NUMERO_B = 5

NUMERO_A = int(input("Ingresa un numero"))
NUMERO_B = int(input("Ingresa otro numero"))

if NUMERO_A > NUMERO_B and (NUMERO_B+1 != NUMERO_A):
    NUMERO_B +=1
    while NUMERO_B < NUMERO_A:
        print(NUMERO_B)
        NUMERO_B += 1
elif NUMERO_B > NUMERO_A and (NUMERO_A+1 != NUMERO_B):
    NUMERO_A += 1
    while NUMERO_A < NUMERO_B:
        print(NUMERO_A)
        NUMERO_A += 1
else:
    print("No hay numeros intermedios")

print("*"*10)



#Escribe un script que dado un número aleatorio permita encontrar su valor por medio de interacción con usuario,
# mostrando cuantos intentos le llevó al mismo detectarlo. Para realizar
# este script será necesario utilizar la librería random y del comando input para ingresar el número por consola.

import random
numero = random.randint(0,10)
print(numero)
my_value = -1
while my_value != numero:
    my_value = int(input("Ingresa un numero entre 0 y 10"))


print(f"{my_value} es el numero correcto")




