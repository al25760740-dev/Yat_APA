# ⚔️ Sistema de Aventureros en Python

Este proyecto implementa un sistema básico de personajes utilizando programación orientada a objetos en Python. Incluye tres tipos de personajes: `Guerrero`, `Mago` y `Arquero`, cada uno con habilidades únicas.

## 🚀 Características

* Uso de clases y objetos
* Separación en módulos (`guerrero.py`, `mago.py`, `arquero.py`)
* Métodos personalizados por tipo de personaje
* Simulación de habilidades en consola

## 🧩 Clases

### 🗡️ Guerrero

* Atributos: nombre, nivel, arma
* Métodos:

  * `presentarse()`
  * `usar_habilidad()` → ataque cuerpo a cuerpo

### 🧙 Mago

* Atributos: nombre, nivel, hechizo
* Métodos:

  * `presentarse()`
  * `usar_habilidad()` → uso de magia

### 🏹 Arquero

* Atributos: nombre, nivel, precisión
* Métodos:

  * `presentarse()`
  * `usar_habilidad()` → ataque a distancia

## ▶️ Ejecución

```bash id="run123"
python main.py
```

## 📌 Ejemplo de uso

El programa crea tres personajes:

* Wilson (Guerrero)
* Ozz (Mago)
* Charlie (Arquero)

Cada uno se presenta y ejecuta su habilidad especial, mostrando resultados en consola.

## 🛠️ Requisitos

* Python 3

## 📈 Posibles mejoras

* Agregar sistema de combate
* Implementar herencia con una clase base `Personaje`
* Añadir interfaz gráfica
* Guardar progreso en archivos
