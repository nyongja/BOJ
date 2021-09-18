import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
    global m, n, array

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n :
            if array[nx][ny] == 1 :
                array[nx][ny] = 0
                dfs(nx, ny)
    return

T = int(input()) # 테스트 케이스
for _ in range(T) :
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    array = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k) :
        x, y = map(int, input().split()) # 배추 위치
        array[x][y] = 1
    cnt = 0
    for i in range(m) :
        for j in range(n) :
            if array[i][j] == 1 :
                array[i][j] = 0 # 방문 처리
                cnt += 1
                dfs(i, j)
    print(cnt)
