n, m = map(int, input().split()) # 맵 크기, 이동 횟수
array = [list(map(int, input().split())) for _ in range(n)] # 맵 정보
move_info = []
for _ in range(m) :
    d, s = map(int, input().split())
    move_info.append((d-1, s)) # 이동정보

# 이동 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물 복사
c_dx = [-1, -1, 1, 1]
c_dy = [-1, 1, -1, 1]

def cloud_move(x, y, d, s) :
    nx, ny = (x + dx[d]*s)%n, (y + dy[d]*s)%n
    return nx, ny

def rain(x, y) :
    array[x][y] += 1
    return 

def water_copy(x, y) :
    for i in range(4) :
        nx, ny = x + c_dx[i], y + c_dy[i]
        if (0 <= nx < n) and (0 <= ny < n) :
            if array[nx][ny] != 0 :
                array[x][y] += 1
    return

def make_cloud() :
    new_cloud = []
    for x in range(n) :
        for y in range(n) :
            if (x, y) not in cloud and array[x][y] >= 2 :
                array[x][y] -= 2
                new_cloud.append((x, y))
    return new_cloud

def sum_water() :
    water = 0
    for i in range(n) :
        for j in range(n) :
            water += array[i][j]
    return water

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for i in range(len(move_info)) :
    # 비바라기 시전 시 구름 생성
    
    # 이동 명령
    d, s = move_info[i]
    for j in range(len(cloud)) :
        nx, ny = cloud_move(cloud[j][0], cloud[j][1], d, s)
        cloud[j] = (nx, ny)
        rain(nx, ny)

    for j in range(len(cloud)) :
        water_copy(cloud[j][0], cloud[j][1])

    cloud = make_cloud()

print(sum_water())