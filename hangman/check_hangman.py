import random
import string
'''
The character "//" denotes completed todo.
TODO//: 1st create user class
TODO//: 2nd get secret word from words.txt
TODO//: 3rd display # of guesses
TODO: 4th take user guess / validate
TODO: 5th check if guess in word - if yes, replace correct underscore - if no, subtract 1 from guesses left
TODO: 6th track user guesses / append latest guess
TODO: 7th fix load word function
TODO//: 8th fix is_word_guessed func to check how many guesses left.
TODO//: 8TH if there are guesses left return how many guesses left.
TODO//: 8TH else determine if player won or lost and return msg accordingly.
BONUS: beautiful soup is a library for web scraping
'''
message = {'congrats': 'Congratulations you won the game!',
            'fail': 'You died!'}
alphabet = string.ascii_lowercase

def load_word():
   # f = open('hangman_words.txt', 'r')
   # words_list = f.read_lines()
   # f.close()
   #
   # words_list = words_list[0].split(' ')
   # secret_word = random.choice(words_list)
   # # return secret_word
   return 'oxygen'

def game_so_far(secret_word, letters_guessed):
    '''
    Returns the state of the game so far.
    Underscores for every word that has not been guessed.
    Loop places underscores in place of letter to hide secret word.
    '''
    if len(letters_guessed) == 0:
        current_game = ' '.join(['_' for underscore in range(len(secret_word))])




def is_word_guessed(secret_word, letters_guessed, guesses_left):
    '''
    secret_word: string, the random word the user is trying to guess.  This is selected on line 9.
    letters_guessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if guesses_left > 0:
        return guesses_left
    elif secret_word in letters_guessed:
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the random word the user is trying to guess.  This is selected on line 9.
    letters_guessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...




def getAvailableLetters(letters_guessed):
    '''
    letters_guessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...


secret_word = load_word()
# hangman(load_word())
