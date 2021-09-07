import heapq
import sys
input = sys.stdin.readline

N = int(input())

lheap = [] # 중간 값보다 작은 값
rheap = [] # 중간 값보다 큰 값
mid = 0

for i in range(1, N + 1) :
    x = int(input())
    if i == 1 :
        mid = x
    else :
        if mid >= x :
            heapq.heappush(lheap, (-x, x))
        else :
            heapq.heappush(rheap, x)
        
        if i % 2 == 0 :
            if len(lheap) > len(rheap) :
                heapq.heappush(rheap, mid)
                mid = heapq.heappop(lheap)[1]
        else :
            if len(lheap) < len(rheap) :
                heapq.heappush(lheap, (-mid, mid))
                mid = heapq.heappop(rheap)
                    
    print(mid)
