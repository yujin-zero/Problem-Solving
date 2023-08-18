import sys

n, m = map(int, sys.stdin.readline().split())
six = float('inf')
one = float('inf')
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x < six:
        six = x
    if y < one:
        one = y

if one*6 < six:
    print(one*n)
else:
    print(min(six*(n//6) + one*(n % 6), six*(n//6+1)))
