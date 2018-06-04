#Jan Lukas Strozyk
#05-24-2018
#Homework 2, Part 2
#Part 1 - Lists
# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['China', 'Russia', 'Tuvalu', 'The Holy See', 'Austria']
# 2) Using a for loop, print each element of the list
for i in countries:
    print(i)
# 3) Sort the list permanently.
countries_sorted = (sorted(countries))
# 4) Display the first element of the list.
print(countries_sorted[1])
# 5) Display the second-to-last element of the list.
print(countries_sorted[-2])
# 6) Delete one of the countries from the list using its name.
del_country = 'Russia'
countries_sorted.remove(del_country)
print(countries_sorted)
# 7) Using a for loop, print each country's name in all caps.
for i in countries_sorted:
    print(i.upper())
print("\n")
#Part 2 - Dictionaries
#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees
tree = {
    'age' : 249,
    'location_name' : 'Palo Alto, Ca.',
    'name' : 'El Palo Alto',
    'lat' : 37.44727,
    'long' : -122.17014
}
#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(tree['name'], "is", tree['age'], "years old and is located in", tree['location_name'])
print("\n")
#3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC
nyc = {
    'lat': 40.7128,
    'long': -74.0059
}
if nyc['lat'] > tree['lat']:
    print("New York City is north of", tree['name'], "in", tree['location_name'])
else:
    print("New York City is south of", tree['name'], "in", tree['location_name'])
print("\n")
#4) Ask the user how old they are...
user_age = input("How old are you? ")
user_age = int(user_age)
if user_age > tree['age']:
    print("You are", user_age-tree['age'],"years older than", tree['name'],".")
else:
    print("When you were born,", tree['name'], "was already", tree['age']-user_age, "years old.")
print("\n")

#Part 2 - List of dictionaries
#1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude.
cities = [
    {'name':'Moscow','lat':55.75, 'long':37.616667 },
    {'name':'Teheran', 'lat':35.689167, 'long':51.388889},
    {'name':'Falkland Islands', 'lat':-51.683333, 'long':-59.166667},
    {'name':'Seoul','lat':37.566667,'long':126.966667},
    {'name':'Santiago','lat':-33.45,'long':-70.666667},
]
# #2)  Loop through the list, printing each city's name and whether it is above or below the equator
for i in cities:
    if i['lat'] < 0:
        print(i['name'], "is south of the equator.")
    else:
        print(i['name'], "is north of the equator.")
    if i['name'] == 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")
print("\n")
# #3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
# #I made it east/west of the tree instead of north/south, because otherwise I would've searched for the 'long'-data for nothing :)
for i in cities:
    if i['long'] < tree['long']:
        print(i['name'], "is west of", tree['name'])
    else:
        print(i['name'], "is east of", tree['name'])
