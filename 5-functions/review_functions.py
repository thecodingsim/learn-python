# Build TripPlanner V1.0
# Welcome your users, must have a parameter called name
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)
trip_planner_welcome("the coding sim")
#def function: estimated_time_rounded
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(5.52)
# generate messages for a user's planned trip
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time), "hours")
destination_setup("origin", "destination" , estimate, "Car")


# RESULT
# Welcome to tripplanner v1.0 the coding sim
# Your trip starts off in origin
# And you are traveling to destination
# You will be traveling by Car
# It will take approximately 6 hours