import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]

for _ in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

def dijkstra(start, end) :
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[0]
            if cost < distance[i[1]] :
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    return distance[end]

ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))
if ans >= INF :
    print(-1)
else :
    print(ans)        

'''
#####
플로이드워샬 알고리즘 - 시간초과
#####

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1) :
    graph[i][i] = 1

for _ in range(e) :
    a, b, c = map(int, input().split()) # a <-> b (비용 : c)
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split()) # 반드시 거쳐야하는 정점

for i in range(1, n+1) :
    for j in range(1, n+1) :
        for k in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = min(graph[1][v1] + graph[v1][v2] + graph[v2][n], graph[1][v2] + graph[v2][v1] + graph[v1][n])
if ans == "INF" : 
    print(-1)
else :
    print(ans)
'''