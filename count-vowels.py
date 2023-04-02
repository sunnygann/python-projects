word = input("Please input a word to count vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0

if " " not in word:
    wordList = list(word)
    for word in wordList:
        if word in vowels:
            vowelCount = vowelCount + 1
    print(vowelCount)
elif " " in word:
    print("Please only enter a single word.")



