from aventurero import Aventurero

class Mago (Aventurero):
    def __init__(self, nombre, nivel, hechizo):
        super().__init__(nombre, nivel)
        self.hechizo = hechizo
    def presentarse(self):
        print(f"Hola Soy {self.nombre}: aventurero de nivel {self.nivel}")
    
    def usar_habilidad(self):
            print(f"{self.nombre} lanza {self.hechizo}")