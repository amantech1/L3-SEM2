# Program to create a card guessing game where the player guesses a randomly selected card value and suit.

# Import random module
import random

# List of card values
card_values = [
    '2', '3', '4', '5', '6', '7',
    '8', '9', '10', 'Jack',
    'Queen', 'King', 'Ace'
]

# List of card suits
card_suits = ['Heart', 'Diamond', 'Club', 'Spades']

# Computer selects a random card
answer_value = random.choice(card_values)
answer_suit = random.choice(card_suits)

print("===== CARD GUESSING GAME =====")
print("You have 5 chances to guess the card!")

attempts = 5

while attempts > 0:

    print("\nAttempts Left:", attempts)

    # Player guesses
    guess_value = input("Guess the card value: ")
    guess_suit = input("Guess the card suit: ")

    # Both match
    if guess_value == answer_value and guess_suit == answer_suit:
        print("❤️ 😊 Congratulations! You guessed the card correctly.")
        break

    # One part matches
    elif guess_value == answer_value or guess_suit == answer_suit:
        print("😊 Good try! One part of your guess is correct.")

    # No match
    else:
        print("💔 Wrong guess!")

    attempts -= 1

# Game Ends
if attempts == 0:
    print("\n💔 Game Over!")
    print("The correct card was:", answer_value, "of", answer_suit)