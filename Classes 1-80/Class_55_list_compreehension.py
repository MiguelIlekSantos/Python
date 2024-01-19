# list compreehension= a way to create a list with less syntax
#                                      can mimic certain lambda function, easier to read
#                                        list = [expreesion for an item in iterable]
square = []                     #creates a empty list
for i in range(1,11):       #create a for loop
    square.append(i * i)    #define what each loop iteration should do

print(square)

#list comprehension

squares=[i*i for i in range(1,11)]
print(squares)

'''
student = [100,90,80,70,60,50,40,30,0]

#passed_student = list(filter(lambda x:x >= 60, student))
passed_student = [i for i in student if i >= 60]
#passed_student = [i if i >= 60 else "Failed" for i in student]
print(passed_student)
'''