usuarios  = ["elrubiusomg",   "ubisoftgames",  "adminepic"]
passwords = ["callofduty7",   "assasinscreed", "metalgearsolid"]
roles     = ["Jugador",       "Desarrolladora","Administrador"]

# Datos extra del perfil jugador
nombres          = ["Rubén",    "Ubisoft",  "Epic"]
apellidos        = ["Doblas",   "Games",    "Admin"]
paises           = ["España",   "Francia",  "EEUU"]
generos_favoritos= ["FPS",      "Aventura", "Acción"]
horas_jugadas    = [1500,       3200,       800]
juegos_comprados = [42,         15,         5]
logros           = [320,        210,        90]

def validar_login(usuario: str, password: str) -> int:
    """Busca el usuario y contraseña en las listas predefinidas.

    Args:
        usuario (str): Nombre de usuario ingresado.
        password (str): Contraseña ingresada.

    Returns:
        int: Índice del usuario si existe y la contraseña es correcta, -1 en caso contrario.
    """
    retorno = -1
    i = 0
    while i < len(usuarios) and retorno == -1:
        if usuarios[i] == usuario and passwords[i] == password:
            retorno = i
        i += 1
    return retorno

def iniciar_sesion() -> int:
    """Solicita usuario y contraseña al usuario, valida el formato y verifica
    las credenciales. Repite hasta que el login sea exitoso.

    Returns:
        int: Índice del usuario logueado en las listas.
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
            indice = validar_login(usuario, password)
            if indice == -1:
                print("Error: usuario o contraseña incorrectos.\n")
            else:
                print(f"Bienvenido, {usuarios[indice]}! Rol: {roles[indice]}\n")
                retorno = indice
    return retorno
    