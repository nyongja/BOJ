import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
parents[1] = 1

for _ in range(n-1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start) :
    for node in tree[start] :
        if parents[node] == 0 : # 아직 방문 전이면
            parents[node] = start # 부모 노드 설정
            dfs(node)

dfs(1)

for i in parents[2:] :
    print(i)