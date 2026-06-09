from Inputs import *
from Prints import *
 
#  JUGADOR

def ver_perfil_jugador(indice_usuario: int) -> None:
    """Muestra los datos del jugador logueado.

    Combina el nombre de usuario de la sesión con los datos
    hardcodeados del perfil (4 str y 3 int).

    Args:
        indice_usuario (int): Índice del usuario en las listas globales.
    """
    mostrar_perfil_jugador(
        usuarios[indice_usuario],
        nombres[indice_usuario],
        apellidos[indice_usuario],
        paises[indice_usuario],
        generos_favoritos[indice_usuario],
        horas_jugadas[indice_usuario],
        juegos_comprados[indice_usuario],
        logros[indice_usuario],
    )



def explorar_catalogo() -> None:
    """Permite al jugador buscar juegos por empresa, elegir un título
    y simular una compra con método de pago.
    """
    # ── Datos hardcodeados ──────────────────────────────────
    empresas = ["ubisoft",    "ea",         "valve"]
    titulos  = [
        ["Assassin's Creed", "Far Cry 6",  "Rainbow Six"],
        ["FIFA 25",          "The Sims 4", "Apex Legends"],
        ["CS2",              "Dota 2",     "Half-Life: Alyx"],
    ]
    precios  = [
        [59.99, 49.99, 39.99],
        [69.99, 39.99,  0.00],
        [49.99,  0.00, 59.99],
    ]
    metodos_pago = ["Tarjeta de Crédito", "PayPal"]

    # ── 1. Buscar empresa ───────────────────────────────────
    empresa = ""
    while len(empresa) < 3:
        empresa = input("Ingrese el nombre de la empresa desarrolladora: ").lower()
        if len(empresa) < 3:
            print("Error: debe tener al menos 3 caracteres.\n")

    indice_empresa = -1
    i = 0
    while i < len(empresas) and indice_empresa == -1:
        if empresas[i] == empresa:
            indice_empresa = i
        i += 1

    if indice_empresa == -1:
        print(f"No se encontró la empresa '{empresa}'.\n")
        return

    # ── 2. Submenú de juegos ────────────────────────────────
    mostrar_catalogo_juegos(empresa, titulos[indice_empresa], precios[indice_empresa])

    juego_elegido = -1
    while juego_elegido == -1:
        opcion = input("Elija un juego (número): ")
        if opcion.isdigit():
            num = int(opcion)
            if 1 <= num <= len(titulos[indice_empresa]):
                juego_elegido = num - 1
            else:
                print("Opción fuera de rango.\n")
        else:
            print("Ingrese un número válido.\n")

    # ── 3. Submenú de métodos de pago ───────────────────────
    print("\n==== MÉTODO DE PAGO ====\n")
    i = 0
    while i < len(metodos_pago):
        print(f"  {i + 1} - {metodos_pago[i]}")
        i += 1
    print("  0 - Ninguno")

    metodo_elegido = -1
    while metodo_elegido == -1:
        opcion = input("\nElija un método de pago: ")
        if opcion == "0":
            print("\nCompra cancelada.\n")
            return
        elif opcion.isdigit():
            num = int(opcion)
            if 1 <= num <= len(metodos_pago):
                metodo_elegido = num - 1
            else:
                print("Opción fuera de rango.\n")
        else:
            print("Ingrese un número válido.\n")

    # ── 4. Confirmar compra ─────────────────────────────────
    mostrar_confirmacion_compra(
        titulos[indice_empresa][juego_elegido],
        metodos_pago[metodo_elegido],
        precios[indice_empresa][juego_elegido],
    )

#  DESARROLLADORA
 
def ver_datos_desarrolladora(indice_usuario: int) -> None:
    """Muestra los datos de la desarrolladora logueada (hardcodeados).
 
    Incluye al menos 3 datos de tipo str y 3 de tipo int.
 
    Args:
        indice_usuario (int): Índice del usuario en las listas globales.
    """
    # Datos hardcodeados por índice de usuario desarrolladora
    nombres_estudio  = ["Blyts", "HyperBeard",    "The Game Kitchen"]
    paises_estudio   = ["Argentina",           "México",        "España"]
    sitios_web       = ["https://en.blyts.com/",  "https://hyperbeard.com/", "https://thegamekitchen.com/"]
    juegos_pub       = [8,                     3,               12]
    ventas_tot       = [45000,                 12000,           98000]
    año_fund       = [2015,                  2019,            2010]

    mostrar_datos_desarrolladora(
        nombres_estudio[indice_usuario],
        paises_estudio[indice_usuario],
        sitios_web[indice_usuario],
        juegos_pub[indice_usuario],
        ventas_tot[indice_usuario],
        año_fund[indice_usuario],
    )
 
 
 
def publicar_juego() -> None:
    """Solicita los datos de un nuevo juego y simula su publicación.
 
    Validaciones:
        - Nombre del videojuego: no vacío.
        - Precio: debe ser mayor a 0.
    """
    nombre_juego = ""
    while nombre_juego == "":
        nombre_juego = input("Ingrese el nombre del videojuego: ")
        if nombre_juego == "":
            print("Error: el nombre no puede estar vacío.\n")

    precio = 0.0
    precio_valido = False
    while not precio_valido:
        entrada = input("Ingrese el precio del juego: ")
        es_numero = True
        cantidad_puntos = 0
        i = 0
        while i < len(entrada):
            if entrada[i] == ".":
                cantidad_puntos += 1
            elif not entrada[i].isdigit():
                es_numero = False
            i += 1
        if cantidad_puntos > 1:
            es_numero = False

        if not es_numero or entrada == "" or entrada == ".":
            print("Error: ingrese un número válido.\n")
        else:
            precio = float(entrada)
            if precio <= 0:
                print("Error: el precio debe ser mayor a 0.\n")
            else:
                precio_valido = True

    mostrar_confirmacion_publicacion(nombre_juego, precio)
 
 
def ver_ventas() -> None:
    """Simula la visualización de ventas del mes con datos ficticios."""
    mostrar_ventas()
 
 
#  ADMINISTRADOR
 
def crear_usuario() -> None:
    """Solicita y valida los datos para crear un nuevo usuario.
 
    Validaciones:
        - Nombre de usuario: mínimo 4 caracteres.
        - Contraseña: mínimo 8 caracteres.
        - Rol: 'Jugador' o 'Desarrolladora'.
        - Datos adicionales según el rol elegido.
    """
    pass
 
 
def borrar_usuario() -> None:
    """Solicita un nombre de usuario y simula su eliminación del sistema.
 
    Validaciones:
        - Nombre de usuario: mínimo 4 caracteres.
 
    Nota:
        No elimina datos reales. Solo muestra un mensaje de confirmación.
    """
    pass
 
 
def ver_info_sistema() -> None:
    """Muestra información general del sistema GameHub.
 
    Incluye:
        - Nombres de los integrantes del grupo.
        - Descripción del sistema (propósito, problema que resuelve, tipos de usuario).
        - Funcionalidades extra por rol (mínimo 3 para Jugador,
          2 para Desarrolladora, 2 para Administrador).
    """
    pass