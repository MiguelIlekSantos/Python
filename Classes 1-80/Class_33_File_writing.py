text = "\nYoooooooooo\nThis is some text\nHave a good day "

with open('hello','a') as file: # Must be written 'a' to write inside a file
    file.write(input("Whats your name: "))
