from Prints import mostrar_bienvenida
from Inputs import iniciar_sesion
from Menu import limpiar_consola, iniciar_menu
from Persistencia import cargar_usuarios, cargar_juegos, cargar_compras, cargar_eliminados


mostrar_bienvenida()
input("Toque enter para continuar...")
limpiar_consola()

usuarios = cargar_usuarios()
juegos = cargar_juegos()
compras = cargar_compras()
eliminados = cargar_eliminados()

indice_usuario = iniciar_sesion(usuarios)
limpiar_consola()

iniciar_menu(indice_usuario, usuarios, juegos, compras, eliminados)