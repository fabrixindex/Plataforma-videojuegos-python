import os
from Funciones import *
from Inputs import *
from Prints import *

# USUARIO | CONTRASEÑA | TIPO
usuario_harcodeado1 = ["elrubiusomg", "callofduty7", "Jugador"]
usuario_harcodeado2 = ["ubisoftgames", "assasinscreed", "Desarrolladora"]
usuario_harcodeado3 = ["adminepic", "metalgearsolid", "Administrador"]


def limpiar_consola() -> None:
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')
    print("")
    
def esperar_menu() -> None:
    input("Toque enter para continuar...")
    limpiar_consola()

def mostrar_menu()-> None:
    vector_usuarios = [usuario_harcodeado1, usuario_harcodeado2, usuario_harcodeado3]
    mostrar_bienvenida()
    esperar_menu()
    
    #Una vez iniciada sesión, el sistema debe mostrar un menú diferente según el rol.
    
    while True:
        print("==== GAMEHUB MENÚ ====")
        print("1 - opción 1")
        print("10 - Salir")

        opcion = input("Ingrese su opcion: ")
        
        limpiar_consola()
        match opcion:
            case "1":
                pass
            case "10":
                print("Saliendo...")
                print("GRACIAS POR USAR EL SISTEMA!")
                break                
            case _:
                print("Opción invalida...")
                
        esperar_menu()