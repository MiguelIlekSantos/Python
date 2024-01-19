#exception = events detected during execution that interrupt the floe of the programme

try:
    numerator = int(input("Enter the number to divide: "))
    denominator  = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by Zero !! Idiot")
except ValueError as e:
    print(e)
    print("A carcter cannot de divided or divide! You idiot")
except Exception as e:
    print(e)
    print("Something went wrong : (")
else:
    print(result)
finally:
    print("Always Executed")
