import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start) :
    q = []
    distance = [INF] * (n+1)
    heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, now = heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] : 
            cost = dist + i[0]
            if cost < distance[i[1]] :
                heappush(q, (cost, i[1]))
                distance[i[1]] = cost
    return distance

INF = int(1e9)
T = int(input())
for _ in range(T) :
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, input().split()) # s : 예술가들의 출발지, g, h : 예술가들이 지나간 곳
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m) : # 도로 정보
        a, b, d = map(int, input().split()) # a <-> b (도로 길이 = d)
        graph[a].append((d, b))
        graph[b].append((d, a))

    s_ = dijkstra(s) 
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    
    candidates = []
    for _ in range(t) : # 목적지 후보
        target = int(input())
        
        path1 = s_[g] + g_[h] + h_[target]
        path2 = s_[h] + h_[g] + g_[target]
        if s_[target] == min(path1, path2) :
            candidates.append(target)

    candidates.sort()
    print(*candidates)