k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
lan.sort()

def binary_search(start, end) :
    while start <= end :
        mid = (start + end) // 2
        cnt = 0
        for i in lan :
            cnt += i // mid
        if cnt >= n :
            answer = mid
            start = mid + 1
        else :
            end = mid - 1
    return answer

print(binary_search(1, lan[-1]))
