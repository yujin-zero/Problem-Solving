import sys
import math

n = sys.stdin.readline()
l = len(n)-1
n = int(n)
num = [0 for _ in range(10)]

i = 0
while n > 0:
    x = int(n % 10)
    num[x] += 1
    n //= 10
    i += 1
num[0] += l-i

answer = 0
six = 0
for i in range(10):
    if i == 6 or i == 9:
        six += num[i]
    else:
        if answer < num[i]:
            answer = num[i]

six = math.ceil(six/2)
if six > answer:
    answer = six

print(answer)
