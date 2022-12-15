import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return 'You win!'

    return 'You lost!'


def is_win(player_1, player_2):
    if (player_1 == 'r' and player_2 == 's') or (player_1 == 's' and player_2 == 'p') or (
            player_1 == 'p' and player_2 == 'r'):
        return True


print(play())
