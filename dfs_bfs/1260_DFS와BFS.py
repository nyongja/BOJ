import sys
from collections import deque
input = sys.stdin.readline

def dfs(node, graph, visited) :
    if visited[node] == False :
        visited[node] = True
        print(node, end = ' ')
        for i in sorted(graph[node]) :
            dfs(i, graph, visited)
    return

def bfs(start, graph, visited) :
    queue = deque([start])
    while queue :
        x = queue.popleft()
        if visited[x] == False : # 아직 방문 이전이면
            for i in sorted(graph[x]) :
                queue.append(i)
            visited[x] = True
            print(x, end = ' ')
    return 

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색을 시작할 정점 번호
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(V, graph, [False]*(len(graph)))
print('')
bfs(V, graph, [False]*(len(graph)))