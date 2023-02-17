import datetime

obtiene_mes = int(input("Ingresa el numero de mes actual"))
if obtiene_mes in (3,4,5):
     print("Estamos en Primavera")
elif obtiene_mes in(6,7,8):
     print("Estamos en Verano")
elif obtiene_mes in (9, 10, 11):
    print("Estamos en Otoño")
elif obtiene_mes in(12,1,2):
    print("Estamos en Invierno")
else:
    print("El mes ingresado no existe. Por favor verifique e intente de nuevo")


