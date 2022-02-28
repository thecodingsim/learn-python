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

# import module_name as name_you_pick_for_the_module
# import* "*" is known as the wildcard and matches anything with everything. Becareful when using this because it can pollute the namespace
# Pollution occurs when the same name could apply for two possible things.
# random.sample() takes a range and a number as its arguments

import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt

import random
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
#print(numbers_b)

plt.plot(numbers_a, numbers_b)
plt.show()

# RESULT: image of plot 

#------------------------

# modules python decimals
# use Decimal to fix floating points


# Import Decimal below:
from decimal import Decimal

# Below are variables to return the amount of either two decimal points or four decimal points
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# result: 
# 0.89
# 0.3445

#----------------------------

#python files and scope
# scope applies to classes and to the files you are working within. Files have scope.
#files are modules, so you can give access to another file's content using import

#in library.py
def always_three():
  return 3

#results: 3
#--------------------------------

# https://www.youtube.com/watch?v=BVr-6Ki96XM&t=15s