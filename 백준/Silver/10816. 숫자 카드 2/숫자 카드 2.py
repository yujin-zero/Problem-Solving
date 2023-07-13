from collections import defaultdict
import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

count = defaultdict(int)  # int :기본값 0
for v in card:
    count[v] += 1

for i in x:
    print(count[i], end=' ')
