# kwargs  = parameter that will pack all arguments into a dictionary
#                   useful so that a function can accept a varying amont of keyword arguments
# kwargs = key words arguments
def printer(**kwargs):
    #print("Hello "+ kwargs['first']+ " " + kwargs['middle'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")

printer(first = "Sabin",middle = "lol", last = "Baral")




