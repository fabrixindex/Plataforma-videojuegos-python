from datetime import date

from Inputs import hashear_password
from Prints import *
from Persistencia import guardar_usuarios, guardar_juegos, guardar_compras, guardar_eliminados


#  FUNCIONES PURAS (búsqueda, filtrado, cálculo) ─────────────────

def buscar_indice_usuario(usuarios: list, nombre_usuario: str) -> int:
    """Busca el índice de un usuario por nombre de usuario.

    Args:
        usuarios (list): Lista de diccionarios de usuarios.
        nombre_usuario (str): Nombre de usuario a buscar.

    Returns:
        int: Índice del usuario si existe, -1 en caso contrario.
    """
    indice = -1
    i = 0
    while i < len(usuarios) and indice == -1:
        if usuarios[i]["usuario"] == nombre_usuario:
            indice = i
        i += 1
    return indice


def buscar_indice_juego(juegos: list, nombre: str, desarrolladora: str) -> int:
    """Busca el índice de un juego a partir de su nombre y desarrolladora.

    Args:
        juegos (list): Lista de diccionarios de juegos.
        nombre (str): Nombre del juego.
        desarrolladora (str): Nombre de usuario de la desarrolladora.

    Returns:
        int: Índice del juego si existe, -1 en caso contrario.
    """
    indice = -1
    i = 0
    while i < len(juegos) and indice == -1:
        if juegos[i]["nombre"] == nombre and juegos[i]["desarrolladora"] == desarrolladora:
            indice = i
        i += 1
    return indice


def buscar_juegos_por_empresa(juegos: list, empresa: str) -> list:
    """Filtra los juegos publicados por una desarrolladora específica.

    Args:
        juegos (list): Lista de diccionarios de juegos.
        empresa (str): Nombre de usuario de la desarrolladora.

    Returns:
        list: Lista de juegos cuya 'desarrolladora' coincide (sin distinguir mayúsculas).
    """
    resultado = []
    i = 0
    while i < len(juegos):
        if juegos[i]["desarrolladora"].lower() == empresa.lower():
            resultado.append(juegos[i])
        i += 1
    return resultado


def calcular_ventas_totales(compras: list, desarrolladora: str) -> float:
    """Calcula el monto total facturado por una desarrolladora en base a las compras.

    Args:
        compras (list): Lista de diccionarios de compras.
        desarrolladora (str): Nombre de usuario de la desarrolladora.

    Returns:
        float: Suma de los precios de las compras asociadas a esa desarrolladora.
    """
    total = 0.0
    i = 0
    while i < len(compras):
        if compras[i]["desarrolladora"].lower() == desarrolladora.lower():
            total += compras[i]["precio"]
        i += 1
    return total


def contar_ventas(compras: list, desarrolladora: str) -> int:
    """Cuenta la cantidad de compras asociadas a una desarrolladora.

    Args:
        compras (list): Lista de diccionarios de compras.
        desarrolladora (str): Nombre de usuario de la desarrolladora.

    Returns:
        int: Cantidad de compras encontradas.
    """
    cantidad = 0
    i = 0
    while i < len(compras):
        if compras[i]["desarrolladora"].lower() == desarrolladora.lower():
            cantidad += 1
        i += 1
    return cantidad


def juego_mas_vendido(juegos: list) -> dict:
    """Determina el juego con más copias vendidas dentro de una lista.

    Args:
        juegos (list): Lista de diccionarios de juegos.

    Returns:
        dict: Diccionario del juego más vendido, o {} si la lista está vacía.
    """
    if len(juegos) == 0:
        return {}
    mejor = juegos[0]
    i = 1
    while i < len(juegos):
        if juegos[i]["copias_vendidas"] > mejor["copias_vendidas"]:
            mejor = juegos[i]
        i += 1
    return mejor


def construir_matriz_juegos(juegos: list) -> list:
    """Construye una matriz (lista de listas) con los datos de cada juego.

    Args:
        juegos (list): Lista de diccionarios de juegos.

    Returns:
        list: Matriz con filas [nombre, desarrolladora, precio, copias_vendidas].
    """
    matriz = []
    i = 0
    while i < len(juegos):
        j = juegos[i]
        matriz.append([j["nombre"], j["desarrolladora"], j["precio"], j["copias_vendidas"]])
        i += 1
    return matriz


