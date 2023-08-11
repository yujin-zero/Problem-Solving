import sys

n = int(sys.stdin.readline())
minL, minM, minR = 0, 0, 0
maxL, maxM, maxR = 0, 0, 0

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())

    minL_t = min(minL, minM)
    minM_t = min(minL, minM, minR)
    minR_t = min(minM, minR)
    maxL_t = max(maxL, maxM)
    maxM_t = max(maxL, maxM, maxR)
    maxR_t = max(maxM, maxR)

    minL = minL_t + a
    minM = minM_t + b
    minR = minR_t + c
    maxL = maxL_t + a
    maxM = maxM_t + b
    maxR = maxR_t + c

print(max(maxL, maxM, maxR), min(minL, minM, minR))
