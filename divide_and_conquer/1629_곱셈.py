import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
answer = a


def pow(a, b) :
    if b == 1 :
        return a % c
    else :
        tmp = pow(a, b//2)
        if b % 2 == 0 :
            return tmp * tmp % c
        else :
            return tmp * tmp * a % c

print(pow(a, b))