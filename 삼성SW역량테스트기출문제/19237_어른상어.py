from collections import defaultdict

n, m, k = map(int, input().split()) # 격자 크기, 상어 수, 냄새 유지 시간
array = [list(map(int, input().split())) for _ in range(n)]
direct = list(map(int, input().split()))

sharks = defaultdict(list)

for i in range(n) :
    for j in range(n) :
        if array[i][j] != 0 :
            num = array[i][j]
            sharks[(i, j)].append((num, direct[num-1]))
            array[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

priority = defaultdict(list)
for i in range(m) :
    for j in range(4) :
        priority[i+1].append(list(map(int, input().split()))) # 우선순위

def chk_pos(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def get_out() : # 상어 내쫓기 & 냄새 뿌리기
    for x, y in sharks.keys() :
        if len(sharks[(x, y)]) > 1 :
            sharks[(x, y)] = [min(sharks[(x, y)])]
        array[x][y] = (sharks[(x, y)][0][0], k) # 냄새 뿌리기

def move() : # 상어 이동하기
    global sharks

    new_sharks = defaultdict(list)
    for x, y in sharks.keys() :
        #print(sharks)
        num, d = sharks[(x, y)][0]
        flag = False
        # 아무 냄새 없는지 확인
        for i in priority[num][d-1] :
            nx, ny = x + dx[i-1], y + dy[i-1]
            
            if chk_pos(nx, ny) and array[nx][ny] == 0 :
                new_sharks[(nx, ny)].append((num, i))
                flag = True
                break
        if not flag :
            # 자신의 냄새 있는 칸으로 이동
            for i in priority[num][d-1] :
                nx, ny = x + dx[i-1], y + dy[i-1]
                if chk_pos(nx, ny) and array[nx][ny][0] == num :
                    new_sharks[(nx, ny)].append((num, i))
                    break
    sharks = new_sharks
    return

def time_out() :
    for i in range(n) :
        for j in range(n) :
            if array[i][j] != 0 :
                if array[i][j][1] -1 == 0 :
                    array[i][j] = 0
                else :
                    array[i][j] = (array[i][j][0], array[i][j][1]-1)

answer = 0
while len(sharks) > 1 :
    get_out()
    move()
    time_out()
    answer += 1
    if answer > 1000 :
        answer = -1
        break

print(answer)