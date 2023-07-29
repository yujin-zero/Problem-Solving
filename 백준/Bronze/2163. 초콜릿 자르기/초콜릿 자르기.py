import sys


def chocolate(a, b):
    global count
    if not (a == 1 and b == 1):
        count += 1
        if a > b:
            temp = a//2
            chocolate(temp, b)
            chocolate(a-temp, b)
        else:
            temp = b//2
            chocolate(a, temp)
            chocolate(a, b-temp)


n, m = map(int, sys.stdin.readline().split())

count = 0
chocolate(n, m)
print(count)
