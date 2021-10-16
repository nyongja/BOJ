from collections import deque

n, m = map(int, input().split()) # 게임보드 크기, 색상 종류 수
board = [list(map(int, input().split())) for _ in range(n)] # 게임보드 정보

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def find_group(x, y, num) : # BFS
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([])
    q.append((x, y))
    group = [(x, y)]
    
    basic = None
    color = None
    rainbow = 0
    visited[x][y] = True

    while q :
        x, y = q.popleft()
        if board[x][y] != 0 and not basic : # 기준 블록 정하기
            basic = (x, y)
            color = board[x][y]
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and not visited[nx][ny] :
                if board[nx][ny] == 0 :
                    rainbow += 1            
                if board[nx][ny] == 0 or board[nx][ny] == color :
                    group.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True
    
    if len(group) >= 0 and color :
        return group, [len(group), rainbow, basic[0], basic[1], num]
    return None, None

def delete(group) :
    global board
    for b_x, b_y in group :
        board[b_x][b_y] = -2
    return

def gravity() :
    global array

    for x in range(n-2, -1, -1) :
        for y in range(n) :
            if board[x][y] != -1 and board[x][y] != -2 :
                dx = x
                while dx+1 < n and board[dx+1][y] == -2:
                    dx = dx + 1
                
                if dx != x :
                    board[dx][y] = board[x][y]
                    board[x][y] = -2
    return

def rotate() :
    global board
    new_board = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n) :
        for y in range(n) :
            new_board[n-1-y][x] = board[x][y]
    board = new_board

def auto_play() :
    score = 0

    while True :
        basic_info = []
        group_info = {}
        real_visited = [[False for _ in range(n)] for _ in range(n)]
        num = 1
        for x in range(n) :
            for y in range(n) :
                if board[x][y] != -1 and board[x][y] != -2 and not real_visited[x][y]:
                    group, info = find_group(x, y, num)
                    if group and len(group) > 1:
                        group_info[num] = group
                        basic_info.append(info)
                        num += 1
                        for b_x, b_y in group :
                            if board[b_x][b_y] != 0 :
                                real_visited[b_x][b_y] = True
        if not basic_info :
            break
        basic_info.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))

        delete_num = basic_info[0][-1] # 삭제할 블록 번호
        delete(group_info[delete_num])
        gravity()
        rotate()
        gravity()
        score += len(group_info[delete_num])**2

    return score
print(auto_play())