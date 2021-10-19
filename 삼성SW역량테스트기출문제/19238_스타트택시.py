from collections import deque

n, m, oil = map(int, input().split()) # 맵 크기, 손님 수, 초기 연료 양
array = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split()) # 시작 위치
x, y = x-1, y-1
for _ in range(m) : # 손님 위치 저장
    s_r, s_c, e_r, e_c = map(int, input().split())
    array[s_r-1][s_c-1] = (e_r-1, e_c-1)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def chk_pos(x, y) :
    if 0 <= x < n and 0 <= y < n and array[x][y] != 1 :
        return True
    return False

def find_passenger(x, y) : # 승객 최단 거리 찾기
    q = deque([(0, x, y)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    if array[x][y] != 0 : # 현재 위치에 이미 승객 있는 경우
        return q.popleft()
    visited[x][y] = True
    while q :
        q = deque(sorted(q))
        tmp_oil, x, y = q.popleft()
        if array[x][y] != 0 : # 다음 손님 찾는 순서 주의할 것!
            return tmp_oil, x, y
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((tmp_oil+1, nx, ny))
    return -1, -1, -1

def find_destination(x, y) :
    e_x, e_y = array[x][y]
    array[x][y] = 0
    q = deque([(0, x, y)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    if e_x == x and e_y == y : # 현재 위치에 이미 승객 있는 경우
        return q.popleft()
    while q :
        tmp_oil, x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and not visited[nx][ny] :
                if nx == e_x and ny == e_y :
                    return tmp_oil+1, nx, ny
                visited[nx][ny] = True
                q.append((tmp_oil+1, nx, ny))
    return -1, -1, -1

num_pass = m
for _ in range(m) :
    tmp_oil, x, y = find_passenger(x, y) # 현재 위치에서 가까운 승객 위치 & 승객까지 가는 연료 양

    if oil < tmp_oil or tmp_oil == -1:
        oil = -1
        break
    
    oil -= tmp_oil

    tmp_oil, x, y = find_destination(x, y)

    if oil < tmp_oil or tmp_oil == -1 :
        oil = -1
        break

    oil += tmp_oil
    num_pass -= 1
if num_pass != 0 :
    oil = -1
print(oil)