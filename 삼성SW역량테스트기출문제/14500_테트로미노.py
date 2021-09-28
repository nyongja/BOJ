import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 종이의 세로, 가로 
array = [list(map(int, input().split())) for _ in range(n)]

tetromino = [
     [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]]
    
answer = 0

def chk_pos(a, b) :
    if a < 0 or a >= n or b < 0 or b >= m :
        return False
    return True

def find(x, y) :
    global answer
    for i in range(19) : # 몇 번째 테트로미노
        result = 0
        flag = True
        for j in range(4) : # 몇 번재 블록인지
            nx = x + tetromino[i][j][0]
            ny = y + tetromino[i][j][1]
            if chk_pos(nx, ny) :
                result += array[nx][ny]
            else :
                flag = False
                break
        if flag :
            answer = max(answer, result)

for i in range(n) :
    for j in range(m) :
        find(i, j)

print(answer)