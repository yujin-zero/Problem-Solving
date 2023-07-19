import sys

m = int(sys.stdin.readline())
s = []

for _ in range(m):
    x = sys.stdin.readline()
    if "add" in x:
        y = int(x.split()[1])
        if y not in s:
            s.append(y)
    elif "remove" in x:
        y = int(x.split()[1])
        if y in s:
            s.remove(y)
    elif "check" in x:
        y = int(x.split()[1])
        if y in s:
            print(1)
        else:
            print(0)
    elif "toggle" in x:
        y = int(x.split()[1])
        if y in s:
            s.remove(y)
        else:
            s.append(y)
    elif "all" in x:
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16, 17, 18, 19, 20]
    elif "empty" in x:
        s = []
