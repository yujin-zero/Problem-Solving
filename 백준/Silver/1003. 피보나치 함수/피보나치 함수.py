import sys

t = int(sys.stdin.readline())
fibonacci = []
case = []
for _ in range(t):
    x = int(sys.stdin.readline())
    case.append(x)
fibonacci.append([1, 0])
fibonacci.append([0, 1])

for i in range(2, max(case)+1):
    fibonacci.append([fibonacci[i-1][0]+fibonacci[i-2][0],
                     fibonacci[i-1][1]+fibonacci[i-2][1]])

for i in range(len(case)):
    print(fibonacci[case[i]][0], fibonacci[case[i]][1])
