from calendar import c
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idx_lst = list(map(int, input().split())) # 뽑고자하는 숫자의 위치
queue = deque([i for i in range(1, n+1)])

answer = 0
for idx in idx_lst :
    while True :
        if queue[0] == idx :
            queue.popleft()
            break
        else :
            if queue.index(idx) < len(queue) / 2 :
                while queue[0] != idx :
                    queue.append(queue.popleft())
                    answer += 1
            else :
                while queue[0] != idx :
                    queue.appendleft(queue.pop())
                    answer += 1
print(answer)