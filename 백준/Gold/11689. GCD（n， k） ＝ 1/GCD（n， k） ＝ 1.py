import sys


def prime_factor(x):
    factors = set()

    while x % 2 == 0:
        x //= 2
        factors.add(2)

    for i in range(3, int(x ** (1/2))+1, 2):
        if x == 1:
            break

        while x % i == 0:
            x //= i
            factors.add(i)

    if x > 1:
        factors.add(x)

    return factors


n = int(sys.stdin.readline())
answer = n
for i in prime_factor(n):
    answer *= (1-1/i)
print(int(answer))