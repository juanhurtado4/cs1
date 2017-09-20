'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
random.seed(1)

# # bankroll = int(input('Please enter bankroll'))
# bet_amount = 0
# bet_color = None
# bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

class Take_bet():
    def __init__(self, name, bet_color, bet_amount, bet_num=None):
        self.name = name
        self.bet_color = bet_color
        self.bet_num = bet_num
        self.bet_amount = bet_amount

    def __str__(self):
        if self.bet_num == None:
            no_bet_num = '{name} placed a bet of ${bet_amount} on the color {bet_color}'
            return no_bet_num.format(name=self.name,
                               bet_amount=self.bet_amount,
                               bet_color=self.bet_color)
        else:
            with_bet_num = '{name} placed a bet of ${bet_amount} on number {bet_num} and color {bet_color}'
            return with_bet_num.format(name=self.name,
                                       bet_amount=self.bet_amount,
                                       bet_num=self.bet_num,
                                       bet_color=self.bet_color)

    def get_bet_color(self):
        return self.bet_color

    def get_bet_num(self):
        return self.bet_num

    def get_bet_amount(self):
        return self.bet_amount

num_bet = Take_bet("Juan", "Red", 30, 2)
no_num_bet = Take_bet("Jose", "Red", 30)

print('This is bet num', num_bet.get_bet_num())
print('This is bet amount', num_bet.get_bet_amount())
print('This is bet color', num_bet.get_bet_color())
print(num_bet)

print('This is bet num', no_num_bet.get_bet_num())
print('This is bet amount', no_num_bet.get_bet_amount())
print('This is bet color', no_num_bet.get_bet_color())
print(no_num_bet)



def roll_ball():
    '''returns a color and number after roll'''
    num = random.randrange(0, 37)
    if num in green:
        color = 'green'
    elif num in red:
        color = 'red'
    elif num in black:
        color = 'black'
    return (color, num)

def check_results(rolled, bet):
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled if there was a bet on a number.'''
    color_rolled = rolled[0]
    num_rolled = rolled[1]
    bet_color = bet[0]
    bet_rolled = bet[1]
    if bet[1] == None:
        if bet_color == color_rolled:
            return True
        else:
            return False


def payout():
    '''returns total amount won or lost by user based on results of roll. '''
    pass

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """

    pass
