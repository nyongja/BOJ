n = int(input()) # 전깃줄의 개수
array = []
dp = [1 for _ in range(n)]

for _ in range(n) :
    a, b = map(int, input().split())
    array.append((a, b))

array.sort() # 왼쪽 전봇대를 기준으로 정렬

for i in range(n) :
    for j in range(i) :
        # 오른쪽 전봇대를 기준으로 가장 긴 수열 찾기
        if array[i][1] > array[j][1] :
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) # n - (제거 하지 않아도 되는 전깃줄 최대개수)
