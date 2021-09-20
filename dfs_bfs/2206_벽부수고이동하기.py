import sys
import copy
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    global n, m
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    return True

def bfs(x, y, f) :
    global visited

    queue = deque([(x, y, f)])
    visited[x][y][f] = 1 # 처음 시작 방문처리
    while queue :
        x, y, f = queue.popleft()
        if x == n-1 and y == m-1 :
            return visited[x][y][f]
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) :
                if array[nx][ny] == 1 and f == 0 : # 만약 벽이고, 아직 벽을 뚫기 전이라면
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                elif array[nx][ny] == 0 and visited[nx][ny][f] == 0 : # 벽도 아니고, 방문하기도 전이라면
                    visited[nx][ny][f] = visited[x][y][f] + 1
                    queue.append((nx, ny, f))

    return -1

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, list(input().strip()))))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, 0))