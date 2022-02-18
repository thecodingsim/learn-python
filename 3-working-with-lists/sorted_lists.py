#SORTING LISTS I | IN NUMERICAL OR ALPHABETICAL ORDER, 
# .sort(reverse=True) will sort list in a reverse order, descending

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
# sort the addresses
addresses.sort()
print(addresses)
#RESULT: ['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave', '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace']

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)
#The .sort() method does not return any value and thus does not need to be assigned to a variable. This is why we will see the value of None as our output for sorted_cities

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

#result: ['Rome', 'Paris', 'New York', 'Los Angeles', 'London']



# SORTING LIST II | BUILT IN FUNCTION

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)
