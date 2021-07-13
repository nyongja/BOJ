from collections import defaultdict
from itertools import combinations

t = int(input())
for _ in range(t) :
    n = int(input()) # 의상의 수
    clothes = defaultdict(int)
    for _ in range(n) :
        name, type = map(str, input().split())
        clothes[type] += 1
    answer = 1
    for i in clothes.values() :
        answer *= (i + 1)
    answer -= 1 # 아무것도 안 입은 경우 제외
    print(answer)
