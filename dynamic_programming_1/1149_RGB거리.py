n = int(input())
rgb_array = []

for _ in range(n) :
    rgb_array.append(list(map(int, input().split())))

dp = [[0 for _ in range(3)] for _ in range(n)]

for i in range(3) :
    dp[0][i] = rgb_array[0][i]

for i in range(1, n) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_array[i][0] # i 번째 집에 r 칠하기
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb_array[i][1] # i 번째 집에 g 칠하기
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb_array[i][2] # i 번째 집에 b 칠하기

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
    