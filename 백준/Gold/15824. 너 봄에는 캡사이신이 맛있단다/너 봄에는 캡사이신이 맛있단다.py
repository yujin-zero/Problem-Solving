import sys

def axxb(a,b) :
    if b == 0 :
        return 1
    elif b % 2 == 0 :
        tmp = axxb(a,b/2)
        return tmp * tmp
    tmp = axxb(a,b-1)
    return tmp * a

N = int(sys.stdin.readline())
hot = list(map(int,sys.stdin.readline().split()))
hot.sort()
answer = 0
mod = 1000000007

for i in range(N) :
    min_cnt = axxb(2,N-i-1)
    max_cnt = axxb(2,i)
    answer += (hot[i] * (max_cnt - min_cnt) % mod)

print(answer % mod)