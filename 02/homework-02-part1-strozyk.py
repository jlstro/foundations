#Jan Lukas Strozyk
#5-23-2018
#Homework 2, Part 1
#Part One: Lists
# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
nums = [22, 90, 0, -10, 3, 22, 48]
#Display the number of elements in the list.
print(len(nums))
#Display the 4th element of this list.
print(nums[3])
#Display the sum of the 2nd and 4th element of the list.
print(nums[1] + nums[3])
#Display the 2nd-largest value in the list.
#I stole this and don't really know how it works but it looks really smart. Another option would be to sort into a new list and then print [1] of that list.
print(max(i for i in nums if i != max(nums)))
#Display the last element of the original unsorted list
print(nums[-1])
#Display the sum of all of the numbers divided by two.
print(sum(nums)/2)
print("\n")
#Print whether the median or the mean of the numbers is higher
import statistics
if statistics.mean(nums) > statistics.median(nums):
    print("The mean is larger then the median")
else:
    print("The median is larger then the mean  ")
print("\n")
#Part One: Dictionaries
#Define a dictionary called movie that works with the following code(...)
movie = {
    'title': "Brust oder Keule",
    'year': "1976",
    'director': "Claude Zidi",
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
print("\n")
#On the lines after that, add keys to the movie dictionary for budget and revenue
#I made these figures up, could not find any info online...
movie['budget'] = 300000
movie['revenue'] = 1250000
print(abs(movie['budget']-movie['revenue']))
print("\n")
#If the movie cost more to make than it made in theaters, print "That was a bad investment"(...)
if movie['budget'] > movie['revenue']:
    print("That was a bad investment!")
elif movie['budget'] < movie['revenue']/5:
    print("That was a great investment!")
elif movie['budget'] < movie['revenue']:
    print("That was an OK investment!")
print("\n")
#Make ONE dictionary that describes the population of the boroughs of NYC.
boros = {
    'manhattan':1.6,
    'brooklyn':2.6,
    'bronx':1.4,
    'queens':2.3,
    'staten':0.47
}
#Display the population of Brooklyn.
print("The population of Brooklyn is", boros['brooklyn'], "million.")
#Display the combined population of all five boroughs.
print("The population of all 5 boroughs is", (sum(boros.values())), "million")
#Display what percent of NYC's population lives in Manhattan.
manhattan_perc = 100*round(boros['manhattan']/(sum(boros.values())),4)
print(manhattan_perc,"per cent of all New Yorkers live in Manhattan.")
