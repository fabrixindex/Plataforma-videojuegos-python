import os
from Funciones import *


def limpiar_consola() -> None:
    """Limpia la pantalla según el sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("")


def esperar_menu() -> None:
    """Pausa la ejecución hasta que el usuario presione Enter y limpia la consola."""
    input("Toque enter para continuar...")
    limpiar_consola()


#  Menú Jugador

def menu_jugador(indice_usuario: int, usuarios: list, juegos: list, compras: list) -> None:
    """Muestra y gestiona el menú del rol Jugador.

    Args:
        indice_usuario (int): Índice del usuario logueado en `usuarios`.
        usuarios (list): Lista de diccionarios de usuarios.
        juegos (list): Lista de diccionarios de juegos.
        compras (list): Lista de diccionarios de compras.
    """
    while True:
        print("==== GAMEHUB — JUGADOR ====\n")
        print(f"Usuario: {usuarios[indice_usuario]['usuario']} | Rol: {usuarios[indice_usuario]['rol']}\n")
        print("1 - Ver perfil")
        print("2 - Explorar catálogo y comprar")
        print("3 - Ver catálogo completo (tabla)")
        print("0 - Salir")
        opcion = input("\nIngrese su opción: ")
        limpiar_consola()

        match opcion:
            case "1":
                ver_perfil_jugador(usuarios, indice_usuario)
                esperar_menu()
            case "2":
                explorar_catalogo(usuarios, juegos, compras, indice_usuario)
                esperar_menu()
            case "3":
                matriz = construir_matriz_juegos(juegos)
                mostrar_tabla_juegos(matriz)
                esperar_menu()
            case "0":
                print("Saliendo...")
                print("¡GRACIAS POR USAR GAMEHUB!")
                break
            case _:
                print("Opción inválida...")
                esperar_menu()


#  Menú Desarrolladora

def menu_desarrolladora(indice_usuario: int, usuarios: list, juegos: list, compras: list) -> None:
    """Muestra y gestiona el menú del rol Desarrolladora.

    Args:
        indice_usuario (int): Índice del usuario logueado en `usuarios`.
        usuarios (list): Lista de diccionarios de usuarios.
        juegos (list): Lista de diccionarios de juegos.
        compras (list): Lista de diccionarios de compras.
    """
    while True:
        print("==== GAMEHUB — DESARROLLADORA ====\n")
        print(f"Usuario: {usuarios[indice_usuario]['usuario']} | Rol: {usuarios[indice_usuario]['rol']}\n")
        print("1 - Ver datos del estudio")
        print("2 - Publicar juego")
        print("3 - Ver ventas")
        print("4 - Ver mis juegos (tabla)")
        print("0 - Salir")
        opcion = input("\nIngrese su opción: ")
        limpiar_consola()

        match opcion:
            case "1":
                ver_datos_desarrolladora(usuarios, indice_usuario)
                esperar_menu()
            case "2":
                publicar_juego(usuarios, juegos, indice_usuario)
                esperar_menu()
            case "3":
                ver_ventas(usuarios, juegos, compras, indice_usuario)
                esperar_menu()
            case "4":
                propios = buscar_juegos_por_empresa(juegos, usuarios[indice_usuario]["usuario"])
                matriz = construir_matriz_juegos(propios)
                mostrar_tabla_juegos(matriz)
                esperar_menu()
            case "0":
                print("Saliendo...")
                print("¡GRACIAS POR USAR GAMEHUB!")
                break
            case _:
                print("Opción inválida...")
                esperar_menu()


#  Menú Administrador

def menu_administrador(indice_usuario: int, usuarios: list, eliminados: list) -> None:
    """Muestra y gestiona el menú del rol Administrador.

    Args:
        indice_usuario (int): Índice del usuario logueado en `usuarios`.
        usuarios (list): Lista de diccionarios de usuarios.
        eliminados (list): Lista de diccionarios de usuarios eliminados.
    """
    while True:
        print("==== GAMEHUB — ADMINISTRADOR ====\n")
        print(f"Usuario: {usuarios[indice_usuario]['usuario']} | Rol: {usuarios[indice_usuario]['rol']}\n")
        print("1 - Crear usuario")
        print("2 - Borrar usuario")
        print("3 - Ver información del sistema")
        print("4 - Ver usuarios (tabla)")
        print("0 - Salir")
        opcion = input("\nIngrese su opción: ")
        limpiar_consola()

        match opcion:
            case "1":
                crear_usuario(usuarios)
                esperar_menu()
            case "2":
                borrar_usuario(usuarios, eliminados)
                esperar_menu()
            case "3":
                ver_info_sistema()
                esperar_menu()
            case "4":
                matriz = construir_matriz_usuarios(usuarios)
                mostrar_tabla_usuarios(matriz)
                esperar_menu()
            case "0":
                print("Saliendo...")
                print("¡GRACIAS POR USAR GAMEHUB!")
                break
            case _:
                print("Opción inválida...")
                esperar_menu()


#  Organizador de Menús

def iniciar_menu(indice_usuario: int, usuarios: list, juegos: list, compras: list, eliminados: list) -> None:
    """Deriva al menú correspondiente según el rol del usuario logueado.

    Args:
        indice_usuario (int): Índice del usuario logueado en `usuarios`.
        usuarios (list): Lista de diccionarios de usuarios.
        juegos (list): Lista de diccionarios de juegos.
        compras (list): Lista de diccionarios de compras.
        eliminados (list): Lista de diccionarios de usuarios eliminados.
    """
    rol = usuarios[indice_usuario]["rol"]

    if rol == "Jugador":
        menu_jugador(indice_usuario, usuarios, juegos, compras)
    elif rol == "Desarrolladora":
        menu_desarrolladora(indice_usuario, usuarios, juegos, compras)
    elif rol == "Administrador":
        menu_administrador(indice_usuario, usuarios, eliminados)
    else:
        print("Error: rol no reconocido.")