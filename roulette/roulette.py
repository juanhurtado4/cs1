# import random
import check_roulette as check

# random.seed(1)

class Player():
    def __init__(self, name, bankroll, bet_color, bet_amount, bet_num=None):
        self.name = name
        self.bankroll = bankroll
        self.bet_color = bet_color
        self.bet_num = bet_num
        self.bet_amount = bet_amount

    def __str__(self):
        return '{player_name} has a bankroll of ${bankroll}'.format(player_name=self.name,
                                                                    bankroll=self.bankroll)

    def get_name(self):
        return self.name

    def get_bankroll(self, new_bankroll=None):
        '''
        TODO: CREATE NEW BANKROLL CHECKING FUNCTION INSIDE MODULE
        '''
        if new_bankroll == None:
            return self.bankroll
        else:
            return new_bankroll


    def get_bet_color(self, new_bet_color=None):
        '''
        TODO: CREATE NEW COLOR CHECKING FUNCTION INSIDE MODULE
        '''
        if new_bet_color == None:
            return self.bet_color
        else:
            return new_bet_color

    def get_bet_num(self):
        return self.bet_num

    def get_bet_amount(self):
        return self.bet_amount

player1 = Player("juan", 200, "red", 50, 3)
player2 = Player("jose", 100, "black", 20)

print('This is player: ', player1)
print('This is bet amount: ', player1.get_bet_amount())
print('This is bet num: ', player1.get_bet_num())
print('This is name: ', player1.get_name())

print('This is player 2 bet num: ', player2.get_bet_num())
print('This is player 2: ', player2)

print("Juan's old bankroll: ", player1.get_bankroll())

change_bankroll = player1.get_bankroll(500)

print("Juan's new bankroll:", change_bankroll)

print('This is bet color: ', player1.get_bet_color())
new_color = player1.get_bet_color('green')
print('This is new bet color: ', player1.get_bet_color(new_color))



# In functions write description of what functions do, outputs, arguments (data types)
# def roll_ball():
#     '''returns a color and number after roll'''
#     ran_num = random.randrange(0, 37)
#     if ran_num in check.nums_colors['green']:
#         color = 'green'
#     elif ran_num in check.nums_colors['red']:
#         color = 'red'
#     elif ran_num in check.nums_colors['black']:
#         color = 'black'
#     return (color, ran_num)
#
# def check_results(rolled, bet):
#     '''Compares bet_color to color rolled.  Compares
#     bet_number to number_rolled if there was a bet on a number.'''
#     color_rolled = rolled[0]
#     num_rolled = rolled[1]
#     bet_color = bet[0]
#     bet_rolled = bet[1]
#     if bet[1] == None:
#         if bet_color == color_rolled:
#             return True
#         else:
#             return False
#
#
# def payout():
#     '''returns total amount won or lost by user based on results of roll. '''
#     pass
#
# def play_game():
#     """This is the main function for the game.
#     When this function is called, one full iteration of roulette,
#     including:
#     Take the user's bet.
#     Roll the ball.
#     Determine if the user won or lost.
#     Pay or deduct money from the user accordingly.
#     """
#
#     pass
#
#
# # DEBUGGING
# juan = Player("Juan", 200)
# jose = Player("Jose", 100)
#
# juan_bet = Take_bet(juan)
#
# print('This is bet num', juan.get_bet_num())
# print('This is bet amount', juan.get_bet_amount())
# print('This is bet color', juan.get_bet_color())
# print(juan)
#
# print('This is bet num', jose.get_bet_num())
# print('This is bet amount', jose.get_bet_amount())
# print('This is bet color', jose.get_bet_color())
# print(jose)

# def __str__(self):
#     # Receives a string from check_bet func and returns an evaluated version of that string.
#     return eval(check.check_bet_num(self.bet_num))
