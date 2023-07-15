import sys
import math

# 에라토스테네스의 체 알고리즘
m, n = map(int, sys.stdin.readline().split())
prime = [True]*(n+1)  # prime[i]가 Ture면 i가 소수
prime[0] = False
prime[1] = False

# i가 소수면 그 배수들은 소수가 아님
for i in range(2, int(math.sqrt(n))+1):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False

for i in range(m, n+1):
    if prime[i]:
        print(i)
