t = int(input())
result = []

for _ in range(t):
    n, k = map(int,input().split())
    candy = list(map(int,input().split()))
    candy.sort()
    answer = float('inf')

    for i in range(n-k+1):
        tmp = candy[i+k-1] - candy[i]
        if tmp < answer :
            answer = tmp
    result.append(answer)

for i in range(t) :
    print('#%d %d'%(i+1,result[i]))