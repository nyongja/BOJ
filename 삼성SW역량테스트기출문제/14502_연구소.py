import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
tmp_visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

def chk_pos(a, b) :
    if a < 0 or a >= n or b < 0 or b >= m :
        return False
    return True

def bfs() :
    global ans
    tmp_arr = copy.deepcopy(array)
    queue = deque([])
    
    for i in range(n) :
        for j in range(m) :
            if tmp_arr[i][j] == 2 :
                queue.append((i, j))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) :
                if tmp_arr[nx][ny] == 0 :
                    tmp_arr[nx][ny] = 2
                    queue.append((nx, ny))

    cnt = 0 
    for i in tmp_arr :
        cnt += i.count(0)
    ans = max(ans, cnt)

def dfs(k, r, c) :
    if k == 3 :
        bfs()
        return
    for i in range(n) :
        for j in range(m) :
            if i < r or (i == r and j < c) :
                continue
            if array[i][j] == 0 :
                array[i][j] = 1
                dfs(k+1, i, j)
                array[i][j] = 0
dfs(0, 0, 0)
print(ans)