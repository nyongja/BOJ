n, k = map(int, input().split())

m1 = 1
m2 = 1
for i in range(1, n+1) :
    if i > k : # 이항 계수 계산 시 중복되는 부분 최소화 계산
        m1 *= i
    if i <= (n-k) :
        m2 *= i

print(int(m1/m2))