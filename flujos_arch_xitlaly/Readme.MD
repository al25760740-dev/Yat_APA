📁 Calculadora de Tamaño de Archivos en Python

Este proyecto en Python permite obtener el tamaño de un archivo y mostrarlo en:

Bytes
Kilobytes (KB)
Megabytes (MB)
📌 Código
import os

ruta = "test.txt"

# Bytes
size = os.path.getsize(ruta)

kb = size / 1024
mb = size / (1024 ** 2)

print(f"tamaño:{kb:.2f}KB")
print(f"tamaño:{mb:.2f}MB")

🚀 ¿Cómo funciona?

El programa utiliza el módulo os de Python para obtener el tamaño de un archivo mediante:

os.path.getsize(ruta)

Esta función devuelve el tamaño del archivo en bytes.

Después convierte:

Bytes → Kilobytes
Bytes → Megabytes
📂 Estructura del proyecto

── add.py

├── escritura.py

├── main.py

└── test.txt

✅ Ejemplo de salida
tamaño:0.01KB
tamaño:0.00MB


🛠 Tecnologías usadas

Python 3

Módulo os


📖 Conceptos utilizados

Bytes a Kilobytes

KB= 1024 Bytes
	​


Bytes a Megabytes

MB= 1024 2 Bytes
	​
