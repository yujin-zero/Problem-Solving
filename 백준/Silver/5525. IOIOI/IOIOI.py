import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

# I와 O로 이루어진 패턴 생성
pattern = 'I' + 'OI'*n
count = 0
i = 0

while i < m - len(pattern) + 1:
    # 패턴의 일치 여부를 확인
    if s[i:i + len(pattern)] == pattern:
        count += 1
    i += 1

print(count)