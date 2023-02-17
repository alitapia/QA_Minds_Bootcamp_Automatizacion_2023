def conversor_temp(num1: float):
   farenheit= (num1 *9/5)+32
   return farenheit


numero1 = int(input("Introduce la temperatura en °C que quieres convertir"))
print(f"La temperatura {numero1}°C es igual a {conversor_temp(numero1)}°F")