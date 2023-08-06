import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    word = sys.stdin.readline()
    w = []
    for i in range(len(word)):
        if word[i] not in w:
            w.append(word[i])
        else:
            if w[-1] != word[i]:
                count += 1
                break

print(n-count)
