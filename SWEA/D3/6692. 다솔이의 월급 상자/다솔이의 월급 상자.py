t = int(input())

for i in range(1,t+1) :
    n = int(input())
    answer = 0
    for _ in range(n) :
        p,x = map(float,input().split())
        answer += p*x
    print('#%d %.6f' % (i,answer))