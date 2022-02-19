# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

# Your code below:
# Create a list called "toppings" to keep track of the kinds of pizzas you sell
toppings = [["Pepperoni"], ["Pineapple"], ["Cheese"], ["Sausage"], ["Olives"], ["Anchovies"], ["Mushrooms"]]
print(toppings)
# result: [['Pepperoni'], ['Pineapple'], ['Cheese'], ['Sausage'], ['Olives'], ['Anchovies'], ['Mushrooms']]

# Keep track of how much the pizza costs, create a list called prices, with the provided integer values
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)
# result: [2, 6, 1, 3, 2, 7, 2]

# Count the number of occurences of "2" in the "prices" list and store the result in a variable called "num_two_dollar_slices". Print.
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# result: 3

# Find the length of the toppings list and store in a variable called "num_pizzas"
num_pizzas = len(toppings)
print(num_pizzas)
# result: 7

# Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
print("We sell", num_pizzas, "different kinds of pizza!")
# result: We sell 7 different kinds of pizza!

# Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.
# Each sublist in pizza_and_prices should have one pizza topping and an associated price.
#For this new list make sure the prices come before the topping name
pizza_and_prices = [[2, "Pepperoni"], [6, "Pineapple"], [1, "Cheese"], [3, "Sausage"], [2, "Olives"], [7, "Anchovies"], [2, "Mushrooms"]]
print(pizza_and_prices)
#result: [[2, 'Pepperoni'], [6, 'Pineapple'], [1, 'Cheese'], [3, 'Sausage'], [2, 'Olives'], [7, 'Anchovies'], [2, 'Mushrooms']]

# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_and_prices.sort()
print(pizza_and_prices)
# result: [[1, 'Cheese'], [2, 'Mushrooms'], [2, 'Olives'], [2, 'Pepperoni'], [3, 'Sausage'], [6, 'Pineapple'], [7, 'Anchovies']]

# Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# result : [1, 'Cheese']

# A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
# Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# result: [7, 'Anchovies']

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()
print(pizza_and_prices)
# result: [[1, 'Cheese'], [2, 'Mushrooms'], [2, 'Olives'], [2, 'Pepperoni'], [3, 'Sausage'], [6, 'Pineapple']]

# Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. 
# Add the new peppers pizza topping to our list pizza_and_prices.
# Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!
pizza_and_prices.insert(4, [2.5, "Peppers"])
print(pizza_and_prices)

# result: [[1, 'Cheese'], [2, 'Mushrooms'], [2, 'Olives'], [2, 'Pepperoni'], [2.5, 'Peppers'], [3, 'Sausage'], [6, 'Pineapple']]

# Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
# Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizza_and_prices[:-3]
print(three_cheapest)
# result: [[1, 'Cheese'], [2, 'Mushrooms'], [2, 'Olives'], [2, 'Pepperoni']]
