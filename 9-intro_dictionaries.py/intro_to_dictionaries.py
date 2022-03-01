# dictionary is an unordered set of key: value pairs. It maps pieces of data together so that we can quickly find values that are associated with each other
# dictionary called "menu" to store data, usually ends with curly braces {}
# menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#it will include a variable = {"key": value} and each separated by a comma. The keys can be numbers too.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

#result: {'living room': 21, 'kitchen': 23, 'bedroom': 20, 'pantry': 22}

#-------------------------------

#you can use a string, number, list, or another dictionary as a value associated with a key
#students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

# also mix and match key and value types:
#person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

#dictionary that maps the words in english to their definitions in Sindarin.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

#-----------------------------

#Invalid keys
#we cannot use data types as keys: list/value. if you try you will recieve an error
# ex: powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} 
# result: TypeError: unhashable type: 'list'
# unhashable means that this list is an object that can be changed.
# Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.


children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

#----------------------------

# empty dictionary
# dictionaries don't have to contain anything, sometimes we need an empty one to fill it later
# empty_dict = {}

#--------------------------------------------------

#adding a key to a dictionary
#dictionary[key]= value
# example: menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# menu["cheesecake"] = 8
# result: {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

animals_in_zoo = {"zebras": 8, "monkeys": 12, "dinosaurs": 0}
print(animals_in_zoo)

#result: {'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}

#---------------------------------

#add multiple keys
# .update() to add multiple key : value pairs at once
# example: sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
# result: {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#result: {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

#------------------------------

#overwrite values
#menu["avocado toast"] = 7
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# menu["oatmeal"] = 5
# print(menu)
#result: {"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners.update({"Supporting Actress": "Viola Davis"})
#print(oscar_winners)

oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

#result: {'Best Picture': 'Moonlight', 'Best Actor': 'Casey Affleck', 'Best Actress': 'Emma Stone', 'Animated Feature': 'Zootopia', 'Supporting Actress': 'Viola Davis'}

#--------------------------------

# Dict comprehensions
# zip()
# combine two lists into a dictionary
#names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# heights = [61, 70, 67, 64]
# students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
#dictionary
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)

#result: {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}








