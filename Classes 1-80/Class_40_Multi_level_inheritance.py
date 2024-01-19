#multi-level inheritance = when a derived (child) class inherits another derived (Child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is Eating")

class Dog(Animal):
    def bark(self):
        print("This Dog is barking")

dog = Dog()
print(dog.alive)      #inherits from organism Class
dog.eat()                 #inherits from Animal Class
dog.bark()                #Inherits from Dog Class