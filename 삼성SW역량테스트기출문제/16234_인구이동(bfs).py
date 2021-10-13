from collections import deque

n, l, r = map(int, input().split()) # 땅 크기, l <= 인구 차 <= r
array = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
day = 0

def chk_pos(x, y) :
    if x >= n or x < 0 or y >= n or y < 0 :
        return False
    return True

def bfs(x, y) :
    q = deque([[x, y]])
    tmp = [[x, y]]
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and visited[nx][ny] == 0 : # 아직 방문 전이면
                diff = abs(array[x][y] - array[nx][ny])
                if l <= diff <= r :
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    tmp.append([nx, ny])
    return tmp

while True :
    visited = [[0] * n for _ in range(n)]
    avg = []
    m = 0
    flag = False
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 :
                visited[i][j] = 1
                tmp = bfs(i, j)
                if len(tmp) > 1 :
                    mean_p = sum(array[x][y] for x, y in tmp) // len(tmp)
                    for x, y in tmp :
                        array[x][y] = mean_p
                    flag = True
    if not flag :
        break
    day += 1

print(day)