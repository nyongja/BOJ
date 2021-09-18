import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    global n, m
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    return True

def bfs(queue) :
    global array, n, m
    answer = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and array[nx][ny] == 0 :
                array[nx][ny] = array[x][y]+1
                queue.append((nx, ny))
                answer = max(answer, array[nx][ny])

    for i in range(n) :
        for j in range(m) :
            if array[i][j] == 0 :
                return -1
    if answer == 0 :
        return 0
    return answer - 1

m, n = map(int, input().split()) # 상자의 크기 ( 2 ~ 1000)
array = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 1 :
            queue.append((i, j))

print(bfs(queue))