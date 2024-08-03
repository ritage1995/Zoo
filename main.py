from Zoo import *
from Lion import *
from Elephant import *

#create un instanciation zoo
my_zoo = Zoo()

#create animals
lion = Lion("leo","Lion",3)
elephant = Elephant("ely","Elephant",4)
moneky = Moneky("moni","Moneky",8)

#add animal to list
my_zoo.add_animal(lion)
my_zoo.add_animal(elephant)

#print the animal list
print("Animals :")
for animal in my_zoo.list_animals():
    print(animal)
