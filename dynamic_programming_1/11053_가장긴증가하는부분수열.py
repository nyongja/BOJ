n = int(input())
array = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n) :
    for j in range(i) :
        # 해당 인덱스 기준 이전에 있는 값이 더 작으면 선택할 수 있다는 뜻이므로
        if array[i] > array[j] :
            # 해당 인덱스까지 골라진 숫자 + 나 선택하기 또는 그냥 기존 나 선택하는게 더 나은지 비교!
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))