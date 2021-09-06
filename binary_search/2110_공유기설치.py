n, c = map(int, input().split())
house = list(int(input()) for _ in range(n))
house.sort()

start = 1
end = house[-1] - house[0]
result = 0
while start <= end :
    mid = (start + end) // 2
    pos = house[0]
    cnt = 1

    for i in range(1, n) :
        if house[i] >= pos + mid :
            pos = house[i]
            cnt += 1
    if cnt >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1
print(result)
    