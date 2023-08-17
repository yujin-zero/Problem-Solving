import sys

a, p = map(int, sys.stdin.readline().split())

i = 1
num = {}
num[a] = i

while True:
    x = str(a)
    y = 0
    for j in x:
        y += int(j)**p
    i += 1
    if y in num:
        answer = num[y]
        break
    num[y] = i
    a = y

print(answer-1)
