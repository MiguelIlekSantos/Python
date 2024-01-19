#******************************************
#if __name__ == '__main__'
#******************************************

# y tho?
#1. Module can be run as a standalone  program
#                                   or
#2. Module can be inported by used by other modules

#   Phyton interpreter sets "special variables", one of which is __name__
#   Phyton will assign the __name__ variable a value of '__main__' if it's
#   The initial module being run

# used to detect if the module is being used diretcly or being imported

def main():
    print("Hello")

if __name__ == '__main__':
    main()
