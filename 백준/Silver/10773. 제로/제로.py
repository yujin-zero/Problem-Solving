import sys

k = int(sys.stdin.readline())
stack = []
sum = 0

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        sum -= stack.pop()
    else:
        stack.append(n)
        sum += n

print(sum)