def construir_matriz_usuarios(usuarios: list) -> list:
    """Construye una matriz (lista de listas) con usuario y rol de cada usuario.

    Args:
        usuarios (list): Lista de diccionarios de usuarios.

    Returns:
        list: Matriz con filas [usuario, rol].
    """
    matriz = []
    i = 0
    while i < len(usuarios):
        matriz.append([usuarios[i]["usuario"], usuarios[i]["rol"]])
        i += 1
    return matriz


def construir_matriz_compras(compras: list) -> list:
    """Construye una matriz (lista de listas) con los datos de cada compra.

    Args:
        compras (list): Lista de diccionarios de compras.

    Returns:
        list: Matriz con filas [jugador, juego, precio, metodo_pago, fecha].
    """
    matriz = []
    i = 0
    while i < len(compras):
        c = compras[i]
        matriz.append([c["jugador"], c["juego"], c["precio"], c["metodo_pago"], c["fecha"]])
        i += 1
    return matriz

def buscar_usuario(usuarios: list, nombre: str) -> dict | None:
    """Busca un usuario por nombre de usuario.
 
    Args:
        usuarios (list): Lista de diccionarios de usuarios.
        nombre (str): Nombre de usuario a buscar.
 
    Returns:
        dict | None: Diccionario del usuario si existe, None en caso contrario.
    """
    resultado = None
    i = 0
    while i < len(usuarios) and resultado is None:
        if usuarios[i]["usuario"] == nombre:
            resultado = usuarios[i]
        i += 1
    return resultado
 
 
def filtrar_por_rol(usuarios: list, rol: str) -> list:
    """Filtra los usuarios que tienen un rol específico.
 
    Args:
        usuarios (list): Lista de diccionarios de usuarios.
        rol (str): Rol a filtrar ("Jugador", "Desarrolladora" o "Administrador").
 
    Returns:
        list: Lista de usuarios cuyo rol coincide.
    """
    resultado = []
    i = 0
    while i < len(usuarios):
        if usuarios[i]["rol"] == rol:
            resultado.append(usuarios[i])
        i += 1
    return resultado
 
 
def filtrar_por_desarrolladora(juegos: list, nombre: str) -> list:
    """Filtra los juegos publicados por una desarrolladora específica.
 
    Args:
        juegos (list): Lista de diccionarios de juegos.
        nombre (str): Nombre de usuario de la desarrolladora.
 
    Returns:
        list: Lista de juegos cuya 'desarrolladora' coincide (sin distinguir mayúsculas).
    """
    resultado = []
    i = 0
    while i < len(juegos):
        if juegos[i]["desarrolladora"].lower() == nombre.lower():
            resultado.append(juegos[i])
        i += 1
    return resultado
 
 
def buscar_juego(juegos: list, nombre: str) -> dict | None:
    """Busca un juego por nombre dentro de una lista de juegos.
 
    Se usa junto con filtrar_por_desarrolladora() para chequear si una
    desarrolladora ya tiene un juego publicado con ese nombre.
 
    Args:
        juegos (list): Lista de diccionarios de juegos.
        nombre (str): Nombre del juego a buscar.
 
    Returns:
        dict | None: Diccionario del juego si existe, None en caso contrario.
    """
    resultado = None
    i = 0
    while i < len(juegos) and resultado is None:
        if juegos[i]["nombre"] == nombre:
            resultado = juegos[i]
        i += 1
    return resultado
 
 
def calcular_ventas(compras: list, desarrolladora: str) -> tuple:
    """Calcula la cantidad de copias vendidas y el ingreso total de una desarrolladora.
 
    Args:
        compras (list): Lista de diccionarios de compras.
        desarrolladora (str): Nombre de usuario de la desarrolladora.
 
    Returns:
        tuple: (cantidad_copias (int), ingreso_total (float))
    """
    cantidad = 0
    total = 0.0
    i = 0
    while i < len(compras):
        if compras[i]["desarrolladora"].lower() == desarrolladora.lower():
            cantidad += 1
            total += compras[i]["precio"]
        i += 1
    return cantidad, total
 
 
