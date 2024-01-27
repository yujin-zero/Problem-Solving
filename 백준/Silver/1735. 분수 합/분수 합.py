import sys


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
a = x1*y2 + x2*y1
b = y1*y2

while True:
    i = gcd(a, b)
    if i == 1:
        break
    a //= i
    b //= i

print(a, b)
