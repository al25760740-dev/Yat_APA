from mob import Mob

class Enderman(Mob):
    """Mob neutral, suena distorsionado, se teletransporta."""

    def hacer_sonido(self):
        return "Grrrr..."
    
    def comportamiento(self):
        return "Neutral"
    def moverse(self):
        return "Se teletransporta alrededor del jugador"