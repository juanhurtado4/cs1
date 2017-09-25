import random
import string

message = {'congrats': 'Congratulations you won the game!',
            'fail': 'You died!'}
alphabet = string.ascii_lowercase

def load_word():
    '''
    Returns a randomly selected word to be guessed.
    '''
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
    print('current game before loop:', current_game)
    if letters_guessed == 0:
        return current_game
    else:
        current_game = [underscore for underscore in current_game] # 35
        print('current game after first else:', current_game)
        for letter in letters_guessed:
            print('index function first loop:', index_correct_letter(secret_word, letter))
            if index_correct_letter(secret_word, letter) != 'false':
                if type(index_correct_letter(secret_word, letter)) == type(list('test')):
                    for index in range(len(index_correct_letter(secret_word, letter))):
                        # current_game = [letter for letter in current_game] # Moving 35
                        print('length of current game:', len(current_game))
                        print('index:', index)
                        print('list index out of range:', index_correct_letter(secret_word,letter)[index])
                        current_game[index_correct_letter(secret_word,letter)[index]] =    letter

                # current_game = [letter for letter in current_game]
                # current_game[index_correct_letter(secret_word, letter)] = letter
                # First I need to fix multiple letters then else statement for regular letters
                # Do print statements to see why it is index out of range
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
            return all_index # Returns list


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
    return {'l': [0,2]}
# secret_word = load_word()
# print(secret_word)
# print(len(secret_word))
print(game_so_far('lolipop', ['l']))
# print(index_correct_letter('hello', 'h'))
