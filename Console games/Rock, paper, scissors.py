import random

game = True

vector = ['','rock', 'scissors', 'paper']

for i in range(1,4):
    print(i,"-", vector[i])

while game := input("If Do you wanna play digit 1 : ") == "1":
    player = int(input("Choose : "))
    computer = random.randint(0,2)
    if computer == player:
        print("Empate")
    elif computer == 1 & player == 2 | computer == 2 & player == 3:
        print("Computer wins")
    else:
        print("Player wins")




