import sys
import itertools

# 비둘기집 원리

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    n = int(sys.stdin.readline())
    mbti = list(sys.stdin.readline().split())
    mbti_dict = {}
    for m in mbti:
        if m in mbti_dict:
            mbti_dict[m] += 1
        else:
            mbti_dict[m] = 1

    often = max(mbti_dict.values())

    if often >= 3:
        result.append(0)
    else:
        combinations = list(set(itertools.combinations(mbti, 3)))
        com_min = 50
        for c in combinations:
            sum = 0
            for i in range(4):
                if c[0][i] != c[1][i]:
                    sum += 1
                if c[0][i] != c[2][i]:
                    sum += 1
                if c[1][i] != c[2][i]:
                    sum += 1
            if com_min > sum:
                com_min = sum
            if sum == 2:
                break

        result.append(com_min)

for r in result:
    print(r)
