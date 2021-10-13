from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, l, r = map(int, input().split()) # 땅 크기, l <= 인구 차 <= r
array = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
day = 0
flag = True # 인구 이동이 발생하였는가?

def chk_pos(x, y) :
    if x >= n or x < 0 or y >= n or y < 0 :
        return False
    return True

def dfs(x, y) :
    global visited, union, flag

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if chk_pos(nx, ny) and visited[nx][ny] == False : # 아직 방문이전이면
            diff = abs(array[x][y] - array[nx][ny])
            if l <= diff <= r : # 인구차가 조건에 해당하면
                visited[nx][ny] = True
                union.append((nx, ny))
                dfs(nx, ny)
                flag = True
    return

def merge() :
    global union, array
    avg = sum(array[x][y] for x, y in union) // len(union)
    while union :
        x, y = union.pop()
        array[x][y] = avg

while flag : 
    flag = False
    visited = [[False] * n for _ in range(n)]
    day += 1
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                visited[i][j] = True
                union = deque([(i, j)])
                dfs(i, j)
                if len(union) > 1 :
                    merge()
print(day-1)
