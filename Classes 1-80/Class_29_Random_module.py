import random


x= random.randint(1,6)
y = random.random()  # valor aleatório float entre 0 e 1

mylist = ["Scissors","Rock","Paper"]
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)  # embaralhar
print(cards)