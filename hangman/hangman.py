class Player():
    def __init__(self, name, letters_guessed, letters_left, guesses_left):
        self.name = name
        self.letters_guessed = letters_guessed
        self.letters_left = letters_left
        self.guesses_left = guesses_left

    def __str__(self):
        return '{name} likes to play hangman'.format(name=self.name)

    def get_name(self):
        return self.name

    def get_letters_guessed(self):
        return self.letters_guessed

    def get_letters_left(self):
        return self.letters_left

    def get_guesses_left(self):
        return self.guesses_left
