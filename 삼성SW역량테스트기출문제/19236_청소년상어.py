from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

fish = {i:0 for i in range(1, 17)}
array = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4) :
    row = list(map(int, input().split()))
    for j in range(4) :
        a, b = row[2*j], row[2*j+1]
        fish[a] = [i, j, b-1]
        array[i][j] = a


shark = [0, 0, fish[array[0][0]][2]]
eat = array[0][0]
array[0][0] = -1 # 상어 위치
answer = 0

def chk_pos(x, y) :
    if 0 <= x < 4 and 0 <= y < 4 :
        return True
    return False

def fish_move(array, fish) :
    for num in fish.keys() :
        x, y, d = fish[num]
        if array[x][y] != num :
            continue
        for i in range(8) :
            nx, ny = x + dx[(d+i)%8], y + dy[(d+i)%8]
            if chk_pos(nx, ny) and array[nx][ny] != 0 and array[nx][ny] != -1:
                s_num = array[nx][ny]
                array[nx][ny] = num
                array[x][y] = s_num
                fish[s_num] = [x, y, fish[s_num][2]]
                fish[num] = [nx, ny, (d+i)%8]
                break
            elif chk_pos(nx, ny) and array[nx][ny] == 0 :
                array[nx][ny] = num
                array[x][y] = 0
                fish[num] = [nx, ny, (d+i)%8]
                break
    return array, fish


def shark_move(array, fish, x, y, d, eat) :
    global answer

    t_array, t_fish = fish_move(array, fish)

    nx, ny = x, y
    while True :
        nx, ny = nx + dx[d], ny + dy[d]

        if chk_pos(nx, ny) :
            if t_array[nx][ny] != 0 and t_array[nx][ny] != -1: # 물고기가 있으면
                num = t_array[nx][ny]
                nd = t_fish[num][2]
                t_array[x][y] = 0
                t_array[nx][ny] = -1
                shark_move(deepcopy(t_array), deepcopy(t_fish), nx, ny, nd, eat + num)
                t_array[x][y] = -1
                t_array[nx][ny] = num
            else :
                continue
        else :
            answer = max(answer, eat)
            break
    return

shark_move(array, fish, 0, 0, shark[2], eat)
print(answer)