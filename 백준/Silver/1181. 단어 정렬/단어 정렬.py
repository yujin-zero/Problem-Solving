import sys

n = int(sys.stdin.readline())
word = []

for _ in range(n):
    x = sys.stdin.readline()
    word.append(x)

word = list(set(word))

word.sort(key=lambda x: (len(x), x))

for i in word:
    print(i, end='')
