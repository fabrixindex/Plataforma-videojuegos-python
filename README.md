# 🎮 GameHub — Trabajo Práctico (Entrega 2)

**Materia:** Programación I
**Carrera:** Tecnicatura Universitaria en Programación
**Universidad:** Universidad Tecnológica Nacional — Facultad Regional Avellaneda (UTN FRA)
**Alumnos:** Fabricio Papetti · Ezequiel Popolo
**División:** 314

---

## 📋 Descripción

Sistema de gestión de videojuegos desarrollado en Python. Respecto a la Entrega 1, ahora **todos los datos se leen y persisten en archivos JSON** en lugar de estar hardcodeados: usuarios, catálogo de juegos y compras realizadas viven en `usuarios.json`, `juegos.json` y `compras.json`, y los usuarios eliminados quedan registrados en `eliminados.json`.

---

## 🎯 Criterios de desarrollo

- **Sin uso de objetos ni métodos** — algoritmia pura con funciones, listas y estructuras de control
- **Sin excepciones** (`try/except`) — la falta de un archivo se resuelve verificando su existencia
- **Persistencia real**: toda alta, baja o modificación de datos se guarda en el JSON correspondiente antes de volver al menú
- **Funciones puras** de búsqueda, filtrado y cálculo (`Funciones.py`): reciben listas por parámetro, no tocan variables globales y devuelven un resultado
- **Vista tabular (matriz)** disponible en al menos una opción de menú de cada rol
- **Separación en módulos**: `Prints.py`, `Inputs.py`, `Menu.py`, `Funciones.py`, `Persistencia.py` y `Main.py`

---

## 📁 Estructura del proyecto

```
📦 GameHub — Entrega 2
 ┣ 📄 Main.py           # Punto de entrada: carga los JSON e inicia sesión/menú
 ┣ 📄 Persistencia.py   # Carga y guardado genérico de listas en archivos JSON
 ┣ 📄 Inputs.py         # Login (validar_login, iniciar_sesion) y hash de contraseñas
 ┣ 📄 Funciones.py      # Lógica de negocio + funciones puras de búsqueda/filtrado/cálculo
 ┣ 📄 Menu.py           # Menús diferenciados por rol, reciben las listas por parámetro
 ┣ 📄 Prints.py         # Funciones de salida por consola, incluidas las tablas
 ┣ 📄 usuarios.json     # Lista de usuarios (usuario, contraseña hasheada, rol, datos personales)
 ┣ 📄 juegos.json       # Catálogo de juegos publicados
 ┣ 📄 compras.json      # Historial de compras realizadas
 ┗ 📄 eliminados.json   # Usuarios dados de baja (misma estructura que usuarios.json)
```

---

## 🗄️ Estructura de los archivos JSON

### `usuarios.json`
Lista de diccionarios. Cada uno tiene `usuario`, `contraseña` (hash SHA-256), `rol` (`"Jugador"`, `"Desarrolladora"` o `"Administrador"`) y los datos personales según el rol:
- **Jugador:** `nombre`, `apellido`, `pais`, `genero_favorito`, `horas_jugadas`, `juegos_comprados`, `logros`
- **Desarrolladora:** `nombre_estudio`, `pais`, `sitio_web`, `juegos_publicados`, `ventas_totales`, `año_fundacion`
- **Administrador:** `nombre`, `apellido`, `pais`

### `juegos.json`
Lista de diccionarios con `nombre`, `desarrolladora` (usuario que lo publicó), `precio` y `copias_vendidas`.

### `compras.json`
Lista de diccionarios con `jugador`, `juego`, `desarrolladora`, `precio`, `metodo_pago` (`"Tarjeta de Credito"` o `"MercadoPago"`) y `fecha`.

### `eliminados.json`
Lista de diccionarios con la misma estructura que un elemento de `usuarios.json`, para los usuarios dados de baja.

---

## 👥 Usuarios de prueba

| Rol | Usuario | Contraseña |
|-----|---------|------------|
| Jugador | `elrubiusomg` | `callofduty7` |
| Jugador | `gamerchick99` | `password123` |
| Desarrolladora | `ubisoftgames` | `assasinscreed` |
| Desarrolladora | `hyperbeard01` | `beardgames1` |
| Administrador | `adminepic` | `metalgearsolid` |

---

## ⚙️ Funcionalidades por rol

### 🕹️ Jugador
1. Ver perfil (datos leídos de `usuarios.json`)
2. Explorar catálogo por desarrolladora y comprar (lee `juegos.json`, registra la compra en `compras.json` y actualiza `copias_vendidas` y `juegos_comprados`)
3. **Ver catálogo completo en vista tabla** (matriz con todos los juegos de `juegos.json`)

### 🏢 Desarrolladora
1. Ver datos del estudio
2. Publicar juego (se agrega a `juegos.json` y suma `juegos_publicados`)
3. Ver ventas — calculadas en tiempo real a partir de `compras.json` y `juegos.json` (cantidad de ventas, ingresos totales, juego más vendido)
4. **Ver mis juegos en vista tabla**

### 🔧 Administrador
1. Crear usuario (valida que no exista, hashea la contraseña, persiste en `usuarios.json`)
2. Borrar usuario (lo quita de `usuarios.json` y lo agrega a `eliminados.json`)
3. Ver información del sistema
4. **Ver usuarios en vista tabla**

---

## 🔧 Funciones puras (búsqueda, filtrado y cálculo)

Ubicadas en `Funciones.py`, reciben listas como parámetro y no modifican variables globales:

- `buscar_indice_usuario`, `buscar_indice_juego`
- `buscar_juegos_por_empresa`
- `calcular_ventas_totales`, `contar_ventas`, `juego_mas_vendido`
- `construir_matriz_juegos`, `construir_matriz_usuarios`, `construir_matriz_compras`

---

## ▶️ Ejecución

```bash
python Main.py
```

> Requiere Python 3.10 o superior (por el uso de `match/case`).

---

## 👨‍💻 Conceptos aplicados

- Persistencia de datos en archivos JSON (`json.load` / `json.dump`)
- Hash de contraseñas con `hashlib.sha256`
- Listas de diccionarios como estructura central de datos
- Funciones puras separadas de las funciones con efectos secundarios (E/S, persistencia)
- Vistas tabulares (matrices) construidas a partir de datos reales
- Estructuras de control: `while`, `match/case`
- Validación de entrada sin excepciones
- Separación de responsabilidades en módulos