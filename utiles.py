#importamos las listas
from tabulate import tabulate
#definicion de generar id para una lista
def generar_id(lista):
    max_id = 0
    for item in lista:
        if item["id"] > max_id:
            max_id = item["id"]
    return max_id + 1
def leer_int(mensaje, minimo=None):
    valido = False
    while not valido:
        entrada = input(mensaje)
        if entrada.isdigit(): #verificamos que sea un número entero positivo
            valor = int(entrada)
            if minimo is None or valor >= minimo:
                valido = True
                return valor
        print("Número inválido")
def leer_texto(mensaje):
    texto = ""
    while texto.strip() == "":
        texto = input(mensaje).strip()
        if texto == "":
            print("Texto no puede estar vacío")
    return texto
def imprimir_tabla(filas, columnas):
    if len(filas) > 0:
        print(tabulate(filas, headers=columnas, tablefmt="grid"))
    else:
        print("No hay datos para mostrar")