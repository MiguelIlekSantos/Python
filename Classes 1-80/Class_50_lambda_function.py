'''
lambda function = function written in 1 line using lambda keyword
                                accepts any number of arguments, but only has one expression.
                                (think of it' as a shortcut)
                                (useful if needed for a short period of time, throw-away)

lambda parameters:expression
'''

double = lambda x:x*2
multiply = lambda  x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check= lambda age:True if age >=18 else False

print(double(5))
print(multiply(4,3))
print(add(2,4,5))
print(full_name("Sabin","baral"))
print(age_check(15))


int = lambda x,y:x*y

print(int(2,3))

