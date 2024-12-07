# Import libraries
import random
from nltk.corpus import words

# Download the corpus
import nltk
nltk.download("words")

#ASCII ART
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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

# Retrieve the list of words
word_list = words.words()

lives = 6

# Import the logo
print('''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝''')

# Select a random word
chosen_word = random.choice(word_list).lower()
chosen_word_list = list(chosen_word)
#print(chosen_word)

# Create a "placeholder" with the same number of blanks as the chosen_word
number_of_blanks = len(chosen_word)
placeholder = "_" * number_of_blanks
placeholder_list = list(placeholder)
print(placeholder)
print(stages[lives])

#Ask the user to guess a letter
display = ""

while display != chosen_word:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"**********************YOU GUESSED LETTER {guess},IT'S NOT IN THE WORD**********************")
        print(f"*************************************{lives} LIVES LEFT*************************************")
        if lives == 0:
            print('''
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░  ██╗
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗  ██║
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝  ██║
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗  ╚═╝
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║  ██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═╝''')
            print(f"THE CORRECT WORD IS: {chosen_word}")
            exit()

    if guess in placeholder_list:
        print("**********************LETTER {guess} HAS BEEN ALREADY USED**********************")
        continue

# Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            placeholder_list[index] = letter
    display = "".join(placeholder_list)
    print(display)

print("**********************CONGRATULATIONS! YOU GUESSED THE CORRECT WORD!**********************")
print('''
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝''')