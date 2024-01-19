#nested loop = the "inner loop" will finish all odd it's iteration s before finishing one iteration of "outer loop"

rows = int(input("How many rows: "))
colums = int(input("How many colums: "))

for i in range(rows):
    for j in range(colums):
        print("@",end="")
    print()