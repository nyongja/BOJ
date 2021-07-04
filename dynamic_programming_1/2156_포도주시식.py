n = int(input())
array = []
for _ in range(n) :
    array.append(int(input()))

dp = [0 for _ in range(n)]

for i in range(n) :
    if i == 0 :
        dp[i] = array[i]
    elif i == 1 :
        dp[i] = array[i-1] + array[i]
    elif i == 2 :
        dp[i] = max(array[i-2] + array[i], array[i-1] + array[i], dp[i-1])
    # 내 잔 선택 (+ 이전 이전 이전 잔과 이전 잔 또는 이전이전 잔 or 내 잔 선택하지 않는 경우
    else : 
        dp[i] = max(dp[i-2] + array[i], dp[i-3] + array[i-1] + array[i], dp[i-1])

print(dp[n-1])