# Write your code below:
# 3 types of arguments: positional (can be called by their position in the function), keyword (can be called by their name), default (given default values)

#TRIPCADEMY

# Write your code below:
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  #statement
  print("Here is what your trip will look like!")
# values for parameters
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
#parameters
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
#default arguments
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")