import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

_rx, _ry, _bx, _by = 0, 0, 0, 0
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 'R' : # R 위치 찾기
            _rx, _ry = i, j
        elif board[i][j] == 'B' : # B 위치 찾기
            _bx, _by = i, j
queue.append((_rx, _ry, _bx, _by, 0))
check[_rx][_ry][_bx][_by] = True

def move(_x, _y, _dx, _dy, _c):
    while board[_x+_dx][_y+_dy] != '#' and board[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs() :
    while queue :
        rx, ry, bx, by, d = queue.popleft()
        if d >= 10 :
            break
        for i in range(4) :
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if board[nbx][nby] == 'O' :
                continue
            if board[nrx][nry] == 'O' :
                print(d+1)
                return
            if nrx == nbx and nry == nby : # 위치가 겹쳤으면
                if rc > bc :
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else :
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not check[nrx][nry][nbx][nby] :
                check[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, d+1))
        
    print(-1)
    return
bfs()