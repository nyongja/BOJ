from dis import dis
from itertools import permutations
from math import floor

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

percent = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]
direct = {0 : [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)],
          1 : [(0, -2), (1, -1), (0, -1), (-1, -1), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)],
          2 : [(-2, 0), (-1, 1), (-1, 0), (-1, -1), (0, 2), (1, 1), (1, 0), (1, -1), (2, 0)],
          3 : [(0, -2), (-1, -1), (0, -1), (1, -1), (-2, 0), (-1, 1), (0, 1), (1, 1), (0, 2)]}

def chk_pos(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def move(x, y, i, sail) :
    global array
    total = 0 # 움직인 양
    disappear = 0
    for j in range(9) :
        s_dx, s_dy = direct[i][j][0], direct[i][j][1]
        nx, ny = x + s_dx, y + s_dy
        tmp = floor(sail*percent[j])
        if chk_pos(nx, ny) :
            array[nx][ny] += tmp
            total += tmp
        else :
            disappear += tmp
    return disappear, sail - total - disappear # 움직이고 남은 양

def tornado(x, y, i) :
    global array
    nx, ny = x + dx[i], y + dy[i]
    disappear = 0
    if chk_pos(nx, ny) :
        sail = array[nx][ny] # 이동한 곳의 모래 양    
        array[nx][ny] = 0
        disappear, last = move(nx, ny, i, sail)
        if chk_pos(nx+dx[i], ny+dy[i]) :
            array[nx+dx[i]][ny+dy[i]] += last
        else :
            disappear += last
    return nx, ny, disappear

x, y = n//2, n//2
answer = 0
disappear = 0
for i in range(n*2-1) :
    for _ in range((i//2)+1) :
        x, y, disappear = tornado(x, y, i%4)
        answer += disappear

print(answer)
