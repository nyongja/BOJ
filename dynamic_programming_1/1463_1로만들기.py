n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1) :
    if i != 1 :
        # 이전 값 + 1
        dp[i] = dp[i-1] + 1
        # 3으로 나누어 지는 경우
        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3] + 1)
        # 2로 나누어 지는 경우
        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[n])