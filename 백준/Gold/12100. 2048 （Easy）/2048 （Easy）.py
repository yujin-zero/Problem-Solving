import sys
import copy

def move_next(move_cnt, current_board) :
    global cnt
    global answer

    if move_cnt == 5 :
        answer = max(answer,max(map(max,current_board)))
        return
    
    for direction in ['up','down','left','right'] :
        new_board = move(copy.deepcopy(current_board), direction)
        if new_board != current_board: 
            move_next(move_cnt + 1, new_board)

    
def move(m_board,way) :
    cant_move = []
    if way == 'up' :
        for i in range(N-1) :
            for j in range(N) :
                if (i,j) in cant_move :
                    continue
                for k in range(i+1,N) :
                    if m_board[k][j] == 0 :
                        continue
                    if m_board[i][j] == 0 :
                        m_board[i][j] = m_board[k][j] 
                        m_board[k][j] = 0
                    elif m_board[i][j] == m_board[k][j] :
                        m_board[i][j] *= 2
                        m_board[k][j] = 0
                        cant_move.append((i,j))
                        break
                    else :
                        break
    elif way == 'down' :
        for i in range(N-1,0,-1) :
            for j in range(N) :
                if (i,j) in cant_move :
                    continue
                for k in range(i-1,-1,-1) :
                    if m_board[k][j] == 0:
                        continue
                    if m_board[i][j] == 0 :
                        m_board[i][j] = m_board[k][j]
                        m_board[k][j] = 0
                    elif m_board[i][j] == m_board[k][j] :
                        m_board[i][j] *= 2
                        m_board[k][j] = 0
                        cant_move.append((i,j))
                        break
                    else :
                        break
    elif way == 'left' :
        for j in range(N-1) :
            for i in range(N) :
                if (i,j) in cant_move :
                    continue
                for k in range(j+1,N) :
                    if m_board[i][k] == 0 :
                        continue
                    if m_board[i][j] == 0:
                        m_board[i][j] = m_board[i][k]
                        m_board[i][k] = 0
                    elif m_board[i][j] == m_board[i][k] :
                        m_board[i][j] *= 2
                        m_board[i][k] = 0
                        cant_move.append((i,j))
                        break
                    else :
                        break
    else :
        for j in range(N-1,0,-1) :
            for i in range(N) :
                if (i,j) in cant_move :
                    continue
                for k in range(j-1,-1,-1) :
                    if m_board[i][k] == 0 :
                        continue
                    if m_board[i][j] == 0 :
                        m_board[i][j] = m_board[i][k]
                        m_board[i][k] = 0
                    elif m_board[i][j] == m_board[i][k] :
                        m_board[i][j] *= 2
                        m_board[i][k] = 0
                        cant_move.append((i,j))
                        break
                    else :
                        break

    return m_board

N = int(sys.stdin.readline())
board = []
for _ in range(N) :
    x = list(map(int,sys.stdin.readline().split()))
    board.append(x)
answer = board[0][0]
cnt = 0

move_next(0,board)

print(answer)