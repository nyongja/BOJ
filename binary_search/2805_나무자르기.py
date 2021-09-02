n, m = map(int, input().split()) # n : 나무의 수, m : 집으로 가져가고자 하는 나무의 길이
trees = list(map(int, input().split()))

def binary_search(start, end) :
    global trees, m
    answer = 0
    while start <= end :
        mid = (start + end) // 2
        tmp = 0
        for tree in trees :
            if tree > mid :
                tmp += (tree - mid)
        if tmp >= m :
            start = mid + 1
            answer = mid
        else :
            end = mid - 1
    return answer

trees.sort() 
print(binary_search(1, trees[-1]))