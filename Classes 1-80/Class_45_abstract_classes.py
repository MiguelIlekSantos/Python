#Prevents a user from creating an object of that class
# + compels a user to override abstract method in a child class

# abstract class = a class which contains one or more abstract methods
# abstract methods = a method that has a declaration bit does not have a implementation.
from abc import ABC, abstractmethod

class Vechile(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):

    def go(self):
        print("You are in a Car")

    def stop(self):
        print("Car is stopped")

class Motorcycle(Vechile):
    def go(self):
        print("I am riding a motorcycle")
    def stop(self):
        print("Motorcycle is stopped")

car = Car()
motorcycle = Motorcycle()

motorcycle.go()
car.go()
motorcycle.stop()
car.stop()