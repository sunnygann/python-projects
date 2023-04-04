n = int(input())
scores = map(int, input().split())

scores = list(scores)
runnerUp = 0
if n == len(scores):
    for score in scores:
        if not score < -100 or score > 100:
            sortedScores = sorted(scores)
        else:
            exit()
    for i in range(n):
        if not sortedScores[n - 1] == sortedScores[n - i - 1]:
            runnerUp = sortedScores[n - i - 1]
            break
    print(runnerUp)
else:
    exit()
    
