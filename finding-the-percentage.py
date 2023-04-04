n = int(input())

stuDict = {}
if not n < 2 or n > 10:
    for x in range(n):
        stuScores = input()
        scoresSplit = stuScores.split()
        #print(scoresSplit)
        #print(scoresSplit[0])
        stuName = scoresSplit[0]
        scoresSplit.remove(scoresSplit[0])
        #print(scoresSplit)
        if len(scoresSplit) == 3:
            stuDict[stuName] = scoresSplit
        else:
            exit()

    queryName = input()
    total = 0
    count = 0
    for x in stuDict[queryName]:
        if float(x) <= 100:
            total += float(x)
            count += 1
        else:
            exit()
    print("{:.2f}".format(total / count))