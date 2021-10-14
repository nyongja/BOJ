from collections import deque

n = int(input()) # 공간의 크기
array = [] # 공간 상태
size_info = [0] * 7
for i in range(n) :
    tmp = list(map(int, input().split()))
    for j in range(n) :
        if tmp[j] == 9 :
            s_x, s_y = i, j # 아기 상어 시작 위
            tmp[j] = 0 
        elif tmp[j] != 0 : # 물고기 크기 별로 몇 마리 있는지
            size_info[tmp[j]] += 1
    array.append(tmp)
size = 2 # 아기 상어 사이즈
cnt = 0 # 잡아먹은 물고기 수
answer = 0 

dx = [-1, 0, 0, 1] # 상 좌 우 하
dy = [0, -1, 1, 0]

def chk_pos(x, y) :
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def bfs(s_x, s_y) :
    global size, cnt, array, answer
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[s_x][s_y] = 0
    q = deque([(0, s_x, s_y)])
    while q :
        q = deque(sorted(q))
        num, x, y = q.popleft()
        num = visited[x][y]
        if 0 < array[x][y] < size :
            cnt += 1
            answer += num
            array[x][y] = 0
            if size == cnt :
                size += 1
                cnt = 0
            bfs(x, y)
            return
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and visited[nx][ny] == -1:
                if array[nx][ny] <= size :
                    visited[nx][ny] = num + 1
                    q.append((num+1, nx, ny))
bfs(s_x, s_y)
print(answer)
                