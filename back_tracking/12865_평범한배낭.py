n, k = map(int, input().split())
array = []
for _ in range(n) :
    w, v = map(int, input().split())
    array.append((w, v))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n+1) :
    w, v = array[i-1]
    for j in range(1, k+1) : 
        if w > j : # 넣고자 하는 물품의 무게가 더 크면 넣을 수 없으므로
            dp[i][j] = dp[i-1][j] # 이전 값 가져오기
        else : # 넣고자 하는 물건의 크기가 가방과 같거나 크다면 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v) # 이번 물건을 넣을지 아니면 이전 상태가 더 가치가 높은지 확인해보기

print(dp[n][k])
