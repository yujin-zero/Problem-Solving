import sys


def iterative_power(x, y, mod):
    result = 1
    x %= mod
    while y > 0:
        if y % 2 == 1:
            result = (result*x) % mod
        x = (x*x) % mod
        y //= 2
    return result


a, b, c = map(int, sys.stdin.readline().split())
answer = iterative_power(a, b, c)
print(answer)
