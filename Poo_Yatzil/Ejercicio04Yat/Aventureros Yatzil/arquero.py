from aventurero import Aventurero

class Arquero(Aventurero):
    def __init__(self, nombre, nivel, flechas):
        super().__init__(nombre, nivel)
        self.flechas = flechas
    def presentarse(self):
        print(f"Hola Soy {self.nombre}: aventurero de nivel {self.nivel}")
        
    def usar_habilidad(self):
        self.flechas -= 1
        print(f"{self.nombre} lanzo una flecha, le quedan {self.flechas}")