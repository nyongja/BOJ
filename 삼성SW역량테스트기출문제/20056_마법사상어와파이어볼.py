from collections import deque
from collections import defaultdict
from math import floor

n, num, k = map(int, input().split()) # 맵 크기, 파이어볼 개수, 이동 명령 횟수
array = [[0 for _ in range(n)] for _ in range(n)]
fireball = defaultdict(list)
for _ in range(num) :
    r_, c_, m_, s_, d_ = map(int, input().split()) # 파이어볼 위치, 질량, 속력, 방향
    fireball[(r_-1, c_-1)].append((m_, s_, d_)) # 질량, 속력, 방향

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def do_fireball() :
    global fireball
    new_fireball = defaultdict(list)
    for x, y in fireball.keys() :
        for m, s, d in fireball[(x, y)] :
            nx, ny = x, y
            for _ in range(s) :
                nx, ny = (nx + dx[d]) % n, (ny + dy[d]) % n
            new_fireball[(nx, ny)].append((m, s, d))
    fireball = new_fireball
    return
    
def merge() :
    global fireball
    new_fireball = defaultdict(list)
    for x, y in fireball.keys() :
        if len(fireball[(x, y)]) > 1 :
            total_m, total_s, total_d = 0, 0, []
            for m, s, d in fireball[(x, y)] :
                total_m += m
                total_s += s
                total_d.append(d)
            new_m = floor(total_m / 5)

            if new_m == 0 :
                continue

            new_s = floor(total_s / len(fireball[(x,y)]))

            tmp_d = total_d[0]%2
            new_d = []
            for d in total_d[1:] :
                if d % 2 != tmp_d :
                    new_d = [1, 3, 5, 7] 

            if new_d == [] :
                new_d = [0, 2, 4, 6]
            for d in new_d :
                new_fireball[(x, y)].append((new_m, new_s, d))
        else :
            new_fireball[(x, y)].append(fireball[(x, y)][0])

    fireball = new_fireball            

while k > 0 :
    k -= 1
    do_fireball()
    merge()

ans = 0
for x, y in fireball.keys() :
    for m, s, d in fireball[(x, y)] :
        ans += m
print(ans)
    
