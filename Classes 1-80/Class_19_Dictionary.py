# dictionary = A changeable, unordered collection  of unique key:value pairs
#               fast because they use hashing, allows us to access a value quickly

capitals = {"USA": "washington DC",
                   "India":"New delhi",
                   "China":"Beijing",
                    "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las vegas"})
capitals.pop("China")
    #capitals.clear()

print(capitals["USA"])   # show value
print(capitals.get("Germany"))  # show key
print(capitals.keys())   # show all keys
print(capitals.values()) # show all values
print(capitals.items()) # show all


for key,value in capitals.items():
    print(key,value)
'''
idade  = {"idade" : "ola","idade2":"ola2"}

idade.update({"idade":input("escreve: "),"idade2": input("escreve: ")})

print(idade)
    '''
