# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
# Write your code below: 
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9 
#if you don't return the function the modified version won't be shown
# test function with value of 100 fahrenheit:
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
#Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.
def c_to_f(c_temp):
  return (c_temp * 9/5) + 32
# test function with a value of 0 celsius:
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# USE THE FORCE
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + "Newtons of force.")
#define new function, inside of that function call another function that's already been found
def get_energy(mass, c=3*10**8):
 return mass * c**2
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
#new function
def get_work(mass, acceleration, distance):
  #Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.
  force = get_force(mass, acceleration)
  return force * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + "Joules of work over " + str(train_distance) + "meters.")


