n = int(input())
input_b = [tuple(map(int, input().split())) for _ in range(n)] # 입력으로 들어오늘 블락들
blocks = [[(0, 0)], [(0, 0), (0, 1)], [(0, 0), (1, 0)]] # 블락 종류
array = [[0 for _ in range(10)] for _ in range(10)]
ans = 0

def chk_pos(x, y) :
    if 0 <= x < 10 and 0 <= y < 10 :
        return True
    return False

dx_g, dy_g = 1, 0
dx_b, dy_b = 0, 1

def move(t, x, y, dx, dy) :
    flag = True
    while True :
        x, y = x + dx, y + dy
        for b in blocks[t] :
            x_b, y_b = x + b[0], y + b[1]
            if not chk_pos(x_b, y_b) or array[x_b][y_b] != 0 :
                x, y = x - dx, y - dy
                flag = False
                break
        if not flag :
            break

    for b in blocks[t] :
        array[x+b[0]][y+b[1]] = 1

def get_score() :
    global ans
    # 그린 지우기
    not_del = []
    for i in range(9, 3, -1) :
        if not(4<=i<=5) and sum(array[i]) == 4 :
            ans += 1
        else :
            not_del.append(array[i])
        array[i] = [0 for _ in range(10)]
    for i in range(len(not_del)) :
        array[9-i] = not_del[i]
    
    # 블루 지우기
    not_del = []
    for j in range(9, 3, -1) :
        cnt = 0
        tmp = []
        for i in range(4) :
            if not (4 <= j <= 5) :
                cnt += array[i][j]
            tmp.append(array[i][j])
            array[i][j] = 0

        if cnt == 4 :
            ans += 1
        elif tmp :
            not_del.append(tmp)

    for j in range(len(not_del)) :
        for i in range(4) :
            array[i][9-j] = not_del[j][i]

def del_b() :
    # 그린 지우기
    cnt = 0
    for i in range(4, 6) :
        if sum(array[i]) != 0 :
            cnt += 1

    if cnt : 
        for i in range(9-cnt, 3, -1) :
            array[i+cnt] = array[i]
            array[i] = [0 for _ in range(10)]
        
    # 블루 지우기
    cnt = 0
    for j in range(4, 6) :
        tmp = 0
        for i in range(4) :
            tmp += array[i][j]
        if tmp != 0 :
            cnt += 1
    
    if cnt :
        for j in range(9-cnt, 3, -1) :
            tmp = []
            for i in range(4) :
                tmp.append(array[i][j])

            for i in range(4) :
                array[i][j+cnt] = tmp[i]
                array[i][j] = 0
    
    return

def cnt_blocks() :
    # 그린 개수
    cnt = 0
    for i in range(6, 10) :
        cnt += sum(array[i])

    # 블루 개수
    for i in range(4) :
        cnt += sum(array[i])
    
    return cnt

for t, x, y in input_b :
    move(t-1, x, y, dx_g, dy_g)
    move(t-1, x, y, dx_b, dy_b)
    get_score()
    del_b()

b_cnt = cnt_blocks()
print(ans)
print(b_cnt)