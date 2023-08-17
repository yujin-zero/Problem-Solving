import sys

a, b = sys.stdin.readline().split()
k = len(b)-len(a)
count = 51
for i in range(k+1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            temp += 1
    if temp < count:
        count = temp
print(count)
