import random
import string

alphabet = string.ascii_lowercase
message = {'won': 'Congratulations you won the game!',
            'lost': '''"You died!\\nThe word was: {word}".format(word=secret_word)''',
            'correct': 'Correct!',
            'incorrect': 'Try again',
            'length': "The word has {len_secret_word} letters",
            'welcome': 'Welcome to hangman!',
            'guess': 'Please guess a letter: ',
            'play': 'Play again?\nyes | no: ',
            'name': 'What is your name?: ',
            'guesses_left': 'You have {guesses_left} guesses left',
            'letters_guessed': '''"You have guessed these letters: {letters_guessed}".format(letters_guessed=player1.get_letters_guessed())''',
            'available_letters': '''"You have these letters available: {available_letters}".format(available_letters=player1.get_available_letters())''',
            'acceptable_answers': ('yes', 'y', 'n', 'no')}


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

def is_word_guessed(secret_word, str_letters):
    '''
    Receives secret word as a STRING
    Returns bool if the secret word has been guessed
    '''
    if '_' not in game_so_far(secret_word, str_letters):
        return True
    else:
        return False

def is_letter_correct(secret_word, letter):
    '''
    Receives secret_word and letter as strings
    Returns bool if the letter is in the secret_word
    '''
    if letter in secret_word:
        return True
    else:
        return False
