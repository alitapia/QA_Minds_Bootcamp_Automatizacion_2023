def es_par(num1: int):
   resultado = (num1 % 2)
   print(resultado)
   return not resultado


numero1 = int(input("Introduce el número"))
print(f"El número {numero1} es par?: {es_par(numero1)}")