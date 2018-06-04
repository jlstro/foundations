# Jan Lukas Strozyk
# 05-28-2018
# HOMEWORK 3
# PART ONE: Lists
numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]
# 1) Count how many numbers are in the list. Use a for loop, do NOT use len.
n = 0
for num in numbers:
    n = n+1
print("There are", n, "numbers in the list.")
# 2) Use a Python method to add a new number to the list. You can pick the number!
numbers.append(21)
print(numbers)
# 3) Count how many even numbers are in the list. Use a for loop.
n = 0
for num in numbers:
    if num % 2 == 0:
        n = n+1
print("There are", n, "even numbers in the list.")
# 4) Count how many values are above the mean and how many are below the mean. Use one for loop.
import statistics
n = 0
for num in numbers:
    if num > statistics.mean(numbers):
        n = n+1
print("The mean is", round(statistics.mean(numbers),2), "and there are", n, "numbers above the mean.")
# 5) Total up the numbers. Use a for loop, do NOT use sum().
n = 0
for num in numbers:
    n = n+num
print("The sum of all numbers is", n)
# 6) Total up the numbers that are above the mean, and total up the numbers below the mean. Use one for loop, and do not use sum().
hi = 0
lo = 0
for num in numbers:
    if num > statistics.mean(numbers):
        hi = hi+num
    else:
        lo = lo+num
print("The numbers above the mean add up to", hi, "and the numbers below the mean add up to", lo)
# 7) Find the largest number. Use a for loop.
n = 0
for num in numbers:
    if num > n:
        n = num
print("The largest number ist", n)
# 8) You have a list of dogs, shown below. BUT YOU GOT ANOTHER DOG!!! His name is Maxwell, please add him to the list.
dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
dogs.append("Maxwell")
print(dogs)
# 9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.
dogs_short =[]
for dog in dogs:
    if len(dog) < 6:
        dogs_short.append(dog)
print(dogs_short)

# 10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH (no, it isn't a real URL). Bern is another canton - its abbreviation is BE, so its URL is http://important-swiss-things.ch/docs/download/BE.
# I want to get this kind of link for every single canton in Switzerland, not just Zurich and Bern, but I don't want to type each URL manually. If I give you this list of the canton abbreviations, can you print out all of the URLs?
cantons = [
"ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG","TG", "TI", "VD", "VS", "NE", "GE", "JU"
]
url = "http://important-swiss-things.ch/docs/download/"
for can in cantons:
    print(url+can)
# 11) I'm trying to get some top-secret documents from top-secret-secrets.com, and I know the URL pattern but I don't want to type them all out individually! Programmers are lazy, remember?
url = "www.top-secret-pdfs.com/content/secrets/"
codes = [
"qq7lthm",
"jemsqhg",
"O6itcke",
"cp4Iua0",
"bkijcmo",
"ctoyjrm",
"z8wc6xy",
"zk4Bmm0",
]
for code in codes:
    n = 1
    while n < 13:
        print(url+str.upper(code)+"/page/"+str(n).zfill(3)+".pdf")
        n = n+1



# PART TWO: Dictionaries
#
# Dictionaries are super useful and you use them all of the time, but I wouldn't say there are very many 'tricks' like there are with lists. Most of the time you just want to put things in and take things out using keys.
#
# 1) Let's say we are terrible doctors and we have a patient. Define a dictionary called patient that works with the following code.
#

patient = {
    'name' : "Carol",
    'complaint' : "headache",
}
print("Doctor, it looks like the patient named", patient['name'], "is complaining about", patient['complaint'])
#
# 2) We aren't really listening to their complaint, but as more test results come in, we'll add these things to the patient's record. Add the following to the patient dictionary:
patient.update({
    'heart_rate' : 70,
    'temperature': 98.6,
    'infection': False
})
# 3) Now let's be doctors! Diagnose the patient, and store your diagnosis in a key called diagnosis:
#
#     If their temperature is above 102 but they do not have an infection, they have heat stroke.
#     If they have a temperature above 102 and they have an infection, they have the flu.
#     If they have an infection but a normal temperature, it's probably a cold.
#     If none of the above, tell them to take an aspirin and call you in the morning.
#
# When you are finished diagnosing the patient, display "Your diagnosis is _______."

# if patient['temperature'] > 102:
#     if patient['infection'] == True:
#         patient.update({'diagnosis' = "the flu"})
#     else:
#         diagnosis = "heat stroke"
# elif patient['infection'] == True:
#     diagnosis = "a cold"
# else:
#     diagnosis = "aspirin"

temperature = 101
infection = "No"
if temperature < 102:
    if infection != "No":
        print("blah")
    else:
        print("blubb")
else:
    print("blib")
# if diagnosis != "aspirin":
#     print("Your diagnosis is", diagnosis)
# else:
#     print("Please take an aspirin and call in the morning.")

# 4) Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an infection or not (this will be a list of dictionaries). Use a for loop to diagnose each of them.

