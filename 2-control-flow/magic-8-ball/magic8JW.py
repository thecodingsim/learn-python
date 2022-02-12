#this program will give an output of yes or no
#format: [Name] asks: [Question] Magic 8-Ball’s answer: [Answer]

#importing this module allows me to use the random function:
import random

#variable outputs for: name, question, answer:
#change name and question to provide different outputs
user_name = "Jojo"
user_question = "Do you want to go out to dinner with me?"
answer = ""


#this will run a random answer each time you run a program:
random_number = random.randint(1,12)
#print(random_number)

if random_number == 1:
  answer = "Yes-definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "As I see it, yes."
elif random_number == 11:
  answer = "You may rely on it."
elif random_number == 12:
  answer = "HELL NO."
else:
  answer = "Error"  

# Challenge: if user_name or user_question is empty:

if user_name == "":
  print("Question: ", user_question)
else:
  print(user_name, "asks:", user_question)

# This will print Magic 8-ball's answer:

print("Magic 8 Ball's answer: ", answer)

