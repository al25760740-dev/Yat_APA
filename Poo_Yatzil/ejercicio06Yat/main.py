# Generar las instancias para cada mob, y mostrar su sonido, comportamiento y forma de moverse.

from vaca import Vaca

vaca = Vaca("Vaca", 10)
vaca.presentarse()

from creeper import Creeper

creeper = Creeper("Creeper", 20)
creeper.presentarse()

from enderman import Enderman

enderman = Enderman("Enderman", 40)
enderman.presentarse()

from aldeano import Aldeano

aldeano = Aldeano("Aldeano", 15)
aldeano.presentarse()
