from comida import Comida
from bebida import Bebida
from postre import Postre


comida = Comida("Chilaquiles", 100.00, "Plato fuerte")
bebida = Bebida("Limonada Rosa", 45.00, "Helada")
postre = Postre("Pan de platano", 25.00, False)

comida.mostrar_info()
comida.tipo()
print()

bebida.mostrar_info()
bebida.tipo()
print()

postre.mostrar_info()
postre.tipo()