# Sal's Shipping
# Joanne Wenceslao

# set weight to any number of lbs to find price of shipping.
weight = 41.5 #change this number

# Ground Shipping 🚚 (Weight of Package * Price per Pound	+ Flat Charge)
if weight <= 2:
  cost_ground = (weight * 1.50 + 20)
elif weight <= 6:
  cost_ground = (weight * 3.00 + 20)
elif weight <= 10:
  cost_ground = (weight * 4.00 + 20)
else:
  cost_ground = (weight * 4.75 + 20)

print("Ground Shipping: $", cost_ground)

# Ground Shipping Premium 🚛
cost_premium = 125.00
print("Ground Shipping Premium$: $", cost_premium)

# Drone Shipping ✈ (Weight of Package*Price per Pound)
if weight <= 2:
  cost_drone = (weight * 4.50)
elif weight <= 6:
  cost_drone = (weight * 9.00)
elif weight <= 10:
  cost_drone = (weight * 12.00)
else:
  cost_drone = (weight * 14.25)

print("Drone Shipping: $", cost_drone)

#Run the program and check these examples:
#What is the cheapest method of shipping a 4.8 pound package and how much would it cost?


