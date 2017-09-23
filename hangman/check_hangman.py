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
   f = open('hangman_words.txt')
   words_list = f.read()
   f.close()

   words_list = words_list.split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def game_so_far(secret_word, letters_guessed):
    '''
    Receives a string of secret_word and a list of letters_guessed
    Returns the state of the game so far in a string.
    Underscores for every word that has not been guessed.
    Loop places underscores in place of letter to hide secret word.
    '''
    current_game = ''.join(['_' for underscore in range(len(secret_word))])
    if letters_guessed == 0:
        return current_game
    else:
        for letter in letters_guessed:
            if index_correct_letter(secret_word, letter) != 'false':
                if type(index_correct_letter(secret_word, letter)) == type(list('test')):
                    for index in index_correct_letter(secret_word, letter):
                        current_game = [letter for letter in current_game]
                        current_game[index_correct_letter(secret_word,letter)[index]] =    letter

                current_game = [letter for letter in current_game]
                current_game[index_correct_letter(secret_word, letter)] = letter
            else:
                continue
        current_game = ''.join([letter for letter in current_game])
        return current_game







def index_correct_letter(secret_word, letter_guessed):
    '''
    Function checks if letter_guessed is correct.
    If so it returns the index (Int) of the correct letter in the secret word.
    elif returns list of indexes if a letter is repeated.
    Else returns false.
    '''
    if multiple_lttr_secret_word(secret_word) != 'false':
        multiple_letters = multiple_lttr_secret_word(secret_word) # Dictionary of letter/index pairs
        if letter_guessed in multiple_letters:
            all_index = multiple_letters[letter_guessed]
            return all_index


    elif letter_guessed in secret_word:
        for index in range(len(secret_word)):
            if letter_guessed == secret_word[index]:
                return index
    else:
        return 'false'

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the random word the user is trying to guess.  This is selected on line 9.
    letters_guessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if secret_word in letters_guessed:
        return True
    else:
        return False

def multiple_lttr_secret_word(secret_word):
    '''
    USE COUNT FUNCTION.
    Keep track of all the repeated letters and indexes.
    If multiple letters returns dictionary letter/index pairs.
    Else returns false (string).
    '''
    return {'l': [2, 3]}

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
    pass

# secret_word = load_word()
# print(secret_word)
# print(len(secret_word))
print(game_so_far('whitehouse', ['e']))
# print(index_correct_letter('hello', 'h'))
