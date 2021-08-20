import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



list_words = ["Aardvark", "hangman", "kimono", "crystal"]
lives = 6

print("Welcome to the game Hangman>>>")


chosen_word = list_words[random.randint(0, len(list_words) - 1)].lower()
print(chosen_word)


display = []
for i in chosen_word:
    display += "_"
print(display)


end_of_game = False
while not end_of_game:
    letter = input("Guess a letter...?\n").lower()
    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            display[i] = letter
    print(display)
    if letter not in chosen_word:
        lives -= 1
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("End of game")

    if "_" not in display:
        end_of_game = True
        print("You win")
