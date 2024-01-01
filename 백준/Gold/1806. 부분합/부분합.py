import sys

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = 100001
left = 0
right = 0
hap = num[0]

while True:
    if hap >= s:
        answer = min(answer, right-left+1)
        hap -= num[left]
        left += 1
    else:
        right += 1
        if right == n:
            break
        hap += num[right]


if answer == 100001:
    answer = 0

print(answer)
