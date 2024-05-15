n = int(input())

for i in range(1,n+1):
    cnt = 0 # 박수 횟수
    x = i
    while x>0:
        if (x%10)%3 == 0 and x%10!=0:
            cnt += 1
        x //= 10
    if cnt == 0:
        print(i,end=' ')
    else :
        for j in range(cnt):
            print('-',end='')
        print(' ',end='')