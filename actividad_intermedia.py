#libreria titulo, autor, genero


def add_course(lst: list):
    print("*" * 80)
    print("Agrega Nuevo Curso:")
    print("*" * 80)
    curso = input(" Nombre del curso?")
    alumnos = input(" Cantidad de alumnos?")
    STATUS = ("NO_INICIADO", "ACTIVO")

    status_list = " | ".join(STATUS)
    estado = input(f"Seleccione un status: {status_list}")
    clases = input("Cantidad de clases")



    nueva_entrada = {
        "curso": curso,
        "alumnos": alumnos,
        "estado": estado,
        "clases": clases
    }
    lst.append(nueva_entrada)
    print(lst)

CURSOS = []#Es una lista de diccionarios
def search(lst: list, target: str):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        for key, crs in elem.items():  # acedemos a cada llave(k), valor(v) de cada diccionario
            if crs == target:
                print(lst[index])
print("Curso no existe")
def update(lst:list, target:str , sta:str):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        for key, csr in elem.items():  # acedemos a cada llave(k), valor(v) de cada diccionario
            if csr == target:
                lst[index]['estado'] = sta
                print("Estatus del curso actualizado")
                print(lst[index])
print("Curso no encontrado")





def list(lst:list):
    print(lst)
    pass

while True:
     action = input("Seleccione una acción: SEARCH | ADD | UPDATE | LIST | EXIT ")
     if action == "SEARCH":
         course = input("Que curso buscas?")
     elif action == "ADD":
         add_course(CURSOS)
     elif action == "UPDATE":
         course = input("Que curso deseas actualizar?")
         for index, elem in enumerate(CURSOS):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
             for key, crs in elem.items():  # acedemos a cada llave(k), valor(v) de cada diccionario
                 if crs == course:
                     print(lst[index])
                     continue
             print("Curso no existe")
         break
         status = ("NO_INICIADO", "ACTIVO")
         status_list = " | ".join(status)
         nuevo_estado = input(f"Seleccione un status: {status_list}")
         for estado in status:
             if estado == nuevo_estado:
                 update(CURSOS,course,nuevo_estado)
         print("Status no valido")
         print("Curso no actualizado")
     elif action == "LIST":
         list(CURSOS)
     elif action == "EXIT":
         break
     else:
        print("Operacion no soportada")
