from enum import Enum
import random

##########################################################################################
# ABSTRACIONES DEL JUGADOR, PARTIDAS
##########################################################################################
class Raza(Enum):
    TERRAN = 1
    ZERG = 2
    PROTOSS = 3
class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2
    JUGANDO = 3
class Partida:
    def __init__(self, partida: str, jugador1: str, jugador2: str, nivel: int, ganador: str):
        self.__partida = partida
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__nivel = nivel
        self.__ganador = ganador
    def obtiene_partida(self):
        return self.__partida
    def obtener_jugador1(self):
        return self.__jugador1
    def obtener_jugador2(self):
        return self.__jugador2
    def obtener_nivel(self):
        return self.__nivel
    def obtener_ganador(self):
        return self.__ganador
    def actualizar_ganador(self, ganador: str):
        self.__ganador = ganador
    def __str__(self):
        return repr(self)
    def __repr__(self):
        return f"(partida={self.__partida}, jugador1={self.__jugador1}, jugador2={self.__jugador2}, nivel={self.__nivel}, ganador={self.__ganador})"
class Jugador:
    def __init__(self, nombre: str, mail: str, puntos: int, partidas: int, raza: Raza, estado: Estado):
        self.__nombre = nombre
        self.__mail = mail
        self.__puntos = puntos
        self.__partidas = partidas
        self.__raza = raza
        self.__estado = estado
    def obtener_nombre(self):
        return self.__nombre
    def obtener_mail(self):
        return self.__mail
    def obtener_puntos(self):
        return self.__puntos
    def obtener_partidas(self):
        return self.__partidas
    def obtener_raza(self):
       return self.__raza
    def obtener_estado(self):
        return self.__estado
    def actualizar_estado(self, estado: str):
        self.__estado = estado
    def actualizar_puntos(self, puntos: int):
        self.__puntos = puntos
    def actualizar_partidas(self, partidas: int):
        self.__partidas = partidas
    def __str__(self):
        return repr(self)
    def __repr__(self):
        return f"(nombre={self.__nombre}, mail={self.__mail}, puntos={self.__puntos}, partidas={self.__partidas}, raza={self.__raza}, estado={self.__estado})"


##########################################################################################
# ACCIONES DEL SISTEMA
##########################################################################################
def alta():
    imprimir_header("ALTA")
    nombre = input("Nombre del jugador?")
    nombre = nombre.upper()
    mail = input("Mail del jugador?")
    mail = mail.upper()
    puntos = int(input("Puntos iniciales?"))
    partidas = int(input("Partidas iniciales?"))
    raza = input("Raza?")
    raza = raza.upper()
    estado = input("Estado del jugador?")
    estado = estado.upper()
    jugador = Jugador(nombre, mail, puntos, partidas, Raza[raza], Estado[estado])
    JUGADORES.append(jugador)
    print(f"Jugador registrado: {jugador}")



def genera_partida():
    imprimir_header("NUEVA PARTIDA")
    jugadores_partida = []
    max_nivel = 0
    for index, jugador in enumerate(JUGADORES):
        status = Estado["ACTIVO"]
        if jugador.obtener_estado() == status and jugador.obtener_partidas() >= max_nivel:
            max_nivel = jugador.obtener_partidas()
    for number in range(0,max_nivel+1):
        jugadores_activos = []
        for index, jugador in enumerate(JUGADORES):
            status = Estado["ACTIVO"]
            if jugador.obtener_estado() == status and jugador.obtener_partidas() == number:
                jugadores_activos.append(jugador)
        if len(jugadores_activos) == 0:
            print(f"No hay jugadores activos del nivel: {number}")
        elif len(jugadores_activos) % 2 != 0:
            print(f"No hay suficiente jugadores activos del nivel: {number}")
        else:
            genera = True
            while genera:
                min = 0
                max = len(jugadores_activos) - 1
                index1 = 0
                index2 = 0
                index1 = random.randint(min,max)
                index2 = random.randint(min,max)
                if index1 != index2:
                    jugador1 = jugadores_activos[index1]
                    jugador2 = jugadores_activos[index2]
                    jugadores_partida.append(jugador1)
                    jugadores_partida.append(jugador2)
                    index = len(PARTIDAS) + 1
                    nombre1 = jugador1.obtener_nombre()
                    nombre2 = jugador2.obtener_nombre()
                    partid = index
                    ganador = 'Nadie'
                    partida = Partida(partid, nombre1, nombre2, index1, ganador)
                    PARTIDAS.append(partida)
                    estado_jug = "JUGANDO"
                    status = Estado[estado_jug]
                    actualizar_jugador(jugador1, status)
                    actualizar_jugador(jugador2, status)
                    print(f"Partida creada: {partida}")
                    jugadores_activos = []
                    number = max_nivel + 2
                    genera = False
