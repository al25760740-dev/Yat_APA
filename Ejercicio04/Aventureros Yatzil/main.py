from guerrero import Guerrero
from mago import Mago
from arquero import Arquero

#crear objetos 
guerrero = Guerrero("Wilson", 10,"Espada")
arquero = Arquero("Charlie", 20, "Flechas")
mago = Mago("Ozz", 40, "Hechizo de agujas")

#usar metodos
guerrero.presentarse()
guerrero.usar_habilidad()
print("Habilidad de Leon")

mago.presentarse()
mago.usar_habilidad()
print("Habilidad de Hechizo")

arquero = Arquero("7t")