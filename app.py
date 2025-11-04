# Importamos los menús 
from equipos import menu_equipos
from jugadores import menu_jugadores
from calendario import menu_calendario
from ranking import menu_ranking
# Definir las funciones
def menu_principal():
    salir = False
#Bucle principal siendo el menu donde empieza todo
    while not salir:
        print(" MENÚ PRINCIPAL")
        print("1 Gestión de equipos")
        print("2 Gestión de jugadores")
        print("3 Calendario de partidos")
        print("4 Resultados y clasificación")
        print("5 Salir")
        opcion=input("Opción: ")

        if opcion == "1":
            menu_equipos()
        elif opcion == "2":
            menu_jugadores()
        elif opcion == "3":
            menu_calendario()
        elif opcion == "4":
            menu_ranking()
        elif opcion == "5":
            print("Adiós")
            salir=True
        else:
            print("Opción inválida")
#Llamamos a la def principal
menu_principal()