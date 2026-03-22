from abc import ABC, abstractmethod

#Clase abstracta (olantilla)

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass # No se complementa el metodo

#Clase en especifico

class Perro(Animal):
        
    def hablar(self):
        return "¡Guau!"
    
#Clase en especifico
 
class Gato(Animal):
    def hablar(self):
         return "¡Miau!" 

#Usar las clases
perro = Perro()
gato = Gato()
print (perro.hablar()) #¡Guau!
print (gato.hablar()) #¡Miau!