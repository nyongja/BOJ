import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split()) # 도시 크기, 치킨 집 최대 개수
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 1 : # 집이면
            house.append((i, j))
        elif city[i][j] == 2 : # 치킨
            chicken.append((i, j))

comb = list(combinations(chicken, m))

ans = sys.maxsize
for c in comb : 
    comb_min = 0
    for i, j in house :
        min_n = sys.maxsize
        for x, y in c :
            diff = abs(i-x) + abs(j-y)
            min_n = min(min_n, diff)
        comb_min += min_n
    ans = min(ans, comb_min)
print(ans)