#libreria titulo, autor, genero
STATUS = ("NO_INICIADO", "ACTIVO")


def add_course(lst: list):
    print("*" * 80)
    print("Agrega Nuevo Curso:")
    print("*" * 80)
    curso = input(" Nombre del curso?")
    alumnos = input(" Cantidad de alumnos?")
    clases = input("Cantidad de clases")
    status_list = " | ".join(STATUS)
    estado_add = input(f"Seleccione un status: {status_list}")

    for st in STATUS:  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if estado_add == st:
            nueva_entrada = {
                "curso": curso,
                "alumnos": alumnos,
                "estado": estado_add,
                "clases": clases
            }
            lst.append(nueva_entrada)
            print(lst)
            break
        elif estado_add != st:
            print("Curso no agregado: Status no valido")
            print("Intente de nuevo")
            break
        else:
            break






CURSOS = []#Es una lista de diccionarios

def search(lst: list, target: str):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            print(lst[index])
        else:
            print("Curso no encontrado")

def update(lst:list, target:str , sta:str):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            lst[index]['estado'] = sta
            print("Estatus del curso actualizado")
            print(lst[index])

def list(lst:list):
    print(lst)
    pass

while True:
     action = input("Seleccione una acción: SEARCH | ADD | UPDATE | LIST | EXIT ")
     if action == "SEARCH":
         course = input("Que curso buscas?")
         search(CURSOS,course)
     elif action == "ADD":
         add_course(CURSOS)
     elif action == "UPDATE":
         course = input("Que curso deseas actualizar?")
         status = ("NO_INICIADO", "ACTIVO")
         status_list = " | ".join(status)
         nuevo_estado = input(f"Seleccione un status: {status_list}")
         for index, elem in enumerate(CURSOS):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
             if CURSOS[index]['curso'] == course:
                 for st in status:  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                     if nuevo_estado == st:
                         update(CURSOS, course, nuevo_estado)
                         break
                     elif nuevo_estado != st:
                         print("Curso no actualizado: Status no valido")
                         print("Intente de nuevo")
                         break
                     else:
                         break
             elif CURSOS[index]['curso'] != course:
                 print("Curso no existe en lista")
                 print("Intente de nuevo")
                 break
             else:
                 print("Intente de nuevo")
                 break

     elif action == "LIST":
         list(CURSOS)
     elif action == "EXIT":
         break
     else:
        print("Operacion no soportada")
