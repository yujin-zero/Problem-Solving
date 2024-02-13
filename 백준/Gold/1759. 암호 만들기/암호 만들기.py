import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())
alpha.sort()
for com in combinations(alpha, l):
    i = 0
    for x in com:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            i += 1
    if i >= 1 and (l-i) >= 2:
        print(''.join(com))
