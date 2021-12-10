n, k = map(int, input().split()) # n가지 종류의 동전, 총 k원 만들기
coins = []
INF = int(1e9)
array = [INF for _ in range(k+1)]

array[0] = 0
for _ in range(n) :
    coin = int(input())
    if coin <= k :
        coins.append(coin)
        array[coin] = 1

for idx in range(1, k+1) :
    for coin in coins :
        if idx - coin > 0 and array[idx-coin] > 0 : 
            array[idx] = min(array[idx], array[idx-coin] + 1)
#print(array)
if array[-1] == INF :
    print(-1)
else :
    print(array[-1])