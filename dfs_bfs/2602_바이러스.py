import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited) :
    queue = deque([start])
    answer = 0
    visited[start] = True
    while queue :
        now = queue.popleft()
        for next in graph[now] :
            if visited[next] == False : # 아직 방문 전이면
                answer += 1
                queue.append(next)
            visited[next] = True
    return answer

n = int(input()) # 컴퓨터 수 (1 ~ 100) 
m = int(input()) # 컴퓨터 연결되어있는 쌍 수 (edges)
visited = [False for _ in range(n+1)]

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(1, graph, visited))