import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
parents[1] = 1

for _ in range(n-1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs() :
    q = deque([])
    q.append(1)
    while q :
        start = q.popleft()
        for node in tree[start] :
            if parents[node] == 0 :
                parents[node] = start
                q.append(node)

bfs()

for i in parents[2:] :
    print(i)