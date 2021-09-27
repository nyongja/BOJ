import sys
from collections import deque
import copy

n = int(input())
#board = [list(map(int, input().split())) for _ in range(n)]
board =  [[512, 0, 256, 0], [256, 64, 0, 32], [128, 64, 512, 0], [8, 8, 16, 512]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    return True

queue = deque([(board, 0)])
max_n = 0
while queue :
    _board, cnt = queue.popleft()
    print("****_board : ")
    for i in _board :
        print(*i)
    #print('')
    #if cnt == 5 :
    for i in _board :
        max_n = max(max_n, max(i))
    if cnt == 5 :        
        continue
    for i in range(4) :
        n_board = copy.deepcopy(_board)
        can_merged = [[True] * (n) for _ in range(n)]
        print("*****n_board : ")
        for j in n_board :
            print(*j)
        print('')
        if i == 0 : # 상
            for x in range(n) :
                for y in range(n) :
                    value = n_board[x][y]
                    nx, ny = x + dx[i], y + dy[i]
                    n_board[x][y] = 0
                    while chk_pos(nx, ny) :
                        if n_board[nx][ny] == value and can_merged[nx][ny] == True: # 같은 값이면 
                            n_board[nx][ny] = value * 2
                            can_merged[nx][ny] = False
                            break
                        elif n_board[nx][ny] != 0 : # 다른 값이 막고 있으면
                            n_board[nx-dx[i]][ny-dy[i]] = value
                            break
                        elif n_board[nx][ny] == 0 : # 아예 빈 칸이면 
                            nx, ny = nx + dx[i], ny + dy[i]
                    if chk_pos(nx, ny) == False :
                        n_board[nx-dx[i]][ny-dy[i]] = value
            print("i : ", i, "cnt : ", cnt)
            for b in n_board :
                print(*b)
            print('')
                    
            queue.append((n_board, cnt+1))
        elif i == 1 : # 하
            for x in range(n-1, -1, -1) :
                for y in range(n) :
                    value = n_board[x][y]
                    nx, ny = x + dx[i], y + dy[i]
                    n_board[x][y] = 0
                    while chk_pos(nx, ny) :
                        if n_board[nx][ny] == value and can_merged[nx][ny] == True: # 같은 값이면 
                            n_board[nx][ny] = value * 2
                            can_merged[nx][ny] = False
                            break
                        elif n_board[nx][ny] != 0 : # 다른 값이 막고 있으면
                            n_board[nx-dx[i]][ny-dy[i]] = value
                            break
                        elif n_board[nx][ny] == 0 : # 아예 빈 칸이면 
                            nx, ny = nx + dx[i], ny + dy[i]
                    if chk_pos(nx, ny) == False :
                        n_board[nx-dx[i]][ny-dy[i]] = value
            print("i : ", i)
            for b in n_board :
                print(*b)
            print('')
            queue.append((n_board, cnt+1))
        elif i == 2 : # 좌
            for y in range(n) :
                for x in range(n) :
                    value = n_board[x][y]
                    nx, ny = x + dx[i], y + dy[i]
                    n_board[x][y] = 0
                    while chk_pos(nx, ny) :
                        if n_board[nx][ny] == value and can_merged[nx][ny] == True: # 같은 값이면 
                            n_board[nx][ny] = value * 2
                            can_merged[nx][ny] = False
                            break
                        elif n_board[nx][ny] != 0 : # 다른 값이 막고 있으면
                            n_board[nx-dx[i]][ny-dy[i]] = value
                            break
                        elif n_board[nx][ny] == 0 : # 아예 빈 칸이면 
                            nx, ny = nx + dx[i], ny + dy[i]
                    if chk_pos(nx, ny) == False :
                        n_board[nx-dx[i]][ny-dy[i]] = value
            print("i : ", i)
            for b in n_board :
                print(*b)
            print('')
            queue.append((n_board, cnt+1))
        elif i == 3 : # 우
            for y in range(n-1, -1, -1) :
                for x in range(n) :
                    value = n_board[x][y]
                    nx, ny = x + dx[i], y + dy[i]
                    n_board[x][y] = 0
                    while chk_pos(nx, ny) :
                        if n_board[nx][ny] == value and can_merged[nx][ny] == True: # 같은 값이면 
                            n_board[nx][ny] = value * 2
                            can_merged[nx][ny] = False
                            break
                        elif n_board[nx][ny] != 0 : # 다른 값이 막고 있으면
                            n_board[nx-dx[i]][ny-dy[i]] = value
                            break
                        elif n_board[nx][ny] == 0 : # 아예 빈 칸이면 
                            nx, ny = nx + dx[i], ny + dy[i]
                    if chk_pos(nx, ny) == False :
                        n_board[nx-dx[i]][ny-dy[i]] = value
            print("i : ", i)
            for b in n_board :
                print(*b)
            print('')
            queue.append((n_board, cnt+1))

my_ans = max_n
print(my_ans)