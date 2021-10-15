n, m = map(int, input().split()) # 맵 크기, 마법 수행 수
array = [list(map(int, input().split())) for _ in range(n)] # 맵 정보(구슬)
magic = []
x, y = (n-1)//2, (n-1)//2 # 마법사 상어 위치
for _ in range(m) :
    d, s = map(int, input().split())
    magic.append((d-1, s))

bomb_num = [0, 0, 0]

# 블리자드 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 구슬 정보 방향
m_dx = [0, 1, 0, -1]
m_dy = [-1, 0, 1, 0]

def chk_pos(a, b) :
    if 0 <= a < n and 0 <= b < n :
        return True
    return False

def blizzard(d, s) :
    nx, ny = x, y
    for i in range(1, s+1) :
        nx, ny = nx + dx[d], ny + dy[d]
        if chk_pos(nx, ny) :
            array[nx][ny] = 0

def marble_info() :
    nx, ny = x, y
    marble = []
    for i in range((n-1)* 4+1) :
        for _ in range((i)//2+1) :
            nx, ny = nx + m_dx[i%4], ny +m_dy[i%4]
            if chk_pos(nx, ny) and array[nx][ny] != 0 :
                marble.append(array[nx][ny])
    return marble

def bomb(marble) :
    new_marble = []
    if not marble :
        return marble
    cur = marble[0]
    cnt = 1
    tmp = [cur]
    flag = True
    
    while flag and marble: 
        flag = False
        new_marble = []
        cnt = 1
        cur = marble[0]
        tmp = [cur]
        for i in range(1, len(marble)) :
            if marble[i] == cur :
                cnt += 1
                tmp.append(cur)
            else :
                if cnt >= 4 :
                    bomb_num[cur-1] += cnt
                    flag = True
                else :
                    new_marble += tmp
                cnt = 1
                cur = marble[i]
                tmp.clear()
                tmp = [cur]
        if cnt >= 4 :
            bomb_num[cur-1] += cnt
            flag = True
        else :
            new_marble += tmp
        marble = new_marble
    return marble

def change_marble(marble) :
    if not marble :
        return marble
    cur = marble[0]
    cnt = 1
    new_marble = []
    for i in range(1, len(marble)) :
        if marble[i] != 0 :
            if cur == marble[i] :
                cnt += 1
            else :
                new_marble.append(cnt)
                new_marble.append(cur)
                cnt = 1
                cur = marble[i]
    if cnt != 0 :
        new_marble.append(cnt)
        new_marble.append(cur)
    return new_marble
            
def put_marble(marble) :
    global array

    nx, ny = x, y
    idx = 0
    for i in range((n-1)* 4+1) :
        for _ in range((i)//2+1) :
            nx, ny = nx + m_dx[i%4], ny +m_dy[i%4]
            if chk_pos(nx, ny) and idx < len(marble):
                array[nx][ny] = marble[idx]
            elif chk_pos(nx, ny) and idx >= len(marble) :
                array[nx][ny] = 0
            idx += 1
    return
for i in range(m) :
    d, s = magic[i]
    blizzard(d, s)
    marble = marble_info()
    marble = bomb(marble)
    marble = change_marble(marble)
    put_marble(marble)

print(bomb_num[0] + bomb_num[1] * 2 + bomb_num[2] * 3)