patients = [
    {
    'name' : "Adam",
    'complaint' : "sore throat",
    'heart_rate' : 91,
    'temperature': 106,
    'infection': True
    },
    {
    'name' : "Jennifer",
    'complaint' : "stomach ache",
    'heart_rate' : 68,
    'temperature': 100,
    'infection': False
    },
    {
    'name' : "LeBron",
    'complaint' : "shoulder pain",
    'heart_rate' : 50,
    'temperature': 89.9,
    'infection': False
    }
]
for patient in patients:
    if patient['temperature'] > 102:
        if patient['infection'] == True:
            diagnosis = "the flu"
        else:
            diagnosis = "heat stroke"
    elif patient['infection'] == True:
        diagnosis = "a cold"
    else:
        diagnosis = "aspirin"

    if diagnosis != "aspirin":
        print("Hello", patient['name']+", your diagnosis is", diagnosis)
    else:
        print("Hello", patient['name']+", Please take an aspirin and call in the morning.")


# PART THREE: Reading CSV files
import csv
csvfile = open('/home/jls/Dokumente/Lede/foundations/Homework/Day-3-optional/countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()
for country in data:
    country['Population'] = int(country['Population'])
    country['GDP_per_capita'] = float(country['GDP_per_capita'])
print("The data looks like", data)
# When you run this code, it will open up a file and convert it into a list of dictionaries. Each row becomes a dictionary, and each column becomes a key. Not sure what I mean? Look at what we print out, or try to use a for loop to print out each row.
for country in data:
    print(country)

# 1) What are the columns in our dataset?
for column in data[0]:
    print(column)
# 2) How many countries do we have in our dataset?
print(len(data))
# 3) How many countries in Asia? How about North America?
Asia_countries = [country for country in data if country['Continent'] == 'Asia' ]
print("There are", len(Asia_countries), "countries in Asia.")
n_am_countries = [country for country in data if country['Continent'] == 'N. America']
print("There are", len(n_am_countries), "countries in North America.")
# 4) What is the total population of the world?
total_pop = sum([int(country['Population']) for country in data])
print("The total population is", round(total_pop/1000000000, 2), "billion")
# 5) Which has a larger population, Africa or South America?
s_am_countries = [country for country in data if country['Continent'] == 'S. America']
s_am_pop = sum([int(country['Population']) for country in s_am_countries])
africa_countries =[country for country in data if country['Continent'] == 'Africa']
africa_pop = sum([int(country['Population']) for country in africa_countries])
if africa_pop < s_am_pop:
    print("The population of South America is larger than the population of Africa.")
else:
    print("The population of Africa is larger than the population of South America.")
# 6) Calculate the total GDP of each country and print it out (right now it's per capita).

for country in data:
    gdp = int(country['GDP_per_capita'])*int(country['Population'])
    print(country['Country'], "has a GDP of:", gdp)

total_gdp_per_capita = sum([int(country['GDP_per_capita']) for country in data])
total_gdp = total_gdp_per_capita * total_pop
print("The total worldwide GDP is", round(total_gdp/1000000000000, 2), "trillion")
# 7) What is the median life expectancy of the world?
median_life = statistics.median([float(country['life_expectancy']) for country in data])
print("The median world wide life expectancy is", round(median_life, 2))
# 8) What is the median life expectancy of Europe?
median_life_eu = statistics.median([float(country['life_expectancy']) for country in data if country['Continent'] == 'Europe'])
print("The median life expectancy for Europe is", round(median_life_eu, 2))
# 9) Print out each country that has a below-average life expectancy.
below_av_life = [country['Country'] for country in data if float(country['life_expectancy']) < median_life]
print("These countries have a life expectancy below average:\n"+"\n".join(below_av_life))
# 10) Print out each country that has a below-average GDP but an above-average life expectancy.
median_gdp_capita = statistics.median(int(country['GDP_per_capita']) for country in data)

above_av_life = [country['Country'] for country in data if country['Country'] not in below_av_life]

below_av_gdp = [country['Country'] for country in data if float(country['GDP_per_capita']) < total_gdp_per_capita/len(data)]

below_gdp_above_life = [country['Country'] for country in data if country['Country'] in above_av_life and float(country['GDP_per_capita']) < median_gdp_capita]

print("These countries have an below average GDP and an above average life expectancy:\n"+"\n".join(below_gdp_above_life))

# 11) Calculate the 75th percentile of GDP.
# This is close enough to the actual answer for me today...
gdp_list = [int(country['GDP_per_capita']) for country in data]
gdp_list = sorted(gdp_list)

if len(data) %4 == 0:
    perc75 = (gdp_list[round(len(data)*.75)] + gdp_list[round(len(data)*.75)+1]) / 2
else:
    perc75 = gdp_list[round(len(data)*.75)]
print("The per capita GDP's 75th percentile is", round(perc75,2))
# 12) What percent of the world population has a life expectancy of below 50 years? Above 80 years?
countries_below_50 = sum([int(country['Population']) for country in data if float(country['life_expectancy']) < 50])
countries_above_80 = sum([int(country['Population']) for country in data if float(country['life_expectancy']) > 80])
print(round(countries_above_80/total_pop*100, 2), "per cent of the population have a life expectancy of 80 or more and ", round(countries_below_50/total_pop*100, 2), "per cent of the population have a life expectancy of less than 50.")
