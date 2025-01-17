import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
F = dict()
for a in A : 
    if a in F :
        F[a] += 1
    else :
        F[a] = 1
NGF = [-1] * N
stack = []

for i in range(N) :
    Fi = F[A[i]]

    while stack and F[A[stack[-1]]] < Fi :
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)