import os
from Funciones import *
from Inputs import *
from Prints import *


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
 
def menu_jugador(indice_usuario: int) -> None:
    """Muestra y gestiona el menú del rol Jugador.
 
    Args:
        indice_usuario (int): Índice del usuario logueado en las listas globales.
    """
    while True:
        print("==== GAMEHUB — JUGADOR ====\n")
        print(f"Usuario: {usuarios[indice_usuario]} | Rol: {roles[indice_usuario]}\n")
        print("1 - Ver perfil")
        print("2 - Explorar catálogo (simulado)")
        print("0 - Salir")
        opcion = input("\nIngrese su opción: ")
        limpiar_consola()
 
        match opcion:
            case "1":
                ver_perfil_jugador(indice_usuario)
                esperar_menu()
            case "2":
                explorar_catalogo()
                esperar_menu()
            case "0":
                print("Saliendo...")
                print("¡GRACIAS POR USAR GAMEHUB!")
                break
            case _:
                print("Opción inválida...")
                esperar_menu()
 

#  Menú Desarrolladora
 
def menu_desarrolladora(indice_usuario: int) -> None:
    """Muestra y gestiona el menú del rol Desarrolladora.
 
    Args:
        indice_usuario (int): Índice del usuario logueado en las listas globales.
    """
    while True:
        print("==== GAMEHUB — DESARROLLADORA ====\n")
        print(f"Usuario: {usuarios[indice_usuario]} | Rol: {roles[indice_usuario]}\n")
        print("1 - Ver datos del estudio")
        print("2 - Publicar juego (simulado)")
        print("3 - Ver ventas (simulado)")
        print("0 - Salir")
        opcion = input("\nIngrese su opción: ")
        limpiar_consola()
 
        match opcion:
            case "1":
                ver_datos_desarrolladora(indice_usuario)
                esperar_menu()
            case "2":
                publicar_juego()
                esperar_menu()
            case "3":
                ver_ventas()
                esperar_menu()
            case "0":
                print("Saliendo...")
                print("¡GRACIAS POR USAR GAMEHUB!")
                break
            case _:
                print("Opción inválida...")
                esperar_menu()
 
 
#  Menú Administrador
 
def menu_administrador(indice_usuario: int) -> None:
    """Muestra y gestiona el menú del rol Administrador.
 
    Args:
        indice_usuario (int): Índice del usuario logueado en las listas globales.
    """
    while True:
        print("==== GAMEHUB — ADMINISTRADOR ====\n")
        print(f"Usuario: {usuarios[indice_usuario]} | Rol: {roles[indice_usuario]}\n")
        print("1 - Crear usuario (simulado)")
        print("2 - Borrar usuario (simulado)")
        print("3 - Ver información del sistema")
        print("0 - Salir")
        opcion = input("\nIngrese su opción: ")
        limpiar_consola()
 
        match opcion:
            case "1":
                crear_usuario()
                esperar_menu()
            case "2":
                borrar_usuario()
                esperar_menu()
            case "3":
                ver_info_sistema()
                esperar_menu()
            case "0":
                print("Saliendo...")
                print("¡GRACIAS POR USAR GAMEHUB!")
                break
            case _:
                print("Opción inválida...")
                esperar_menu()
 

#  Organizador de Menus 
 
def iniciar_menu(indice_usuario: int) -> None:
    """Deriva al menú correspondiente según el rol del usuario logueado.
 
    Args:
        indice_usuario (int): Índice del usuario logueado en las listas globales.
    """
    rol = roles[indice_usuario]
 
    if rol == "Jugador":
        menu_jugador(indice_usuario)
    elif rol == "Desarrolladora":
        menu_desarrolladora(indice_usuario)
    elif rol == "Administrador":
        menu_administrador(indice_usuario)
    else:
        print("Error: rol no reconocido.")