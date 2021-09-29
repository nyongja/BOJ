import sys
import copy
input = sys.stdin.readline
import random
n, m = map(int, input().split())

array = []
cctv = []
dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

ans = 0
for i in range(n) :
    array.append(list(map(int, input().split())))
    for j in range(m) :
        if array[i][j] != 0 and array[i][j] != 6 :
            cctv.append((i, j))
        if array[i][j] == 0 :
            ans += 1
            
def chk_pos(x, y) :
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    return True

def scan(x, y, i, arr) :
    nx, ny = x + dx[i], y + dy[i]
    while chk_pos(nx, ny) and arr[nx][ny] != 6:
        if arr[nx][ny] == 0 :
            arr[nx][ny] = '#'
        nx, ny = nx + dx[i], ny + dy[i]
    return arr

def get_space(arr) :
    min_n = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 :
                min_n += 1
    return min_n

def dfs(idx, arr) : # 몇 번째 cctv를 볼 것인지
    global ans
    x, y = cctv[idx] # cctv의 위치
    c_type = arr[x][y] # cctv 타입
    
    if c_type == 1 : # 1번 cctv의 경우
        for i in range(4) :
            t_arr = copy.deepcopy(arr)
            t_arr = scan(x, y, i, t_arr)
            if (idx+1) < len(cctv) :
                dfs(idx+1, t_arr)
            else :
                min_n = get_space(t_arr)
                ans = min(min_n, ans)
    elif c_type == 2 : # 2번 cctv의 경우
        for i in [0, 2] :
            t_arr = copy.deepcopy(arr)
            t_arr = scan(x, y, i, t_arr)
            t_arr = scan(x, y, i+1, t_arr)
            if (idx+1) < len(cctv) :
                dfs(idx+1, t_arr)
            else :
                min_n = get_space(t_arr)
                ans = min(min_n, ans)
    elif c_type == 3 : # 3번 cctv의 경우
        for i, j in [(0, 3), (1, 3), (1, 2), (0, 2)] :
            t_arr = copy.deepcopy(arr)
            t_arr = scan(x, y, i, t_arr)
            t_arr = scan(x, y, j, t_arr)
            if (idx+1) < len(cctv) :
                dfs(idx+1, t_arr)
            else :
                min_n = get_space(t_arr)
                ans = min(min_n, ans)
    elif c_type == 4 : # 4번 cctv의 경우
        for i, j, k in [(0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 1, 2)] :
            t_arr = copy.deepcopy(arr)
            t_arr = scan(x, y, i, t_arr)
            t_arr = scan(x, y, j, t_arr)
            t_arr = scan(x, y, k, t_arr)
            if (idx+1) < len(cctv) :
                dfs(idx+1, t_arr)
            else :
                min_n = get_space(t_arr)
                ans = min(min_n, ans)
    else :
        t_arr = copy.deepcopy(arr)
        t_arr = scan(x, y, 0, t_arr)
        t_arr = scan(x, y, 1, t_arr)
        t_arr = scan(x, y, 2, t_arr)
        t_arr = scan(x, y, 3, t_arr)
        if (idx+1) < len(cctv) :
            dfs(idx+1, t_arr)
        else :
            min_n = get_space(t_arr)
            ans = min(min_n, ans)

if not cctv :
    get_space(array)
else :
    dfs(0, array)
print(ans)