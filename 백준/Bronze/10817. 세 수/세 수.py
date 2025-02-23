import sys

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
print(lst[1])
