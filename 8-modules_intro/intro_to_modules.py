# Modules are also referred as "libraries" or "packages" - package is a directory that holds a collection of modules.
# to use a module in a file, basic syntax to use is: from module_name import object_name
# Import datetime from datetime below:
from datetime import datetime
current_time = datetime.now()
print(current_time)

#RESULT: 2022-02-28 04:03:55.948129

#-------------------------

# random , allows you to generate or select numbers at random
# syntax:  import random
# random.choice()
# random.randint()

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)



# Print randomer_number below:
print(randomer_number)

# results: you will generate random numbers

#-----------------------

# namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. 



