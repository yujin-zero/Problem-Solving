import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
sortedX = sorted(list(set(x)))

dic = {}
count = 0
for i in sortedX:
    dic[i] = count
    count += 1

for value in x:
    print(dic[value], end=' ')
print()
