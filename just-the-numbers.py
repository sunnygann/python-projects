userInput = input("Please enter a list of values delimited by ' ': ")

inputList = userInput.split()
numList = []

for value in inputList:
    if value.isdigit():
        numList.append(value)

print(numList)
