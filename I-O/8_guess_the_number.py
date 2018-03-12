"""
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1
and 20.
"""
import random


def guess_the_number():
    number_to_guess = random.randint(1, 20)
    guesses_left = 20

    number_is_not_guessed = True
    while number_is_not_guessed:
        print(number_to_guess)
        input_is_not_number = True
        while input_is_not_number:
            try:
                user_input = int(input('Enter a number: '))
                input_is_not_number = False
            except ValueError:
                continue
        print('Guesses left: {}'.format(guesses_left))
        if user_input < number_to_guess:
            guesses_left -= 1
            print('Your number is too low!')
        elif user_input > number_to_guess:
            guesses_left -= 1
            print('Your number is too high!')
        else:
            print('Correct! You win!')
            number_is_not_guessed = False


guess_the_number()