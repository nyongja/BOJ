import sys
from collections import deque

def chk_pos(x, y) :
    if x < 0 or x >= l or y < 0 or y >= l :
        return False
    return True

def bfs(x, y) :
    global array
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    queue = deque([(x, y)])

    while queue :
        x, y = queue.popleft()
        if x == ex and y == ey :
            return array[x][y]
        for i in range(8) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and array[nx][ny] == 0 :
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))

input = sys.stdin.readline
T = int(input()) # 테스트 케이스 수
for _ in range(T) :
    l = int(input()) # 체스판 한 변의 길이
    sx, sy = map(int, input().split()) # 나이트가 현재 있는 칸
    ex, ey = map(int, input().split()) # 나이트가 이동하려는 칸
    array = [[0 for _ in range(l)] for _ in range(l)]

    print(bfs(sx, sy))