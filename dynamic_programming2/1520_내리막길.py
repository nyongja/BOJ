import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

M, N = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(M)]

pos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
dp = [[-1 for _ in range(N)] for _ in range(M)]
dp[M-1][N-1] = 1

def check_range(x, y) :
    if x < 0 or x >= M or y < 0 or y >= N :
        return False
    return True

def dfs(x, y) :
    if dp[x][y] != -1 :
        return dp[x][y]
        
    tmp = 0
    for p in pos :
        dx, dy = p[0], p[1]
        if check_range(x+dx, y+dy) :
            if array[x][y] > array[x+dx][y+dy] :
                tmp += dfs(x+dx, y+dy)
    dp[x][y] = tmp
    
    return dp[x][y]

print(dfs(0, 0))
