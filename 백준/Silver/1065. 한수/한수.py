import sys
n = int(sys.stdin.readline())
count = 0
for i in range(1, n+1):
    x = str(i)
    temp = 0
    for j in range(len(x)):
        if j == 1:
            sub = int(x[j])-int(x[j-1])
        elif j > 1:
            if sub != (int(x[j])-int(x[j-1])):
                temp = 1
    if temp == 0:
        count += 1

print(count)
