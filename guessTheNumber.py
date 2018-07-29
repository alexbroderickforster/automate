def guessFunc():
    global number
    guess = 0
    numGuesses = 0
    while guess != number:
        print('Take a guess.')
        guess = int(input())
        numGuesses = numGuesses + 1
        if guess > number:
            print('Your guess is too high.')
        elif guess < number:
            print('Your guess is too low.')
        else:
            return('Good job! You guessed my number in ' + str(numGuesses) + ' guesses!')
    
    
print('I am thinking of a number between 1 and 20.')
import random
number = random.randint(1, 20)
print(guessFunc())
