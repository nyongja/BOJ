import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split()) # 정점의 개수, 간선의 개수
k = int(input()) # 시작 정점의 번호
graph = [[] for _ in range(n+1)] # 각 노드에 연결되어있는 정보 담는 리스트
distance = [INF] * (n+1) # 최단 거리 테이블 무한으로 초기화

for _ in range(e) :
    u, v, w = map(int, input().split()) # u -> v (가중치 : w)
    graph[u].append((v, w))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 넣기
    distance[start] = 0
    while q : 
        dist, now = heapq.heappop(q)
        if distance[now] < dist : 
            continue
        for i in graph[now] :
            cost = dist + i[1] # 현재까지의 비용 + 해당 노드까지 가는 비용
            if cost < distance[i[0]] : # 만약 해당 비용이 지금까지 알고 있는 노드까지 비용보다 적으면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
dijkstra(k)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])