def mostrar_partidas():
    imprimir_header("MOSTRAR TODAS")
    for index, partida in enumerate(PARTIDAS):
        print(f"{index}) {partida}")


def actualizar_jugador(jugadora: Jugador, estado):
    for jugador in JUGADORES:
        if jugador.obtener_nombre() == jugadora.obtener_nombre():
            #print(f"jugador encontrado: {jugador}")
            jugador.actualizar_estado(estado)
            print(f"Status del jugador actualizado: {jugador}")
def actualizar_puntos_jug(jugadora: Jugador, puntos):
    for jugador in JUGADORES:
        if jugador.obtener_nombre() == jugadora.obtener_nombre():
            jugador.actualizar_puntos(puntos)
            print(f"Puntos jugador actualizados: {jugador}")

def mostrar_jugadores():
    imprimir_header("MOSTRAR JUGADORES")
    for index, jugador in enumerate(JUGADORES):
        print(f"{index}) {jugador}")


def actualizar_resultados():
    imprimir_header("ACTUALIZAR PARTIDA")
    mostrar_partidas()
    actualiza_id = int(input("Que partida quieres actualizar?"))
    for index, partida in enumerate(PARTIDAS):
        part_id = partida.obtiene_partida()
        if part_id == actualiza_id:
            jugadores_resultado = []
            jugadores_resultado.append(partida.obtener_jugador1())
            jugadores_resultado.append(partida.obtener_jugador2())
            min = 0
            max = 1
            resultado = True
            while resultado:
                ganador = random.randint(min,max)
                perdedor = random.randint(min,max)
                if ganador != perdedor:
                    for jugador in JUGADORES:
                        if jugador.obtener_nombre() == jugadores_resultado[ganador]:
                            estatus_gan = "ACTIVO"
                            status = Estado[estatus_gan]
                            puntos_ganador = int(jugador.obtener_puntos()) + 3
                            actualizar_puntos_jug(jugador, puntos_ganador)
                            actualizar_jugador(jugador, status)
                            actualizar_partidas_jugador(jugador, 1)
                            print(f"Jugador ganador actualizado: {jugador}")
                            nombre_ganador = jugador.obtener_nombre()
                            partida.actualizar_ganador(nombre_ganador)
                        elif jugador.obtener_nombre() == jugadores_resultado[perdedor]:
                                estado_perd = "INACTIVO"
                                puntos_perd = int(jugador.obtener_puntos()) + 1
                                status = Estado[estado_perd]
                                actualizar_puntos_jug(jugador, puntos_perd)
                                actualizar_jugador(jugador, status)
                                actualizar_partidas_jugador(jugador, 1)
                                print(f"Jugador perdedor actualizado: {jugador}")
                    resultado = False


def actualizar_partidas_jugador(jugadora: Jugador, partidas):
    for jugador in JUGADORES:
        if jugador.obtener_nombre() == jugadora.obtener_nombre():
            nuevo_partidas = int(jugador.obtener_partidas())
            nuevo_partidas += partidas
            jugador.actualizar_partidas(nuevo_partidas)
            print(f"jugador actualizado: {jugador}")

def salir():
    print("Cerrando programa...")
    exit(0)
def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")

##########################################################################################
# CONTROL PRINCIPAL
##########################################################################################
JUGADORES = []
PARTIDAS = []

MENU = {
    "alta": alta,
    "generar partida": genera_partida,
    "mostrar todas": mostrar_partidas,
    "mostrar jugadores": mostrar_jugadores,
    "actualizar resultados": actualizar_resultados,
    "salir": salir
}

OPTIONS = ' | '.join(MENU.keys())  # alta | buscar por nombre | mostrar todos | mostrar por estado
menu = True
while menu == True:
    action = input(f"Que accion deases realizar? {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")
