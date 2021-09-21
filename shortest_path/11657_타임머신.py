import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split()) # 도시의 개수, 버스 노선의 개수
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b, c = map(int, input().split()) # a에서 b로, c : 걸리는 시간
    graph[a].append((c, b))

def bellman_ford() :
    distance = [INF] * (n+1)
    distance[1] = 0
    for _ in range(n-1) : # 정점 개수 -1 만큼 반복
        for i in range(1, n+1) :
            for dist, neighbor in graph[i] :
                cost = dist + distance[i]
                if distance[neighbor] > cost and distance[i] != INF : # distance[i]가 INF면 애초에 갈 수 없는 곳이므로..
                    distance[neighbor] = cost

    for i in range(1, n+1) : 
        for dist, neighbor in graph[i] :
            cost = distance[i] + dist
            if distance[neighbor] > cost and distance[i] != INF:
                return -1
    
    return distance

ans = bellman_ford()

if ans == -1 :
    print(-1)
else :
    for i in ans[2:] :
        print(-1 if i >= INF else i)