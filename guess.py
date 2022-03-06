import random

print('Hello, What is your name?')
name = input()

print("Nice to meet you " + name + ", I am thinking of a number between 1 and 20. Take a guess!")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    guess = int(input())

    if guess < secretNumber:
        print('Too low!')
    elif guess > secretNumber:
        print('Too high!')
    else:
        if guess == secretNumber:
            print('Good job ' + name + '! The number was ' + str(secretNumber) + '! You guessed it in ' + str(guessesTaken) + ' guesses.')
        else:
            print('Sorry, you ran out of guesses!')