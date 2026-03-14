from aventurero import Aventurero

class Arquero(Aventurero):
    def __init__(self, nombre, nivel, flechas):
        super().__init__(nombre, nivel)
        self.flechas = flechas
def usar_habilidad(self):
    self.flechas -= 1
    print(f"{self.nombre} lanzo una flecha, le quedan {self.flechas}")