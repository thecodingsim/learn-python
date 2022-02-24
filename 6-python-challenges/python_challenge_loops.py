# DIVISIBLE BY TEN
 # A function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned.

def divisible_by_ten(nums): 
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count


print(divisible_by_ten([20, 25, 30, 35, 40]))

#In this solution, we defined the function and set up our counter. We use a for loop to iterate through each number and check if it is divisible by ten. If a number is divisible by another number then the remainder should be zero, so we use modulus. After the loop has finished, we return our count.

#------------------------------------------------------------------------

# Greetings

# You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name.

def add_greetings(names):
  new_list = []
  for name in names:
      new_list.append("Hello, " + name)
  return new_list

print(add_greetings(["Owen", "Max", "Sophie"]))

# RESULT: ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

#---------------------------------------

# DELETE STARTING EVEN NUMBERS
# Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed.

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# RESULT: [11, 12, 15]
[]

# After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions for the while loop to continue. We will keep iterating as long as there is at least one number left in the list len(lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. If both of these conditions are true, then we replace the list with every element except for the first one using lst[1:]. Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list.

# -----------------------------------------------------------------------

# ODD INDICES
#This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements.

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst 

print(odd_indices([4, 3, 7, 10, 11, -2]))

#RESULT: [3, 10, -2]
# In our solution, we iterate through a range of values. The function range(1, len(lst), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. This causes the loop to iterate through every odd number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

# Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd.

#------------------------------------------------------------------------
# EXPONENTS

# In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers.


def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))

# RESULT [2, 4, 8, 3, 9, 27, 4, 16, 64]
# As you can see in this solution, we used two nested for loops so that, for every base, we iterate through every power. This allows us to raise each base to every single power in our list and append the answers to our new list. Finally, we return the list of answers.




