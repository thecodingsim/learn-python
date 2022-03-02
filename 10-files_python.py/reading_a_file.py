# file systems are needed to store and retrieve data.
# each file is in anindividual container of related information. 
# .read()

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

#result: Congratulations on reading your first file at codecademy.com!

#-----------------------------

#iterating through lines
# store each line in a variable using .readlines()

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

#result
# 1. How many lines do we write on the daily,

# 2. Many money, we write many many many

# 3. How many lines do you write on the daily,

# 4. Say you say many money, you write many many many

#--------------------------------

# read a line
# .readline() to read ONLY a single line

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

# result: You do look, my son, in a moved sort,

#--------------------------------------

# writing a file
# open() function will need an argument to open a file to write to
# example: with open('generated_file.txt', 'w') as gen_file:
#'w' indicates to open the file in write mode. 'r' passes as read mode.
# gen_file.write("What an incredible file!")

with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('I hate All Time Low')

#-------------------------------------

# Appending to a file
# open with 'a' for append mode

with open('cool_dogs.txt', 'a') as cool_dogs_file:
   cool_dogs_file.write('Air Buddy')

#--------------------------------------------

# Why With?
# the 'with' keyword invokes context manager for the file that we're calling open() on. The context manager takes care of opening the file when we call open() then closing the file after we leave the indented block. 
# replaces older ways to access files where you need to call close()

with open('fun_file.txt') as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)

#result: What did the pirate say when he turned 80?

#----------------------------------------

# CSV file, stands for comma-seperated values is an example of a text file that impose a structure to their data. data from a spreadsheet (like microsoft excel or google sheets) is exported to a portable format.
# example:
# Name,Username,Email
# Roger Smith,rsmith,wigginsryan@yahoo.com
# Michelle Beck,mlbeck,hcosta@hotmail.com
# Ashley Barker,a_bark_x,a_bark_x@turner.com
# Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
# Jennifer Chase,chasej,jchase@ramirez.com
# Charles Hoover,choover,choover89@yahoo.com
# Adrian Evans,adevans,adevans98@yahoo.com
# Susan Walter,susan82,swilliams@yahoo.com
# Stephanie King,stephanieking,sking@morris-tyler.com
# Erika Miller,jessica32,ejmiller79@yahoo.com

with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())

# result:
# Name,Age,ID
# Richard Andrews,43,0de2ecf31df2386377b1d2dc4fae8b16fad05ad0         
# Hailey Sellers,24,3d9b8a95458c1df2687191e8146a97ca4afb28aa          
# Jessica Pace,39,a5daa63ef893cb86bc8df1110cc9a5f8e1d0c563            
# Jasmine Escobar,42,9844e403841ec84b9a2fb3caf9d2a1c9ee042d31         
# Karen Kelly,26,8338f76ac0e9a76d73d57790f1d9843b185b5428             
# Patricia Christensen,70,23099bb630c1c64989458393045f08de3bac0eb9    
# Jessica Hansen,24,a8c035ccd099ef909a46e0d96b76c0f132c9c562          
# Raymond Adams,53,a051901830ff6c2095524ef92b1541eef9f8c64d           
# Stephanie Morrow,53,3bad04a5fc0a7ec33735ae45535f354887988f35        
# Timothy Ramos,34,b4930920b5256c4e592541297e43a556c8fe33a8 

#----------------------------------------

# reading a csv file
# first import the csv library using import
# create an empty list
#newline=' ' will make sure not to accdientally mistake a line break in the data dields as a new row in the CSV. ( read for more info: https://docs.python.org/3/library/csv.html#id3)
# .DictReader converts the lines of the CSV to python dictionaries
# example:
# import csv
 
# list_of_email_addresses = []
# with open('users.csv', newline='') as users_csv:
#   user_reader = csv.DictReader(users_csv)
#   for row in user_reader:
#     list_of_email_addresses.append(row['Email'])

import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

# result: 
# Has never been out of the country.
# Published a small biography on a local legend.
# Happened across a major movie star while biking once.
# Once ate three packages of cookies in one sitting.
# Has been to over fifteen different forests.
# Old job was across the street from their new job.
# Has a dog named Peanut.
# While working a phone bank accidentally called their mother.
# Can whistle the national anthem of twelve different nations.
# Is triple-jointed.

#-----------------------------------------

# reading different types of CSV files
#when using csv.DictReader pass with the delimiter parameter

# import csv
 
# with open('addresses.csv', newline='') as addresses_csv:
#   address_reader = csv.DictReader(addresses_csv, delimiter=';')
#   for row in address_reader:
#     print(row['Address'])

import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]

#----------------------------------

#writing a CSV file
# create CSV files that save output and data that someone could load into their spreadsheet software
# .writeheader() for headers in the writer object
# .writerow() writes each line to the CSV file

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames= fields)
  log_writer.writeheader()
  for list in access_log:
    log_writer.writerow(list)

#----------------------------------------

# reading JSON file, javaScript object notation-file format inspired by the programming language Javascript. 
# .load() creates a python dictionary out of the file
import json
with open('message.json') as message_json:
    #just the json file as an argument to load the dictionary out of the file and saved it to the new variable message
  message = json.load(message_json)
  print(message['text'])

#result: Now that's JSON!

#---------------------------------------

# writing json file
# .dump() to write the file

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)

#-------------------------------------------

# REVIEW

