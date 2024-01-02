import sys


def able(row, col):
    for i in range(row):
        if board[i] == col or (row-i) == abs(col-board[i]):
            return False
    return True


def queen(row):
    global count
    if row == n:
        count += 1
        return
    for i in range(n):
        if able(row, i):
            board[row] = i
            queen(row+1)


n = int(sys.stdin.readline())
board = [-1]*n
count = 0
queen(0)
print(count)
