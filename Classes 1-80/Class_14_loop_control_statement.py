#loop control statement = change a loops execution from its normal sequence

# break=  used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("What is your Name: ")
    if name != "":
        break
phone_number = "123-456.789"

for i in phone_number:
    if i == "-" or i == ".":
        continue
    print(i, end="")

print("\n")
for i in range(1,11):
    if i == 10:
        pass
    else:
        print( i, end="") # isso faz com que não quebre linhas no final