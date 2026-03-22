from guerrero import Guerrero
from mago import Mago
from arquero import Arquero

#crear objetos 
guerrero = Guerrero("Wilson", 10,"Espada")
arquero = Arquero("Charlie", 20, 45)
mago = Mago("Ozz", 40, "Hechizo de agujas")

#usar metodos
guerrero.presentarse()
guerrero.usar_habilidad()
print("Habilidad de leon")

mago.presentarse()
mago.usar_habilidad()
print("Habilidad de Hechizo")

arquero.presentarse()
arquero.usar_habilidad()
print("Habilidad a larga distancia")