import random


def main():
    print_header()
    guessing_game_2()


def print_header():
    print('--------------------')
    print('-- Guessing Game ---')
    print('--------------------')

# %%
def guessing_game():
    number = random.randint(1, 10)
    guess = int(input('Guess a number between 1 and 10: '))
    total_guesses = 1
    while guess != number:
        if guess < number:
            print(f'{guess} is too low.')
            total_guesses += 1
            guess = int(input('Try again: '))
        elif guess > number:
            print(f'{guess} is too high.')
            total_guesses += 1
            guess = int(input('Try again: '))

    if guess == number:
        print(
            f'You guessed it in {total_guesses} tries! The number was {number}.'
        )
# %%

# %%
def guessing_game_2():
    number = random.randint(1, 20)
    total_guesses = 1

    while True:
        if total_guesses == 1:
            guess = int(input("Guess a number between 1 and 20: "))
        else:
            guess = int(input("Try again: "))

        if guess == number:
            print(
                f'You guessed it in {total_guesses} tries! The number was {number}.'
            )
            break

        if guess < number:
            print(f'{guess} is too low!')
            total_guesses += 1
        else:
            print(f'{guess} is too high!')
            total_guesses += 1
# %%

if __name__ == '__main__':
    main()
