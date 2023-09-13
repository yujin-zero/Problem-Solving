import sys

n = int(sys.stdin.readline())
answer = []
for _ in range(n):
    x = int(sys.stdin.readline())
    for i in range(2, x+1):
        temp = 0
        while x % i == 0:
            temp += 1
            x /= i
        if temp != 0:
            answer.append([i, temp])

for a in answer:
    print(*a)
