import random

number = random.randrange(1,50)
guess = int(input("Guess a number between 1 to 50: "))

while guess != number:
    if guess < number:
        print("You need to guess higher, Try again: ")
        guess = int(input("\nGuess a number between 1 to 50: "))
    else:
        print("You need to guess lower, Try again: ")
        guess = int(input("\nGuess a number between 1 to 50: "))
print("\n\nCongratulation! You guess the number correctly! ")