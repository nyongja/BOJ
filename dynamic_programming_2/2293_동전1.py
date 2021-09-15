import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n = 동전 종류 수, k = 만들고자 하는 금액
coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins :
    for i in range(coin, k+1) :
        dp[i] += dp[i-coin]
print(dp[k])