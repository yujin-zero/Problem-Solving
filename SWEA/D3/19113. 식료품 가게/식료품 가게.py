from collections import deque
tc = int(input())

for k in range(tc):
    n = int(input())
    lst = deque(map(int,input().split()))
    i = 0
    cnt = 0 
    while True :
        x = lst[i]
        lst.remove(x//3*4)
        cnt += 1
        i += 1
        if cnt == n :
            break
    print('#',end='')
    print(k+1,end=' ')
    for value in lst :
        print(value,end=' ')
    print()