import sys

result = []

while True:
    line = sys.stdin.readline().strip()
    if line == '#':
        break
    count = 0
    for i in range(len(line)):
        if line[i] == 'a' or line[i] == 'e' or line[i] == 'i' or line[i] == 'o' or line[i] == 'u' or line[i] == 'A' or line[i] == 'E' or line[i] == 'O' or line[i] == 'I' or line[i] == 'U':
            count += 1
    result.append(count)


for r in result:
    print(r)
