#tuple = collechition of code wch is ordered and unchangeable
# used to group together related data

# diferença não pode ser alterado

student = ("Sabin", 21, "male")

print(student.count("Sabin"))
print(student.index("male"))

for x in student:
    print(x,end=" ")

if "Sabin" in student:
    print()
    print(str(student[1])+" is Here")


