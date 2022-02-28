hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

total_revenue = 0

#- - - - - - - - - - - - - - - - - -

for price in prices:
  total_price += price #you can also do total_price = total price + price
average_price = total_price/len(prices) #this will calculate the average price. Which is the total price divided by list of prices.
print("Average Haircut Price: $", average_price)

new_prices = [price - 5 for price in prices]
print("New Prices: ", new_prices)

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i] # prices of haircuts times the number of people who got a haircut last week
print("Total Revenue: $", total_revenue)
# calculate average daily revenue
average_daily_revenue = total_revenue/7
print("Average Daily Revenue: $", average_daily_revenue)

# advertise cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts under 30 dollars: ", cuts_under_30)


# RESULT
# Average Haircut Price: $ 31.875
# New Prices:  [25, 20, 35, 15, 15, 30, 45, 30]
# Total Revenue: $ 1085
# Average Daily Revenue: $ 155.0
# Cuts under 30 dollars:  ['bouffant', 'pixie', 'crew', 'bowl']

