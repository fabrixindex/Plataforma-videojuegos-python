def mostrar_bienvenida() -> None:
    """Muestra el mensaje de bienvenida al iniciar el sistema GameHub."""
    print()
    print("=== Bienvenido a GameHub ===")
    print()
    print("Tu plataforma de videojuegos")
    print()
    print("Descubrí, jugá y conectá con la comunidad gamer.\n")


#  JUGADOR

def mostrar_perfil_jugador(nombre_usuario: str, nombre: str, apellido: str,
                            pais: str, genero_favorito: str,
                            horas_jugadas: int, juegos_comprados: int, logros: int) -> None:
    """Muestra los datos del perfil de un jugador por consola.

    Args:
        nombre_usuario (str): Nombre de usuario de la sesión.
        nombre (str): Nombre real del jugador.
        apellido (str): Apellido del jugador.
        pais (str): País de origen.
        genero_favorito (str): Género de videojuego favorito.
        horas_jugadas (int): Total de horas jugadas en la plataforma.
        juegos_comprados (int): Cantidad de juegos adquiridos.
        logros (int): Cantidad de logros desbloqueados.
    """
    print("\n==== PERFIL DEL JUGADOR ====\n")
    print(f"  Usuario:           {nombre_usuario}")
    print(f"  Nombre:            {nombre}")
    print(f"  Apellido:          {apellido}")
    print(f"  País:              {pais}")
    print(f"  Género favorito:   {genero_favorito}")
    print(f"  Horas jugadas:     {horas_jugadas}")
    print(f"  Juegos comprados:  {juegos_comprados}")
    print(f"  Logros:            {logros}")
    print()


def mostrar_catalogo_juegos(empresa: str, juegos_empresa: list) -> None:
    """Muestra el listado de juegos disponibles de una empresa con sus precios.

    Args:
        empresa (str): Nombre de usuario de la empresa desarrolladora.
        juegos_empresa (list): Lista de diccionarios de juegos de esa empresa.
    """
    print(f"\n==== CATÁLOGO — {empresa.upper()} ====\n")
    i = 0
    while i < len(juegos_empresa):
        print(f"  {i + 1} - {juegos_empresa[i]['nombre']:<25} ${juegos_empresa[i]['precio']:.2f}")
        i += 1
    print()


def mostrar_confirmacion_compra(titulo: str, metodo: str, precio: float) -> None:
    """Muestra el resumen y confirmación de una compra realizada.

    Args:
        titulo (str): Nombre del juego comprado.
        metodo (str): Método de pago utilizado.
        precio (float): Precio total de la compra.
    """
    print("\n==== COMPRA CONFIRMADA ====\n")
    print(f"  Juego:             {titulo}")
    print(f"  Método de pago:    {metodo}")
    print(f"  Total:             ${precio:.2f}")
    print("\n¡Gracias por tu compra!\n")


def mostrar_tabla_juegos(matriz: list) -> None:
    """Muestra una tabla con los juegos cargados en el sistema.

    Args:
        matriz (list): Lista de listas [nombre, desarrolladora, precio, copias_vendidas].
    """
    print("\n==== CATÁLOGO (VISTA TABLA) ====\n")
    if len(matriz) == 0:
        print("  No hay juegos cargados.\n")
        return
    print(f"  {'Nombre':<25}{'Desarrolladora':<20}{'Precio':<12}{'Copias vendidas':<15}")
    print("  " + "-" * 72)
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        print(f"  {fila[0]:<25}{fila[1]:<20}${fila[2]:<11.2f}{fila[3]:<15}")
        i += 1
    print()


#  DESARROLLADORA

def mostrar_datos_desarrolladora(nombre_estudio: str, pais: str, sitio_web: str,
                                  juegos_publicados: int, ventas_totales: int, año_fundacion: int) -> None:
    """Muestra los datos del estudio desarrollador por consola.

    Args:
        nombre_estudio (str): Nombre del estudio.
        pais (str): País de origen del estudio.
        sitio_web (str): Sitio web oficial.
        juegos_publicados (int): Cantidad de juegos publicados en la plataforma.
        ventas_totales (int): Total de copias vendidas.
        año_fundacion (int): Año de fundación del estudio.
    """
    print("\n==== DATOS DEL ESTUDIO ====\n")
    print(f"  Nombre del estudio:   {nombre_estudio}")
    print(f"  País:                 {pais}")
    print(f"  Sitio web:            {sitio_web}")
    print(f"  Juegos publicados:    {juegos_publicados}")
    print(f"  Ventas totales:       {ventas_totales}")
    print(f"  Año de fundación:     {año_fundacion}")
    print()


def mostrar_confirmacion_publicacion(nombre_juego: str, precio: float) -> None:
    """Muestra el mensaje de confirmación al publicar un juego.

    Args:
        nombre_juego (str): Nombre del juego publicado.
        precio (float): Precio asignado al juego.
    """
    print("\n==== JUEGO PUBLICADO ====\n")
    print(f"  Nombre del juego:  {nombre_juego}")
    print(f"  Precio:            ${precio:.2f}")
    print("\n¡Tu juego ya está disponible en GameHub!\n")


