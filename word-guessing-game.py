import random

def guessWord(word, wordList, correctGuess, progressList):
    curGuess = input("######################################################################\n"
                     "Guess a character that may be in the word (lowercase): ")
    if curGuess in progressList:
        print("This character has been added. Please choose another.")
        guessWord(word, wordList, correctGuess, progressList)
    else:
        for j in range(len(word)):
            if curGuess == wordList[j]:
                correctGuess = True
                progressList[j] = curGuess
        if correctGuess == True:
            print("You guessed a character right! All instances of the character has been added.")
        else:
            print("You guessed wrong! Try again.")
        print("\n\t" + str(progressList) + "\n")
        if "_" not in progressList:
            print("You won!")
            exit()
        attemptsLeft = (12 - 1 - i)
        if attemptsLeft == 1:
            print("You have " + str(attemptsLeft) + " attempts left. This is your final attempt.")
        else:
            print("You have " + str(attemptsLeft) + " attempts left. ")

playerName = input("\tPlease enter your name: ")
print("\n\tGood Luck, " + playerName
      + "!\n\n######################################################################")

wordsList = ("pineapple", "watermelon", "programming", "repository", "mangosteen", "lemonade")
word = wordsList[random.randint(0, (len(wordsList) - 1))]
print(word)

progress = ""

for i in range(len(word)):
    progress = progress + "_"
print("Your random word has been rolled. You have 12 tries to guess all the characters that make up the word.")

progressList = list(progress)
wordList = list(word)

for i in range(12):
    correctGuess = False
    guessWord(word, wordList, correctGuess, progressList)