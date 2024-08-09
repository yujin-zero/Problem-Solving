import sys

def DFS(num, oper, i, j) :
    global maxAnswer, minAnswer

    value = graph[i][j]
    if value == '+' or value == '-' or value == '*' :
        if i+1 < n :
            DFS(num, value, i+1, j)
        if j+1 < n :
            DFS(num, value, i, j+1)
    else :
        value = int(value)
        if oper == '+' :
            tmp = num + value
        elif oper == '-' :
            tmp = num - value
        else :
            tmp = num * value

        if i == n-1 and j == n-1 :
            maxAnswer = max(maxAnswer, tmp)
            minAnswer = min(minAnswer, tmp)
        
        if i+1 < n :
            DFS(tmp, oper, i+1, j)
        if j+1 < n :
            DFS(tmp, oper, i, j+1)

n = int(sys.stdin.readline())
graph = []
for _ in range(n) :
    x = list(sys.stdin.readline().split())
    graph.append(x)

firstNum = int(graph[0][0])
minAnswer = float('inf')
maxAnswer = -minAnswer
DFS(firstNum, '+', 0, 1)
DFS(firstNum, '+', 1, 0)

print(maxAnswer, minAnswer)