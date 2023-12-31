import sys

n, m = map(int, sys.stdin.readline().split())
paper = [[0 for _ in range(m+3)] for _ in range(n+3)]
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        paper[i][j] = x[j]

answer = 0
for i in range(n):
    for j in range(m):
        x = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1]
        if x > answer:
            answer = x
##
        x = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]
        if x > answer:
            answer = x

        x = paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2] + paper[i][j+2]
        if x > answer:
            answer = x
##
        x = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
        if x > answer:
            answer = x

        x = paper[i][j+1] + paper[i][j+2] + paper[i+1][j] + paper[i+1][j+1]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2]
        if x > answer:
            answer = x

        x = paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j]
        if x > answer:
            answer = x
##
        x = paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j] + paper[i+2][j+1]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+2][j]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]
        if x > answer:
            answer = x
##
        x = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1]
        if x > answer:
            answer = x

        x = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1]
        if x > answer:
            answer = x

        x = paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
        if x > answer:
            answer = x

        x = paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
        if x > answer:
            answer = x

print(answer)
