from abc import ABC, abstractmethod

class Animal:

  #constructeur
  def __init__(self,name,species,age):
    self.name = name
    self.species = species
    self.age = age
    
  #methode sounds() is abstract so we import it
  @abstractmethod
  def make_sound(self):
    pass
