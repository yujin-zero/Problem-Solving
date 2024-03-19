import sys
input = sys.stdin.readline

palindrome_count_list = [0, 9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000]

n = int(input())
len_n = len(str(n))
answer = 0
for i in range(1, len_n):
    answer += palindrome_count_list[i]

if (len_n % 2 == 0):  # 짝
    temp = 10 ** (len_n // 2 - 1)
    while True:
        left = str(temp)
        right = str(temp)[::-1]
        result = left + right

        if (int(result) <= int(n)):
            temp += 1
            answer += 1
        else:
            break
else:
    temp = 10 ** (len_n // 2)
    while True:
        left = str(temp)
        right = str(temp)[:-1][::-1]
        result = left + right

        if (int(result) <= int(n)):
            temp += 1
            answer += 1
        else:
            break

print(answer)
