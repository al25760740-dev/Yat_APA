# 🎮 Plataforma de Videojuegos: Competidores y Observadores

Este proyecto en Python simula una **plataforma de videojuegos online**, donde existen diferentes tipos de usuarios que interactúan con las partidas.

## 🧠 Concepto

Dentro de la plataforma hay dos roles principales:

* 🏆 **Competidor**: Jugador activo que participa en partidas y acumula puntos.
* 👀 **Observador**: Usuario que visualiza partidas sin participar directamente.

---

## 📂 Estructura del proyecto

```id="struc01"
/proyecto
│── main.py
│── competidor.py
│── observador.py
```

---

## 🚀 Cómo ejecutar

Ejecuta el archivo principal:

```bash id="run01"
python main.py
```

---

## 🎯 Funcionalidades

### 🏆 Competidores

* Crear perfil de jugador
* Unirse a un equipo (clan)
* Ganar puntos al jugar
* Perder puntos en derrotas
* Visualizar su progreso

### 👀 Observadores

* Ver partidas en vivo
* Llevar conteo de partidas vistas
* Consultar su perfil

---

## 🧑‍💻 Clases del sistema

### 🔹 `Competidor`

Representa a un jugador dentro de la plataforma.

**Atributos:**

* `nombre`
* `id`
* `nivel`
* `equipo` (clan o grupo)
* `puntos`

**Métodos:**

* `mostrar_perfil()`
* `ganar_puntos(cantidad)`
* `perder_puntos(cantidad)`

---

### 🔹 `Observador`

Representa a un espectador dentro del sistema.

**Atributos:**

* `nombre`
* `id`
* `nivel`
* `partidas_vistas`

**Métodos:**

* `ver_partida()`
* `mostrar_perfil()`

---

## 🧪 Ejemplo de simulación

El programa realiza:

* Creación de una competidora 🎮
* Actualización de su puntuación
* Creación de una observadora 👀
* Registro de partidas vistas

**Salida esperada:**

```id="out01"
...Competidora...

Nombre: Ary Gameplays
ID: 89111214
Nivel: Avanzado
Equipo: Los Polinesios
Puntos: 0

Gana 50 puntos. Total: 50
Pierde 20 puntos. Total: 30

...Observadora...

Partida observada. Total: 1
Partida observada. Total: 2

Nombre: Alexandra Cruz
ID: 81142018
Nivel: Principiante
Partidas vistas: 2
```

---

## 🕹️ Enfoque del proyecto

Este proyecto está inspirado en plataformas reales de videojuegos donde:

* Los jugadores compiten y suben de rango
* Existen espectadores (streaming / eSports)
* Se gestionan perfiles de usuario

---

## 📌 Requisitos

* Python 3.x
* No requiere librerías externas

---

## 💡 Posibles mejoras

* 🎮 Sistema de ranking global
* 🏅 Logros y recompensas
* 👥 Sistema de amigos
* 🔥 Modo multijugador real
* 💾 Guardado de datos
