from mob import Mob

class Aldeano(Mob):
    """Mob amigable, suena 'Hrrmmm… huh', te pide gemas."""

    def hacer_sonido(self):
        return "Hrrmmm… huh"
    
    def comportamiento(self):
        return "Amigable"
    def moverse(self):
        return "Se mueve lento"