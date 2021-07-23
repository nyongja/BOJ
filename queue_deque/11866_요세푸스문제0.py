from collections import deque

n, k = map(int, input().split())
queue = deque()

for i in range(1, n+1) :
    queue.append(i)

i = 1
print("<", end = "")
while queue :
    if i % k != 0 :
        queue.append(queue.popleft())
    else :
        print(queue.popleft(), end = "")
        if queue :
            print(", ", end = "")
    i += 1
print(">")
