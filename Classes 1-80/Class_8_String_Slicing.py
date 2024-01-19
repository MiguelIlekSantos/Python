# slicing  =  create a substracting by extracting element from another string
# indexing[] or slice[]
# [start:stop:step]

name = "Sabin Baral"
#first_name =  name[0:5]
#second_name = name[6:11]
sliced_name= name[::3]  # de tres em tres
reverse_name = name[::-1]  # de tras para frente

#print(first_name)
#print(second_name)
print(sliced_name)
print(reverse_name)

website = "https://google.com"
website2 = "https://wordlegame.org"

slice = slice(10, -4)

print(website[slice])
print(website2[slice])