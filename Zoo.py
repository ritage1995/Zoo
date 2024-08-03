class Zoo:
  
  #constructeur
  def __init__(self):
    self.animals = []

  #methode add
  def add_animal(self,animal):
    self.animals.append(animal)

  #methode add
  def remove_animal(self,name):
    self.animals = [animal for animal in self.animals if animal.name != name]
