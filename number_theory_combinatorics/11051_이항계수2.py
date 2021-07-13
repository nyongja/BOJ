n, k = map(int, input().split())

dp = [1 for _ in range(1001)]
 
# 정의에 충실하게! 동적 프로그래밍을 통해 구하기
for i in range(2, n+1) :
    dp[i] = dp[i-1] * i
print(int(dp[n]//(dp[k]*dp[n-k]))%10007)