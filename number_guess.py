import random

number = random.randint(1, 10)
guess = ""

while guess != number:

    guess = int(input("I'm thinking of a number between 1 and 10. Guess which one: "))

    if guess == number:
        print("You guessed correctly")
    else:
        print(f"you guessed wrong, try again!!")