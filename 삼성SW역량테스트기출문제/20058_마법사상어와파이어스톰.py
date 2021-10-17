from collections import deque

n, q = map(int, input().split()) # 맵 크기, 파이어스톰 횟수
array = [list(map(int, input().split())) for _ in range(2**n)] # 얼음 맵
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    if 0 <= x < 2**n and 0 <= y < 2**n :
        return True
    return False

def div_square(l) :
    square = []
    
    return square

def firestorm(l) :
    global array
    for x in range(0, 2**n, 2**l) :
        for y in range(0, 2**n, 2**l) :
            raw_square = []
            for i in range(2**l) :
                for j in range(2**l-1, -1, -1) :
                    nx, ny = x + j, y + i
                    raw_square.append(array[nx][ny])
            idx = 0
            for i in range(2**l) :
                for j in range(2**l) :
                    nx, ny = x + i, y + j
                    array[nx][ny] = raw_square[idx]
                    idx += 1
    return

def melting() :
    tmp_array = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for x in range(2**n) :
        for y in range(2**n) :
            cnt = 0 
            if array[x][y] != 0 :
                for i in range(4) :
                    nx, ny = x + dx[i], y + dy[i]
                    if chk_pos(nx, ny) and array[nx][ny] != 0 :
                        cnt += 1
                if cnt < 3 :
                    tmp_array[x][y] = array[x][y] -1
                else :
                    tmp_array[x][y] = array[x][y]
    return tmp_array
    
def bfs(x, y) :
    global visited
    q = deque([(x, y)])
    visited[x][y] = True
    connect = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and not visited[nx][ny] and array[nx][ny] != 0:
                visited[nx][ny] = True
                connect += 1
                q.append((nx, ny))
    return connect

l = list(map(int, input().split()))

for i in l :
    firestorm(i)
    array = melting()


visited = [[False for _ in range(2**n)] for _ in range(2**n)]

total_cnt = 0
max_num = 0
for x in range(2**n) :
    for y in range(2**n) :
        total_cnt += array[x][y]
        if not visited[x][y] and array[x][y] != 0 :
            num = bfs(x, y)
            max_num = max(max_num, num)
        
print(total_cnt)
print(max_num)