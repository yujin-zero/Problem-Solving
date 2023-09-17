import sys

palindrom = sys.stdin.readline().rstrip()
# answer2 = float('inf')
i = len(palindrom)//2
while i < len(palindrom):
    c = 1
    temp = 0
    while i+c < len(palindrom):
        if palindrom[i-c] != palindrom[i+c]:
            temp = 1  # 팰린드롬이 아님
            break
        c += 1
    if temp == 0:
        answer1 = 2*i + 1
        break

    i += 1

if len(palindrom) % 2 == 0:
    i = len(palindrom)//2-1
else:
    i = len(palindrom)//2
while i < len(palindrom):
    c = 0
    temp = 0
    while i+c+1 < len(palindrom):
        if palindrom[i-c] != palindrom[i+1+c]:
            temp = 1
            break
        c += 1
    if temp == 0:
        answer2 = (i+1)*2
        break
    i += 1


print(min(answer1, answer2))