def obtener_biblioteca_jugador(compras: list, jugador: str) -> list:
    """Obtiene la lista de compras (juegos) realizadas por un jugador.
 
    Args:
        compras (list): Lista de diccionarios de compras.
        jugador (str): Nombre de usuario del jugador.
 
    Returns:
        list: Lista de diccionarios de compras de ese jugador.
    """
    resultado = []
    i = 0
    while i < len(compras):
        if compras[i]["jugador"].lower() == jugador.lower():
            resultado.append(compras[i])
        i += 1
    return resultado
 
 
def publicar_juego(juegos: list, nuevo_juego: dict) -> list:
    """Agrega un nuevo juego a una copia de la lista de juegos.
 
    Función pura: no modifica la lista `juegos` original, devuelve una nueva.
 
    Args:
        juegos (list): Lista de diccionarios de juegos.
        nuevo_juego (dict): Diccionario con los datos del juego a agregar.
 
    Returns:
        list: Nueva lista de juegos con el nuevo juego incluido.
    """
    resultado = juegos.copy()
    resultado.append(nuevo_juego)
    return resultado
 
 
def obtener_ventas_a_matriz(juegos: list, desarrolladora: str) -> list:
    """Construye la matriz de ventas de una desarrolladora.
 
    Cada fila representa un juego con [precio, copias_vendidas, ingreso_total].
 
    Args:
        juegos (list): Lista de diccionarios de juegos.
        desarrolladora (str): Nombre de usuario de la desarrolladora.
 
    Returns:
        list: Matriz (lista de listas) [precio, copias_vendidas, ingreso_total].
    """
    matriz = []
    juegos_propios = filtrar_por_desarrolladora(juegos, desarrolladora)
    i = 0
    while i < len(juegos_propios):
        j = juegos_propios[i]
        ingreso_total = j["precio"] * j["copias_vendidas"]
        matriz.append([j["precio"], j["copias_vendidas"], ingreso_total])
        i += 1
    return matriz
 

#  ENTRADA AUXILIAR VALIDADA ──────────────────────────────────

def leer_entero_positivo(mensaje: str) -> int:
    """Solicita un número entero positivo por consola, validando manualmente.

    Args:
        mensaje (str): Texto a mostrar en el input.

    Returns:
        int: Número entero positivo ingresado.
    """
    valor = -1
    while valor == -1:
        entrada = input(mensaje)
        if entrada.isdigit() and int(entrada) > 0:
            valor = int(entrada)
        else:
            print("Error: ingrese un número entero positivo.\n")
    return valor


#  JUGADOR ────────────────────────────────────────────────────

def ver_perfil_jugador(usuarios: list, indice_usuario: int) -> None:
    """Muestra los datos del jugador logueado.

    Args:
        usuarios (list): Lista de diccionarios de usuarios.
        indice_usuario (int): Índice del usuario en la lista.
    """
    u = usuarios[indice_usuario]
    mostrar_perfil_jugador(
        u["usuario"],
        u["nombre"],
        u["apellido"],
        u["pais"],
        u["genero_favorito"],
        u["horas_jugadas"],
        u["juegos_comprados"],
        u["logros"],
    )


def explorar_catalogo(usuarios: list, juegos: list, compras: list, indice_usuario: int) -> None:
    """Permite al jugador buscar juegos por empresa, elegir un título
    y simular una compra con método de pago. Persiste la compra en
    compras.json y actualiza juegos.json y usuarios.json.

    Args:
        usuarios (list): Lista de diccionarios de usuarios (se modifica en memoria y se persiste).
        juegos (list): Lista de diccionarios de juegos (se modifica en memoria y se persiste).
        compras (list): Lista de diccionarios de compras (se modifica en memoria y se persiste).
        indice_usuario (int): Índice del jugador logueado.
    """
    empresa = ""
    while len(empresa) < 3:
        empresa = input("Ingrese el nombre de usuario de la empresa desarrolladora: ")
        if len(empresa) < 3:
            print("Error: debe tener al menos 3 caracteres.\n")

    juegos_empresa = buscar_juegos_por_empresa(juegos, empresa)

    if len(juegos_empresa) == 0:
        print(f"No se encontraron juegos de la desarrolladora '{empresa}'.\n")
        return

    mostrar_catalogo_juegos(empresa, juegos_empresa)

    juego_elegido = -1
    while juego_elegido == -1:
        opcion = input("Elija un juego (número): ")
        if opcion.isdigit():
            num = int(opcion)
            if 1 <= num <= len(juegos_empresa):
                juego_elegido = num - 1
            else:
                print("Opción fuera de rango.\n")
        else:
            print("Ingrese un número válido.\n")

    metodos_pago = ["Tarjeta de Credito", "MercadoPago"]
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

    juego = juegos_empresa[juego_elegido]

    nueva_compra = {
        "jugador": usuarios[indice_usuario]["usuario"],
        "juego": juego["nombre"],
        "desarrolladora": juego["desarrolladora"],
        "precio": juego["precio"],
        "metodo_pago": metodos_pago[metodo_elegido],
        "fecha": date.today().isoformat(),
    }
    compras.append(nueva_compra)
    guardar_compras(compras)

    indice_juego = buscar_indice_juego(juegos, juego["nombre"], juego["desarrolladora"])
    if indice_juego != -1:
        juegos[indice_juego]["copias_vendidas"] += 1
        guardar_juegos(juegos)

    usuarios[indice_usuario]["juegos_comprados"] += 1
    guardar_usuarios(usuarios)

    mostrar_confirmacion_compra(juego["nombre"], metodos_pago[metodo_elegido], juego["precio"])


