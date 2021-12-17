import sys
sys.getrecursionlimit(10**6)
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parents(parents, x) :
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parents[x] != x :
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

# 두 원소가 속한 집합을 합치기
def union_parents(parents, a, b) :
    a = find_parents(parents, a) 
    b = find_parents(parents, b)
    if a < b :
        parents[b] = a
    else :
        parents[a] = b
    return parents

def solution() :
    n, m = map(int, input().split())
    parents = [i for i in range(n+1)]

    for _ in range(m) :
        cmd, a, b = map(int, input().split())
        if cmd == 0 : # 합집합
            parents = union_parents(parents, a, b)
        elif cmd == 1 : # 같은 집합인지 확인
            parents[a] = find_parents(parents, a)
            parents[b] = find_parents(parents, b)
            if parents[a] == parents[b] : 
                print("YES")
            else :
                print("NO")
solution()