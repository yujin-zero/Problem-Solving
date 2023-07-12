import sys

n = int(sys.stdin.readline())
people = []

for _ in range(n):
    info = sys.stdin.readline()
    people.append(info.split())

people.sort(key=lambda x: int(x[0]))
# print(people)

for i in people:
    print(i[0], i[1])
