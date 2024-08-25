import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
result = []

indexA = 0
indexB = 0
tmp = 100

while True :
    if tmp in a[indexA:n] and tmp in b[indexB:m] :
        result.append(tmp)
        for i in range(indexA, n) :
            if a[i] == tmp :
                indexA = i+1
                break
        for i in range(indexB, m) :
            if b[i] == tmp :
                indexB = i+1
                break
    else :
        tmp -= 1

        if tmp < 1 :
            break
 

if result :
    print(len(result))
    print(*result)
else :
    print(0)