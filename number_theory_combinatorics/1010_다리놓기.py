from math import comb

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    answer = comb(m, n)
    print(answer)