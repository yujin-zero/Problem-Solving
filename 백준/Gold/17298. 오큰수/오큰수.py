import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
NGE = [-1] * N
stack = []

for i in range(N) :
    while stack and A[stack[-1]] < A[i] :
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)