import sys

x = int(sys.stdin.readline())
n = []
while x > 0:
    n.append(x % 10)
    x //= 10
n.sort(reverse=True)
for i in n:
    print(i, end='')
