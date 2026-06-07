"""A number guessing game for the user.
The program ask the user to input a number. The program specifications are as mentioned below.
I.The program generates a random number for the answer.
II.The program prompts the user for a number input.
III.The program provides the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
IV.The program checks the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
V.If the user is not able to guess the answer within 5 times, the program displays “Game Over” message and exit."""

import random

# Generate random number
answer = random.randint(1, 100)

attempt = 1

while attempt <= 5:

    guess = int(input('Enter your guess: '))

    if guess > answer:
        print('Too high')

    elif guess < answer:
        print('Too low')

    else:
        print('Correct number')
        break

    attempt += 1

if attempt > 5:
    print('Game Over')
    print('Correct number was: ', answer)