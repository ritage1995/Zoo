from abc import ABC, abstractmethod

# abstract class we make ABC and we import it from abc
class Animal(ABC):

  #constructeur
  def __init__(self,name,species,age):
    self.name = name
    self.species = species
    self.age = age
    
  #methode sounds() is abstract so we import abstractmethod
  @abstractmethod
  def make_sound(self):
    pass
