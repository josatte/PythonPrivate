import random


def guess(x):
    random_number = random.randint(1, x)
    guess1 = 0
    while guess1 != random_number:
        guess1 = int(input(f"Guess a number between 1 and {x}: "))
        print(guess1)
        if guess1 < random_number:
            print('Sorry, guess again. Too low.')
        elif guess1 > random_number:
            print('Sorry, guess again. Too high')
    print(f'Congratulations, number {guess1} is correct!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess2 = int()
    while feedback != 'c':
        if low != high:
            guess2 = random.randint(low, high)
        else:
            guess2 = low
        feedback = input(f'Is {guess2} too high (H), too low (L) or correct (C)? ').lower()
        if feedback == 'h':
            high = guess2 - 1
        elif feedback == 'l':
            low = guess2 + 1
    print(f'The computer guessed your number {guess2} correctly!')


# guess(10)
computer_guess(1000)
