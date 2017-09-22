import check_hangman as check

'''
TODO: Fix get_letters_left func. Return whole alphabet if no letters have been guessed. Else return the available letters left.
'''
class Player():
    def __init__(self, name):
        '''
        Initializes player instance with some default values
        '''
        self.name = name
        self.letters_left = check.alphabet
        self.guesses_left = 6
        self.letters_guessed = []

    def __str__(self):
        return '{name} likes to play hangman'.format(name=self.name)

    def get_name(self):
        '''
        Returns player name as a string
        '''
        return self.name

    def get_letters_guessed(self, letter_guess=None):
        '''
        Returns default empty list of letters guessed.
        Else returns updated list of letters guessed.
        '''
        if letter_guess == None:
            return self.letters_guessed
        else:
            self.letters_guessed.append(letter_guess)
            return self.letters_guessed

    def get_letters_left(self):
        return self.letters_left

    def get_guesses_left(self, guess_left=None):
        '''
        Returns the default int of guesses (6).
        Else returns updated int of guesses left.
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
    name = input('What is your name?: ')
    print('The word to be guessed has {len_secret_word} letters'.format(len(check.secret_word)))
    player1 = Player(name)
    num_guess_left = 6
    while not is_word_guessed:
        if player1.get_guesses_left() < 1: # logic if player fails
            print(check.message['fail'])
            play_again = input('Play again?\nyes | no ')
            while play_again != 'yes' or play_again != 'no': # Enforces user inputs yes or no at the end of game.
                play_again = input('Play again?\nyes | no ')
            if play_again == 'yes':
                main()
            else:
                break
        while guess not in check.alphabet: # Makes sure user input is a letter
            guess = input('Please guess a letter: ')

        num_guesses_left -= 1
        player1.get_guesses_left(num_guesses_left)
        player1.get_letters_guessed(guess)

        if check.check_guess(guess):



    # TODO: Create logic to check if guess equals a letter in secret word






if __name__=='__main__':
    main()

# -----This is debugging-------
# player1 = Player(name)
# print(player1)
# print(player1.get_guesses_left())
# player1.get_guesses_left(5)
# print(player1.get_guesses_left())
# player2 = Player('Jose')
# print('Player 2 guesses', player2.get_guesses_left())
# print(player1.get_guesses_left())
