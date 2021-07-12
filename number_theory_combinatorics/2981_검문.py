from math import gcd, sqrt

n = int(input())
array = []
for i in range(n) :
    array.append(int(input()))

# 값의 차이의 최대공약수의 약수들을 구하면 됨
diff_gcd = array[1] - array[0]
for i in range(2, len(array)) :
    diff_gcd = gcd(diff_gcd, array[i] - array[i-1])

divisor_lst = []
# 전체 다 구하면 시간초과되므로 제곱근까지만 구하고 마지막 값은 따로 추가
for i in range(2, int(diff_gcd ** 0.5) + 1) :
    if diff_gcd % i == 0 :
        divisor_lst.append(i)
        divisor_lst.append(diff_gcd // i)
divisor_lst.append(diff_gcd)
divisor_lst = list(set(divisor_lst))
divisor_lst.sort()

for i in divisor_lst :
    print(i, end = ' ')
