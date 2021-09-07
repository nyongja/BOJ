import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
L = [A[0]] # lowerbound

for a in A[1:] :
    if L[-1] < a :
        L.append(a)
    else :
        start = 0
        end = len(L)
        while start < end :
            mid = (start + end) // 2
            if L[mid] < a :
                start = mid + 1
            else :
                end = mid
        L[end] = a

print(len(L))