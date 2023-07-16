import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []
sum = 0

for _ in range(n):
    x = int(sys.stdin.readline())
    num.append(x)
    sum += x

print(round(sum/n+0.00001))
num.sort()
print(num[n//2])
counter = Counter(num)
if n >= 2:
    if counter.most_common()[0][1] == counter.most_common()[1][1]:
        print(counter.most_common()[1][0])
    else:
        print(counter.most_common()[0][0])
else:
    print(num[0])
print(num[-1]-num[0])
