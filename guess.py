import random

def askForGuess():
    while True:
        guess = input('> ')  # Enter the guess.

        if guess.isdecimal():
            return int(guess)  # Convert string guess to an integer.
        print('Please enter a number between 1 and 100.')


def playGuessingGame():
    secretNumber = random.randint(1, 100)  # Select a random number.
    print('I am thinking of a number between 1 and 100.')

    for i in range(10):  # Give the player 10 guesses.
        print(f'You have {10 - i} guesses left. Take a guess.')

        guess = askForGuess()
        if guess == secretNumber:
            print('Yay! You guessed my number!')
            return

        # Offer a hint:
        if guess < secretNumber:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')

    print('Game over. The number I was thinking of was', secretNumber)


print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
playGuessingGame()
