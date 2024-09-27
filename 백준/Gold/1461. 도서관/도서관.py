import sys

n, m = map(int,sys.stdin.readline().split())
book = [0] + list(map(int,sys.stdin.readline().split()))
book.sort()
home_index = -1
answer = 0
for i in range(n+1) :
    if book[i] == 0 :
        home_index = i
        break

left_index = m
while left_index < home_index :
    answer += (-book[left_index] * 2)
    left_index += m

right_index = n - m
while home_index < right_index :
    answer += (book[right_index] * 2)
    right_index -= m

if -book[0] < book[n] :
    answer += (-book[0] * 2 + book[n])
else :
    answer += (book[n] * 2 + -book[0])

print(answer)