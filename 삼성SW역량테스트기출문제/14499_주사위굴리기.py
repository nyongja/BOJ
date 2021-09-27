import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split()) # 지도의 크기, 주사위의 위치, 명령의 개수
array = [list(map(int, input().split())) for _ in range(n)] # 지도
move = list(map(int, input().split())) # 이동 순서 (동 서 북 남)
dice = [0]*6
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def chk_pos(a, b) :
    if a < 0 or a >= n or b < 0 or b >= m :
        return False
    return True

for i in move :
    if chk_pos(x+dxy[i-1][0], y + dxy[i-1][1]) :
        x, y = x + dxy[i-1][0], y + dxy[i-1][1]
        if i == 1 : # 동쪽
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
        elif i == 2 : # 서쪽
            dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
        elif i == 3 : # 북쪽
            dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
        elif i == 4 : # 남쪽
            dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
        if array[x][y] == 0 :
            array[x][y] = dice[5]
        else :
            dice[5] = array[x][y]
            array[x][y] = 0
        print(dice[0])

