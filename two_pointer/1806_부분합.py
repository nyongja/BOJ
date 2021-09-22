import sys
input = sys.stdin.readline

n, s = map(int, input().split()) # 수열의 길이, 부분합
array = list(map(int, input().split()))

inter_sum = 0
end = 0
result = 100000
for start in range(n) :
    while inter_sum < s and end < n :
        inter_sum += array[end]
        end += 1
    if inter_sum >= s :
        result = min(result, end - start)
    inter_sum -= array[start]

if result == 100000 :
    print(0)
else : print(result)