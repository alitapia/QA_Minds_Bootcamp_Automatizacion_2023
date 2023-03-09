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
    resultado = None
    for st in STATUS:  # accedemos a cada elemento de la lista
        if st == estado_add:
            resultado = st
            break
    if resultado:
        nueva_entrada = {
            "curso": curso,
            "alumnos": alumnos,
            "estado": estado_add,
            "clases": clases
        }
        lst.append(nueva_entrada)
        print(lst)
    else:
        print("Status no valido, curso no agregado")
        print("Intente de nuevo")



CURSOS = []#Es una lista de diccionarios

def search(lst: list, target: str):
    res = None
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            res = lst[index]
            break
    if res:
        print(lst[index])
    else:
        print("Curso no encontrado")

def update_st(lst:list, target:str , sta:str):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            lst[index]['estado'] = sta
            print("Estatus del curso actualizado")
            print(lst[index])
def delete(lst:list, target:str):
    res_del = None
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            res_del = lst[index]['curso']
            break
    if res_del:
            print(f"Lista inicial: {lst}")
            print(f"Eliminando curso {lst[index]}")
            lst.pop(index)
            print("Curso eliminado")
            print(lst)
    else:
            print("Curso no existe en la lista")
            print("Intente de nuevo")



def update_numalumn(lst:list, target:str , num:int):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            lst[index]['alumnos'] = num
            print("Cantidad de alumnos del curso actualizado")
            print(lst[index])

def update_numclases(lst:list, target:str , num:int):
    for index, elem in enumerate(lst):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
        if lst[index]['curso'] == target:
            lst[index]['clases'] = num
            print("Cantidad de clases del curso actualizado")
            print(lst[index])
def list_courses(lst:list):
    listado = []
    for index, elem in enumerate(lst):
        listado.append(lst[index]['curso'])
    if len(listado) > 0:
        print(listado)
    else:
        print("No hay cursos disponibles")

def list(lst:list):
    print(lst)
    pass

while True:
     action = input("Seleccione una acción: SEARCH | DELETE | ADD | UPDATE_STATUS|UPDATE_NUMALUMNOS | UPDATE_NUMCLASES | LIST | EXIT ")
     if action == "SEARCH":
         course = input("Que curso buscas?")
         search(CURSOS,course)
     elif action == "ADD":
         add_course(CURSOS)
     elif action == "DELETE":
         course = input("Que curso deseas eliminar?")
         delete(CURSOS,course)
     elif action == "UPDATE_STATUS":
         course = input("Que curso deseas actualizar?")
         res = None
         for index, elem in enumerate(CURSOS): # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
            if CURSOS[index]['curso'] == course:
                res = CURSOS[index]
                break
         if res:
             res1 = None
             status = ("NO_INICIADO", "ACTIVO")
             status_list = " | ".join(status)
             nuevo_estado = input(f"Seleccione un status: {status_list}")
             for st in status:  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
                 if nuevo_estado == st:
                     res1 = nuevo_estado
                     break
             if res1:
                 update_st(CURSOS, course, nuevo_estado)

             else:
                 print("Status no valido, curso no actualizado")
                 print("Intente de nuevo")
         else:
             print("Curso no existe en catalogo, intente de nuevo")
     elif action == "UPDATE_NUMALUMNOS":
         course = input("Que curso deseas actualizar")
         res = None
         for index, elem in enumerate(CURSOS):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
             if CURSOS[index]['curso'] == course:
                 res = CURSOS[index]
                 break
         if res:
             nuevo_alumnos = input("Cual es el nuevo numero de alumnos en el curso?")
             update_numalumn(CURSOS, course, nuevo_alumnos)
         else:
             print("Curso no existe en el catalogo, intente de nuevo")
     elif action == "UPDATE_NUMCLASES":
         course = input("Que curso deseas actualizar")
         res = None
         for index, elem in enumerate(CURSOS):  # accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
             if CURSOS[index]['curso'] == course:
                 res = CURSOS[index]
                 break
         if res:
             nuevo_clases = input("Cual es el nuevo numero de clases en el curso?")
             update_numclases(CURSOS, course, nuevo_clases)
         else:
             print("Curso no existe en el catalogo, intente de nuevo")
     elif action == "LIST":
         list_courses(CURSOS)
         #list(CURSOS)
     elif action == "EXIT":
         break
     else:
        print("Operacion no soportada")
