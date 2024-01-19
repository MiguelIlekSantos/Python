# *args = parameter that will pack all the arguments into a tuple
#               useful so that a function can accept a varying amount of parameter



def summer(*summ):
    sum = 0
    summ = list(summ)
    summ[0]= 0
    print(summ)
    for i in summ:
        sum += i
    return sum

ola, ola2,ola3 = 1,2,3
print(summer(ola,ola2,ola3))  # cria um tuple dessas variavéis