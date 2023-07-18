import sys

k, n = map(int, sys.stdin.readline().split())
line = []
for _ in range(k):
    line.append(int(sys.stdin.readline().strip()))
line.sort()

start = 1
end = line[-1]

while end-start > 1:
    mid = (start+end)//2  # 길이
    count = 0
    for i in range(k):
        count += line[i]//mid

    if count < n:
        end = mid
    else:
        start = mid

count = 0
for i in range(k):
    count += line[i]//end
if count >= n:
    print(end)
else:
    print(start)
