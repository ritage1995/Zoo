class Animal:

  #constructeur
  def __init__(self,name,species,age):
    self.name = name
    self.species = species
    self.age = age
    
  #methode sounds()
  def make_sound(self):
    return f"sounds of {self.name} "
