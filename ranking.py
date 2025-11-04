#Importamos las listas
from datos import partidos, equipos
from utiles import leer_int, imprimir_tabla
#definicion para registrar los resultados del partido
def registrar_resultado():
    pendientes = []
    i = 0
    while i < len(partidos):
        if not partidos[i]["jugado"]:
            pendientes.append(partidos[i])
        i += 1

    if len(pendientes) == 0:
        print("No hay partidos pendientes")
        return

    imprimir_tabla(
        [[p["id"], p["jornada"], p["local_id"], p["visitante_id"], p["fecha"], p["hora"]] for p in pendientes],
        ["ID", "Jornada", "Local", "Visitante", "Fecha", "Hora"]
    )

    id_partido = leer_int("ID del partido a registrar: ")
    i = 0
    encontrado = False
    while i < len(partidos):
        p = partidos[i]
        if p["id"] == id_partido and not p["jugado"]:
            gL = leer_int("Goles equipo local: ", 0)
            gV = leer_int("Goles equipo visitante: ", 0)
            p["resultado"] = (gL, gV)
            p["jugado"] = True
            print("Resultado registrado")
            encontrado = True
        i += 1

    if not encontrado:
        print("Partido no encontrado o ya jugado")
#Definicion para calcular la clasificacion de los partidos
def calcular_clasificacion():
    tabla = {}
    i = 0
    while i < len(equipos):
        if equipos[i]["activo"]:
            eid = equipos[i]["id"]
            tabla[eid] = {
                "nombre": equipos[i]["nombre"],
                "PJ": 0, "G": 0, "E": 0, "P": 0,
                "GF": 0, "GC": 0, "DG": 0, "PTS": 0
            }
        i += 1

    i = 0
    while i < len(partidos):
        p = partidos[i]
        if p["jugado"]:
            lid = p["local_id"]
            vid = p["visitante_id"]
            gL, gV = p["resultado"]

            if lid in tabla and vid in tabla:
                tabla[lid]["PJ"] += 1
                tabla[vid]["PJ"] += 1
                tabla[lid]["GF"] += gL
                tabla[lid]["GC"] += gV
                tabla[vid]["GF"] += gV
                tabla[vid]["GC"] += gL

                if gL > gV:
                    tabla[lid]["G"] += 1
                    tabla[vid]["P"] += 1
                    tabla[lid]["PTS"] += 3
                elif gL < gV:
                    tabla[vid]["G"] += 1
                    tabla[lid]["P"] += 1
                    tabla[vid]["PTS"] += 3
                else:
                    tabla[lid]["E"] += 1
                    tabla[vid]["E"] += 1
                    tabla[lid]["PTS"] += 1
                    tabla[vid]["PTS"] += 1
        i += 1

    for t in tabla.values():
        t["DG"] = t["GF"] - t["GC"]

    filas = []
    for eid in tabla:
        t = tabla[eid]
        filas.append([
            t["nombre"], t["PJ"], t["G"], t["E"], t["P"],
            t["GF"], t["GC"], t["DG"], t["PTS"]
        ])

    filas.sort(key=lambda x: x[8], reverse=True)
    imprimir_tabla(filas, ["Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "PTS"])
#Definicion estadisticas de cada equipo
def estadisticas_equipo():
    id_eq = leer_int("ID del equipo: ")
    nombre = ""
    i = 0
    while i < len(equipos):
        if equipos[i]["id"] == id_eq:
            nombre = equipos[i]["nombre"]
        i += 1

    if nombre == "":
        print("Equipo no encontrado.")
        return

    PJ = 0
    GF = 0
    GC = 0
    PTS = 0

    i = 0
    while i < len(partidos):
        p = partidos[i]
        if p["jugado"]:
            gL, gV = p["resultado"]
            if p["local_id"] == id_eq:
                PJ += 1
                GF += gL
                GC += gV
                if gL > gV:
                    PTS += 3
                elif gL == gV:
                    PTS += 1
            elif p["visitante_id"] == id_eq:
                PJ += 1
                GF += gV
                GC += gL
                if gV > gL:
                    PTS += 3
                elif gV == gL:
                    PTS += 1
        i += 1

    imprimir_tabla([[nombre, PJ, GF, GC, PTS]], ["Equipo", "PJ", "GF", "GC", "PTS"])
#Definicion del menu del ranking
def menu_ranking():
    salir = False
    while not salir:
        print("MENÚ RESULTADOS Y CLASIFICACIÓN")
        print("1 Registrar resultado")
        print("2 Ver clasificación")
        print("3 Estadísticas por equipo")
        print("4 Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_resultado()
        elif opcion == "2":
            calcular_clasificacion()
        elif opcion == "3":
            estadisticas_equipo()
        elif opcion == "4":
            salir = True
        else:
            print("Opción inválida")