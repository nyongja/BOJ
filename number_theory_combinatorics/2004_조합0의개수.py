def div(i, k) :
    ans = 0
    while i:
        i //= k
        ans += i
    return ans

n, m = map(int, input().split())
print(min(div(n, 2) - div(m, 2) - div(n-m, 2), div(n, 5) - div(m, 5) - div(n-m, 5)))