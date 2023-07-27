import sys


def count(n, x, y):
    global white, blue
    color = colorPaper[x][y]
    if n == 1:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        temp = 0
        for i in range(x, x+n):
            for j in range(y, y+n):
                if color != colorPaper[i][j]:
                    count(n//2, x, y)
                    count(n//2, x, y+n//2)
                    count(n//2, x+n//2, y)
                    count(n//2, x+n//2, y+n//2)
                    temp = 1
                    break
            if temp == 1:
                break
        if temp == 0:
            if color == 0:
                white += 1
            else:
                blue += 1


n = int(sys.stdin.readline())
colorPaper = []
for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    colorPaper.append(x)

white = 0
blue = 0
x = 0
y = 0
count(n, x, y)
print(white)
print(blue)
