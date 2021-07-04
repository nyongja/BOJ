n = int(input())
array = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp_up = [1 for _ in range(n)]
dp_down = [1 for _ in range(n)]

# 증가하는 수열 구하기
for i in range(n) :
    for j in range(i) :
        if array[i] > array[j] :
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

# 감소하는 수열 구하기
for i in range(n-1, -1, -1) :
    for j in range(n-1, i, -1) :
        if array[i] > array[j] :
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)
 
# 중복 계산되는 수열 하나 빼주기
for i in range(n) :
    dp[i] = dp_up[i] + dp_down[i] - 1

print(max(dp))

