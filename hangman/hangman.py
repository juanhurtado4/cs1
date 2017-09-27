import check_hangman as check

class Player():
    def __init__(self, name):
        '''
        Initializes player instance with some default values
        '''
        self.name = name
        self.available_letters = check.alphabet
        self.guesses_left = 5
        self.letters_guessed = ''

    def __str__(self):
        return '{name} likes to play hangman'.format(name=self.name)

    def get_name(self):
        '''
        Returns player name as a string
        '''
        return self.name

    def get_letters_guessed(self, letter_guess=None):
        '''
        Returns letters guessed
        Default is empty string
        '''
        if letter_guess == None:
            return self.letters_guessed
        else:
            self.letters_guessed += letter_guess
            return self.letters_guessed

    def get_available_letters(self, letters_guessed=None):
        '''
        Receives String of letters and checks if alphabet letters are in letters guessed.
        Returns a list of letters that have not been guessed yet.
        '''
        if letters_guessed == None:
            return self.available_letters
        else:
            self.available_letters = ''.join([letter for letter in self.available_letters if letter not in letters_guessed])

    def get_guesses_left(self, guess_left=None):
        '''
        Returns the default Int of guesses (5).
        Else returns updated Int of guesses left.
        '''
        if guess_left == None:
            return self.guesses_left
        else:
            self.guesses_left = guess_left
            return self.guesses_left

def main():
    '''
    Runs the main functionality of game
    '''
    secret_word = check.load_word()
    name = input(check.message['name'])
    print(check.message['welcome'])
    print(check.message['length'].format(len_secret_word=len(secret_word)))
    print(' '.join(['_' for underscore in secret_word]))

    player1 = Player(name) # Creates player instance

    while not check.is_word_guessed(secret_word, player1.get_letters_guessed()):
        if player1.get_guesses_left() < 1: # If player fails break
            break

        guess = input(check.message['guess'])
        while guess in player1.get_letters_guessed():
            guess = input('Please enter a new letter: ')
        print('\n')
        while guess not in check.alphabet: # Makes sure user input is a letter
            guess = input(check.message['guess'])


        player1.get_letters_guessed(guess) # Updates letters guessed
        player1.get_available_letters(guess) # Updates letters available
        if check.is_letter_correct(secret_word, guess):
            print(check.message['correct'])
        else:
            player1.get_guesses_left(player1.get_guesses_left() - 1) # Updates guesses left
            print(check.message['incorrect'])

        print(eval(check.message['letters_guessed']))
        print(check.message['guesses_left'].format(guesses_left=player1.get_guesses_left()))
        print(eval(check.message['available_letters']))
        print(check.game_so_far(secret_word, player1.get_letters_guessed()))

    if check.is_word_guessed(secret_word, player1.get_letters_guessed()):
        print(check.message['won'])

        play_again = input(check.message['play'])
        while play_again not in check.message['acceptable_answers']: # Enforces user inputs yes or no at the end of game.
            play_again = input(check.message['play'])
            print('play again:', play_again)
            play_again = input(check.message['play'])
        if play_again == 'yes' or play_again == 'y':
            main()
        else:
            exit()

    else:
        print(eval(check.message['lost']))
        play_again = input(check.message['play'])
        while play_again not in check.message['acceptable_answers']:
            play_again = input(check.message['play'])
        if play_again == 'yes' or play_again == 'y':
            main()
        else:
            exit()



if __name__=='__main__':
    main()
