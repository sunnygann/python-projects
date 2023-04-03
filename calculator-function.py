try:
    firstNum = int(input("Please enter the first number: "))
    operator = input("Please enter a mathematical operator (+ - * /): ")
    secondNum = int(input("Please enter the second number: "))

    if operator == '*':
        print(firstNum * secondNum)
    elif operator == '/':
        print(firstNum / secondNum)
    elif operator == '+':
        print(firstNum + secondNum)
    elif operator == '-':
        print(firstNum - secondNum)
    else:
        print("Please provide a valid operator. ")
        exit()
except ValueError:
    print("Please enter a valid integer value. ")
