#Jan Lukas Strozyk
#5/21/2018
#Homework 1

userinput=input("What year were you born? ")
yearborn=int(userinput)
age=2018-yearborn

#check if input makes sense
if yearborn>2018 or yearborn<1890:
    userinput=input("That doesn't make sense. Please type in your real year of birth: ")
    yearborn=int(userinput)
    age=2018-yearborn

#print age
print("You are (approximately)",age,"years old.")

#compare heartbeats
print("\n""Your heart beat",age*365*24*60*75, "times if your life was a bit boring and around", age*365*24*60*100, "times if it was really exciting so far.")
print("At the same time, a blue whale's heart only beat",age*365*24*60*9, "times and a rabbit's heart beat",age*365*24*60*205, "times")
if age*365*24*60*205>1000000:
    print("That's", round(age*365*24*60*205/10000000, 2), "billion hearbeats for every rabbit that's your age!")

#Space Age!
print("\n""In Venus years, you are",round(age*365/224.7, 2),"years old. And if you were living on Neptun, your age would only be",round(age*365/60190, 2),"years.")

#Check if older or younger than me
if yearborn>1984:
    print("\n""You are",abs(yearborn-1984),"years younger than I, Jan, am.")
elif yearborn<1984:
    print("\n""You are",abs(yearborn-1984),"years older than I, Jan, am.")
elif yearborn == 1984:
    print("\n""You and I were born in the same year!")

#Check if year born is even or odd
if yearborn % 2 == 0:
    print("\n""Your birthyear is even.""\n")
else:
    print("\n""Your birthyear is odd, mathematically...""\n")

#Who ruled the US of A?
pres2 =""
presidents = [
    "Franklin D. Roosevelt",
    "Harry S. Truman",
    "Dwight D. Eisenhower",
    "John F. Kennedy",
    "Lyndon B. Johnson",
    "Richard Nixon",
    "Gerald Ford",
    "Jimmy Carter",
    "Ronald Reagan",
    "George H.W. Bush",
    "Bill Clinton",
    "George W. Bush",
    "Barack Obama",
    "Donald Trump"
]
if yearborn < 1934:
    print("An old man with a b/w picture on Wikipedia was POTUS when you were born...")
#years of double presidents below
elif yearborn == 1945:
    pres = presidents[0]
    pres2 = presidents[1]
elif yearborn == 1953:
    pres = presidents[1]
    pres2 = presidents[2]
elif yearborn == 1961:
    pres = presidents[2]
    pres2 = presidents[3]
elif yearborn == 1962:
    pres = presidents[3]
elif yearborn == 1963:
    pres = presidents[3]
    pres2 = presidents[4]
elif yearborn == 1969:
    pres = presidents[4]
    pres2 = presidents[5]
elif yearborn == 1974:
    pres = presidents[5]
    pres2 = presidents[6]
elif yearborn == 1977:
    pres = presidents[6]
    pres2 = presidents[7]
elif yearborn == 1981:
    pres = presidents[7]
    pres2 = presidents[8]
elif yearborn == 1989:
    pres = presidents[8]
    pres2 = presidents[9]
elif yearborn == 1993:
    pres = presidents[9]
    pres2 = presidents[10]
elif yearborn == 2001:
    pres = presidents[10]
    pres2 = presidents[11]
elif yearborn == 2009:
    pres = presidents[11]
    pres2 = presidents[12]
elif yearborn == 2017:
    pres = presidents[12]
    pres2 = presidents[13]
#Years of single presidents below
elif yearborn <= 1944:
    pres = presidents[0]
elif yearborn <= 1952:
    pres = presidents[1]
elif yearborn <= 1960:
    pres = presidents[2]
#Don't forget that Kennedy is dead!
elif yearborn <= 1968:
    pres = presidents[4]
elif yearborn <= 1973:
    pres = presidents[5]
elif yearborn <= 1976:
    pres = presidents[6]
elif yearborn <= 1980:
    pres = presidents[7]
elif yearborn <= 1988:
    pres = presidents[8]
elif yearborn <= 1992:
    pres = presidents[9]
elif yearborn <= 2000:
    pres = presidents[10]
elif yearborn <= 2008:
    pres = presidents[11]
elif yearborn <= 2015:
    pres = presidents[12]
#check if single or double, print accordingly
if len(pres2)>0:
    print("There were two presidents the year you were born.", pres, "and", pres2)
else:
    print(pres, "was POTUS the year you were born.")
