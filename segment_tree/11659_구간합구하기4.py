n, m = map(int, input().split())
array = list(map(int, input().split()))
cumsum = [0]

tmp = 0
for i in range(n) : # 누적 합 구하기
    tmp += array[i]
    cumsum.append(tmp)

for _ in range(m) :
    i, j = map(int, input().split())
    print(cumsum[j] - cumsum[i-1])