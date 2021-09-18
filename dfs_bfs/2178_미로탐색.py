import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def chk_pos(x, y) :
    global n, m
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    return True

def bfs(x, y) :
    global array
    queue = deque([(x, y)])

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if chk_pos(nx, ny) and array[nx][ny] == '1' :
                queue.append((nx, ny))
                array[nx][ny] = int(array[x][y]) + 1 
    return

n, m = map(int, input().split()) # 미로 크기
array = []
for _ in range(n) :
    array.append(list(input())[:-1])

bfs(0, 0)
print(array[-1][-1])
