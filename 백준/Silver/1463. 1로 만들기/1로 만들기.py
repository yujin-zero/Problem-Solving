import sys

n = int(sys.stdin.readline())

num = [0, 0, 1, 1]
if n >= 4:
    for i in range(4, n+1):
        x3 = num[i-1]+1
        x1 = x2 = x3
        if i % 3 == 0:
            x1 = num[i//3] + 1
        if i % 2 == 0:
            x2 = num[i//2] + 1
        num.append(min(x1, x2, x3))

print(num[n])
