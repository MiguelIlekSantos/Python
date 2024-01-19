# str.format = optional method gives user
#                        more control when displaying output

'''
animal = "cow"
item =  "moon"

#print("The "+ animal + " jumped over the "+ item)

#print("The {} Jumped over the {}".format(animal, item))
#print("The {0} Jumped over the {1}".format(animal, item)) #positonal arguments
#print("The {animal} Jumped over the {item}".format(animal="cow", item="moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal,item))
'''

##   padding in string

name = 'Sabin'

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))


## formating munber in string

number = 1000
print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))  # 1,000
print("The number is {:o}".format(number))  #octal
print("The number is {:X}".format(number))  #hexadecimal
print("The number is {:b}".format(number))  #binário
print("The number is {:E}".format(number))  #científico
