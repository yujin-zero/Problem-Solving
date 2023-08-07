import sys
from itertools import product

n = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())

if m == 0:
    print(min(len(n), abs(int(n)-100)))
    sys.exit()

cant = set(map(int, sys.stdin.readline().split()))
if m == 10:
    print(abs(int(n)-100))
    sys.exit()

if m == 9 and 0 not in cant:  # 0만 누를 수 있음
    print(min(abs(int(n)-100), int(n)+1))
    sys.exit()
can = []
for i in range(10):
    if i not in cant:
        can.append(i)


k = float('inf')
count = 0
t = 0
m = abs(int(n)-100)
# len(n)-1
l = len(n)-1
if len(n)-1 < 1:
    l = 1
for r in range(l, len(n)+2):
    for combo in product(can, repeat=r):
        combined_number = int(''.join(map(str, combo)))
        if len(str(combined_number)) > len(n):
            count += 1
            if count > 1:
                t = 1
                break

        temp = 0
        for j in range(len(str(combined_number))):
            if int(str(combined_number)[j]) in cant:
                temp = 1
        if temp == 0:
            now = len(str(combined_number)) + abs(int(n)-combined_number)
            if k > now:
                k = now
    if t == 1:
        break

print(min(k, m))
