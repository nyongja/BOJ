from bisect import bisect_left
from copy import deepcopy

n = int(input())
a = list(map(int, input().split()))

lst = [a[0]]
memoization = [0 for _ in range(n)]

for idx, num in enumerate(a[1:], start = 1) :
    if lst[-1] < num :
        lst.append(num)
        memoization[idx] = len(lst)-1
    else :
        b_idx = bisect_left(lst, num)
        lst[b_idx] = num
        memoization[idx] = b_idx


maxVal = len(lst)
print(maxVal)
answer = []
maxVal -= 1
for idx in range(n-1, -1, -1) :
    if memoization[idx] == maxVal :
        answer.append(a[idx])
        maxVal -= 1
answer.reverse()
print(* answer)
    