import sys
input = sys.stdin.readline

n, m, h = map(int, input().split()) # 세로, 가로, 가로선 놓을 위치
array = [[0]*(n+1) for _ in range(h+1)] # 사다리 정보
ans = 4

for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[a][b+1] = -1

def down(y) : # y 번째 세로선에서 내려가보기
    nx = 1
    ny = y
    while nx <= h :
        ny += array[nx][ny]
        nx += 1
    if ny == y :
        return True
    return False

def dfs(a, b, k) : # 가로선 추가해보기
    global ans
    flag = True
    if k+1 > ans :
        return 
    for i in range(1, n+1) :
        if not down(i) :
            flag = False
            break
    if flag :
        ans = min(ans, k)
        return
    
    for i in range(a, h+1) :
        for j in range(1, n) :
            if k+1 > ans :
                return
            if i == a and j < b :
                continue
            # 해당 위치, 양옆이 다 0이면 가로선 놓을 수 있음
            if array[i][j] == 0 and array[i][j-1] != 1 and array[i][j+1] != 1 : 
                array[i][j] = 1
                array[i][j+1] = -1
                dfs(i, j+1, k+1)
                array[i][j] = 0
                array[i][j+1] = 0

dfs(1, 1, 0)
if ans > 3 :
    print(-1)
else :
    print(ans)
