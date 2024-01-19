#reduce() = apply  a function to an iterable and reduce it to a single cumulative value
#                   performs function on first two element and repeats process until 1 value remains
#reduce (function, iterable)
import functools
letters = ["H","E","L","L","0"]

word = functools.reduce(lambda x,y: x+y,letters)
print(word)

factorials= [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorials)
print(result)