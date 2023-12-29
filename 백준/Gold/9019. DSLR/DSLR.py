import sys
from collections import deque

t = int(sys.stdin.readline())


def D(n):
    n *= 2
    if n > 9999:
        n %= 10000
    return n


def S(n):
    n -= 1
    if n == -1:
        n = 9999
    return n


def L(n):
    x = n//1000
    n %= 1000
    n *= 10
    n += x
    return n


def R(n):
    x = n % 10
    n //= 10
    n += x*1000
    return n


for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    visit = set()
    queue = deque([(a, "")])
    while queue:
        num, command = queue.popleft()

        if num == b:
            print(command)
            break

        if num not in visit:
            visit.add(num)

            queue.append((D(num), command+"D"))
            queue.append((S(num), command+"S"))
            queue.append((L(num), command+"L"))
            queue.append((R(num), command+"R"))