def mostrar_ventas(cantidad: int, total: float, mas_vendido: str) -> None:
    """Muestra un resumen de ventas calculado a partir de compras.json.

    Args:
        cantidad (int): Cantidad de compras registradas para la desarrolladora.
        total (float): Monto total facturado.
        mas_vendido (str): Nombre del juego más vendido de la desarrolladora.
    """
    print("\n==== VENTAS ====\n")
    print(f"  Ventas registradas: {cantidad} copias vendidas.")
    print(f"  Ingresos totales:   ${total:.2f}")
    print(f"  Juego más vendido:  {mas_vendido}")
    print()


#  ADMINISTRADOR

def mostrar_confirmacion_creacion(nombre_usuario: str, rol: str) -> None:
    """Muestra el mensaje de confirmación al crear un usuario.

    Args:
        nombre_usuario (str): Nombre del usuario creado.
        rol (str): Rol asignado al nuevo usuario.
    """
    print("\n==== USUARIO CREADO ====\n")
    print(f"  Usuario:  {nombre_usuario}")
    print(f"  Rol:      {rol}")
    print("\n¡El usuario fue registrado exitosamente en el sistema!\n")


def mostrar_confirmacion_borrado(nombre_usuario: str) -> None:
    """Muestra el mensaje de confirmación al borrar un usuario.

    Args:
        nombre_usuario (str): Nombre del usuario eliminado.
    """
    print("\n==== USUARIO ELIMINADO ====\n")
    print(f"  El usuario '{nombre_usuario}' fue eliminado del sistema.")
    print()


def mostrar_tabla_usuarios(matriz: list) -> None:
    """Muestra una tabla con los usuarios cargados en el sistema.

    Args:
        matriz (list): Lista de listas [usuario, rol].
    """
    print("\n==== USUARIOS (VISTA TABLA) ====\n")
    if len(matriz) == 0:
        print("  No hay usuarios cargados.\n")
        return
    print(f"  {'Usuario':<20}{'Rol':<20}")
    print("  " + "-" * 40)
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        print(f"  {fila[0]:<20}{fila[1]:<20}")
        i += 1
    print()


def mostrar_tabla_compras(matriz: list) -> None:
    """Muestra una tabla con las compras registradas en el sistema.

    Args:
        matriz (list): Lista de listas [jugador, juego, precio, metodo_pago, fecha].
    """
    print("\n==== COMPRAS (VISTA TABLA) ====\n")
    if len(matriz) == 0:
        print("  No hay compras registradas.\n")
        return
    print(f"  {'Jugador':<15}{'Juego':<20}{'Precio':<10}{'Método':<20}{'Fecha':<12}")
    print("  " + "-" * 77)
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        print(f"  {fila[0]:<15}{fila[1]:<20}${fila[2]:<9.2f}{fila[3]:<20}{fila[4]:<12}")
        i += 1
    print()


def mostrar_info_sistema() -> None:
    """Muestra la información general del sistema, integrantes y funcionalidades."""
    print("\n==== INFORMACIÓN DEL SISTEMA ====\n")

    print("  Integrantes del grupo:")
    print("    - Fabricio Papetti")
    print("    - Ezequiel Pololo")
    print()

    print("  Descripción del sistema:")
    print("    GameHub es una plataforma digital de videojuegos que conecta")
    print("    a jugadores con el catálogo de títulos disponibles y permite")
    print("    a desarrolladoras gestionar la publicación y seguimiento de")
    print("    sus juegos en un solo lugar. Todos los datos se persisten en")
    print("    archivos JSON (usuarios, juegos, compras y eliminados).")
    print()
    print("    Problema que resuelve:")
    print("    Centraliza la compra de juegos, la gestión de estudios y la")
    print("    administración de usuarios en un único sistema unificado,")
    print("    con datos reales que persisten entre ejecuciones.")
    print()
    print("    Tipos de usuario:")
    print("    - Jugador: accede al catálogo y gestiona su perfil.")
    print("    - Desarrolladora: publica juegos y consulta sus ventas.")
    print("    - Administrador: administra los usuarios del sistema.")
    print()

    print("  Funcionalidades por rol:")
    print()
    print("    Jugador (3):")
    print("      1. Ver perfil con estadísticas personales.")
    print("      2. Explorar catálogo de juegos por empresa y comprar.")
    print("      3. Ver catálogo completo en vista tabla.")
    print()
    print("    Desarrolladora (3):")
    print("      1. Ver los datos del estudio registrado.")
    print("      2. Publicar un nuevo juego con nombre y precio.")
    print("      3. Consultar ventas reales calculadas desde compras.json.")
    print("      4. Ver los juegos propios en vista tabla.")
    print()
    print("    Administrador (3):")
    print("      1. Crear un nuevo usuario con rol asignado.")
    print("      2. Eliminar un usuario existente (se guarda en eliminados.json).")
    print("      3. Ver la información general del sistema.")
    print("      4. Ver usuarios en vista tabla.")
    print()