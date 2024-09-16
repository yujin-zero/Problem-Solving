import sys

X = 1000000007

def multi(x,y) :
    if y == 0 :
        return 1
    elif y % 2 == 0 :
        tmp = multi(x,y//2)
        return tmp*tmp % X
    else :
        tmp = multi(x,y-1)
        return tmp * x % X

m = int(sys.stdin.readline())
answer = 0
for _ in range(m) :
    b, a = map(int,sys.stdin.readline().split())
    answer += (a * multi(b,X-2) % X)
    answer %= X

print(answer)