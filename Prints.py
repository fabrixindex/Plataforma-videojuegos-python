def mostrar_bienvenida() -> None:
    """Muestra el mensaje de bienvenida al iniciar el sistema GameHub.
    
    Imprime por consola el nombre de la plataforma y una descripción
    breve, sin recibir parámetros ni retornar valores.
    """
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


def mostrar_catalogo_juegos(empresa: str, titulos: list, precios: list) -> None:
    """Muestra el listado de juegos disponibles de una empresa con sus precios.

    Args:
        empresa (str): Nombre de la empresa desarrolladora.
        titulos (list): Lista de títulos de juegos.
        precios (list): Lista de precios correspondientes a cada título.
    """
    print(f"\n==== CATÁLOGO — {empresa.upper()} ====\n")
    i = 0
    while i < len(titulos):
        print(f"  {i + 1} - {titulos[i]:<25} ${precios[i]:.2f}")
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
 
#  DESARROLLADORA
 
def mostrar_datos_desarrolladora(nombre_estudio: str, pais: str, sitio_web: str,
                                  juegos_publicados: int, ventas_totales: int, anio_fundacion: int) -> None:
    """Muestra los datos del estudio desarrollador por consola.
 
    Args:
        nombre_estudio (str): Nombre del estudio.
        pais (str): País de origen del estudio.
        sitio_web (str): Sitio web oficial.
        juegos_publicados (int): Cantidad de juegos publicados en la plataforma.
        ventas_totales (int): Total de copias vendidas.
        anio_fundacion (int): Año de fundación del estudio.
    """
    pass
 
 
def mostrar_confirmacion_publicacion(nombre_juego: str, precio: float) -> None:
    """Muestra el mensaje de confirmación al publicar un juego.
 
    Args:
        nombre_juego (str): Nombre del juego publicado.
        precio (float): Precio asignado al juego.
    """
    pass
 
 
def mostrar_ventas() -> None:
    """Muestra un resumen ficticio de ventas del mes."""
    pass
 
 
#  ADMINISTRADOR
 
def mostrar_confirmacion_creacion(nombre_usuario: str, rol: str) -> None:
    """Muestra el mensaje de confirmación al crear un usuario.
 
    Args:
        nombre_usuario (str): Nombre del usuario creado.
        rol (str): Rol asignado al nuevo usuario.
    """
    pass
 
 
def mostrar_confirmacion_borrado(nombre_usuario: str) -> None:
    """Muestra el mensaje de confirmación al simular el borrado de un usuario.
 
    Args:
        nombre_usuario (str): Nombre del usuario a eliminar.
    """
    pass
 
 
def mostrar_info_sistema() -> None:
    """Muestra la información general del sistema, integrantes y funcionalidades."""
    pass