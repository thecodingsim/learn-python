# TENTH POWER
# Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number.

def tenth_power(num):
  return num ** 10


print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# The first line is the function header which uses def to define the function followed by the function name. Within the parentheses we include num which is our formal parameter. Because of this, num is the variable name for the value we pass into this function.

# On our next line, we use return to show that this function is going to return a value when it is called. Next to the return keyword, we define what value is going to be returned. Since we need the tenth power of our input value, we can use the power operator in python which is **. Using this knowledge, in order to get the tenth power of our input value, we use num ** 10.

#----------------------------------------------------------------------

# SQUARE ROOT
# Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. 

def square_root(num):
  return num ** 0.5


print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# As you can see, this solution is very similar to the last problem. In this case, the only changes we need are the function name and changing the power value to 0.5. We define the function called square_root with one parameter. We then take the one half power of the input value which is mathematically the same as taking the square root and return it.

#-------------------------------------------------------------------------------

# WIN PERCENTAGE
#Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). 

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100


print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# First, we defined our function with two parameters, one for games won and one for games lost. Next, we calculated the total number of games using the number of wins + losses. After that, we use calculate the ratio of wins out of the total number of games by dividing wins by our total_games variable. Since this gives us a ratio and we want it in percentage form, we multiply the answer by 100 and return it.

#--------------------------------------------------------------------------

# AVERAGE
#Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two.

def average(num1, num2):
  return (num1 + num2) / 2


print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

#In this solution, we defined the function with two parameters one line and returned the average on the next line. When returning the value, we used parentheses around the addition to cause the two numbers to be added together first before dividing by two.

#-----------------------------------------------------------------------

#REMAINDER
#For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder.

def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# Our solution It shortened to use only two lines of code. The first line defines the function with two input parameters. The second line performs the two mathematical operations on either side of the modulus within parenthesis. This causes the two calculations to be performed before taking the remainder of the left side divided by the right side.

#---------------------------------------------------------------------


# ADVANCED
# First three multiples
#Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number.

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3



# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# In this solution, we start by defining the function header with an input. We then use the next three lines to print the result of multiplying the input value by one, two, and three. Finally, we return the result of multiplying the input value by 3.

#-----------------------------------------------------------------------

# TIP
# Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. 

def tip(total, percentage):
  return (total * percentage) / 100
  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# In this solution, we defined the function with two parameters and then used them to calculate the tip amount. We multiplied the input values together and divided by 100 since the second input is in percentage form and we want a monetary amount. Lastly, we returned the calculated tip value.

#-----------------------------------------------------------------------------

# BOND, JAMES BOND
#It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs. 

def introduction(first_name, last_name):
  return last_name + "," + " " + first_name + " " + last_name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# First, we defined the method to accept the first and last names. On the next line, we performed all of the concatenations at once by adding the comma, spaces, and names in the correct order. We also returned the result on the same line.

#-----------------------------------------------------------------------------

# DOG YEARS 
#Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age.

def dog_years(name, age):
  return name + ", you are " + str(age * 7) + " years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# In this solution we used two lines of code to accomplish this task. The first line defines the function with the two inputs and the second line concatenates the string while also performing the calculation. We used str(age * 7) to convert the number to a string, and since that function call returns a string, we can concatenate it in-line with the rest of the string.

#-----------------------------------------------------------------------------

# All operations
#For the final code challenge, we are going to perform multiple mathematical operations on multiple inputs to the function. We will begin with adding the first two inputs, then we will subtract the third and fourth inputs. After that, we will multiply the first result and the second result. In the end, we will return the remainder of the previous result divided by the first input. We will also print each of the steps.

def lots_of_math(a, b, c, d):
  sum_a_b = a + b
  diff_c_d = c - d
  mul_a_b = sum_a_b * diff_c_d
  e = mul_a_b % a
  print(sum_a_b)
  print(diff_c_d)
  print(a * b)
  return e

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

# After defining the function, we store each result into its own variable for first and second. We then use these two variables in the calculation for third and we use the value of third to get fourth. Afterwards, we print the first three variables and return the fourth one.

