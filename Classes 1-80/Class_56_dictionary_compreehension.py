# dictoinary compreehension = create dictionaries using  an expression
#                                                      can replace for loops and certain lambda functions

# dictionary = {key: expression for (key value) in iterable}
#dictionary = {key: expression for (key,value) in iterable id conditional}
#dictionary = {key: (if/else) for (key,value) in iterable}

#-------------------------------------------------------------------------------------------------

#cities_in_F = {'Newyork':32, 'Boston':75, 'los Angelos':100, 'Chicago':50}
#cities_in_c = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_c)


#-------------------------------------------------------------------------------------------------

#weather = {'Newyork':"Snowing", 'Boston':"sunny", 'los Angelos':"sunny", 'Chicago':"cloudy"}

#sunny_weather = {key : value for (key,value) in weather.items() if value == "sunny"}
#print(sunny_weather)

#-------------------------------------------------------------------------------------------------

#cities = {'Newyork':32, 'Boston':75, 'los Angelos':100, 'Chicago':50}
#desc_cities = {key: ("Warm"if value >=40 else "Cold") for (key,value) in cities.items()}
#print(desc_cities)

#-------------------------------------------------------------------------------------------------

def check_temp(value):

    if value >= 70:
        return "Hot"
    elif 69 >= value >=40:
        return ("Warm")
    else:
        return "Cold"

cities = {'Newyork':32, 'Boston':75, 'los Angelos':100, 'Chicago':50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)
