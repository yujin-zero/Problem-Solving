import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

count = 0
for i in range(0, m-2*n):
    if s[i] == 'I':
        temp = 1
        check = 0
        for j in range(i+1, 2*n + i+1):
            if temp == 1:
                if s[j] == 'O':
                    temp = 0
                else:
                    check = 1
                    break
            else:
                if s[j] == 'I':
                    temp = 1
                else:
                    check = 1
                    break
    else:
        check = 1
    if check == 0:
        count += 1


print(count)
