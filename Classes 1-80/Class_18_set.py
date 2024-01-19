# Set = collection of code which os unordered , unindexed. no duplicate values

name = {"sabin","Radha","Rabi","Astha"}
age = {21,20,19,18,"Astha"}

name.add("ola")
name.remove("sabin")
name.update(age)   # mescla exceto se forem iguais
all = name.union(age)  # mescla tudo até valores iguais

print(str(age.union(name)))

print(age.difference(name))   # mostra todos que são diferentes
print(name.intersection(age))  # mostra todos que são iguais

for i in all:
   print(i)