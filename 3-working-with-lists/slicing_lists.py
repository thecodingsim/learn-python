
#SLICING LISTS I
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]

# Your code below: 
print(beginning)
#we get ['shirt', 'shirt', 'pants', 'pants']

#modifying beginning to select the first 2 elements of suitcase
beginning = suitcase[0:2]
#['shirt', 'shirt', 'pants', 'pants']

#create a new list called "middle", it should contain the middle two items from suitcase. Print middle.

middle = suitcase[2:4]
print(middle)
#['pants', 'pants']


#SLICING LISTS II

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

#RESULT
#['pajamas', 'books']

#create a new list, containing ALL, BUT the last three elements
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)
#RESULT
# ['shirt', 'shirt', 'pants']







