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

#_________________________________________________________________________

# SORTING LIST II | BUILT IN FUNCTION

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)

#_________________________________________________________________________
#REVIEW | CHALLENGE



#Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.
#Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.
#First, how many items are in the warehouse?
#Save the answer to a variable called inventory_len.

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)
#result: 19

#Select the first element in inventory. Save it to a variable called first.
first = inventory[1]
print(first)
#result: twin bed

#Select the last element from inventory. Save it to a variable called last.
last = inventory[-1]
print(last)
#result: pillow

#Select items from the inventory starting at index 2 and up to, but not including, index 6.
#Save your answer to a variable called inventory_2_6.
inventory_2_6 = inventory[2:6]
print(inventory_2_6)
#result: ['headboard', 'queen bed', 'king bed', 'dresser']

#Select the first 3 items of inventory. Save it to a variable called first_3.
first_3 = inventory[:3]
#result: ['headboard', 'queen bed', 'king bed', 'dresser']

#How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.
twin_beds = inventory.count("twin bed")
print(twin_beds)
#result: 4

#Remove the 5th element in the inventory. Save the value to a variable called removed_item. *Since lists in Python of zero_indexed, the 5th element will be at index 4.
removed_item = inventory.pop(4)
print(removed_item)
#result: king bed

#There was a new item added to our inventory called "19th Century Bed Frame".
#Use the .insert() method to place the new item as the 11th element in our inventory.
inventory.insert(10, "19th Century Bed Frame")
print(inventory)
#result: ['twin bed', 'twin bed', 'headboard', 'queen bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', '19th Century Bed Frame', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

#Sort inventory using the .sort() method or the sorted() function.
#Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().
#Print inventory to see the result.

inventory.sort()
print(inventory)

#result: ['19th Century Bed Frame', 'dresser', 'dresser', 'headboard', 'king bed', 'king bed', 'nightstand', 'nightstand', 'pillow', 'pillow', 'queen bed', 'sheets', 'sheets', 'table', 'table', 'twin bed', 'twin bed', 'twin bed', 'twin bed']
# using sorted() you will get the same result. Make sure to inventory equals the value of sorted()
inventory = sorted(inventory)
print(inventory)





