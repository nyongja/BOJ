n = int(input())
k = int(input())

start = 1
end = k
result = 0
while start <= end :
    mid = (start + end) // 2
    tmp = 0
    for i in range(1, n+1) :
        tmp += min(mid // i, n)
    if tmp < k :
        start = mid + 1
    elif tmp >= k :
        result = mid
        end = mid - 1
print(result)