n = int(input())

list = []

for i in range(n):
    command = input()
    commandSplit = command.split()
    if commandSplit[0] == 'insert':
        list.insert(int(commandSplit[1]), int(commandSplit[2]))
    elif commandSplit[0] == 'print':
        print(list)
    elif commandSplit[0] == 'remove':
        list.remove(int(commandSplit[1]))
    elif commandSplit[0] == 'append':
        list.append(int(commandSplit[1]))
    elif commandSplit[0] == 'sort':
        list = sorted(list)
    elif commandSplit[0] == 'pop':
        list.pop()
    elif commandSplit[0] == 'reverse':
        list.reverse()