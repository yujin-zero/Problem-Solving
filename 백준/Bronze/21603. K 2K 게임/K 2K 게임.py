import sys

n,k = map(int,sys.stdin.readline().split())

f_k = k%10
f_2k = (2*k)%10
cnt = 0
answer = []
for i in range(1,n+1):
    f_x = i%10
    if f_x != f_k and f_x != f_2k :
        cnt += 1
        answer.append(i)


print(cnt)
for a in answer :
    print(a,end=' ')