class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
         return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def animal_speak(animal_list):
    for animal in animal_list:
        print(animal.speak())

##############################################################

animals = [Dog(), Cat(), Cow()]
animal_speak(animals)
print()
