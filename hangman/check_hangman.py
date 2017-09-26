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

def game_so_far(secret_word, str_letters):
    '''
    Receives secret_word and str_letters as a STRING
    Checks to see if each letter is in secret word
    Returns STRING of the state of the game
    '''
    current_game = ['_' for underscore in range(len(secret_word))]
    for letter in str_letters:
        for num, char in enumerate(secret_word):
            if letter == char:
                current_game[num] = letter
    return ' '.join(current_game)

def is_word_guessed(secret_word):
    '''
    Receives secret word as a STRING
    Returns bool if the secret word has been guessed
    '''
    if '_' not in game_so_far(secret_word, str_letters):
        return True
    else:
        return False
