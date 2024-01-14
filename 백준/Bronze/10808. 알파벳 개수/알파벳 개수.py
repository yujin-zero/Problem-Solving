import sys
word = sys.stdin.readline().rstrip()
alpha = [0 for _ in range(26)]
for i in range(len(word)):
    alpha[ord(word[i])-97] += 1
for a in alpha:
    print(a, end=' ')
