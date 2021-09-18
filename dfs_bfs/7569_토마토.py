import sys
from collections import deque
input = sys.stdin.readline

def chk_pos(z, x, y) :
    global m, n, h
    if z < 0 or z >= h or x < 0 or x >= n or y < 0 or y >= m :
        return False
    return True

def bfs(queue) :
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    answer = 0
    while queue :
        z, x, y = queue.popleft()
        
        for i in range(6) :
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if chk_pos(nz, nx, ny) and array[nz][nx][ny] == 0 :
                array[nz][nx][ny] = array[z][x][y] + 1
                queue.append((nz, nx, ny))
                answer = max(answer, array[nz][nx][ny])

    for i in range(h) :
        for j in range(n) :
            for k in range(m) :
                if array[i][j][k] == 0 :
                    return -1
    if answer == 0 :
        return 0
    return answer-1


m, n, h = map(int, input().split()) # 가로, 세로, 높이
array = []

for i in range(h) :
    array.append([])
    for _ in range(n) :
        array[i].append(list(map(int, input().split())))
queue = deque([])
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if array[i][j][k] == 1 :
                queue.append((i, j, k))

print(bfs(queue))