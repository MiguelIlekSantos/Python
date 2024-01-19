# zip (*iterables) = aggregate elements from two or more iterables(list, tuple, etc..)
#                                creates a zip object with paired element stored in tuples for each element

username = ["Sabin", "Suii","Minister"]
password = ("p@ssword", "abc123","guest")
login_date = ["1/1/2021", "1/2/2021","1/3/2022"]

users = zip(username,password,login_date)

for i in users:
    print(i)