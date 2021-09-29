import sys
import copy
input = sys.stdin.readline


def turn(x, d) : # 시계 방향으로 회전
    new_x = [0]*8
    for i in range(8) :
        new_x[i] = x[(i-d)%8]
    return new_x

def solve(n, d, t) : # t : all = 양쪽 다, left = 왼쪽만, right = 오른쪽만
    prev = copy.deepcopy(array[n]) # 돌리기 전 위치 저장
    array[n] = turn(array[n], d) # 회전 시키기
    if t == 'all' or t == 'left' : # 왼쪽을 볼지 말지
        if n-1 != 0 :
            if prev[6] != array[n-1][2] :
                solve(n-1, d*-1, 'left')
    if t == 'all' or t == 'right' : # 오른쪽을 볼지 말
        if n+1 != 5 :
            if prev[2] != array[n+1][6] :
                solve(n+1, d*-1, 'right')

def get_score() :
    score_lst = [0, 1, 2, 4, 8]
    score = 0
    for i in range(1, 5) :
        if array[i][0] == 1 :
            score += score_lst[i]
    return score

array = [[]]
for _ in range(4) :
    array.append(list(map(int, input().strip())))  # 톱니바퀴 현재 상태 입력
k = int(input()) # 회전 횟수
for _ in range(k) : # 회전 시키는 방법
    n, d = map(int, input().split()) # 몇 번째 톱니바퀴를, 어느 방향으로 회전(1 : 시계, -1 : 반시계)
    solve(n, d, 'all')
print(get_score())