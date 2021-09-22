import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e) :
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(v+1) :
    for i in range(v+1) :
        for j in range(v+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF
for i in range(1, v+1) :
    ans = min(graph[i][i], ans)

if ans == INF :
    print(-1)
else :
    print(ans)