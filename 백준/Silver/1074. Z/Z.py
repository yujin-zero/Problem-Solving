import sys

n, r, c = map(int, sys.stdin.readline().split())

temp = 4**(n-1)  # 4
answer = 0
while n > 0:
    k = 2**(n-1)  # 2
    if (r < k) and (c < k):
        set = 1
    elif (r < k) and (c >= k):
        answer += temp
    elif (r >= k) and (c < k):
        answer += temp*2  # 8
    else:
        answer += temp*3
    n -= 1  # 1
    temp /= 4  # 1
    r %= k
    c %= k

print(int(answer))