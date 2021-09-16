import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # N : 앱의 개수, M : 추가로 필요한 바이트 수
memory = list(map(int, input().split())) # 현재 사용 중인 메모리 바이트
cost = list(map(int, input().split())) # 비활성화 비용
total_cost = sum(cost)
dp = [[0 for _ in range(total_cost+1)] for _ in range(N+1)]

answer = int(1e9)
for i in range(1, N+1) : # 몇 번째 앱을 선택했을 때
    for j in range(total_cost+1) : # 해당 비용으로 만들 수 있는 최대 메모리
        if cost[i-1] > j : # 해당 앱의 비용이 현재 비용보다 큰 경우 (이번 앱 선택 불가)
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        
        if dp[i][j] >= M :
            answer = min(j, answer)

print(answer)