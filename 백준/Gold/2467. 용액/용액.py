import sys

n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))
startIndex = -1
for i in range(n):
    if solution[i] > 0:
        startIndex = i
        break

if startIndex == 0:
    print(solution[0], solution[1])
    exit()
elif startIndex == -1:
    print(solution[n-2], solution[n-1])
    exit()

numMinus = startIndex
numPlus = n - startIndex
zero = float('inf')
answer1, answer2 = 0, 0
left, right = startIndex-1, startIndex
while True:
    tmp = solution[left] + solution[right]
    if abs(tmp) < zero:
        zero = abs(tmp)
        answer1, answer2 = solution[left], solution[right]

    if left == 0 and right == n-1:
        break
    elif left == 0:
        right += 1
    elif right == n-1:
        left -= 1
    elif tmp > 0:
        left -= 1
    else:
        right += 1


if numMinus >= 2:
    if abs(solution[startIndex-1] + solution[startIndex-2]) < zero:
        answer1, answer2 = solution[startIndex-2], solution[startIndex-1]
        zero = abs(solution[startIndex-1] + solution[startIndex-2])
if numPlus >= 2:
    if abs(solution[startIndex] + solution[startIndex+1]) < zero:
        answer1, answer2 = solution[startIndex], solution[startIndex+1]

print(answer1, answer2)
