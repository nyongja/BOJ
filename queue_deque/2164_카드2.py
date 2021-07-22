from collections import deque

n = int(input())
queue = deque()

for i in range(1, n+1) :
    queue.append(i)

flag = True
while len(queue) != 1 :
    if flag :
        queue.popleft()
        flag = False
    else :
        queue.append(queue.popleft())
        flag = True
        
print(queue.pop())