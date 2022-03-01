#In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# accomodate lowercase letter variants of uppercase already in use
letters += [letter.lower() for letter in letters]
points *=2

#create a dictionary
letter_to_points = {key:value for key, value in zip(letters, points)}
#print(letters_to_points)

#add new blank tile that is missing
letter_to_points[" "] = 0
print(letter_to_points)

# create a function that will take in a word and return how many points that word is worth

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# test function
brownie_points = score_word("BROWNIE")
print(brownie_points)
# result should give: 15

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
update_point_totals()
print(player_to_points)

# play_word function adds new words to the game
def play_word(player, word):
    player_to_words[player].append(word)
play_word("player1", "CODE")
print(player_to_words)




