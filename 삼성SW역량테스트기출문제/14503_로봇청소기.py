
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
x, y, d = map(int, input().split()) # 로봇 청소기 위치, 방향(북, 동, 남, 서)
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 1
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

arr[x][y] = 2
def chk_pos(x, y) :
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    return True

while True :
    check = False
    for i in range(4) :
        d = (d-1) % 4
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if chk_pos(nx, ny) :
            if arr[nx][ny] == 0 : # 만약 왼쪽을 아직 청소하지 않았다면
                arr[nx][ny] = 2
                ans += 1
                x, y = nx, ny
                check = True
                break
    if not check : # 주변에 청소할 곳이 하나도 없으면 한 칸 후진
        nx = x - dxy[d][0]
        ny = y - dxy[d][1]
        if chk_pos(nx, ny) :
            if arr[nx][ny] == 2 : # 후진
                x, y = nx, ny
            else : # 후진 못하면 여기서 끝
                break
print(ans)