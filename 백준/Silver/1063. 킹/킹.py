import sys
from collections import deque

king, stone, n = sys.stdin.readline().split()
king_row, king_col = int(king[1]), ord(king[0])  # 숫자, 알파벳
stone_row, stone_col = int(stone[1]), ord(stone[0])
n = int(n)

for _ in range(n):
    x = sys.stdin.readline()
    temp_row, temp_col = king_row, king_col
    t_r, t_c = stone_row, stone_col
    for i in range(len(x)):
        y = x[i]
        if y == 'R':
            king_col += 1
        elif y == 'L':
            king_col -= 1
        elif y == 'B':
            king_row -= 1
        elif y == 'T':
            king_row += 1

    if king_row == stone_row and king_col == stone_col:
        stone_row += (king_row - temp_row)
        stone_col += (king_col - temp_col)

    if stone_row < 1 or stone_row > 8 or stone_col < ord('A') or stone_col > ord('H') or king_row < 1 or king_row > 8 or king_col < ord('A') or king_col > ord('H'):
        king_row, king_col = temp_row, temp_col
        stone_row, stone_col = t_r, t_c

print(chr(king_col), end='')
print(king_row)
print(chr(stone_col), end='')
print(stone_row)
