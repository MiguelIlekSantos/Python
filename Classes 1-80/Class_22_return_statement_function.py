#return statement = function send phyton values/ object back to the caller
#                       These value/object are known as the function's retuns vlaue

def multiply(number1,number2):
    result = number1 * number2
    return result

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
result = multiply(number1,number2)
print(result)