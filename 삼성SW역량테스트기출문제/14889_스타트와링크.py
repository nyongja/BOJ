import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
members = set(range(n))
comb = list(combinations(members, n//2))
ans = sys.maxsize

for i in range(len(comb)//2) :
    s = comb[i]
    l = comb[-i-1]
    s_score = 0
    l_score = 0

    for j in range(n//2) :
        member = s[j]
        for k in s :
            s_score += arr[member][k]
    for j in range(n//2) :
        member = l[j]
        for k in l :
            l_score += arr[member][k]
        
    diff = abs(s_score - l_score)
    ans = min(ans, diff)
print(ans)