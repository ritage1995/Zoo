class Zoo:
  
  #constructeur
  def __init__(self):
    self.animals = []

  #methode add
  def add_animal(self,animal):
    self.animals.append(animal)

  #methode remove
  def remove_animal(self,name):
    self.animals = [animal for animal in self.animals if animal.name != name]

  #method list
  def list_animals(self):
    return [f"{animal.name} the {animal.species}" for animal in self.animals]

  #method make sounds
  def make_all_sounds(self):
    return [animal.make_sound() for animal in self.animals]
  
