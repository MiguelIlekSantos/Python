class Car:
    def turn_on(self):
        print("Engine is starting")
        return self

    def drive(self):
        print("Driving the Car")
        return self

    def brake(self):
        print("Opps!! Steps on the Brake")
        return self

    def turn_off(self):
        print("Engine Off")
        return self

car = Car()
'''
car.turn_on().drive()
car.brake().turn_off()
'''
(car.turn_on()
 .drive()
 .brake()
 .turn_off())
