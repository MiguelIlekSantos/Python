# while loop = a statement that will execute it's block of code,
# as long it's condition is true

name = ""

while len(name) == 0:
    name = input("What is your name: ")
    print("\tPlz write your name")

print("Hello " + name)