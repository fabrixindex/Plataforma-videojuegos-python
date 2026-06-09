from Inputs import usuarios, roles
 
#  JUGADOR

def ver_perfil_jugador(indice_usuario: int) -> None:
    """Muestra los datos del jugador logueado (hardcodeados).
 
    Incluye al menos 4 datos de tipo str y 3 de tipo int.
 
    Args:
        indice_usuario (int): Índice del usuario en las listas globales.
    """
    pass
 
 
def explorar_catalogo() -> None:
    """Permite al jugador buscar juegos por empresa desarrolladora,
    elegir un título y simular una compra con método de pago.
 
    Flujo:
        1. Solicita nombre de empresa (mínimo 3 caracteres).
        2. Muestra submenú de juegos de esa empresa con precios.
        3. Muestra submenú de métodos de pago.
        4. Calcula precio total y confirma la compra (o cancela si elige 0).
    """
    pass
 

#  DESARROLLADORA
 
def ver_datos_desarrolladora(indice_usuario: int) -> None:
    """Muestra los datos de la desarrolladora logueada (hardcodeados).
 
    Incluye al menos 3 datos de tipo str y 3 de tipo int.
 
    Args:
        indice_usuario (int): Índice del usuario en las listas globales.
    """
    pass
 
 
def publicar_juego() -> None:
    """Solicita los datos de un nuevo juego y simula su publicación.
 
    Validaciones:
        - Nombre del videojuego: no vacío.
        - Precio: debe ser mayor a 0.
    """
    pass
 
 
def ver_ventas() -> None:
    """Simula la visualización de ventas del mes con datos ficticios."""
    pass
 
 
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