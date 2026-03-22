from abc import ABC, abstractmethod

# Tabla de daño por material
DAÑO_MATERIAL = {
    "madera"    : 2,
    "piedra"    : 3,
    "hierro"    : 4,
    "oro"       : 3,
    "diamante"  : 6,
    "netherite" : 8,
}

class Herramienta(ABC):
    """Clase abstracta para todas las herramientas."""

    def __init__(self, material: str, durabilidad: int):
        self._material = material.lower()
        self._durabilidad = durabilidad
        self._usos_restantes = durabilidad

    # Propiedad ABSTRACTA
    @property
    @abstractmethod
    def nombre(self) -> str:
        pass

    # Método ABSTRACTO
    @abstractmethod
    def usar(self, objetivo: str) -> str:
        pass

    # Métodos CONCRETOS heredados por todas las subclases
    def calcular_daño(self) -> int:
        return DAÑO_MATERIAL.get(self._material, 1)

    def desgastar(self):
        if self._usos_restantes > 0:
            self._usos_restantes -= 1

    @property
    def rota(self) -> bool:
        return self._usos_restantes == 0

    def estado(self):
        if self.rota:
            print(f"[{self.nombre} de {self._material}] ROTA")
        else:
            print(f"[{self.nombre} de {self._material}] {self._usos_restantes} usos")