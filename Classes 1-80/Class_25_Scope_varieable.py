#Scope = The region that a varieble is recognized
#               A varieable is onlu available fron inside the region is's is created.
#                A global varieable is locally scopped version of a varieable can be created

name =  "ola" # Global scope (available inside and outside function's)
def display_name():
    name = 'ol' # local scope (only available inside the function)
    print(name)

display_name()
print(name)