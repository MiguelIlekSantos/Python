# if statement = a block of a code that will only execute when it's condition is true

age = int(input("How old are you: "));

if age > 18:
    print("You are old enough to drive a car")
elif age ==18:
    print("You just turned 18 you cant drive")
elif age <= 0:
    print("You are not Born yet")
else:
    print("You are not old enough to drive a car")