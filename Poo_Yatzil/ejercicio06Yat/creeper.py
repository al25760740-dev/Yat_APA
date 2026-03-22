from mob import Mob

class Creeper(Mob):
    """Mob agresivo, suena '...Sssss', Camina rapido hacia el jugador"""
    # TODO: implementa hacer_sonido, comportamiento, moverse

    def hacer_sonido(self) -> str:
        return "...Sssss"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Camina rapido hacia el jugador"