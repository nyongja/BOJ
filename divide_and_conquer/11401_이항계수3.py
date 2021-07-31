n, k = map(int, input().split())
p =  1000000007
fact = [1 for _ in range(n+1)]

def power(x, y) : # 분할 정복을 이용하여 x^y 구하기
    if y == 0 :
        return 1
    if y % 2 :  # 홀수이면
        return (power(x, y // 2) ** 2 * x) % p
    else:
        return (power(x, y // 2) ** 2) % p

for i in range(2, n+1) :
    fact[i] = fact[i-1] * i % p

# 페르마의 소정리
a = fact[n] % p
b = (fact[k] * fact[n-k]) % p

answer = (a % p) * (power(b, p-2) % p) % p
print(answer)