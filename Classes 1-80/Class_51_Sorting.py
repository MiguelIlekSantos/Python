# sort() = method = used with lists
# sorted() = function = used with iterables
'''
student = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

#student.sort()
sorted_student = sorted(student)

for i in sorted_student:
    print(i)
'''

students = (("Squidward", "F ",60),
                    ("Sandy","A",33),
                    ("Patrick","D",36),
                    ("Spongebob","B",20),
                    ("Mr.Krabs","C",78))

grades = lambda grade:grade[1]
#students.sort(key=grade)
students_sorted = sorted(students,key = grades)

for i in students_sorted:
    print(i)

