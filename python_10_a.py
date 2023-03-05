#Define una tupla con los valores [1, 2, 3, 4, 5] e imprime el tamaño de la misma.
#Luego dado un número aleatorio  entre el 1 y 5 recorrer la tupla e imprimí todos los números hasta que
# coincida el número generado.
import random
print("Ejercicio 1")
tupla = (1,2,3,4,5)

print(f"El tamaño de la tupla es: {len(tupla)}")


rand_num = (random.randint(1,5))
print(f"Numero aleatorio: {rand_num}")

for num in tupla:
    print(num)
    if num == rand_num:
        break
    else:
        continue

print("*"*30)
print("Ejercicio 2")
# Dada una tupla de distribución de puntos para la Fórmula 1 (25, 18, 15, 12, 10, 8, 6, 4, 2, 1 ) indique:
# Cuántos de estos números son pares
# Cuantos puntos se le entregan a los tres primeros.
# Cual seria la sumatoria de todos los números.

tupla_1 = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1 )

pares = []
suma = 0

for num in tupla_1:
    #print(num)
    if num % 2 == 0:
        pares.append(num)
    suma += num
print(f"La tupla: {tupla_1}")
print(f"{len(pares)} son pares {pares}")
print(f"La suma es: {suma}")

print("*"*30)


print("Ejercicio 3 ")
# Crear un metodo para validar si una lista es un palindromo.
#
# Por ejemplo:
# lista = ["a", "c", "a", "v", "a", "r", "a", "c", "a", "r", "a", "v", "a", "c", "a"]
#
# is_palindrome(lista) # Debe regresar true
def is_palindromo(lista):
    lista_back = list(lista)
    lista_back.reverse()
    print(lista)
    print(lista_back)
    #resultado = False
    #if lista == lista_back:
    #    resultado = True
    #else:
    #    resultado = False
    #print(resultado)
    print(lista==lista_back)



lista_a = ["a", "c", "a", "v", "a", "r", "a", "c", "a", "r", "a", "v", "a", "c", "a"]
is_palindromo(lista_a)