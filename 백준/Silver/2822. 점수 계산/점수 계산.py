import sys

score = []
for _ in range(8):
    score.append(int(sys.stdin.readline()))
score2 = score
score2 = sorted(score2)
score2 = score2[3:8]

print(sum(score2))
for i in range(8):
    if score[i] in score2:
        print(i+1, end=' ')
print()
