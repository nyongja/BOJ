import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # 물건 수, 가방 용량
weights = list(map(int, input().split()))
a_weights = weights[:n//2]
b_weights = weights[n//2:]
a_sum = []
b_sum = []

def bruteforce(w_arr, sum_arr, l, w) : 
    if l >= len(w_arr) :
        sum_arr.append(w)
        return
    bruteforce(w_arr, sum_arr, l+1, w) # 자기 자신 그대로 넣기
    bruteforce(w_arr, sum_arr, l+1, w + w_arr[l]) # 자기 자신 + 다른 값

def binarysearch(arr, target, start, end) :
    while start < end :
        mid = (start + end) // 2
        if arr[mid] <= target :
            start = mid + 1
        else :
            end = mid
    return end # 타겟보다 작은 값의 개수를 찾아야 하므로

bruteforce(a_weights, a_sum, 0, 0)
bruteforce(b_weights, b_sum, 0, 0)
b_sum.sort()

cnt = 0
for i in a_sum :
    if c - i < 0 : # 가방에 못넣는 경우이므로
        continue
    cnt += binarysearch(b_sum, c-i, 0, len(b_sum)) # 
print(cnt)