#  DESARROLLADORA ─────────────────────────────────────────────

def ver_datos_desarrolladora(usuarios: list, indice_usuario: int) -> None:
    """Muestra los datos de la desarrolladora logueada.

    Args:
        usuarios (list): Lista de diccionarios de usuarios.
        indice_usuario (int): Índice del usuario en la lista.
    """
    u = usuarios[indice_usuario]
    mostrar_datos_desarrolladora(
        u["nombre_estudio"],
        u["pais"],
        u["sitio_web"],
        u["juegos_publicados"],
        u["ventas_totales"],
        u["año_fundacion"],
    )


def gestionar_publicacion_juego(usuarios: list, juegos: list, indice_usuario: int) -> None:
    """Solicita los datos de un nuevo juego, lo agrega a juegos.json y
    actualiza el contador de juegos publicados de la desarrolladora.

    Validaciones:
        - Nombre del videojuego: no vacío.
        - Precio: debe ser mayor a 0.

    Args:
        usuarios (list): Lista de diccionarios de usuarios (se modifica en memoria y se persiste).
        juegos (list): Lista de diccionarios de juegos (se modifica en memoria y se persiste).
        indice_usuario (int): Índice de la desarrolladora logueada.
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

    nuevo_juego = {
        "nombre": nombre_juego,
        "desarrolladora": usuarios[indice_usuario]["usuario"],
        "precio": precio,
        "copias_vendidas": 0,
    }
    juegos_actualizados = publicar_juego(juegos, nuevo_juego)
    juegos.clear()
    juegos.extend(juegos_actualizados)
    guardar_juegos(juegos)

    usuarios[indice_usuario]["juegos_publicados"] += 1
    guardar_usuarios(usuarios)

    mostrar_confirmacion_publicacion(nombre_juego, precio)


def ver_ventas(usuarios: list, juegos: list, compras: list, indice_usuario: int) -> None:
    """Calcula y muestra las ventas reales de la desarrolladora logueada,
    a partir de los datos persistidos en compras.json y juegos.json.

    Args:
        usuarios (list): Lista de diccionarios de usuarios.
        juegos (list): Lista de diccionarios de juegos.
        compras (list): Lista de diccionarios de compras.
        indice_usuario (int): Índice de la desarrolladora logueada.
    """
    desarrolladora = usuarios[indice_usuario]["usuario"]
    cantidad = contar_ventas(compras, desarrolladora)
    total = calcular_ventas_totales(compras, desarrolladora)
    juegos_propios = buscar_juegos_por_empresa(juegos, desarrolladora)
    mejor = juego_mas_vendido(juegos_propios)
    nombre_mejor = mejor["nombre"] if "nombre" in mejor else "N/A"
    mostrar_ventas(cantidad, total, nombre_mejor)


#  ADMINISTRADOR ──────────────────────────────────────────────

def crear_usuario(usuarios: list) -> None:
    """Solicita y valida los datos para crear un nuevo usuario, lo agrega
    a la lista en memoria y persiste el cambio en usuarios.json.

    Validaciones:
        - Nombre de usuario: mínimo 4 caracteres y no debe existir ya.
        - Contraseña: mínimo 8 caracteres (se guarda hasheada).
        - Rol: 'Jugador' o 'Desarrolladora'.
        - Datos adicionales según el rol elegido.

    Args:
        usuarios (list): Lista de diccionarios de usuarios (se modifica en memoria y se persiste).
    """
    print("\n==== CREAR USUARIO ====\n")

    nombre_usuario = ""
    usuario_valido = False
    while not usuario_valido:
        nombre_usuario = input("Ingrese el nombre de usuario (mín. 4 caracteres): ")
        if len(nombre_usuario) < 4:
            print("Error: el nombre de usuario debe tener al menos 4 caracteres.\n")
        elif buscar_indice_usuario(usuarios, nombre_usuario) != -1:
            print("Error: ese nombre de usuario ya existe.\n")
        else:
            usuario_valido = True

    contraseña = ""
    while len(contraseña) < 8:
        contraseña = input("Ingrese la contraseña (mín. 8 caracteres): ")
        if len(contraseña) < 8:
            print("Error: la contraseña debe tener al menos 8 caracteres.\n")

    roles_validos = ["Jugador", "Desarrolladora"]
    print("\nRoles disponibles:")
    i = 0
    while i < len(roles_validos):
        print(f"  {i + 1} - {roles_validos[i]}")
        i += 1

    rol_elegido = -1
    while rol_elegido == -1:
        opcion = input("\nElija un rol: ")
        if opcion.isdigit():
            num = int(opcion)
            if 1 <= num <= len(roles_validos):
                rol_elegido = num - 1
            else:
                print("Opción fuera de rango.\n")
        else:
            print("Ingrese un número válido.\n")

    rol = roles_validos[rol_elegido]
    print(f"\nDatos adicionales para {rol}:\n")

    nuevo_usuario = {
        "usuario": nombre_usuario,
        "contraseña": hashear_password(contraseña),
        "rol": rol,
    }

    if rol == "Jugador":
        nuevo_usuario["nombre"] = input("Nombre: ")
        nuevo_usuario["apellido"] = input("Apellido: ")
        nuevo_usuario["pais"] = input("País: ")
        nuevo_usuario["genero_favorito"] = input("Género de videojuego favorito: ")
        nuevo_usuario["horas_jugadas"] = 0
        nuevo_usuario["juegos_comprados"] = 0
        nuevo_usuario["logros"] = 0
    else:
        nuevo_usuario["nombre_estudio"] = input("Nombre del estudio: ")
        nuevo_usuario["pais"] = input("País: ")
        nuevo_usuario["sitio_web"] = input("Sitio web del estudio: ")
        nuevo_usuario["juegos_publicados"] = 0
        nuevo_usuario["ventas_totales"] = 0
        nuevo_usuario["año_fundacion"] = leer_entero_positivo("Año de fundación: ")

    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

    mostrar_confirmacion_creacion(nombre_usuario, rol)


def borrar_usuario(usuarios: list, eliminados: list) -> None:
    """Solicita un nombre de usuario, lo quita de usuarios.json y lo
    registra en eliminados.json.

    Validaciones:
        - Nombre de usuario: mínimo 4 caracteres.
        - Debe existir en la lista de usuarios.

    Args:
        usuarios (list): Lista de diccionarios de usuarios (se modifica en memoria y se persiste).
        eliminados (list): Lista de diccionarios de usuarios eliminados (se modifica en memoria y se persiste).
    """
    print("\n==== BORRAR USUARIO ====\n")

    nombre_usuario = ""
    while len(nombre_usuario) < 4:
        nombre_usuario = input("Ingrese el nombre de usuario a eliminar (mín. 4 caracteres): ")
        if len(nombre_usuario) < 4:
            print("Error: el nombre de usuario debe tener al menos 4 caracteres.\n")

    indice = buscar_indice_usuario(usuarios, nombre_usuario)
    if indice == -1:
        print(f"No se encontró el usuario '{nombre_usuario}'.\n")
        return

    usuario_eliminado = usuarios.pop(indice)
    eliminados.append(usuario_eliminado)

    guardar_usuarios(usuarios)
    guardar_eliminados(eliminados)

    mostrar_confirmacion_borrado(nombre_usuario)


def ver_info_sistema() -> None:
    """Muestra información general del sistema GameHub."""
    mostrar_info_sistema()