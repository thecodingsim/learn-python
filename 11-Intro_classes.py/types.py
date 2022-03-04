# you can check the type of python variable by using type()
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

#result: 
# <class 'int'>
# <class 'dict'>
# <class 'list'>

#-------------------------

#CLASS is a template for a data type. It describes the kind of information that class will hold and how a programmer will interact with that data. 
class Facade:
  pass

#--------------------------

#Instantiation: we must create an instance of the class in order to breathe life into the schematic
# example: cool_instance = CoolClass()
class Facade:
  pass
facade_1 = Facade()

#---------------------------

# Object Oriented Programming : pattern of defining classes and creating objects to represent the responsiblities of a program is known as object oriented programming or OOP.
# print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"

# In python, _main_ means "this is the current file we're running"class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

#result: <class '__main__.Facade'>

#-----------------------------

# Class Variables: a variable that's the same for every instance of the class
class Grade:
  minimum_passing = 65

#----------------------

# Methods: functions that are define as part of a class
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#--------------------------

# methods with arguments
# A medium pizza that is 12 inches across.
# Your teaching table which is 36 inches across.
# The Round Room auditorium, which is 11,460 inches across.

class Circle:
  pi = 3.14
  
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

#---------------------------------------------------

# Constructors
#_init_()

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
#result: New circle with diameter: 36

#-----------------------------

#Instance Variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"
#--------------------------------------

#attribute functions
# hasattr() will return true if the object has been given an attribute, otherwise it will return false. 
#getattr() is a python function that will return the value of a given object and attribute
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

#------------------------

#self

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#--------------------------------------

# Everything is an object
print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object))

#result:
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
#-----------------------------------

#string representation
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

#result: Circle with radius 6.0
# Circle with radius 18.0
# Circle with radius 5730.0

#-------------------------------

#REVIEW

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
