from operator import truediv
from pickle import TRUE
import random
import sys

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True

# is_word_guessed("loki", ["o", "i", "k", "l"])
# is_word_guessed("loki", ["o", "i", "k", "p"])

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters \
    that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain \
        the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so 
    # far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    guess = ""
    for letter in secret_word:
      if letter in letters_guessed:
        guess += letter
      else:
        guess += "_"    
    return guess


#     print(guess)

# get_guessed_word("loki", ["s","o","i", "t", "u"])
# get_guessed_word("loki", ["u","o","i", "k", "l"])

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
      return True
    else:
      return False
    
# is_guess_in_word("l", "loki")
# is_guess_in_word("x", "loki")





def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")

    rounds = 0
    letters_guessed = [] 

    while rounds < 5: 
      while get_guessed_word != secret_word:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = ""

        while len(guess) != 1:
          guess = str(input("Guess one letter: "))
          if len(guess) != 1:
            print("Please type a single letter.")

        letters_guessed.append(guess)
        rounds += 1

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
          print("You guess correctly.")
        else:
          print("You guess wrong.")

        #TODO: show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))
        print()
        # print(get_guessed_word("loki", ["j", "l", "o", "k", "i"]))

        #TODO: check if the game has been won or lost
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
          print("You guessed the secret word: " + secret_word + ".")
          sys.exit()
        # else:
        #   print("You haven't guessed the secret word yet.\n")
        if rounds == 5:
          print("Game over. You ran out of guesses.")
          sys.exit()



#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())