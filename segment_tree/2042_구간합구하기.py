import sys
input = sys.stdin.readline

def init(node, start, end) :
    if start == end :
        tree[node] = array[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

# start, end : 노드에게 주어진 범위
# left, right : 내가 찾고자 하는 범위
def sum(node, start, end, left, right) :
    if start > right or end < left : # 내가 찾고자 하는 범위와 전혀 상관 없음
        return 0
    elif left <= start and end <= right : # 내가 찾고자 하는 범위가 노드에 완전히 포함이면 그대로 리턴 (자식 노드를 굳이 볼 필요가 없음)
        return tree[node]
    else :
        mid = (start + end) // 2
        return sum(2*node, start, mid, left, right) + sum(2*node+1, mid+1, end, left, right)

def update(node, start, end, idx, diff) :
    if start > idx or end < idx : # 범위에 포함되지 않으면 교체할 필요 없음
        return 
    tree[node] += diff # 범위에 포함되니 수정
    if start != end : # 리프노드가 아니면 자식 노드도 수정
        mid = (start + end) // 2
        update(2 * node, start, mid, idx, diff)
        update(2* node + 1, mid + 1, end, idx, diff)    
    return

n, m, k = map(int, input().split()) # 배열의 숫자 개수, 수의 변경 횟수, 구간의 합 횟수
array = list()
tree = [0] * (4*n)
for _ in range(n) :
    array.append(int(input()))

init(1, 0, n-1) # 트리 초기화

for _ in range(m + k) :
    a, b, c = map(int, input().split())
    if a == 1 : # 구간 숫자 바꾸기
        diff = c - array[b-1]
        array[b-1] = c
        update(1, 0, n-1, b-1, diff)
    elif a == 2 : # 구간 합 구하기
        print(sum(1, 0, n-1, b-1, c-1))
