n = int(input())
like = dict()

for _ in range(n*n) : # 좋아하는 학생 정보
    tmp = list(map(int, input().split()))
    like[tmp[0]] = tmp[1:]

array = [[0 for _ in range(n)] for _ in range(n)] # 자리 정보

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def check_around(num) : # 주변 체크하기
    possible = []
    
    for x in range(n) :
        for y in range(n) :
            if array[x][y] == 0 :  # 공석이면
                bf = 0 # 인접한 칸에 좋아하는 친구 수
                empty = 0 # 인접한 칸에 비어있는 칸
                for i in range(4) :
                    nx, ny = x + dx[i], y + dy[i]
                    if chk_pos(nx, ny) :
                        if array[nx][ny] in like[num] :
                            bf += 1
                        elif array[nx][ny] ==  0:
                            empty += 1
                possible.append((bf, empty, x, y))
    return possible

def sit_down(possible) :
    possible.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    return possible[0][2], possible[0][3]

def get_score() :
    answer = 0
    for x in range(n) :
        for y in range(n) :
            num = array[x][y] # 학생 번호
            bf = 0
            for i in range(4) :
                nx, ny = x + dx[i], y + dy[i]
                if chk_pos(nx, ny) :
                    if array[nx][ny] in like[num] :
                        bf += 1
            if bf != 0 :
                answer += 10**(bf-1)
    return answer

for num in like.keys() : # 각 학생에 대하여
    possible = check_around(num)
    x, y = sit_down(possible)
    array[x][y] = num
print(get_score())