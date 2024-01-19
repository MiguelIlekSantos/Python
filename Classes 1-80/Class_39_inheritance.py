class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
         print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("Rabbit is running")

class Fish(Animal):

    def swim(self):
        print("Fish is Swimming")

class Hawk(Animal):

    def fly(self):
        print("Hawk is Flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.eat()
fish.swim()
hawk.fly()