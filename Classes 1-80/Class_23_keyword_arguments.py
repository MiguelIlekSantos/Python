# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                                       The Order of the arguments doesn't matter, unlike positional arguments
#                                       Phyton knows the name of the arguments that ours functions receives

def name_printer(name,middle,last):
    print("Hello " + name + " " + middle + " " + last)

first_name = input("What is your First_Name: ")
middle_name =  input("What is your middle_Name: ")
last_name = input("What is your last_Name: ")


name_printer(name=first_name,last=last_name,middle=middle_name)