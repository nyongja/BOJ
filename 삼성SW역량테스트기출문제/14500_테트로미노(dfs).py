import sys
input = sys.stdin.readline

def dfs(k, tmp, r, c) :
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    global visited
    global answer

    if k == 4 :
        answer = max(answer, tmp)
        return
    if tmp + (4-k) * max_val < answer : # 나머지 값들이 최고값이 나와도 answer를 못넘으면 더 볼 필요 없음
        return
    for step in steps :
        nr = r + step[0]
        nc = c + step[1]
        if 0 <= nr < n and 0 <= nc < m :
            if not visited[nr][nc] :
                visited[nr][nc] = True
                if k == 2 :
                    # ㅗ 모양을 위해
                    dfs(k+1, tmp + array[nr][nc], r, c)
                dfs(k+1, tmp+array[nr][nc], nr, nc)
                visited[nr][nc] = False
    return

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
answer = 0
visited = [[False for _ in range(m)] for _ in range(n)]
max_val = max(map(max, array))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(1, array[i][j], i, j)
        visited[i][j] = False
print(answer)