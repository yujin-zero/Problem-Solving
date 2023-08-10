import sys

n = int(sys.stdin.readline())
Red = 0
Green = 0
Blue = 0

for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    tempRed = min(Green, Blue)
    tempGreen = min(Red, Blue)
    tempBlue = min(Red, Green)

    Red = tempRed + r
    Green = tempGreen + g
    Blue = tempBlue + b


print(min(Red, Green, Blue))
