import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    num = sys.stdin.readline().rstrip()
    if n != 0:
        num = list(map(int, num[1: len(num)-1].split(',')))

    num = deque(num)
    countR = 0
    check = 0
    for i in range(len(p)):
        if p[i] == 'R':
            countR += 1
        elif p[i] == 'D':
            if n == 0:
                check = 1
                break
            if countR % 2 == 0:
                num.popleft()
                n -= 1
            else:
                num.pop()
                n -= 1

    if check == 1:
        print("error")
    else:
        if n == 0:
            print([])
        else:
            if countR % 2 == 1:
                num.reverse()
            print('[', end='')
            for i in range(n):
                if i != n-1:
                    print(num[i], end=',')
                else:
                    print(num[i], end='')
            print(']')
