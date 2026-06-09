from Prints import mostrar_bienvenida
from Inputs import iniciar_sesion
from Menu import limpiar_consola, iniciar_menu
 
 
mostrar_bienvenida()
input("Toque enter para continuar...")
limpiar_consola()
 
indice_usuario = iniciar_sesion()
limpiar_consola()
 
iniciar_menu(indice_usuario)
