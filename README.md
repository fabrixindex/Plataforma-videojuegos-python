# 🎮 GameHub — Trabajo Práctico

**Materia:** Programación I  
**Carrera:** Tecnicatura Universitaria en Programación  
**Universidad:** Universidad Tecnológica Nacional — Facultad Regional Avellaneda (UTN FRA)  
**Alumnos:** Fabricio Papetti · Ezequiel Pololo  
**División:** 314

---

## 📋 Descripción

Sistema de gestión de videojuegos desarrollado en Python como trabajo práctico de la materia Programación I. El programa simula una plataforma digital donde jugadores, desarrolladoras y administradores interactúan con un sistema de autenticación por roles, aplicando los conceptos fundamentales de algoritmia y programación estructurada vistos en clase.

---

## 🎯 Criterios de desarrollo

El trabajo fue desarrollado respetando las siguientes restricciones propias de la materia:

- **Sin uso de objetos ni métodos** — algoritmia pura con funciones, listas y estructuras de control
- **Sin excepciones** (`try/except`)
- **Validaciones manuales**: longitud de cadenas, rangos numéricos, entradas vacías
- **Funciones reutilizables**: cada opción de menú tiene su propia función documentada
- **Separación en módulos**: `Prints.py`, `Inputs.py`, `Menu.py`, `Funciones.py` y `Main.py`

---

## 📁 Estructura del proyecto

```
📦 GameHub — Segundo Parcial
 ┣ 📄 Prints.py         # Funciones para la salida de datos por consola
 ┣ 📄 Inputs.py         # Datos globales (usuarios, contraseñas, roles) y funciones de login
 ┣ 📄 Funciones.py      # Lógica de negocio para cada opción de menú
 ┣ 📄 Menu.py           # Menús diferenciados por rol e invocación de funciones
 ┗ 📄 Main.py           # Punto de entrada del programa
```

---

## 👥 Roles del sistema

El sistema distingue tres tipos de usuario, cada uno con su propio menú:

| Rol | Usuario de prueba | Contraseña |
|-----|-------------------|------------|
| Jugador | `elrubiusomg` | `callofduty7` |
| Desarrolladora | `ubisoftgames` | `assasinscreed` |
| Administrador | `adminepic` | `metalgearsolid` |

---

## ⚙️ Funcionalidades

### 🕹️ Jugador
| Opción | Descripción |
|--------|-------------|
| 1 | **Ver perfil** — Muestra los datos del jugador (nombre, apellido, país, género favorito, horas jugadas, juegos comprados, logros) |
| 2 | **Explorar catálogo** — Busca juegos por empresa, elige un título y simula una compra con método de pago |

### 🏢 Desarrolladora
| Opción | Descripción |
|--------|-------------|
| 1 | **Ver datos** — Muestra información del estudio (nombre, país, sitio web, juegos publicados, ventas totales, año de fundación) |
| 2 | **Publicar juego** — Solicita nombre y precio del juego (validando precio > 0) y simula su publicación |
| 3 | **Ver ventas** — Muestra un resumen ficticio de ventas del mes |

### 🔧 Administrador
| Opción | Descripción |
|--------|-------------|
| 1 | **Crear usuario** — Solicita y valida usuario (mín. 4 caracteres), contraseña (mín. 8) y rol |
| 2 | **Borrar usuario** — Solicita un nombre de usuario y simula su eliminación con mensaje de confirmación |
| 3 | **Ver información del sistema** — Muestra integrantes, descripción del sistema y funcionalidades por rol |

---

## 🔧 Funciones principales

### Autenticación (`Inputs.py`)
- `validar_login(usuario, password)` — Busca las credenciales en las listas y retorna el índice del usuario o -1
- `iniciar_sesion()` — Solicita y valida las credenciales con reintento hasta el éxito

### Menús (`Menu.py`)
- `menu_jugador(indice_usuario)` — Menú y flujo del rol Jugador
- `menu_desarrolladora(indice_usuario)` — Menú y flujo del rol Desarrolladora
- `menu_administrador(indice_usuario)` — Menú y flujo del rol Administrador
- `iniciar_menu(indice_usuario)` — Dispatcher que deriva al menú según el rol

### Lógica de negocio (`Funciones.py`)
- `ver_perfil_jugador(indice_usuario)` — Recupera y delega la visualización del perfil
- `explorar_catalogo()` — Búsqueda por empresa, selección de juego y simulación de compra
- `ver_datos_desarrolladora(indice_usuario)` — Muestra datos del estudio
- `publicar_juego()` — Solicita nombre y precio con validación
- `ver_ventas()` — Muestra resumen de ventas ficticio
- `crear_usuario()` — Solicita y valida datos del nuevo usuario
- `borrar_usuario()` — Simula la eliminación de un usuario
- `ver_info_sistema()` — Muestra información general del sistema

### Presentación (`Prints.py`)
- `mostrar_bienvenida()` — Pantalla de inicio de la plataforma
- `mostrar_perfil_jugador(...)` — Datos completos del jugador
- `mostrar_catalogo_juegos(...)` — Lista de títulos con precios
- `mostrar_confirmacion_compra(...)` — Resumen de la compra realizada
- `mostrar_datos_desarrolladora(...)` — Datos del estudio desarrollador
- `mostrar_ventas()` — Resumen de ventas del mes
- `mostrar_info_sistema()` — Información general y funcionalidades

---

## ▶️ Ejecución

```bash
python Main.py
```

> Requiere Python 3.10 o superior (por el uso de `match/case`).

---

## 👨‍💻 Conceptos aplicados

- Estructuras de control: `while`, `match/case`
- Listas paralelas como estructura de datos
- Funciones con parámetros y retorno tipado
- Validación de entrada sin excepciones
- Autenticación por índice con recorrido secuencial
- Separación de responsabilidades en módulos
- Menús diferenciados por rol de usuario