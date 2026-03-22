
# Sistema de Gestión de Estudiantes en Python

Este proyecto es un ejemplo básico en Python que modela una clase `Estudiante`, permitiendo almacenar información personal y gestionar calificaciones para calcular promedios.

---

##Características

* Crear objetos de tipo estudiante
* Almacenar nombre, edad y carrera
* Agregar calificaciones dinámicamente
* Calcular el promedio de calificaciones
* Mostrar información del estudiante

---

##  Tecnologías utilizadas

* Python 3

---

##  Estructura del código

El programa contiene:

### Clase `Estudiante`

Incluye los siguientes métodos:

* `__init__(nombre, edad, carrera)`
  Constructor que inicializa los datos del estudiante.

* `setCalificaciones(calificacion)`
  Agrega una calificación a la lista.

* `getNombre()`
  Devuelve el nombre del estudiante.

* `mostrarPromedio()`
  Calcula y retorna el promedio de las calificaciones.

* `mostrarInformacionUsuario()`
  Retorna un mensaje con la información del estudiante.

---

## ▶️ Ejecución

1. Asegúrate de tener Python instalado
2. Guarda el archivo como `main.py`
3. Ejecuta el programa:

```bash
python main.py
```

---

##  Ejemplo de uso

El programa crea tres estudiantes:

* Yatzil (Ing. en Sistemas)
* Estrella (Ing. en Industrial)
* Pepe (Ing. en Electrónica)

Se agregan calificaciones a uno de ellos y se muestran los resultados en consola.

---

##  Ejemplo de salida

```
Hola, soy Yatzil, tengo 19 años y estudio Ing. en Sistemas
La calificación de Yatzil es: 63.333333333333336
La calificación es: Estrella es: 0
La calificacion es: Pepe es: 0
```

---

##  Posibles mejoras

* Validar que las calificaciones estén en un rango válido (0–100)
* Agregar eliminación de calificaciones
* Guardar datos en archivos o base de datos
* Crear interfaz gráfica
* Manejar múltiples estudiantes con listas o diccionarios

---

##  Contribuciones

Las contribuciones son bienvenidas. Puedes hacer un fork del proyecto y enviar un pull request.

---

##  Licencia

Este proyecto es de uso libre para fines educativos.
