n = int(input())
a = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
a.sort()

def binary_search(start, end, target) :
    while start <= end :
        mid = (start + end) // 2
        if a[mid] > target :
            end = mid - 1
        elif a[mid] < target :
            start = mid + 1
        elif a[mid] == target :
            return 1
    return 0

for i in targets :
    print(binary_search(0, len(a)-1, i))