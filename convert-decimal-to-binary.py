try:
    decimalNum = int(input("Please enter a decimal number to be converted into binary: "))

    decimalNum2 = decimalNum
    binaryLen = 0
    while decimalNum2 > 1:
        decimalNum2 = decimalNum2 / 2
        binaryLen = binaryLen + 1

    binaryList = []
    for i in range(binaryLen):
        if decimalNum > decimalNum % pow(2, binaryLen - i - 1):
            decimalNum = decimalNum % pow(2, binaryLen - i - 1)
            binaryList.append(1)
        else:
            binaryList.append(0)

    binary = ''
    for i in binaryList:
        binary = binary + str(i)
    print(binary)

except ValueError:
    print("Please enter a valid integer value.")
