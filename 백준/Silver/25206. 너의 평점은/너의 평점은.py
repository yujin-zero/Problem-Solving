import sys

hakjum = 0
hap = 0
for _ in range(20):
    x = sys.stdin.readline().split()
    h = float(x[1])
    grade = x[2]
    if grade == "A+":
        hap += 4.5 * h
        hakjum += h
    elif grade == "A0":
        hap += 4.0 * h
        hakjum += h
    elif grade == "B+":
        hap += 3.5 * h
        hakjum += h
    elif grade == "B0":
        hap += 3.0 * h
        hakjum += h
    elif grade == "C+":
        hap += 2.5 * h
        hakjum += h
    elif grade == "C0":
        hap += 2.0 * h
        hakjum += h
    elif grade == "D+":
        hap += 1.5 * h
        hakjum += h
    elif grade == "D0":
        hap += 1.0 * h
        hakjum += h
    elif grade == "F":
        hakjum += h


print(hap/hakjum)
