#duck typing = concept the classes of an object is less important than the methods/attributes
#                        class type is not checked if minimum methods/attributes are present
#                        "if it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This Duck is qwuacking")

class Chicken:

    def walk(self):
        print("This Chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person =Person()

person.catch(chicken)
