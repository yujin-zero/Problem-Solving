import sys

N = int(sys.stdin.readline())
input = []
B = dict()
for _ in range(N) :
    a, b = map(int,sys.stdin.readline().split())
    input.append((a,b))
    B[b] = a
input.sort()

lis = []
total = []
answer = []
find_idx = -1

for _, value in input :
    if not lis or value > lis[-1] :
        lis.append(value)
        total.append((len(lis),value))
        find_idx = len(lis)
    else :
        left = 0
        right = len(lis)-1

        while left <= right :
            mid = (left+right)//2

            if lis[mid] > value :
                right = mid-1
            else : 
                left = mid+1
        
        lis[left] = value
        total.append((left+1,value))

for i in range(len(total)-1,-1,-1) :
    idx, num = total[i]
    if idx == find_idx :
        find_idx -= 1
    else :
        answer.append(B[num])

answer.sort()
print(len(answer))
for a in answer :
    print(a)