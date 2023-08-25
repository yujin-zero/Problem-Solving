import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = list(product(num, repeat=m))
answer.sort()

for a in answer:
    print(*a)
