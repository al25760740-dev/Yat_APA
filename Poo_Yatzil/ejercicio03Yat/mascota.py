class Mascota:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

# Validar que el nivel de felicidad este entre 0 y 100
        if nivelFelicidad < 0:
            self.nivelFelicidad = 0
        elif nivelFelicidad > 100:
            self.nivelFelicidad = 100
        else:
            self.nivelFelicidad = nivelFelicidad

    def alimentar(self):
        # Aumenta 10 sin pasar de 100
        self.nivelFelicidad = min(self.nivelFelicidad + 10, 100)

    def jugar(self):
        # Aumenta 20 sin pasar de 100
        self.nivelFelicidad = min(self.nivelFelicidad + 20, 100)
    
    def mostrarEstado(self):
        return f"{self.nombre} es un {self.tipo} con felicidad: {self.nivelFelicidad}"
    
    def esFeliz(self):
        return self.nivelFelicidad > 70
    
    # Crear mascotas

mascota1 = Mascota("Doky", "Perro", 3, 50)
mascota2 = Mascota("Tomy", "Gato", 2, 80)

#Mostrar estado inicial
print(mascota1.mostrarEstado())
print("¿Es feliz?", mascota1.esFeliz())

print(mascota2.mostrarEstado())
print("¿Es feliz?", mascota2.esFeliz())

print("\n--- Interacciones ---")

#Interactuar con mascota1
mascota1.alimentar()
print(mascota1.mostrarEstado())

mascota1.jugar()
print(mascota1.mostrarEstado())
print("¿Es feliz?", mascota1.esFeliz())

#Interactuar mascota2
mascota2.jugar()
print(mascota2.mostrarEstado())

mascota2.alimentar()
print(mascota2.mostrarEstado())
print("¿Es feliz?", mascota2.esFeliz())
