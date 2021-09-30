import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 드래곤 커브의 개수
array = [[False]*101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
ans = 0

def next_generation() :
    global dragon, x, y, g

    while g > 0 :
        for i in range(len(dragon)-1, -1, -1) :
            d = dragon[i]
            d = (d + 1) % 4
            
            x += dx[d]
            y += dy[d]

            array[x][y] = True
            dragon.append(d)
        g -= 1

def count() :
    ans = 0
    for i in range(100) :
        for j in range(100) :
            if array[i][j] and array[i+1][j] and array[i][j+1] and array[i+1][j+1] :
                ans += 1
    return ans

for _ in range(n) :
    dragon = []
    y, x, d, g = map(int, input().split()) # x, y : 시작점, d : 시작 방향, g : 세대

    # 0세대 추가 
    array[x][y] = True # 0세대 시작점
    
    x += dx[d]
    y += dy[d]
    
    array[x][y] = True# 0세대 끝점
    dragon.append(d)

    next_generation()

print(count())