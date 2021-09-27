import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 보드 크기
k = int(input()) # 사과의 개수

board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k) : # 사과의 위치
    r, c = map(int, input().split())
    board[r-1][c-1] = 2 # 사과 위치 표시

l = int(input()) # 뱀의 방향 변환 횟수
move = list()
for _ in range(l) :
    t, d = map(str, input().split())
    move.append((int(t), d))


board[0][0] = 1 # 뱀 초기 위치 표시
cur_time = 0 # 현재 게임 진행 초

queue = deque([(0, 0, 'h')]) # 초기 위치
change_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_dir = 0 # 현재 뱀의 얼굴 방향
def chk_pos(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    return True

apple = False
idx = 0
next_time = move[idx][0]
next_dir = move[idx][1]
snake_len = 1
while queue :
    r, c, t = queue.popleft()
    if t == 'h' : # 머리일경우
        cur_time += 1
        nr, nc = r + change_dir[cur_dir][0], c + change_dir[cur_dir][1]

        if chk_pos(nr, nc) == False or board[nr][nc] == 1 : 
            break
        queue.append([nr, nc, 'h'])
        if board[nr][nc] == 2 :
            apple = True
        else :
            apple = False
        board[nr][nc] = 1
        if apple : # 사과가 있으면
            if snake_len == 1 :
                queue.append([r, c, 't'])
                snake_len += 1
        else :
            apple = False
            if snake_len == 1 :
                board[r][c] = 0
        if next_time == cur_time : # 방향 전환 시간이라면
            if next_dir == 'D' :
                cur_dir += 1
                cur_dir %= 4
            else :
                cur_dir -= 1
                if cur_dir == -1 :
                    cur_dir = 3
            idx += 1
            if idx < len(move) :
                next_time = move[idx][0]
                next_dir = move[idx][1]
    elif t == 'b' : # 몸통일 경우
        queue.append([prev_r, prev_c, 'b'])
    else : # 꼬리일 경우
        if apple : # 사과가 있으면
            queue.append([prev_r, prev_c, 'b'])
            queue.append([r, c, 't'])
        else :
            queue.append([prev_r, prev_c, 't'])
            board[r][c] = 0
    prev_r, prev_c = r, c
print(cur_time)
