import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, flag) :
    global visited, set1, set2

    for i in graph[x] :
        if flag == 1 : # 첫 번째 집합에 속해있는 노드면
            set2.add(i)
            if visited[i] == 0 :
                visited[i] = 1
                dfs(i, 2)
        else :
            set1.add(i)
            if visited[i] == 0 :
                visited[i] = 1
                dfs(i, 1)
            
K = int(input()) # 테스트 케이스 
for _ in range(K) :
    v, e = map(int, input().split()) # v : 정점의 개수, e : 간선의 개수
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    set1 = set()
    set2 = set()
    for _ in range(e) :
        a, b = map(int, input().split()) # 간선 정보
        graph[a].append(b)
        graph[b].append(a)
    set1.add(1)
    for i in range(1, v+1) :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(i, 1)
    
    if set1 & set2 :
        print("NO")
    else :
        print("YES")