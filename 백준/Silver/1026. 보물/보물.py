import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
answer = 0
for i in range(n):
    answer += A[i]*B[i]

print(answer)
