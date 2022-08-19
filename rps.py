import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

# we know that if the user and computer throw out the same thing then it is a tie
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'you win!'
    
    #if is_win(computer, user): -- we do not need this if statement here because the only way we are going to reach this return statement is if the first two if statements are not true. in that case you know you have lost
    #this saves you a line of code
    return 'you lose!'

# second we want to define the winner 
# rock beats scissors, scissors beats paper, and paper beats rock
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True



print(play())