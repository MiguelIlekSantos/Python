# logical operator (and, or) = used to check if two or more statement is true

temp = int(input("What is temperature outside: "))

if temp >= 0 and temp <= 30:
    print("Temperature is good today!")
    print("go outdside")
elif temp < 0 or temp >30:
    print("Temperature is not good today")
    print("Don't go outside")