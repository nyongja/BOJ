import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()

left = 0
right = n-1
cnt = 0
while left < right :
    tmp_sum = array[left] + array[right]
    if tmp_sum == x :
        cnt += 1
        left += 1
    elif tmp_sum > x :
        right -= 1
    else :
        left += 1

print(cnt)