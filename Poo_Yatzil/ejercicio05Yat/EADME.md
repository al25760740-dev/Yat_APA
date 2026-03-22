# 🐾 Clases Abstractas en Python

Este proyecto demuestra el uso de clases abstractas y herencia en Python, creando una plantilla general `Animal` y clases específicas que implementan sus métodos.

## 🚀 Funcionalidad

* Definir una clase abstracta `Animal` con un método abstracto `hablar()`
* Crear clases concretas (`Perro` y `Gato`) que implementan `hablar()`
* Instanciar objetos y llamar a sus métodos específicos

## ▶️ Ejecución

```bash id="abstract01"
python main.py
```

## 📌 Ejemplo de uso

```text id="abstract_example"
perro = Perro()
gato = Gato()

print(perro.hablar())  # ¡Guau!
print(gato.hablar())    # ¡Miau!
```

## 🛠️ Requisitos

* Python 3

## 📈 Posibles mejoras

* Agregar más animales y sonidos
* Implementar métodos abstractos adicionales (comer, dormir, moverse)
* Usar herencia múltiple o interfaces para comportamientos comunes
