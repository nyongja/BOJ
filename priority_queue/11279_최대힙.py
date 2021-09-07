import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N) :
    x = int(input())
    if x == 0 :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    else :
        heapq.heappush(heap, (-x, x))