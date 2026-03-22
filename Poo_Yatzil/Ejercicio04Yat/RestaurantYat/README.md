# 🍽️ Sistema de Menú en Python

Este proyecto implementa un sistema básico de menú utilizando programación orientada a objetos en Python. Incluye diferentes tipos de productos: `Comida`, `Bebida` y `Postre`.

## 🚀 Características

* Uso de clases y objetos
* Organización en múltiples archivos (`comida.py`, `bebida.py`, `postre.py`)
* Métodos para mostrar información y tipo de producto
* Simulación de un menú en consola

## 🧩 Clases

### 🍲 Comida

* Atributos: nombre, precio, categoría
* Métodos:

  * `mostrar_info()`
  * `tipo()`

### 🥤 Bebida

* Atributos: nombre, precio, temperatura
* Métodos:

  * `mostrar_info()`
  * `tipo()`

### 🍰 Postre

* Atributos: nombre, precio, contiene azúcar
* Métodos:

  * `mostrar_info()`
  * `tipo()`

## ▶️ Ejecución

```bash id="menu01"
python main.py
```

## 📌 Ejemplo

El programa crea:

* Chilaquiles (Comida)
* Limonada Rosa (Bebida)
* Pan de plátano (Postre)

Y muestra su información junto con su tipo en consola.

## 🛠️ Requisitos

* Python 3

## 📈 Posibles mejoras

* Agregar más tipos de productos
* Implementar herencia (clase base `Producto`)
* Crear un sistema de pedidos
* Añadir interfaz gráfica
