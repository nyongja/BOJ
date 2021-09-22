import sys
input = sys.stdin.readline

n = int(input()) # 전체 용액의 수
liquids = list(map(int, input().split()))
liquids.sort()
left = 0
right = n-1
result_l = 0
result_r = n-1
result = sys.maxsize
while left < right :
    tmp_sum = liquids[left] + liquids[right]
    if tmp_sum == 0 :
        result_l = left
        result_r = right
        break
    else :
        if abs(result) > abs(tmp_sum) :
            result_l = left
            result_r = right
            result = tmp_sum
        if tmp_sum > 0 : right -= 1
        else : left += 1
print(liquids[result_l], liquids[result_r]) 
    