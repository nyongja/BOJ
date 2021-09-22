import math

def is_prime(n):
    primes = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)+1)):
        if primes[i] == True:
            j = 2
            while (i * j) <= n: # 배수들은 다 소수가 아니므로
                primes[i*j] = False
                j += 1
    return primes

n = int(input())
prime_sum = 0
cnt = 0
end = 2
primes = is_prime(n)
for i in range(2, n+1) :
    if primes[i] == True :
        while prime_sum < n and end <= n : 
            if primes[end] == True :
                prime_sum += end
            end += 1
        if prime_sum == n :
            cnt += 1
        prime_sum -= i

print(cnt)
    