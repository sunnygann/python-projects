word = input("Please enter a string: ")
xCount = 0
oCount = 0

for i in word:
    if i.lower() == 'x':
        xCount += 1
    elif i.lower() == 'o':
        oCount += 1

if xCount == oCount:
    print('True')
else:
    print('False')
