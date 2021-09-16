import sys
input = sys.stdin.readline

x = int(input()) # 추의 개수
weight = list(map(int, input().split()))
y = int(input()) # 구슬의 개수
marble = list(map(int, input().split()))

dp = [[0] * 15001 for _ in range(x+1)]
possible = []

def dfs(weight, x, now, left, right) :
    diff = abs(left-right)

    if diff not in possible :
        possible.append(diff)
    
    if now == x : # 마지막 추, 즉 이제 더 이상 둘 추 없으면
        return 0
    
    if dp[now][diff] == 0 :
        dfs(weight, x, now + 1, left + weight[now], right)
        dfs(weight, x, now + 1, left, right + weight[now])
        dfs(weight, x, now + 1, left, right)
        dp[now][diff] = 1

dfs(weight, x, 0, 0, 0)

for m in marble :
    if m in possible :
        print("Y", end = ' ')
    else :
        print("N", end = ' ')

