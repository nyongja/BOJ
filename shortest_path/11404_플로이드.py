import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
graph = [[INF] *(n+1) for _ in range(n+1)]

for _ in range(m) :
    a, b, c = map(int, input().split()) # a -> b로 가는 비용
    if graph[a][b] > c :
        graph[a][b] = c

for i in range(1, n+1) :
    graph[i][i] = 0

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF :
            print(0, end = ' ')
        else :
            print(graph[i][j], end = ' ')
    print('')