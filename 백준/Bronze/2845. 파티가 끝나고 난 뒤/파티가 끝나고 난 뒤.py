import sys

l, p = map(int, sys.stdin.readline().split())
answer = l*p
news = list(map(int, sys.stdin.readline().split()))
for n in news:
    print(n-answer, end=' ')
print()
