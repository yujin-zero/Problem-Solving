import sys

a, b = map(int, sys.stdin.readline().split())
i = 2
answer = 1
while True:
    if a % i == 0 and b % i == 0:
        answer *= i
        a //= i
        b //= i
    elif a % i == 0:
        answer *= i
        a //= i
    elif b % i == 0:
        answer *= i
        b //= i
    else:
        i += 1

    if a == 1 and b == 1:
        break

print(answer)
