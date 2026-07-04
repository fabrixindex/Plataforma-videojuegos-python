import json
import os

RUTA_USUARIOS = "usuarios.json"
RUTA_JUEGOS = "juegos.json"
RUTA_COMPRAS = "compras.json"
RUTA_ELIMINADOS = "eliminados.json"


def cargar_json(ruta: str) -> list:
    """Carga una lista de diccionarios desde un archivo JSON.

    Si el archivo no existe todavía, se retorna una lista vacía en lugar
    de lanzar una excepción (el proyecto no utiliza try/except).

    Args:
        ruta (str): Ruta del archivo JSON a cargar.

    Returns:
        list: Lista de diccionarios con los datos leídos del archivo.
    """
    if not os.path.exists(ruta):
        return []

    archivo = open(ruta, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()
    return datos


def guardar_json(ruta: str, datos: list) -> None:
    """Guarda una lista de diccionarios en un archivo JSON.

    Args:
        ruta (str): Ruta del archivo JSON destino.
        datos (list): Lista de diccionarios a persistir.
    """
    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(datos, archivo, indent=2, ensure_ascii=False)
    archivo.close()


#  Usuarios

def cargar_usuarios() -> list:
    """Carga la lista de usuarios desde usuarios.json."""
    return cargar_json(RUTA_USUARIOS)


def guardar_usuarios(usuarios: list) -> None:
    """Persiste la lista de usuarios en usuarios.json."""
    guardar_json(RUTA_USUARIOS, usuarios)


#  Juegos

def cargar_juegos() -> list:
    """Carga la lista de juegos desde juegos.json."""
    return cargar_json(RUTA_JUEGOS)


def guardar_juegos(juegos: list) -> None:
    """Persiste la lista de juegos en juegos.json."""
    guardar_json(RUTA_JUEGOS, juegos)


#  Compras

def cargar_compras() -> list:
    """Carga la lista de compras desde compras.json."""
    return cargar_json(RUTA_COMPRAS)


def guardar_compras(compras: list) -> None:
    """Persiste la lista de compras en compras.json."""
    guardar_json(RUTA_COMPRAS, compras)


#  Eliminados

def cargar_eliminados() -> list:
    """Carga la lista de usuarios eliminados desde eliminados.json."""
    return cargar_json(RUTA_ELIMINADOS)


def guardar_eliminados(eliminados: list) -> None:
    """Persiste la lista de usuarios eliminados en eliminados.json."""
    guardar_json(RUTA_ELIMINADOS, eliminados)