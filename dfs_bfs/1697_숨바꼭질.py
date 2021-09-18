from collections import deque

def bfs(start, target) :
    global array
    queue = deque([start])
    while queue :
        pos = queue.popleft()
        if pos == target :
            return array[pos]
        n_pos = [pos-1, pos+1, pos*2]
        for i in n_pos :
            if i >= 0 and i < len(array) and array[i] == 0 :
                array[i] = array[pos] + 1
                queue.append(i)

    
n, k = map(int, input().split())
array = [0 for _ in range(100001)]

print(bfs(n, k))