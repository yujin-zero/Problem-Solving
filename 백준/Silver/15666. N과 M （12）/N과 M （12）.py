import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
num = list(set(map(int, sys.stdin.readline().split())))
num.sort()

answer = list(itertools.combinations_with_replacement(num, m))

for a in answer:
    print(*a)
