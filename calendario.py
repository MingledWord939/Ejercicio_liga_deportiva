#Importamos las funciones
from datos import partidos, equipos
from utiles import generar_id
from datetime import datetime
#Funcion para partidos
def crear_partido():
    try:
        jornada = int(input("Número de jornada (≥ 1): "))
    except:
        print("Jornada inválida")
        return

    if jornada < 1:
        print("La jornada debe ser mayor o igual a 1")
        return
#Pedimos los ID para los equipos
    try:
        local_id = int(input("ID del equipo local: "))
        visitante_id = int(input("ID del equipo visitante: "))
    except:
        print("ID inválido.")
        return

    if local_id == visitante_id:
        print("El equipo local y visitante no pueden ser el mismo")
        return

    local_activo = False
    visitante_activo = False
    i = 0
    while i < len(equipos):
        if equipos[i]["id"] == local_id and equipos[i]["activo"]:
            local_activo = True
        if equipos[i]["id"] == visitante_id and equipos[i]["activo"]:
            visitante_activo = True
        i += 1
#Validacion
    if not local_activo or not visitante_activo:
        print("Ambos equipos deben existir y estar activos")
        return

    i = 0
    repetido = False
    while i < len(partidos):
        p = partidos[i]
        if p["jornada"] == jornada and (
            (p["local_id"] == local_id and p["visitante_id"] == visitante_id) or
            (p["local_id"] == visitante_id and p["visitante_id"] == local_id)
        ):
            repetido = True
        i += 1

    if repetido:
        print("Este enfrentamiento ya existe en esta jornada")
        return
    #Pedimos fecha y hora 
    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora (HH:MM): ")

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        datetime.strptime(hora, "%H:%M")
    except:
        print("Formato de fecha u hora inválido")
        return
    #Diccionario de partido y añadirlo a una lista
    partido = {
        "id": generar_id(partidos),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    }
    partidos.append(partido)
    print("Partido creado")

def obtener_nombre_equipo(equipo_id):
    i = 0
    while i < len(equipos):
        if equipos[i]["id"] == equipo_id:
            return equipos[i]["nombre"]
        i += 1
    return "Desconocido"

def listar_partidos():
    print("1. Todos los partidos")
    print("2. Por jornada")
    opcion = input("Opción: ")

    if opcion == "2":
        try:
            jornada = int(input("Número de jornada: "))
        except:
            print("Jornada inválida")
            return
    else:
        jornada = None
    #Recorremos la lista de partidos 
    i = 0
    while i < len(partidos):
        p = partidos[i]
        if jornada is None or p["jornada"] == jornada:
            local = obtener_nombre_equipo(p["local_id"])
            visitante = obtener_nombre_equipo(p["visitante_id"])
            estado = "Jugado" if p["jugado"] else "Pendiente"
            resultado = ""
            if p["resultado"] is not None:
                resultado = f"{p['resultado'][0]} - {p['resultado'][1]}"
            print(f"ID {p['id']} | Jornada {p['jornada']} | {local} vs {visitante} | {p['fecha']} {p['hora']} | {estado} {resultado}")
        i += 1
#Reprogramamos los parametros del partido
def reprogramar_partido():
    try:
        id_partido = int(input("ID del partido a reprogramar: "))
    except:
        print("ID inválido")
        return

    i = 0
    encontrado = False
    while i < len(partidos):
        if partidos[i]["id"] == id_partido:
            if partidos[i]["jugado"]:
                print("No se puede reprogramar un partido ya jugado")
                return
            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            nueva_hora = input("Nueva hora (HH:MM): ")
            try:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                datetime.strptime(nueva_hora, "%H:%M")
                partidos[i]["fecha"] = nueva_fecha
                partidos[i]["hora"] = nueva_hora
                print("Partido reprogramado.")
            except:
                print("Formato de fecha u hora inválido")
            encontrado = True
        i += 1

    if not encontrado:
        print("Partido no encontrado")
#Eliminamos los partidos jugados por su ID
def eliminar_partido():
    try:
        id_eliminar = int(input("ID del partido a eliminar: "))
    except:
        print("ID inválido")
        return

    i = 0
    eliminado = False
    while i < len(partidos):
        if partidos[i]["id"] == id_eliminar:
            if partidos[i]["jugado"]:
                print("No se puede eliminar un partido ya jugado.")
                return
            partidos.pop(i)
            print("Partido eliminado")
            eliminado = True
            i = len(partidos)  
        else:
            i += 1

    if not eliminado:
        print("Partido no encontrado")
#Menu principal
def menu_calendario():
    salir = False
    while not salir:
        print("MENÚ CALENDARIO")
        print("1 Crear partido")
        print("2 Listar partidos")
        print("3 Reprogramar partido")
        print("4 Eliminar partido")
        print("5 Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            crear_partido()
        elif opcion == "2":
            listar_partidos()
        elif opcion == "3":
            reprogramar_partido()
        elif opcion == "4":
            eliminar_partido()
        elif opcion == "5":
            salir = True
        else:
            print("Opción inválida ")