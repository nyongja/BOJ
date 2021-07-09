n = int(input())
road = list(map(int, input().split()))
gas_station = list(map(int, input().split()))

answer = 0
min_p = int(1e9) # 현재 상태에서 최소 주유값
for idx, price in enumerate(gas_station[:-1]) : # 맨 마지막 도시에서는 주유를 할 필요가 없으므로
    if min_p > price : # 현재 최소 주유값보다 더 작은 도시가 나오면 거기서 주유 아니면 이전 주유소에서 계속 주유
        min_p = price
    answer += min_p * road[idx]

print(answer)
    