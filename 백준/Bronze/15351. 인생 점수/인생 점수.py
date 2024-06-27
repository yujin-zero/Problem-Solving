import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    x = list(sys.stdin.readline().rstrip())
    score = 0
    for xx in x :
        if xx != ' ' :
            score += ord(xx) -64
    if score == 100 :
        print("PERFECT LIFE")
    else :
        print(score)