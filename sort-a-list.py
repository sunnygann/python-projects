numString = input("Please enter your numbers, delimited by a space: ")

try:
    numList = [int (num) for num in numString.split()]
    sortInstructions = input("Please enter either 'asc', 'desc', or 'none': ")
    sortInstructionsLower = sortInstructions.lower()
    if sortInstructionsLower == 'asc':
        print(sorted(numList))
    elif sortInstructionsLower == 'desc':
        print(sorted(numList, reverse=True))
    elif sortInstructionsLower == 'none':
        print(numList)
    else:
        print("Please enter either 'asc, 'desc', or 'none. ")
except ValueError:
    print("Please do not enter non-numerical characters. ")