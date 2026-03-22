from pico import Pico
from espada import Espada
from pala import Pala
from arco import Arco

if __name__ == "__main__":
    herramientas = [
        Pico("Diamante", 5),
        Espada("Hierro", 3),
        Pala("Madera",2),
    ]

    objetivos = ["mena de diamante", "Creeper", "Arena"]

    for h,obj in zip(herramientas, objetivos):
        #Bucle hasta que se rompa
        while not  h.rota:
            print(h.usar(obj))
            h.estado()
            print()