#Importamos las listas
from datos import equipos
from utiles import generar_id
from datos import equipos, jugadores
#Funcion para nuevos equipos
def crear_equipo():
    nombre = input("Nombre del equipo: ").strip()
    ciudad = input("Ciudad del equipo: ").strip()
    if nombre != "" and ciudad != "":
        nuevo = {
            "id": generar_id(equipos),
            "nombre": nombre,
            "ciudad": ciudad,
            "activo": True
        }
        equipos.append(nuevo)
        print("Equipo creado")
    else:
        print("Nombre y ciudad no pueden estar vacíos.")
#Funcion para listar los equipos
def listar_equipos():
    print("Equipos activos:")
    for e in equipos:
        if e["activo"]:
            print(f"{e['id']:>3} | {e['nombre']:<15} | {e['ciudad']:<15}")
#Funcion para buscar un equipo por su ID
def buscar_equipo():
    try:
        id_buscar = int(input("ID a buscar: "))
    except:
        print("ID inválido")
        return
    for e in equipos:
        if e["id"] == id_buscar:
            print(f"\nID: {e['id']}")
            print(f"Nombre: {e['nombre']}")
            print(f"Ciudad: {e['ciudad']}")
            print(f"Activo: {e['activo']}")
            return
    print("No encontrado")
#Funcion para actualizar un equipo por su ID
def actualizar_equipo():
    try:
        id_act = int(input("ID a actualizar: "))
    except:
        print("ID inválido")
        return
    for e in equipos:
        if e["id"] == id_act:
            nuevo_nombre = input(f"Nuevo nombre ({e['nombre']}): ").strip()
            nueva_ciudad = input(f"Nueva ciudad ({e['ciudad']}): ").strip()
            if nuevo_nombre != "":
                e["nombre"] = nuevo_nombre
            if nueva_ciudad != "":
                e["ciudad"] = nueva_ciudad
            print("Actualizado")
            return
    print("No encontrado")
#Funcion para actualizar 
def eliminar_equipo():
    try:
        id_elim = int(input("ID a eliminar: "))
    except:
        print("ID inválido")
        return

    tiene_jugadores = False
    for j in jugadores:
        if j["equipo_id"] == id_elim and j["activo"]:
            tiene_jugadores = True
            break

    if tiene_jugadores:
        print("No se puede eliminar el equipo. Tiene jugadores activos")
        return

    for e in equipos:
        if e["id"] == id_elim:
            e["activo"] = False
            print("Equipo marcado como inactivo")
            return

    print("Equipo no encontrado")
#Funcion para el menu de los equipos
def menu_equipos():
    salir = False
    while not salir:
        print("MENÚ EQUIPOS")
        print("1 Crear equipo")
        print("2 Listar equipos")
        print("3 Buscar equipo")
        print("4 Actualizar equipo")
        print("5 Eliminar equipo")
        print("6 Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            buscar_equipo()
        elif opcion == "4":
            actualizar_equipo()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "6":
            salir = True
        else:
            print("Opción inválida")