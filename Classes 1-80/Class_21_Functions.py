#function = is a block of code which is only executed when it is called

def hello(name, last_name,  age):
    print("Hello "+ name + last_name)
    print("You are "+ str(age)+ " years old")
    print("Have a nice day")

name = "Sabin"
last_name = "Baral"
age = 21
hello(name, last_name, age)