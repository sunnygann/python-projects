ccNum = input("Please input your credit card number: ")

ccNumList = list(ccNum)
censoredCc = ''
if not ccNum.isdigit():
    print("Please enter integer values only. ")
else:
    for i in range(len(ccNum) - 4):
        ccNumList[i] = '*'

    for i in ccNumList:
        censoredCc = censoredCc + i

    print(censoredCc)


