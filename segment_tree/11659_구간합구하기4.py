import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
cumsum = [0 for _ in range(n+1)]

for i in range(1, n+1) : # 누적 합 구하기
    cumsum[i] = cumsum[i-1] + array[i-1]

for _ in range(m) :
    i, j = map(int, input().split())
    print(cumsum[j] - cumsum[i-1])