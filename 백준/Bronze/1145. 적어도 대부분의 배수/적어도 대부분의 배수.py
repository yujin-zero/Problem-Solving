import sys

num = list(map(int,sys.stdin.readline().split()))
answer = 4

while True :
    tmp = 0
    for i in range(5) :
        if answer%num[i] == 0 :
            tmp += 1
    if tmp > 2 :
        print(answer)
        sys.exit(0) 

    answer += 1
