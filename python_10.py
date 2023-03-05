import random
print("Ejercicio 1")
lista_a =[1,2,3,4,5]

print(f"Tamaño : {len(lista_a)}")

nuevo = (random.randint(1,10))
print(f"Numero aleatorio: {nuevo}")

lista_a.append(nuevo)
print(lista_a)
tamaño=len(lista_a)
count = 0

for num in range(0, tamaño, 1):
    if lista_a[num] == nuevo:
        count +=1
print(f"El numero {nuevo} aparece {count} en la lista {lista_a}")

print("*"*20)
print ("Ejercicio 2")
# Define una lista de 9 registros con valores aleatorios del 1 al 9.
#
# Recorre la lista en búsqueda de números repetidos. Si existe un número repetido cancela el proceso y
# manda un mensaje indicando cuál número está repetido. De lo contrario, muestra un mensaje que indique que no
# existen números repetidos.



lista_b = []
for _ in range(0, 9, 1):
 lista_b.append(random.randint(1,9))
print(f"Lista= {lista_b}")
tamaño = len(lista_b)

# while len(lista_b)<9
# rnd_num = random.randint(1,9)
#lista_b.append(rnd_num)

num = 0
for num in lista_b:
    if lista_b.count(num) > 1:
        print(f"Numero repetido: {lista_b[num]}")
        break
else:
    print ("Numero no repetido")
print("*"*20)

print("Ejercicio 3")
#Dada una lista de Poker Planning [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100 ] indique:
#Cuantos de estos números son pares
# Cuantos son divisibles por el numero anterior y que de un resultado entero mayor que cero. Ejemplo 2 / 1 = 2.
#Cual seria la sumatoria de todos los números.
pares = []
divisibles = []
suma = 0
lista_planning = [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100]

for index , num in enumerate(lista_planning):
    #if index > 0:
    # prev_num = lista[index-1]
    #else: None
    prev_num = lista_planning[index - 1] if index >0 else None
    if num % 2 == 0:
        pares.append(num)

    if prev_num and prev_num > 0 and num % prev_num == 0:
        divisibles.append(num)
    suma += num

print(f"{len(pares)} son números pares {pares}")
print(f"{len(divisibles)} son números divisibles {divisibles}")
print(f"La suma es: {suma}")

