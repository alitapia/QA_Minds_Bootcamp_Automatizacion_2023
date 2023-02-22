import datetime

def calcula_edad (mes, año):
    today = datetime.date.today()
    current_year = today.year
    if (mes <= 2):
        edad = (current_year- (año +1))
        cumple = "Ya cumplió años"
    # nprint(edad)
    # print("Aun no cumple años")
    else:
        edad = (current_year - año)
        cumple = ("Aun no cumple años")
    # print(edad)
    # print("Ya cumplió años")
    return (edad, cumple)


day = int(input("Introduce el dia de tu nacimiento"))
month = int(input("Introduce el mes de tu nacimiento"))
year = int(input("Introduce el año de tu nacimiento"))

if year > 1920 and year < 1939:
    print("Generación silenciosa")
    print(f"La edad es:  {calcula_edad(month , year)}")
elif year > 1940 and year < 1959:
    print("Baby boomers")
    print(f"La edad es:  {calcula_edad(month, year)}")
elif year > 1960 and year < 1979:
    print("Generación X")
    print(f"La edad es:  {calcula_edad(month, year)}")
elif year > 1980 and year < 1989:
    print("Generación Y")
    print(f"La edad es:  {calcula_edad(month, year)}")
else:
    print("Generación Z")
    print(f"La edad es:  {calcula_edad(month, year)}")

