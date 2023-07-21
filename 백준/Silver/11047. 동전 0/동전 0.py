import sys

n, k = map(int, sys.stdin.readline().split())
money = []
count = 0

for _ in range(n):
    x = int(sys.stdin.readline())
    if x <= k:
        money.append(x)

i = len(money)-1
while k != 0:
    if money[i] <= k:
        y = k//money[i]
        k -= money[i]*y
        count += y
    i -= 1

print(count)
