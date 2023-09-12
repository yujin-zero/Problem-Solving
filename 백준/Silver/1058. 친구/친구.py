import sys

n = int(sys.stdin.readline())
friend = [[] for _ in range(n)]
two_friend = []

for i in range(n):
    people = sys.stdin.readline()
    for j in range(n):
        if people[j] == 'Y':
            friend[i].append(j)
    two_friend.append(len(friend[i]))

for i in range(n):
    for j in range(n):
        if j not in friend[i]:
            if i != j:
                for f in friend[i]:
                    if j in friend[f]:
                        two_friend[i] += 1
                        break

print(max(two_friend))
