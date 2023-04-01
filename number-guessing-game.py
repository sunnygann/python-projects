import random
import math

def guessingGame(gg1, gg2):
    return random.randint(gg1, gg2)

print("This is a guessing game. \nYou will enter 2 numbers and the program will randomly "
      "choose a number in between the two numbers. \nYou will have to guess the number. "
      "The program will stipulate the number of attempts you have. \nYou will be guided with higher and lower prompts.")

try:
    x = int(input("\n\tPlease enter the first number: "))
    y = int(input("\tPlease enter the second number: "))
    if y > x:
        randomNumber = guessingGame(x, y)
        numTries = round(math.log(y - x + 1, 2))
    elif x > y:
        randomNumber = guessingGame(y, x)
        numTries = round(math.log(x - y + 1, 2))
    else:
        print("Please provide different numbers. ")
except ValueError:
    print("Please enter a valid integer. ")
print("You have " + str(numTries) + " number of attempts to guess the random number.")
# print("Random Number: " + str(randomNumber))

for i in range(numTries):
    guess = int(input("Please enter your guess: "))
    if guess == randomNumber:
        print("You guessed correct!")
        exit()
    elif guess > randomNumber:
        print("Try again! Your guess is higher than the random number. ")
        numTriesLeft = numTries - (i + 1)
        if numTries - (i + 1) == 0:
            print("\nYou have failed to guess the number in the given number of attempts. Better luck next time!")
        else:
            print("You have " + str(numTriesLeft) + " attempts left. ")
    else:
        print("Try again! Your guess is lower than the random number. ")
        numTriesLeft = numTries - (i + 1)
        if numTries - (i + 1) == 0:
            print("\nYou have failed to guess the number in the given number of attempts. Better luck next time!")
        else:
            print("You have " + str(numTriesLeft) + " attempts left. ")