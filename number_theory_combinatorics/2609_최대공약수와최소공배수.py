def gcd(n1, n2) : # 최대공약수 
    while n2 :
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2) : # 최소공배수
    return n1 * n2 // gcd(n1, n2)

n1, n2 = map(int, input().split())
print(gcd(n1, n2), lcm(n1, n2))
'''
from math import gcd, lcm
gcd(n1, n2)
lcm(n1, n2)
'''