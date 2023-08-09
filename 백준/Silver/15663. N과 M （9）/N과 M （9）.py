import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
answer = list(set(permutations(lst, m)))
answer.sort()

for a in answer:
    for i in range(m):
        print(a[i], end=' ')
    print()
