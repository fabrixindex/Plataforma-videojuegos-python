import hashlib


def hashear_password(password: str) -> str:
    """Genera el hash SHA-256 de una contraseña en texto plano.

    Se usa para no almacenar contraseñas en texto plano dentro de
    usuarios.json.

    Args:
        password (str): Contraseña en texto plano.

    Returns:
        str: Representación hexadecimal del hash de la contraseña.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def validar_login(usuarios: list, usuario: str, password: str) -> int:
    """Busca las credenciales dentro de la lista de usuarios cargada desde archivo.

    Función pura: recibe la lista de usuarios y no la modifica.

    Args:
        usuarios (list): Lista de diccionarios de usuarios (usuarios.json).
        usuario (str): Nombre de usuario ingresado.
        password (str): Contraseña ingresada en texto plano.

    Returns:
        int: Índice del usuario si usuario y contraseña coinciden, -1 si no.
    """
    hash_ingresado = hashear_password(password)
    retorno = -1
    i = 0
    while i < len(usuarios) and retorno == -1:
        if usuarios[i]["usuario"] == usuario and usuarios[i]["contraseña"] == hash_ingresado:
            retorno = i
        i += 1
    return retorno


def iniciar_sesion(usuarios: list) -> int:
    """Solicita usuario y contraseña, valida el formato y las credenciales.

    Repite la solicitud hasta que el login sea exitoso.

    Args:
        usuarios (list): Lista de diccionarios de usuarios cargada desde usuarios.json.

    Returns:
        int: Índice del usuario logueado dentro de la lista `usuarios`.
    """
    retorno = -1
    while retorno == -1:
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        if len(usuario) < 4:
            print("Error: el usuario debe tener al menos 4 caracteres.\n")
        elif len(password) < 8:
            print("Error: la contraseña debe tener al menos 8 caracteres.\n")
        else:
            indice = validar_login(usuarios, usuario, password)
            if indice == -1:
                print("Error: usuario o contraseña incorrectos.\n")
            else:
                print(f"Bienvenido, {usuarios[indice]['usuario']}! Rol: {usuarios[indice]['rol']}\n")
                retorno = indice
    return retorno