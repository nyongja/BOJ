import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_pos(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    return True

def dfs(x, y) :
    global arary, cnt
    array[x][y] = 0
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if check_pos(nx, ny)==True :
            if int(array[nx][ny]) == 1 :
                array[nx][ny] = 0 
                cnt += 1
                dfs(nx, ny)
    return cnt

n = int(input()) # 지도의 크기
array = [list(input())[:-1] for _ in range(n)]
answer = []

for i in range(n) :
    for j in range(n) :
        if int(array[i][j]) == 1 :
            cnt = 1
            answer.append(dfs(i, j))

answer.sort()

print(len(answer))
for i in answer :
    print(i)