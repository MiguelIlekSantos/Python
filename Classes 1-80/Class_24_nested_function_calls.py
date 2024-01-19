# nested function calls  = functions calls inside other functions calls
#                                         innermost function are called or resolved first
#                                         returned values is used as arguments for the next outer function

'''
num = input("Enter a whore positive number")
num = float(num)
num = abs(num)
num = round(num)
print(num)
'''

print(round(abs(float(input("Enter a whore positive number: ")))))