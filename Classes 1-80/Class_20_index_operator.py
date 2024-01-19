# index operator [] = gives access to a sequence's element's element (str,list, tuples)

name = "sabin baRal!"

if (name[0].islower()):
    name = name.capitalize()

first_name = name[0:6].upper()
last_name = name[6:].lower()
last_caracter = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_caracter)